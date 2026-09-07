"""
Severant Vale Heightmap Generator v3
Generates a 16-bit grayscale PNG heightmap at 8129x8129 for UE5 landscape import.
8km x 8km map, 1 pixel = 1 meter.

UE5 value mapping (Scale Z = 400):
  pixel_value = 32768 + (elevation_meters * 32)
  32768 = Z origin (0m)
  Range: 0m-700m fits within 32768-55168 (well under 65535 max)

Changes from v2:
  1. Mistwater Lake: subtle 20m depression, not a crater
  2. River Serpentis: deeper (15-25m), wider, clearly visible from above
  3. Farmland: rolling hills with 15-25m amplitude, 300-600m wavelength
  4. Eastern Ridge: continuous N-S spine, Sunspear flat-top 400m, gradual west, steep east
  5. South boundary: nearly flat/open (Crimson Flats approach), only N/W walled
  6. Settlement plateaus: clearly flattened 150-600m radius circles
  7. 4-6 visible tributary channels at 8-12m depth
"""

import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter, zoom
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
        factor_y = shape[0] / grid_h
        factor_x = shape[1] / grid_w
        layer = zoom(low_res, (factor_y, factor_x), order=3)
        layer = layer[:shape[0], :shape[1]]
        noise += amplitude * layer
        amplitude *= 0.5
        freq *= 2.0
    noise = (noise - noise.min()) / (noise.max() - noise.min() + 1e-10)
    return noise


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
    # 1. NORTHERN FOOTHILLS
    # =========================================================================
    print("Painting northern foothills...")
    mask_north = yy < 2000
    t = np.clip((2000 - yy) / 2000.0, 0, 1)
    north_elev = BASELINE + t * (meters_to_pixel(500) - BASELINE)
    heightmap = np.where(mask_north, np.maximum(heightmap, north_elev), heightmap)

    # Northern peaks
    peaks = [
        (3000, 300, meters_to_pixel(650), 600),
        (5200, 450, meters_to_pixel(550), 500),
        (6800, 250, meters_to_pixel(600), 550),
        (1800, 500, meters_to_pixel(500), 450),
    ]
    for px, py, val, sigma in peaks:
        dist2 = (xx - px)**2 + (yy - py)**2
        peak_contrib = (val - BASELINE) * np.exp(-dist2 / (2 * sigma**2))
        heightmap += peak_contrib

    # Mountain pass at X=4065, Y=1000
    pass_dist2 = (xx - 4065)**2 + (yy - 1000)**2
    pass_depression = delta_to_pixel(200) * np.exp(-pass_dist2 / (2 * 400**2))
    heightmap -= pass_depression
    heightmap = np.clip(heightmap, 0, 65535)

    # =========================================================================
    # 2. WESTERN BOUNDARY (high terrain, walled)
    # =========================================================================
    print("Painting western boundary...")
    mask_west = xx < 1500
    t_west = np.clip((1500 - xx) / 1500.0, 0, 1)
    west_elev = BASELINE + t_west * (meters_to_pixel(380) - BASELINE)
    heightmap = np.where(mask_west, np.maximum(heightmap, west_elev), heightmap)

    # Canyon valleys running E-W
    canyons = [
        (700, 2000, 5500, 80, meters_to_pixel(160)),
        (500, 3800, 4500, 60, meters_to_pixel(170)),
        (900, 5200, 3000, 70, meters_to_pixel(150)),
    ]
    for cx, cy, length, width, floor_val in canyons:
        canyon_mask_x = np.exp(-0.5 * ((xx - cx) / (200))**2)
        canyon_mask_y = np.exp(-0.5 * ((yy - cy) / (length * 0.4))**2)
        canyon_effect = canyon_mask_x * canyon_mask_y
        heightmap = heightmap * (1 - canyon_effect) + floor_val * canyon_effect

    # =========================================================================
    # 3. EASTERN RIDGE — continuous N-S spine (FIX #4)
    #    Peak 400m at Sunspear with flat-topped summit.
    #    West face: gradual slope over 1-2km. East face: steep drop.
    # =========================================================================
    print("Painting eastern ridge (continuous spine)...")
    ridge_y_start = 1200
    ridge_y_end = 6200
    ridge_length = ridge_y_end - ridge_y_start

    for iy in range(max(0, ridge_y_start - 200), min(SIZE, ridge_y_end + 200)):
        t_ridge = np.clip((iy - ridge_y_start) / ridge_length, 0, 1)
        # Ridge center X drifts slightly west going south
        ridge_cx = 6500 + (6200 - 6500) * t_ridge

        # Height profile along the ridge: continuous spine
        # North end: 280m, builds to Sunspear peak 400m at t~0.45, tapers to 220m south
        if t_ridge < 0.45:
            t_peak = t_ridge / 0.45
            ridge_height_m = 280 + (400 - 280) * np.sin(t_peak * np.pi / 2)
        else:
            t_peak = (t_ridge - 0.45) / 0.55
            ridge_height_m = 400 - (400 - 220) * t_peak

        # Saddle points (reduced depth so ridge stays continuous)
        saddle_positions = [0.25, 0.6, 0.82]
        for sp in saddle_positions:
            saddle_effect = np.exp(-0.5 * ((t_ridge - sp) / 0.035)**2)
            ridge_height_m -= saddle_effect * 40  # 40m saddles

        ridge_height = meters_to_pixel(ridge_height_m)

        # Flat-topped summit area at Sunspear (t_ridge ~ 0.4-0.5)
        sunspear_flat = np.exp(-0.5 * ((t_ridge - 0.45) / 0.04)**2)

        # Asymmetric profile: gentle west (2km linear taper), steep east (400px Gaussian)
        row_x = np.arange(SIZE)
        west_dist = np.clip(ridge_cx - row_x, 0, None)
        east_dist = np.clip(row_x - ridge_cx, 0, None)
        # West: linear falloff over 2000px (2km), reaches zero cleanly
        west_reach = 2000.0
        west_slope = np.clip(1.0 - west_dist / west_reach, 0, 1)
        west_slope = west_slope**2  # Smooth quadratic taper
        # East: steep Gaussian drop (300px sigma)
        east_slope = np.exp(-0.5 * east_dist**2 / (300**2))
        profile = np.where(row_x <= ridge_cx, west_slope, east_slope)

        # For Sunspear summit, flatten the top by clamping the profile near peak
        if sunspear_flat > 0.3:
            summit_width = 400  # 400m flat-topped area
            summit_mask = np.abs(row_x - ridge_cx) < (summit_width / 2)
            profile = np.where(summit_mask, np.maximum(profile, sunspear_flat), profile)

        contribution = profile * (ridge_height - BASELINE)
        heightmap[iy, :] = np.maximum(heightmap[iy, :], BASELINE + contribution)

        # Track cliff faces on east side
        cliff_profile = np.where((row_x > ridge_cx) & (row_x < ridge_cx + 500),
                                 1.0, 0.0)
        cliff_mask[iy, :] = np.maximum(cliff_mask[iy, :], cliff_profile * profile)

    # =========================================================================
    # 4. VERDANTHEART TERRAIN (east of ridge)
    # =========================================================================
    print("Painting Verdantheart terrain...")
    verdant_mask = xx > 6500
    t_verdant = np.clip((xx - 6500) / 1600.0, 0, 1)
    verdant_base = meters_to_pixel(200) + t_verdant * delta_to_pixel(150)
    verdant_noise = make_perlin_noise((SIZE, SIZE), scale=600, octaves=4, seed=77)
    verdant_variation = verdant_noise * delta_to_pixel(100)
    verdant_total = verdant_base + verdant_variation
    heightmap = np.where(
        verdant_mask & (verdant_total > heightmap),
        verdant_total, heightmap
    )

    # Wellspring basin at (7000, 3800)
    well_dist2 = (xx - 7000)**2 + (yy - 3800)**2
    well_radius = 200
    well_mask = np.exp(-well_dist2 / (2 * (well_radius * 0.6)**2))
    heightmap = heightmap * (1 - well_mask) + meters_to_pixel(450) * well_mask

    # =========================================================================
    # 5. MISTWATER LAKE — subtle 20m depression (FIX #1)
    #    Surrounding terrain ~100m, lake floor ~80m. NOT a crater.
    # =========================================================================
    print("Painting Mistwater Lake (subtle depression)...")
    lake_cx, lake_cy = 4300, 3300
    lake_radius = 800  # Reduced from 1000 — tighter footprint
    lake_dist2 = (xx - lake_cx)**2 + (yy - lake_cy)**2

    # Use a sharper falloff so the depression stays local
    # Flat-bottomed bowl: full depth inside inner radius, tapers at edge
    lake_dist = np.sqrt(lake_dist2)
    lake_inner = lake_radius * 0.6  # Flat floor region
    lake_blend = np.clip(1.0 - (lake_dist - lake_inner) / (lake_radius - lake_inner), 0, 1)
    lake_blend = np.where(lake_dist < lake_inner, 1.0, lake_blend)
    lake_blend = lake_blend**2  # Smooth taper at edges

    # Only 20m depression from surrounding terrain
    lake_depth = delta_to_pixel(20)  # 20m drop, not 25m Gaussian crater
    heightmap -= lake_blend * lake_depth

    # Lake mask for noise protection
    lake_mask = np.where(lake_dist2 < (lake_radius * 1.1)**2, 1.0, 0.0)

    # =========================================================================
    # 6. SOUTHERN BOUNDARY — nearly flat, open (FIX #5)
    #    Crimson Flats approach: gently slopes DOWN toward south edge.
    #    NOT walled — open and exposed.
    # =========================================================================
    print("Painting southern boundary (open Crimson Flats)...")
    mask_south = yy > 6000
    t_south = np.clip((yy - 6000) / (SIZE - 6000), 0, 1)
    # Gentle downslope: 90m at Y=6000, dropping to 70m at map edge
    # Much less dramatic than v2's drop to 50m
    south_elev = meters_to_pixel(90) - t_south * delta_to_pixel(20)
    # Use minimum to carve down hills but DON'T raise flat terrain
    heightmap = np.where(mask_south, np.minimum(heightmap, south_elev), heightmap)

    # =========================================================================
    # 7. SE MARSHLAND
    # =========================================================================
    print("Painting SE marshland...")
    marsh_cx, marsh_cy = 5500, 5500
    marsh_dist2 = (xx - marsh_cx)**2 + (yy - marsh_cy)**2
    marsh_radius = 800
    marsh_effect = np.exp(-marsh_dist2 / (2 * (marsh_radius * 0.7)**2))
    marsh_floor = meters_to_pixel(65)
    heightmap = heightmap * (1 - marsh_effect) + marsh_floor * marsh_effect

    # Marsh pools
    rng = np.random.default_rng(123)
    for _ in range(7):
        pool_x = marsh_cx + rng.integers(-500, 500)
        pool_y = marsh_cy + rng.integers(-500, 500)
        pool_r = rng.integers(20, 40)
        pool_depth_m = rng.integers(2, 3)
        pool_dist2 = (xx - pool_x)**2 + (yy - pool_y)**2
        pool_mask = np.exp(-pool_dist2 / (2 * (pool_r * 0.6)**2))
        heightmap -= pool_mask * delta_to_pixel(pool_depth_m)

    # =========================================================================
    # 8. SETTLEMENT PLATEAUS — clearly flattened (FIX #6)
    #    Applied BEFORE river so the river carves through settlement areas.
    #    Each has a distinct flat circular area, 150-600m radius
    # =========================================================================
    print("Flattening settlement plateaus...")
    settlements = [
        ("Hollowford",  3300, 4900, 600,  meters_to_pixel(85)),   # Large town
        ("Ironwood",    2600, 2900, 250,  meters_to_pixel(180)),
        ("Ashford",     2100, 1900, 200,  meters_to_pixel(240)),
        ("Grainfell",   5600, 2900, 350,  meters_to_pixel(120)),
        ("Southwatch",  5900, 6000, 250,  meters_to_pixel(90)),
        ("Reach House", 3000, 3400, 50,   meters_to_pixel(150)),  # Wardens HQ, small fortified lodge
    ]
    for name, sx, sy, radius, value in settlements:
        dist2 = (xx - sx)**2 + (yy - sy)**2
        dist = np.sqrt(dist2)
        inner_r = radius * 0.7
        outer_r = radius * 1.0
        blend = np.clip(1.0 - (dist - inner_r) / (outer_r - inner_r), 0, 1)
        blend = blend * blend * (3 - 2 * blend)  # Cubic smoothstep
        heightmap = heightmap * (1 - blend) + value * blend
        plateau_mask = np.maximum(plateau_mask,
                                  np.where(dist2 < (radius * 1.3)**2, 1.0, 0.0))

    # =========================================================================
    # 9. RIVER SERPENTIS — deeper, wider, clearly visible (FIX #2)
    #    Channel 15-25m below surrounding terrain. Floodplain 500-800m near Hollowford.
    #    Applied AFTER settlements so river cuts through plateaus.
    # =========================================================================
    print("Carving River Serpentis (deeper channel)...")
    num_pts = 5000
    t_river = np.linspace(0, 1, num_pts)

    # Base diagonal path NE to SW (positions unchanged from v2)
    base_x = 6100 + (2000 - 6100) * t_river
    base_y = 2300 + (6200 - 2300) * t_river

    # Meanders increasing toward SW
    meander_amp = 50 + 350 * t_river**1.5
    meander_freq = 0.008 + 0.004 * t_river
    angle = np.arctan2(6200 - 2300, 2000 - 6100)
    perp_angle = angle + np.pi / 2
    cumulative_phase = np.cumsum(meander_freq)
    offset = meander_amp * np.sin(2 * np.pi * cumulative_phase)

    river_cx_arr = base_x + offset * np.cos(perp_angle)
    river_cy_arr = base_y + offset * np.sin(perp_angle)
    river_cx_arr = np.clip(river_cx_arr, 0, SIZE - 1)
    river_cy_arr = np.clip(river_cy_arr, 0, SIZE - 1)

    # --- Pre-sample surrounding terrain to compute absolute river floor ---
    # Sample terrain 400m perpendicular to river at each point (before carving)
    print("  Sampling surrounding terrain...")
    surround_elev = np.zeros(num_pts)
    perp_offset = 400  # Sample 400m to the side (outside floodplain)
    for i in range(num_pts):
        sx1 = int(np.clip(river_cx_arr[i] + perp_offset * np.cos(perp_angle), 0, SIZE - 1))
        sy1 = int(np.clip(river_cy_arr[i] + perp_offset * np.sin(perp_angle), 0, SIZE - 1))
        sx2 = int(np.clip(river_cx_arr[i] - perp_offset * np.cos(perp_angle), 0, SIZE - 1))
        sy2 = int(np.clip(river_cy_arr[i] - perp_offset * np.sin(perp_angle), 0, SIZE - 1))
        surround_elev[i] = max(heightmap[sy1, sx1], heightmap[sy2, sx2])
    # Smooth the sampled elevation to avoid noise
    from scipy.ndimage import uniform_filter1d
    surround_elev = uniform_filter1d(surround_elev, size=200)

    print("  Carving channel (this takes a moment)...")
    chunk_step = 2
    for i in range(0, num_pts, chunk_step):
        t = t_river[i]
        rpx, rpy = river_cx_arr[i], river_cy_arr[i]

        # River floor = surrounding terrain - depth_below (absolute target)
        if t < 0.2:       # NE section
            width = 60
            depth_below = 18
            fp_width = 100
        elif t < 0.5:     # Mid section
            width = 100
            depth_below = 22
            fp_width = 200
        elif t < 0.75:    # Near Hollowford — widest
            width = 150
            depth_below = 25
            fp_width = 600
        else:              # SW exit
            width = 120
            depth_below = 20
            fp_width = 300

        # Compute absolute river floor elevation
        river_floor = surround_elev[i] - delta_to_pixel(depth_below)

        half_w = width / 2
        margin = int(fp_width + half_w + 100)
        ipx, ipy = int(rpx), int(rpy)
        x_min = max(0, ipx - margin)
        x_max = min(SIZE, ipx + margin)
        y_min = max(0, ipy - margin)
        y_max = min(SIZE, ipy + margin)

        if x_max <= x_min or y_max <= y_min:
            continue

        local_xx, local_yy = np.meshgrid(
            np.arange(x_min, x_max), np.arange(y_min, y_max)
        )
        dist = np.sqrt((local_xx - rpx)**2 + (local_yy - rpy)**2)

        # Channel carve — blend toward absolute floor (no compounding)
        # Reduce carve strength inside settlement plateau cores
        channel_blend = np.exp(-0.5 * (dist / (half_w * 0.7))**2)
        local_plateau = plateau_mask[y_min:y_max, x_min:x_max]
        channel_blend = channel_blend * (1 - local_plateau * 0.85)  # 85% protection in plateaus
        region = heightmap[y_min:y_max, x_min:x_max]
        carved = region * (1 - channel_blend) + river_floor * channel_blend
        heightmap[y_min:y_max, x_min:x_max] = np.minimum(region, carved)

        # Floodplain: gentle depression toward river (skip inside plateaus)
        if 0.35 < t < 0.85:
            fp_floor = surround_elev[i] - delta_to_pixel(8)  # 8m below surrounding
            fp_blend = np.exp(-0.5 * (dist / (fp_width * 0.45))**2)
            fp_blend = np.clip(fp_blend - channel_blend, 0, 1)
            fp_blend = fp_blend * (1 - local_plateau)  # No floodplain in settlements
            current = heightmap[y_min:y_max, x_min:x_max]
            fp_carved = current * (1 - fp_blend) + fp_floor * fp_blend
            heightmap[y_min:y_max, x_min:x_max] = np.minimum(current, fp_carved)

        # Update river mask (wider for protection)
        river_channel = dist < (half_w * 3)
        river_mask[y_min:y_max, x_min:x_max] = np.maximum(
            river_mask[y_min:y_max, x_min:x_max],
            river_channel.astype(np.float64)
        )

    # =========================================================================
    # 10. TRIBUTARY CHANNELS — 4-6 visible channels, 8-12m deep (FIX #7)
    # =========================================================================
    print("Carving tributary channels (visible from aerial)...")
    tributaries = [
        # West-side feeders (from higher western terrain into river)
        # (start_xy, end_xy, width_px, depth_meters)
        ((1400, 3000), (3600, 3400), 25, 12),   # NW feeder into mid-river
        ((1300, 4200), (3100, 4700), 22, 10),   # W feeder near Hollowford
        ((1600, 5300), (2700, 5600), 20, 9),    # SW feeder
        # East-side feeders (from ridge down to river)
        ((5900, 2200), (5200, 2800), 25, 11),   # NE feeder from ridge
        ((5700, 3500), (4700, 4000), 22, 10),   # E feeder mid-section
        ((5500, 4800), (4300, 5200), 20, 9),    # SE feeder
    ]

    for (sx, sy), (ex, ey), trib_width, depth_m in tributaries:
        num_t = 800
        t_trib = np.linspace(0, 1, num_t)
        trib_x = sx + (ex - sx) * t_trib
        trib_y = sy + (ey - sy) * t_trib
        # Gentle sinusoidal meander
        trib_x += 40 * np.sin(t_trib * 6 * np.pi)
        trib_y += 25 * np.cos(t_trib * 5 * np.pi)

        half_w = trib_width / 2
        depth_cut = delta_to_pixel(depth_m)

        for i in range(0, num_t, 3):
            tpx, tpy = int(trib_x[i]), int(trib_y[i])
            margin = int(half_w + 30)
            x_min = max(0, tpx - margin)
            x_max = min(SIZE, tpx + margin)
            y_min = max(0, tpy - margin)
            y_max = min(SIZE, tpy + margin)
            if x_max <= x_min or y_max <= y_min:
                continue
            local_xx, local_yy = np.meshgrid(
                np.arange(x_min, x_max), np.arange(y_min, y_max)
            )
            dist = np.sqrt((local_xx - tpx)**2 + (local_yy - tpy)**2)
            blend = np.exp(-0.5 * (dist / (half_w * 0.6))**2)
            # Taper depth: full at start (headwaters), full at end (confluence)
            t_depth = 0.8 + 0.2 * (2 * abs(t_trib[i] - 0.5))
            region = heightmap[y_min:y_max, x_min:x_max]
            # Use absolute floor (region center minus depth) to avoid compounding
            trib_floor = region - depth_cut * t_depth
            carved = region * (1 - blend) + trib_floor * blend
            heightmap[y_min:y_max, x_min:x_max] = np.minimum(region, carved)

    # =========================================================================
    # 11a. RESTORE SETTLEMENT CORES after river/tributary carving
    #      Re-flatten inner 50% of each settlement to guarantee correct elevation
    # =========================================================================
    print("Restoring settlement cores...")
    for name, sx, sy, radius, value in settlements:
        core_radius = radius * 0.5  # Inner half
        dist2 = (xx - sx)**2 + (yy - sy)**2
        dist = np.sqrt(dist2)
        blend = np.clip(1.0 - dist / core_radius, 0, 1)
        blend = blend**2  # Smooth taper
        heightmap = heightmap * (1 - blend) + value * blend

    # =========================================================================
    # 11b. ROLLING HILLS — stronger Perlin noise on farmland (FIX #3)
    #     Amplitude 15-25m, wavelength 300-600m
    # =========================================================================
    print("Adding rolling hills noise (stronger)...")
    # Two noise layers at different wavelengths for natural variation
    hill_noise_1 = make_perlin_noise((SIZE, SIZE), scale=450, octaves=5, seed=99)
    hill_noise_2 = make_perlin_noise((SIZE, SIZE), scale=300, octaves=4, seed=137)
    # Combined: 15m from first layer + 8m from second = up to ~23m variation
    hill_amplitude_1 = delta_to_pixel(15)  # 15m (was 8m in v2)
    hill_amplitude_2 = delta_to_pixel(8)   # 8m secondary
    hill_contribution = ((hill_noise_1 - 0.5) * 2 * hill_amplitude_1 +
                         (hill_noise_2 - 0.5) * 2 * hill_amplitude_2)

    # Only apply to farmland elevations (75m-160m), not protected areas
    farmland_mask = ((heightmap >= meters_to_pixel(75)) &
                     (heightmap <= meters_to_pixel(160))).astype(np.float64)
    protection = np.maximum(river_mask, np.maximum(plateau_mask, lake_mask))
    farmland_mask *= (1 - protection)

    farmland_mask = gaussian_filter(farmland_mask, sigma=25)
    heightmap += hill_contribution * farmland_mask

    # =========================================================================
    # 12. SMOOTHING
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

    output_dir = "C:/Users/kyler/OneDrive/Desktop/ShatteredDominion/Assets/3D/Exports/Environment"

    print("Saving full-resolution heightmap (8129x8129)...")
    img = Image.fromarray(heightmap, mode='I;16')
    img.save(f"{output_dir}/SeverantVale_Heightmap_v3.png")
    print(f"  Saved: {output_dir}/SeverantVale_Heightmap_v3.png")

    print("Saving 1024x1024 preview...")
    preview = img.resize((1024, 1024), Image.BILINEAR)
    preview.save(f"{output_dir}/SeverantVale_Heightmap_v3_Preview.png")
    print(f"  Saved: {output_dir}/SeverantVale_Heightmap_v3_Preview.png")

    # Print stats with UE5 mapping
    print(f"\nHeightmap stats (UE5 Scale Z = 400):")
    hmin, hmax, hmean = int(heightmap.min()), int(heightmap.max()), float(heightmap.mean())
    print(f"  Min pixel: {hmin}  -> {(hmin - 32768) / 32:.1f}m")
    print(f"  Max pixel: {hmax}  -> {(hmax - 32768) / 32:.1f}m")
    print(f"  Mean pixel: {hmean:.0f} -> {(hmean - 32768) / 32:.1f}m")
    print(f"  Origin (0m) = pixel 32768")
    print(f"\nKey landmark verification:")
    landmarks = [
        ("Hollowford (85m)", 3300, 4900, 85),
        ("Ironwood (180m)", 2600, 2900, 180),
        ("Ashford (240m)", 2100, 1900, 240),
        ("Grainfell (120m)", 5600, 2900, 120),
        ("Southwatch (90m)", 5900, 6000, 90),
        ("Mistwater Lake center (80m)", 4300, 3300, 80),
        ("Reach House (150m)", 3000, 3400, 150),
    ]
    for name, lx, ly, expected_m in landmarks:
        actual_px = int(heightmap[ly, lx])
        actual_m = (actual_px - 32768) / 32
        print(f"  {name}: pixel={actual_px}, actual={actual_m:.1f}m, expected={expected_m}m")

    # River depth check — sample a few points along the river
    print(f"\nRiver depth verification (should be 15-25m below surrounding):")
    river_checks = [
        ("NE section (t=0.1)", 0.1),
        ("Mid section (t=0.35)", 0.35),
        ("Hollowford (t=0.65)", 0.65),
        ("SW exit (t=0.9)", 0.9),
    ]
    for label, t_check in river_checks:
        idx = int(t_check * (num_pts - 1))
        rx, ry = int(river_cx_arr[idx]), int(river_cy_arr[idx])
        river_elev = (int(heightmap[ry, rx]) - 32768) / 32
        # Check 200m to the side for surrounding terrain
        side_x = min(SIZE - 1, rx + 200)
        surround_elev = (int(heightmap[ry, side_x]) - 32768) / 32
        print(f"  {label}: river={river_elev:.1f}m, surround(+200px)={surround_elev:.1f}m, "
              f"depth={surround_elev - river_elev:.1f}m")

    print("\nDone!")


if __name__ == "__main__":
    t0 = time.time()
    generate_heightmap()
    print(f"Total time: {time.time() - t0:.1f}s")
