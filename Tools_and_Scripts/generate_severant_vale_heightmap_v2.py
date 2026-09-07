"""
Severant Vale Heightmap Generator v2
Generates a 16-bit grayscale PNG heightmap at 8129x8129 for UE5 landscape import.
8km x 8km map, 1 pixel = 1 meter.

UE5 value mapping (Scale Z = 400):
  pixel_value = 32768 + (elevation_meters * 32)
  32768 = Z origin (0m)
  Range: 0m-700m fits within 32768-55168 (well under 65535 max)

ALL terrain shapes, features, and positions are identical to v1.
Only the value mapping has changed.
"""

import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter
import time


# ---- Value mapping helpers ----
def meters_to_pixel(elevation_m):
    """Convert an elevation in meters to a 16-bit pixel value for UE5 (Scale Z=400)."""
    return 32768.0 + (elevation_m * 32.0)

def delta_to_pixel(delta_m):
    """Convert a relative elevation delta in meters to pixel-value delta."""
    return delta_m * 32.0

# Pre-computed constants
BASELINE = meters_to_pixel(100)      # 35968 — central valley floor
LAKE_SURFACE = meters_to_pixel(80)   # 35328
LAKE_SURROUND = meters_to_pixel(105) # 36128
MARSH_FLOOR = meters_to_pixel(65)    # 34848
ORIGIN = meters_to_pixel(0)          # 32768


def make_perlin_noise(shape, scale, octaves=4, seed=42):
    """Generate Perlin-like noise using layered smooth random gradients."""
    rng = np.random.default_rng(seed)
    noise = np.zeros(shape, dtype=np.float64)
    amplitude = 1.0
    freq = 1.0
    for _ in range(octaves):
        grid_h = max(2, int(shape[0] / (scale / freq)))
        grid_w = max(2, int(shape[1] / (scale / freq)))
        low_res = rng.standard_normal((grid_h, grid_w))
        from scipy.ndimage import zoom
        factor_y = shape[0] / grid_h
        factor_x = shape[1] / grid_w
        layer = zoom(low_res, (factor_y, factor_x), order=3)
        layer = layer[:shape[0], :shape[1]]
        noise += amplitude * layer
        amplitude *= 0.5
        freq *= 2.0
    noise = (noise - noise.min()) / (noise.max() - noise.min() + 1e-10)
    return noise


def bezier_curve(points, num_samples=2000):
    """Evaluate a cubic Bezier curve through control points."""
    t = np.linspace(0, 1, num_samples)
    all_x, all_y = [], []
    for i in range(0, len(points) - 1, 3):
        seg_pts = points[i:i+4]
        if len(seg_pts) < 4:
            seg_pts_arr = np.array(seg_pts)
            t_seg = np.linspace(0, 1, num_samples // max(1, (len(points) // 3)))
            for tt in t_seg:
                idx = min(int(tt * (len(seg_pts_arr) - 1)), len(seg_pts_arr) - 2)
                local_t = tt * (len(seg_pts_arr) - 1) - idx
                px = seg_pts_arr[idx][0] * (1 - local_t) + seg_pts_arr[idx+1][0] * local_t
                py = seg_pts_arr[idx][1] * (1 - local_t) + seg_pts_arr[idx+1][1] * local_t
                all_x.append(px)
                all_y.append(py)
            continue
        p0, p1, p2, p3 = seg_pts
        t_seg = np.linspace(0, 1, num_samples // max(1, (len(points) // 3)))
        for tt in t_seg:
            x = ((1-tt)**3 * p0[0] + 3*(1-tt)**2*tt * p1[0] +
                 3*(1-tt)*tt**2 * p2[0] + tt**3 * p3[0])
            y = ((1-tt)**3 * p0[1] + 3*(1-tt)**2*tt * p1[1] +
                 3*(1-tt)*tt**2 * p2[1] + tt**3 * p3[1])
            all_x.append(x)
            all_y.append(y)
    return np.array(all_x), np.array(all_y)


def generate_heightmap():
    SIZE = 8129
    heightmap = np.full((SIZE, SIZE), BASELINE, dtype=np.float64)  # 100m baseline
    print(f"Heightmap initialized: {SIZE}x{SIZE} (baseline={BASELINE:.0f}, 100m)")

    # Track masks to protect certain areas from noise later
    river_mask = np.zeros((SIZE, SIZE), dtype=np.float64)
    plateau_mask = np.zeros((SIZE, SIZE), dtype=np.float64)
    lake_mask = np.zeros((SIZE, SIZE), dtype=np.float64)
    cliff_mask = np.zeros((SIZE, SIZE), dtype=np.float64)

    yy, xx = np.meshgrid(np.arange(SIZE), np.arange(SIZE), indexing='ij')

    # =========================================================================
    # 5. NORTHERN FOOTHILLS — apply before river so river carves through
    # =========================================================================
    print("Painting northern foothills...")
    north_gradient = np.zeros((SIZE, SIZE), dtype=np.float64)
    # Gradient: Y=2000 -> 150m, Y=1200 -> 250m, Y=500 -> 400-500m
    mask_north = yy < 2000
    t = np.clip((2000 - yy) / 2000.0, 0, 1)
    # 100m at Y=2000, up to 500m at Y=0
    north_elev = BASELINE + t * (meters_to_pixel(500) - BASELINE)
    heightmap = np.where(mask_north, np.maximum(heightmap, north_elev), heightmap)

    # Northern peaks (pixel coords unchanged, elevations converted)
    peaks = [
        (3000, 300, meters_to_pixel(650), 600),   # was 65000
        (5200, 450, meters_to_pixel(550), 500),    # was 55000
        (6800, 250, meters_to_pixel(600), 550),    # was 60000
        (1800, 500, meters_to_pixel(500), 450),    # was 50000
    ]
    for px, py, val, sigma in peaks:
        dist2 = (xx - px)**2 + (yy - py)**2
        peak_contrib = (val - BASELINE) * np.exp(-dist2 / (2 * sigma**2))
        heightmap += peak_contrib

    # Mountain pass at X=4065, Y=1000
    pass_dist2 = (xx - 4065)**2 + (yy - 1000)**2
    pass_depression = delta_to_pixel(200) * np.exp(-pass_dist2 / (2 * 400**2))  # 200m depression
    heightmap -= pass_depression
    heightmap = np.clip(heightmap, 0, 65535)

    # =========================================================================
    # 7. WESTERN BOUNDARY
    # =========================================================================
    print("Painting western boundary...")
    mask_west = xx < 1500
    t_west = np.clip((1500 - xx) / 1500.0, 0, 1)
    # 100m at X=1500, up to 380m at X=0
    west_elev = BASELINE + t_west * (meters_to_pixel(380) - BASELINE)
    heightmap = np.where(mask_west, np.maximum(heightmap, west_elev), heightmap)

    # Canyon valleys running E-W (floor values converted)
    canyons = [
        (700, 2000, 5500, 80, meters_to_pixel(160)),  # was 16000
        (500, 3800, 4500, 60, meters_to_pixel(170)),   # was 17000
        (900, 5200, 3000, 70, meters_to_pixel(150)),   # was 15000
    ]
    for cx, cy, length, width, floor_val in canyons:
        canyon_mask_x = np.exp(-0.5 * ((xx - cx) / (200))**2)
        canyon_mask_y = np.exp(-0.5 * ((yy - cy) / (length * 0.4))**2)
        canyon_effect = canyon_mask_x * canyon_mask_y
        heightmap = heightmap * (1 - canyon_effect) + floor_val * canyon_effect

    # =========================================================================
    # 3. EASTERN RIDGE
    # =========================================================================
    print("Painting eastern ridge...")
    # Ridge runs from ~(6500, 1500) to ~(6200, 6000)
    ridge_length = 4500
    for iy in range(max(0, 1500 - 200), min(SIZE, 6000 + 200)):
        t_ridge = np.clip((iy - 1500) / ridge_length, 0, 1)
        ridge_cx = 6500 + (6200 - 6500) * t_ridge
        # Peak height varies: north=250m, peak at Sunspear=400m, south=200m
        if t_ridge < 0.51:
            t_peak = t_ridge / 0.51
            ridge_height = meters_to_pixel(250) + (meters_to_pixel(400) - meters_to_pixel(250)) * np.sin(t_peak * np.pi / 2)
        else:
            t_peak = (t_ridge - 0.51) / 0.49
            ridge_height = meters_to_pixel(400) - (meters_to_pixel(400) - meters_to_pixel(200)) * t_peak

        # Saddle points
        saddle_positions = [0.25, 0.55, 0.8]
        for sp in saddle_positions:
            saddle_effect = np.exp(-0.5 * ((t_ridge - sp) / 0.03)**2)
            ridge_height -= saddle_effect * (ridge_height - meters_to_pixel(290)) * 0.4

        # Asymmetric profile: gentle west (1500px), steep east (400px)
        row_x = np.arange(SIZE)
        west_slope = np.exp(-0.5 * np.clip(ridge_cx - row_x, 0, None)**2 / (750**2))
        east_slope = np.exp(-0.5 * np.clip(row_x - ridge_cx, 0, None)**2 / (200**2))
        profile = np.where(row_x <= ridge_cx, west_slope, east_slope)

        contribution = profile * (ridge_height - BASELINE)
        heightmap[iy, :] = np.maximum(heightmap[iy, :], BASELINE + contribution)

        # Track cliff faces on east side for smoothing protection
        cliff_profile = np.where((row_x > ridge_cx) & (row_x < ridge_cx + 500),
                                 1.0, 0.0)
        cliff_mask[iy, :] = np.maximum(cliff_mask[iy, :], cliff_profile * profile)

    # =========================================================================
    # 12. VERDANTHEART TERRAIN (east of ridge)
    # =========================================================================
    print("Painting Verdantheart terrain...")
    verdant_mask = xx > 6500
    t_verdant = np.clip((xx - 6500) / 1600.0, 0, 1)
    # 200m to 350m
    verdant_base = meters_to_pixel(200) + t_verdant * delta_to_pixel(150)
    # Undulating character
    verdant_noise = make_perlin_noise((SIZE, SIZE), scale=600, octaves=4, seed=77)
    verdant_variation = verdant_noise * delta_to_pixel(100)  # 100m variation
    verdant_total = verdant_base + verdant_variation
    heightmap = np.where(
        verdant_mask & (verdant_total > heightmap),
        verdant_total, heightmap
    )

    # Wellspring basin at (7000, 3800) — 450m per user spec
    well_dist2 = (xx - 7000)**2 + (yy - 3800)**2
    well_radius = 200
    well_mask = np.exp(-well_dist2 / (2 * (well_radius * 0.6)**2))
    heightmap = heightmap * (1 - well_mask) + meters_to_pixel(450) * well_mask

    # =========================================================================
    # 6. MISTWATER LAKE
    # =========================================================================
    print("Painting Mistwater Lake...")
    lake_cx, lake_cy = 4300, 3300
    lake_radius = 1000
    lake_dist2 = (xx - lake_cx)**2 + (yy - lake_cy)**2
    # Smooth bowl: Gaussian subtraction
    lake_bowl = np.exp(-lake_dist2 / (2 * (lake_radius * 0.65)**2))
    heightmap = heightmap - lake_bowl * (LAKE_SURROUND - LAKE_SURFACE)  # 105m - 80m = 25m drop
    # Build the lake mask for noise protection
    lake_mask = np.where(lake_dist2 < (lake_radius * 1.1)**2, 1.0, 0.0)

    # =========================================================================
    # 8. SOUTHERN BOUNDARY
    # =========================================================================
    print("Painting southern boundary...")
    mask_south = yy > 6000
    t_south = np.clip((yy - 6000) / (SIZE - 6000), 0, 1)
    # 90m dropping to 50m at south edge
    south_elev = meters_to_pixel(90) - t_south * delta_to_pixel(40)
    heightmap = np.where(mask_south, np.minimum(heightmap, south_elev), heightmap)

    # =========================================================================
    # 9. SE MARSHLAND
    # =========================================================================
    print("Painting SE marshland...")
    marsh_cx, marsh_cy = 5500, 5500
    marsh_dist2 = (xx - marsh_cx)**2 + (yy - marsh_cy)**2
    marsh_radius = 800
    marsh_effect = np.exp(-marsh_dist2 / (2 * (marsh_radius * 0.7)**2))
    heightmap = heightmap * (1 - marsh_effect) + MARSH_FLOOR * marsh_effect

    # Marsh pools
    rng = np.random.default_rng(123)
    for _ in range(7):
        pool_x = marsh_cx + rng.integers(-500, 500)
        pool_y = marsh_cy + rng.integers(-500, 500)
        pool_r = rng.integers(20, 40)
        pool_depth_m = rng.integers(2, 3)  # 2-3m depth (was 200-300 at 100/m)
        pool_dist2 = (xx - pool_x)**2 + (yy - pool_y)**2
        pool_mask = np.exp(-pool_dist2 / (2 * (pool_r * 0.6)**2))
        heightmap -= pool_mask * delta_to_pixel(pool_depth_m)

    # =========================================================================
    # 2. RIVER SERPENTIS
    # =========================================================================
    print("Carving River Serpentis...")
    num_pts = 5000
    t_river = np.linspace(0, 1, num_pts)

    # Base diagonal path (positions unchanged)
    base_x = 6100 + (2000 - 6100) * t_river
    base_y = 2300 + (6200 - 2300) * t_river

    # Add meanders that increase toward SW (unchanged)
    meander_amp = 50 + 350 * t_river**1.5
    meander_freq = 0.008 + 0.004 * t_river
    angle = np.arctan2(6200 - 2300, 2000 - 6100)
    perp_angle = angle + np.pi / 2
    cumulative_phase = np.cumsum(meander_freq)
    offset = meander_amp * np.sin(2 * np.pi * cumulative_phase)

    river_cx = base_x + offset * np.cos(perp_angle)
    river_cy = base_y + offset * np.sin(perp_angle)

    river_cx = np.clip(river_cx, 0, SIZE - 1)
    river_cy = np.clip(river_cy, 0, SIZE - 1)

    print("  Carving channel (this takes a moment)...")
    chunk_step = 3
    for i in range(0, num_pts, chunk_step):
        t = t_river[i]
        px, py = river_cx[i], river_cy[i]

        # Width (pixels, unchanged) and depth (converted to new mapping)
        if t < 0.2:       # NE section — 95m depth
            width = 30
            depth = meters_to_pixel(95)       # was 9500
            fp_width = 50
        elif t < 0.5:     # Mid section — 72m to 95m
            width = 50
            depth = meters_to_pixel(72) + (meters_to_pixel(95) - meters_to_pixel(72)) * (0.5 - t) / 0.3
            fp_width = 100
        elif t < 0.75:    # Near Hollowford — 58m (ford depth)
            width = 80
            depth = meters_to_pixel(58)       # was 5800
            fp_width = 250
        else:              # SW exit — 50m to 58m
            width = 70
            depth = meters_to_pixel(50) + (meters_to_pixel(58) - meters_to_pixel(50)) * (1.0 - t) / 0.25
            fp_width = 150

        half_w = width / 2
        margin = int(fp_width + half_w + 60)
        ipx, ipy = int(px), int(py)
        x_min = max(0, ipx - margin)
        x_max = min(SIZE, ipx + margin)
        y_min = max(0, ipy - margin)
        y_max = min(SIZE, ipy + margin)

        if x_max <= x_min or y_max <= y_min:
            continue

        local_xx, local_yy = np.meshgrid(
            np.arange(x_min, x_max), np.arange(y_min, y_max)
        )
        dist = np.sqrt((local_xx - px)**2 + (local_yy - py)**2)

        # Channel carve
        channel_blend = np.exp(-0.5 * (dist / (half_w * 0.6))**2)
        region = heightmap[y_min:y_max, x_min:x_max]
        heightmap[y_min:y_max, x_min:x_max] = np.minimum(
            region, region * (1 - channel_blend) + depth * channel_blend
        )

        # Floodplain near Hollowford
        if 0.4 < t < 0.85:
            fp_blend = np.exp(-0.5 * (dist / (fp_width * 0.5))**2)
            fp_blend = np.clip(fp_blend - channel_blend, 0, 1)
            # Floodplain: 65m near channel, 85m at edge
            fp_val = meters_to_pixel(65) + (meters_to_pixel(85) - meters_to_pixel(65)) * (dist / (fp_width + half_w))
            fp_val = np.clip(fp_val, meters_to_pixel(65), meters_to_pixel(85))
            current = heightmap[y_min:y_max, x_min:x_max]
            heightmap[y_min:y_max, x_min:x_max] = np.minimum(
                current, current * (1 - fp_blend) + fp_val * fp_blend
            )

        # Update river mask
        river_channel = dist < (half_w * 2)
        river_mask[y_min:y_max, x_min:x_max] = np.maximum(
            river_mask[y_min:y_max, x_min:x_max],
            river_channel.astype(np.float64)
        )

    # =========================================================================
    # 4. SETTLEMENT PLATEAUS
    # =========================================================================
    print("Flattening settlement plateaus...")
    settlements = [
        ("Hollowford",  3300, 4900, 600,  meters_to_pixel(85)),   # was 8500  -> 35488
        ("Ironwood",    2600, 2900, 150,  meters_to_pixel(180)),  # was 18000 -> 38528
        ("Ashford",     2100, 1900, 125,  meters_to_pixel(240)),  # was 24000 -> 40448
        ("Grainfell",   5600, 2900, 200,  meters_to_pixel(120)),  # was 12000 -> 36608
        ("Southwatch",  5900, 6000, 150,  meters_to_pixel(90)),   # was 9000  -> 35648
    ]
    for name, sx, sy, radius, value in settlements:
        dist2 = (xx - sx)**2 + (yy - sy)**2
        inner_r = radius * 0.7
        blend = np.clip(1.0 - (np.sqrt(dist2) - inner_r) / (radius - inner_r), 0, 1)
        blend = blend**2
        heightmap = heightmap * (1 - blend) + value * blend
        plateau_mask = np.maximum(plateau_mask,
                                  np.where(dist2 < (radius * 1.2)**2, 1.0, 0.0))

    # =========================================================================
    # 10. TRIBUTARY CHANNELS
    # =========================================================================
    print("Carving tributary channels...")
    # Depth cuts converted: old values / 100 = meters, then * 32 = new delta
    tributaries = [
        # West-side feeders (from higher western terrain)
        ((1500, 2800), (3800, 3200), 6, delta_to_pixel(1.5)),   # was 150
        ((1200, 3500), (3500, 3800), 7, delta_to_pixel(1.8)),   # was 180
        ((1800, 4200), (3200, 4600), 5, delta_to_pixel(1.2)),   # was 120
        ((2000, 5500), (2800, 5800), 6, delta_to_pixel(1.6)),   # was 160
        ((1500, 5000), (2900, 5200), 7, delta_to_pixel(1.4)),   # was 140
        ((2500, 6000), (2200, 6100), 5, delta_to_pixel(1.0)),   # was 100
        # East-side feeders (from ridge)
        ((6000, 2000), (5500, 2600), 6, delta_to_pixel(1.7)),   # was 170
        ((5800, 3000), (5000, 3500), 7, delta_to_pixel(1.5)),   # was 150
        ((5900, 3800), (4800, 4200), 5, delta_to_pixel(1.3)),   # was 130
        ((5600, 4500), (4500, 4800), 6, delta_to_pixel(1.6)),   # was 160
        ((5500, 5200), (4200, 5500), 7, delta_to_pixel(1.4)),   # was 140
        ((5700, 5600), (4500, 5900), 5, delta_to_pixel(1.2)),   # was 120
    ]

    for (sx, sy), (ex, ey), width, depth_cut in tributaries:
        num_t = 500
        t_trib = np.linspace(0, 1, num_t)
        trib_x = sx + (ex - sx) * t_trib
        trib_y = sy + (ey - sy) * t_trib
        trib_x += 30 * np.sin(t_trib * 8 * np.pi)
        trib_y += 20 * np.cos(t_trib * 6 * np.pi)

        half_w = width / 2
        for i in range(0, num_t, 4):
            px, py = int(trib_x[i]), int(trib_y[i])
            margin = int(half_w + 15)
            x_min = max(0, px - margin)
            x_max = min(SIZE, px + margin)
            y_min = max(0, py - margin)
            y_max = min(SIZE, py + margin)
            if x_max <= x_min or y_max <= y_min:
                continue
            local_xx, local_yy = np.meshgrid(
                np.arange(x_min, x_max), np.arange(y_min, y_max)
            )
            dist = np.sqrt((local_xx - px)**2 + (local_yy - py)**2)
            blend = np.exp(-0.5 * (dist / (half_w * 0.5))**2)
            region = heightmap[y_min:y_max, x_min:x_max]
            heightmap[y_min:y_max, x_min:x_max] = region - blend * depth_cut

    # =========================================================================
    # 11. ROLLING HILLS (Perlin noise on farmland areas)
    # =========================================================================
    print("Adding rolling hills noise...")
    hill_noise = make_perlin_noise((SIZE, SIZE), scale=400, octaves=5, seed=99)
    hill_amplitude = delta_to_pixel(8)  # 8m variation (was 800 at 100/m)
    hill_contribution = (hill_noise - 0.5) * 2 * hill_amplitude

    # Only apply to farmland elevations (75m-150m), not protected areas
    farmland_mask = ((heightmap >= meters_to_pixel(75)) & (heightmap <= meters_to_pixel(150))).astype(np.float64)
    protection = np.maximum(river_mask, np.maximum(plateau_mask, lake_mask))
    farmland_mask *= (1 - protection)

    farmland_mask = gaussian_filter(farmland_mask, sigma=20)
    heightmap += hill_contribution * farmland_mask

    # =========================================================================
    # 13. SMOOTHING
    # =========================================================================
    print("Applying final smoothing...")
    smoothed = gaussian_filter(heightmap, sigma=4)

    smooth_protection = np.maximum(cliff_mask, river_mask)
    smooth_protection = gaussian_filter(smooth_protection, sigma=2)
    smooth_protection = np.clip(smooth_protection, 0, 1)

    heightmap = smoothed * (1 - smooth_protection) + heightmap * smooth_protection

    # =========================================================================
    # FINAL CLAMP AND EXPORT
    # =========================================================================
    heightmap = np.clip(heightmap, 0, 65535).astype(np.uint16)

    print("Saving full-resolution heightmap (8129x8129)...")
    img = Image.fromarray(heightmap, mode='I;16')
    output_dir = "C:/Users/kyler/OneDrive/Desktop/ShatteredDominion/Assets/3D/Exports/Environment"
    img.save(f"{output_dir}/SeverantVale_Heightmap_v2.png")
    print(f"  Saved: {output_dir}/SeverantVale_Heightmap_v2.png")

    print("Saving 1024x1024 preview...")
    preview = img.resize((1024, 1024), Image.BILINEAR)
    preview.save(f"{output_dir}/SeverantVale_Heightmap_v2_Preview.png")
    print(f"  Saved: {output_dir}/SeverantVale_Heightmap_v2_Preview.png")

    # Print stats with UE5 mapping
    print(f"\nHeightmap stats (UE5 Scale Z = 400):")
    print(f"  Min pixel: {heightmap.min()}  -> {(heightmap.min() - 32768) / 32:.1f}m")
    print(f"  Max pixel: {heightmap.max()}  -> {(heightmap.max() - 32768) / 32:.1f}m")
    print(f"  Mean pixel: {heightmap.mean():.0f} -> {(heightmap.mean() - 32768) / 32:.1f}m")
    print(f"  Origin (0m) = pixel 32768")
    print(f"\nKey landmark verification:")
    # Sample specific settlement locations
    landmarks = [
        ("Hollowford (85m)", 3300, 4900, 85),
        ("Ironwood (180m)", 2600, 2900, 180),
        ("Ashford (240m)", 2100, 1900, 240),
        ("Grainfell (120m)", 5600, 2900, 120),
        ("Southwatch (90m)", 5900, 6000, 90),
        ("Mistwater Lake (80m)", 4300, 3300, 80),
    ]
    for name, lx, ly, expected_m in landmarks:
        actual_px = heightmap[ly, lx]
        actual_m = (actual_px - 32768) / 32
        print(f"  {name}: pixel={actual_px}, actual={actual_m:.1f}m, expected={expected_m}m")

    print("Done!")


if __name__ == "__main__":
    t0 = time.time()
    generate_heightmap()
    print(f"Total time: {time.time() - t0:.1f}s")
