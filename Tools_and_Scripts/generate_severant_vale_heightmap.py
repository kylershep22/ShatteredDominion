"""
Severant Vale Heightmap Generator
Generates a 16-bit grayscale PNG heightmap at 8129x8129 for UE5 landscape import.
8km x 8km map, 1 pixel = 1 meter, 100 values per meter of elevation.
"""

import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter
import time


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
        # Bilinear upsample
        from scipy.ndimage import zoom
        factor_y = shape[0] / grid_h
        factor_x = shape[1] / grid_w
        layer = zoom(low_res, (factor_y, factor_x), order=3)
        # Crop to exact shape in case of rounding
        layer = layer[:shape[0], :shape[1]]
        noise += amplitude * layer
        amplitude *= 0.5
        freq *= 2.0
    # Normalize to [0, 1]
    noise = (noise - noise.min()) / (noise.max() - noise.min() + 1e-10)
    return noise


def bezier_curve(points, num_samples=2000):
    """Evaluate a cubic Bezier curve through control points."""
    t = np.linspace(0, 1, num_samples)
    # Use piecewise cubic Bezier segments
    all_x, all_y = [], []
    for i in range(0, len(points) - 1, 3):
        seg_pts = points[i:i+4]
        if len(seg_pts) < 4:
            # Linear fallback for remaining points
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


def carve_river_channel(heightmap, cx, cy, width, depth_value, floodplain_width=0,
                        floodplain_value=None):
    """Carve a river segment around a set of centerline points."""
    size = heightmap.shape[0]
    yy, xx = np.ogrid[0:size, 0:size]

    for i in range(len(cx)):
        px, py = cx[i], cy[i]
        # Compute distance from this centerline point
        half_w = width / 2
        # Only affect nearby pixels for performance
        x_min = max(0, int(px - floodplain_width - half_w - 50))
        x_max = min(size, int(px + floodplain_width + half_w + 50))
        y_min = max(0, int(py - floodplain_width - half_w - 50))
        y_max = min(size, int(py + floodplain_width + half_w + 50))

        local_xx, local_yy = np.meshgrid(
            np.arange(x_min, x_max), np.arange(y_min, y_max)
        )
        dist = np.sqrt((local_xx - px)**2 + (local_yy - py)**2)

        # River channel with Gaussian cross-section
        channel_mask = np.exp(-0.5 * (dist / (half_w * 0.6))**2)
        region = heightmap[y_min:y_max, x_min:x_max]
        target = depth_value
        blend = channel_mask
        heightmap[y_min:y_max, x_min:x_max] = (
            region * (1 - blend) + target * blend
        )

        # Floodplain
        if floodplain_width > 0 and floodplain_value is not None:
            fp_mask = np.exp(-0.5 * (dist / (floodplain_width * 0.5))**2)
            fp_mask = np.clip(fp_mask - channel_mask, 0, 1)
            heightmap[y_min:y_max, x_min:x_max] = (
                heightmap[y_min:y_max, x_min:x_max] * (1 - fp_mask) +
                floodplain_value * fp_mask
            )


def generate_heightmap():
    SIZE = 8129
    heightmap = np.full((SIZE, SIZE), 10000.0, dtype=np.float64)
    print(f"Heightmap initialized: {SIZE}x{SIZE}")

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
    # Gradient: Y=2000 -> 15000, Y=1200 -> 25000, Y=500 -> 40000-50000
    mask_north = yy < 2000
    # Linear interpolation from Y=2000 (15000) to Y=0 (50000)
    t = np.clip((2000 - yy) / 2000.0, 0, 1)
    north_elev = 10000 + t * (50000 - 10000)
    heightmap = np.where(mask_north, np.maximum(heightmap, north_elev), heightmap)

    # Northern peaks
    peaks = [
        (3000, 300, 65000, 600),
        (5200, 450, 55000, 500),
        (6800, 250, 60000, 550),
        (1800, 500, 50000, 450),
    ]
    for px, py, val, sigma in peaks:
        dist2 = (xx - px)**2 + (yy - py)**2
        peak_contrib = (val - 10000) * np.exp(-dist2 / (2 * sigma**2))
        heightmap += peak_contrib

    # Mountain pass at X=4065, Y=1000
    pass_dist2 = (xx - 4065)**2 + (yy - 1000)**2
    pass_depression = 20000 * np.exp(-pass_dist2 / (2 * 400**2))
    heightmap -= pass_depression
    heightmap = np.clip(heightmap, 0, 65535)

    # =========================================================================
    # 7. WESTERN BOUNDARY
    # =========================================================================
    print("Painting western boundary...")
    mask_west = xx < 1500
    t_west = np.clip((1500 - xx) / 1500.0, 0, 1)
    west_elev = 10000 + t_west * (38000 - 10000)
    heightmap = np.where(mask_west, np.maximum(heightmap, west_elev), heightmap)

    # Canyon valleys running E-W
    canyons = [
        (700, 2000, 5500, 80, 16000),   # (center_x, center_y, length_y, width, floor)
        (500, 3800, 4500, 60, 17000),
        (900, 5200, 3000, 70, 15000),
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
        # Parameter along ridge
        t_ridge = np.clip((iy - 1500) / ridge_length, 0, 1)
        # Ridge center X interpolates from 6500 to 6200
        ridge_cx = 6500 + (6200 - 6500) * t_ridge
        # Peak height varies: north=25000, peak at Sunspear=40000, south=20000
        if t_ridge < 0.51:  # North to Sunspear (~3800)
            t_peak = t_ridge / 0.51
            ridge_height = 25000 + (40000 - 25000) * np.sin(t_peak * np.pi / 2)
        else:  # Sunspear to south
            t_peak = (t_ridge - 0.51) / 0.49
            ridge_height = 40000 - (40000 - 20000) * t_peak

        # Saddle points
        saddle_positions = [0.25, 0.55, 0.8]
        for sp in saddle_positions:
            saddle_effect = np.exp(-0.5 * ((t_ridge - sp) / 0.03)**2)
            ridge_height -= saddle_effect * (ridge_height - 29000) * 0.4

        # Asymmetric profile: gentle west (1500px), steep east (400px)
        row_x = np.arange(SIZE)
        west_slope = np.exp(-0.5 * np.clip(ridge_cx - row_x, 0, None)**2 / (750**2))
        east_slope = np.exp(-0.5 * np.clip(row_x - ridge_cx, 0, None)**2 / (200**2))
        profile = np.where(row_x <= ridge_cx, west_slope, east_slope)

        contribution = profile * (ridge_height - 10000)
        heightmap[iy, :] = np.maximum(heightmap[iy, :], 10000 + contribution)

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
    verdant_base = 20000 + t_verdant * 15000
    # Undulating character
    verdant_noise = make_perlin_noise((SIZE, SIZE), scale=600, octaves=4, seed=77)
    verdant_variation = verdant_noise * 10000
    verdant_total = verdant_base + verdant_variation
    heightmap = np.where(
        verdant_mask & (verdant_total > heightmap),
        verdant_total, heightmap
    )

    # Wellspring basin at (7000, 3800)
    well_dist2 = (xx - 7000)**2 + (yy - 3800)**2
    well_radius = 200
    well_mask = np.exp(-well_dist2 / (2 * (well_radius * 0.6)**2))
    heightmap = heightmap * (1 - well_mask) + 44000 * well_mask

    # =========================================================================
    # 6. MISTWATER LAKE
    # =========================================================================
    print("Painting Mistwater Lake...")
    lake_cx, lake_cy = 4300, 3300
    lake_radius = 1000
    lake_dist2 = (xx - lake_cx)**2 + (yy - lake_cy)**2
    # Smooth bowl: Gaussian subtraction
    lake_bowl = np.exp(-lake_dist2 / (2 * (lake_radius * 0.65)**2))
    surrounding_elev = 10500
    lake_floor = 8000
    heightmap = heightmap - lake_bowl * (surrounding_elev - lake_floor)
    # Build the lake mask for noise protection
    lake_mask = np.where(lake_dist2 < (lake_radius * 1.1)**2, 1.0, 0.0)

    # =========================================================================
    # 8. SOUTHERN BOUNDARY
    # =========================================================================
    print("Painting southern boundary...")
    mask_south = yy > 6000
    t_south = np.clip((yy - 6000) / (SIZE - 6000), 0, 1)
    south_elev = 9000 - t_south * 4000
    heightmap = np.where(mask_south, np.minimum(heightmap, south_elev), heightmap)

    # =========================================================================
    # 9. SE MARSHLAND
    # =========================================================================
    print("Painting SE marshland...")
    marsh_cx, marsh_cy = 5500, 5500
    marsh_dist2 = (xx - marsh_cx)**2 + (yy - marsh_cy)**2
    marsh_radius = 800
    marsh_effect = np.exp(-marsh_dist2 / (2 * (marsh_radius * 0.7)**2))
    marsh_floor = 6500
    heightmap = heightmap * (1 - marsh_effect) + marsh_floor * marsh_effect

    # Marsh pools
    rng = np.random.default_rng(123)
    for _ in range(7):
        pool_x = marsh_cx + rng.integers(-500, 500)
        pool_y = marsh_cy + rng.integers(-500, 500)
        pool_r = rng.integers(20, 40)
        pool_depth = rng.integers(200, 300)
        pool_dist2 = (xx - pool_x)**2 + (yy - pool_y)**2
        pool_mask = np.exp(-pool_dist2 / (2 * (pool_r * 0.6)**2))
        heightmap -= pool_mask * pool_depth

    # =========================================================================
    # 2. RIVER SERPENTIS
    # =========================================================================
    print("Carving River Serpentis...")
    # Define centerline control points with increasing meander
    # NE start: (6100, 2300) -> SW exit: (2000, 6200)
    num_pts = 5000
    t_river = np.linspace(0, 1, num_pts)

    # Base diagonal path
    base_x = 6100 + (2000 - 6100) * t_river
    base_y = 2300 + (6200 - 2300) * t_river

    # Add meanders that increase toward SW
    meander_amp = 50 + 350 * t_river**1.5   # Amplitude grows
    meander_freq = 0.008 + 0.004 * t_river   # Frequency increases slightly
    # Perpendicular offset (perpendicular to NE-SW diagonal)
    angle = np.arctan2(6200 - 2300, 2000 - 6100)
    perp_angle = angle + np.pi / 2
    cumulative_phase = np.cumsum(meander_freq)
    offset = meander_amp * np.sin(2 * np.pi * cumulative_phase)

    river_cx = base_x + offset * np.cos(perp_angle)
    river_cy = base_y + offset * np.sin(perp_angle)

    # Clip to bounds
    river_cx = np.clip(river_cx, 0, SIZE - 1)
    river_cy = np.clip(river_cy, 0, SIZE - 1)

    # Carve with varying width and depth along the path
    print("  Carving channel (this takes a moment)...")
    # Process in chunks for memory efficiency
    chunk_step = 3  # Process every 3rd point for performance
    for i in range(0, num_pts, chunk_step):
        t = t_river[i]
        px, py = river_cx[i], river_cy[i]

        # Width and depth vary along river
        if t < 0.2:    # NE section
            width = 30
            depth = 9500
            fp_width = 50
        elif t < 0.5:  # Mid section
            width = 50
            depth = 7200 + (9500 - 7200) * (0.5 - t) / 0.3
            fp_width = 100
        elif t < 0.75: # Near Hollowford
            width = 80
            depth = 5800
            fp_width = 250
        else:           # SW exit
            width = 70
            depth = 5000 + (5800 - 5000) * (1.0 - t) / 0.25
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
            fp_val = 6500 + (8500 - 6500) * (dist / (fp_width + half_w))
            fp_val = np.clip(fp_val, 6500, 8500)
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
        ("Hollowford",  3300, 4900, 600,  8500),
        ("Ironwood",    2600, 2900, 150, 18000),
        ("Ashford",     2100, 1900, 125, 24000),
        ("Grainfell",   5600, 2900, 200, 12000),
        ("Southwatch",  5900, 6000, 150,  9000),
    ]
    for name, sx, sy, radius, value in settlements:
        dist2 = (xx - sx)**2 + (yy - sy)**2
        # Smooth plateau with Gaussian blend at edges
        inner_r = radius * 0.7
        blend = np.clip(1.0 - (np.sqrt(dist2) - inner_r) / (radius - inner_r), 0, 1)
        blend = blend**2  # Smooth falloff
        # Blend toward plateau value
        heightmap = heightmap * (1 - blend) + value * blend
        # Mark plateau for noise protection
        plateau_mask = np.maximum(plateau_mask,
                                  np.where(dist2 < (radius * 1.2)**2, 1.0, 0.0))

    # =========================================================================
    # 10. TRIBUTARY CHANNELS
    # =========================================================================
    print("Carving tributary channels...")
    # Define 12 tributaries as start/end points flowing toward the Serpentis
    tributaries = [
        # West-side feeders (from higher western terrain)
        ((1500, 2800), (3800, 3200), 6, 150),
        ((1200, 3500), (3500, 3800), 7, 180),
        ((1800, 4200), (3200, 4600), 5, 120),
        ((2000, 5500), (2800, 5800), 6, 160),
        ((1500, 5000), (2900, 5200), 7, 140),
        ((2500, 6000), (2200, 6100), 5, 100),
        # East-side feeders (from ridge)
        ((6000, 2000), (5500, 2600), 6, 170),
        ((5800, 3000), (5000, 3500), 7, 150),
        ((5900, 3800), (4800, 4200), 5, 130),
        ((5600, 4500), (4500, 4800), 6, 160),
        ((5500, 5200), (4200, 5500), 7, 140),
        ((5700, 5600), (4500, 5900), 5, 120),
    ]

    for (sx, sy), (ex, ey), width, depth_cut in tributaries:
        num_t = 500
        t_trib = np.linspace(0, 1, num_t)
        trib_x = sx + (ex - sx) * t_trib
        trib_y = sy + (ey - sy) * t_trib
        # Small meander
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
    hill_amplitude = 800  # 500-1000 range
    hill_contribution = (hill_noise - 0.5) * 2 * hill_amplitude

    # Only apply to farmland elevations (7500-15000), not protected areas
    farmland_mask = ((heightmap >= 7500) & (heightmap <= 15000)).astype(np.float64)
    protection = np.maximum(river_mask, np.maximum(plateau_mask, lake_mask))
    farmland_mask *= (1 - protection)

    # Smooth the mask edges
    farmland_mask = gaussian_filter(farmland_mask, sigma=20)
    heightmap += hill_contribution * farmland_mask

    # =========================================================================
    # 13. SMOOTHING
    # =========================================================================
    print("Applying final smoothing...")
    smoothed = gaussian_filter(heightmap, sigma=4)

    # Protect river edges and cliff faces from smoothing
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
    img.save(f"{output_dir}/SeverantVale_Heightmap.png")
    print(f"  Saved: {output_dir}/SeverantVale_Heightmap.png")

    print("Saving 1024x1024 preview...")
    preview = img.resize((1024, 1024), Image.BILINEAR)
    preview.save(f"{output_dir}/SeverantVale_Heightmap_Preview.png")
    print(f"  Saved: {output_dir}/SeverantVale_Heightmap_Preview.png")

    # Print stats
    print(f"\nHeightmap stats:")
    print(f"  Min: {heightmap.min()} ({heightmap.min()/100:.0f}m)")
    print(f"  Max: {heightmap.max()} ({heightmap.max()/100:.0f}m)")
    print(f"  Mean: {heightmap.mean():.0f} ({heightmap.mean()/100:.0f}m)")
    print("Done!")


if __name__ == "__main__":
    t0 = time.time()
    generate_heightmap()
    print(f"Total time: {time.time() - t0:.1f}s")
