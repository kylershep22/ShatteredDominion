# THE SHATTERED DOMINION — UE5 WORLD IMPLEMENTATION PLAN
## Version 1.0 | Depends on: SD-08, SD-10, SD-13, SD UE5 Architecture, World Map

---

## Status: What Has Already Been Established

The earlier thread (March 28, 2026) and existing project documents have established:

- **UE5 architecture is defined** — project folder structure, naming conventions, subsystem architecture, component patterns, Blueprint vs C++ boundary, and anti-patterns are documented in the SD UE5 Architecture skill
- **Map size is finalized** — ~20 km² Severant Vale, not 120 km² (SD-08 v3.0 revision)
- **Sightline architecture was identified as the most important pre-build task** — three specific sightlines were named: Hollowford north gate → Mistwater Lake, Sunspear Ridge → Verdantheart canopy, eastern ridge → Hollowford
- **Wilderness traversal map was recommended** — SD-13 now provides this: visual hooks at 500m intervals along all four road corridors, with specific POIs, discovery tiers, and payoffs per hook
- **Three-layer Verdantheart verticality was specified** — ground (0–5m), lower canopy (15–30m), upper canopy (40–60m), each with distinct lighting and traversal
- **Atmospheric treatment per zone was identified** — valley mist, Verdantheart canopy haze, Mistwater fog, corruption post-process
- **Interactive world map exists** — all settlements, dungeons, corruption zones, POIs, water features, roads, and biomes are spatially positioned

This plan builds directly on all of the above. Nothing here contradicts or replaces those decisions.

---

## Critical Dependency: What Must Exist Before World Building

The MVP roadmap (SD-10) Phase 1 Pre-Production specifies four prototype gates that must pass before committing to full world construction. Two of them directly gate world building:

1. **Proto-2: World state system** — Two locations, three Act state variants each. This validates that the flag system works before you build 15+ locations that depend on it.
2. **Proto-7: Corruption zone dynamic expansion** — Zone 1 (Ashfield Scar) expansion applied to geometry. Validates that corruption zone boundaries can change at runtime.

If you build the full world terrain before these prototypes pass, you risk discovering that your corruption zone implementation requires a different terrain approach, or that your world state transitions need scene reloads instead of streaming — either of which could force a terrain rebuild.

**Recommendation:** Run this plan's Phases 0–2 (project setup through terrain blockout) in parallel with Proto-2 and Proto-7 prototyping. Do not proceed past Phase 2 into biome detailing until both prototypes pass their Go/No-Go gates. The terrain blockout itself is safe — it's the content placed on it that becomes expensive to redo.

---

## Phase 0 — Project Setup and Pre-Build Work (Week 1–2)

### 0.1 UE5 Project Configuration

Create the project using the folder structure from the SD UE5 Architecture skill exactly as documented. Key settings for world building:

- **Enable World Partition** in Project Settings. This is non-negotiable for a ~20 km² map — without it, the entire world loads simultaneously and performance is unmanageable.
- **Set World Partition cell size to 256m × 256m** for the Vale. This gives you roughly 625–700 cells for the playable area. Fine enough for meaningful streaming control without excessive overhead.
- **Enable Nanite** for environment meshes (rocks, cliffs, hero trees). Nanite handles LOD automatically, which eliminates one of the most time-consuming aspects of environment art for a small team.
- **Enable Lumen** for global illumination. Severant Vale's biomes depend heavily on lighting mood — the dappled forest shade, the corruption zone purple override, the Verdantheart perpetual twilight. Lumen delivers this without manual light probe placement.
- **Set up a Landscape with 4 components** — one per quadrant (NW, NE, SW, SE). Each component can be independently edited and streamed.

### 0.2 Reference Material Import

Import the interactive world map and the key reference images/documents into the project as reference material. Specifically:

- Create a top-down reference texture from the world map showing terrain zones, settlement positions, road paths, and water features. This gets applied as an overlay on the landscape while you sculpt.
- Import the SD-13 road corridor tables as a reference DataTable so visual hook positions can be placed at correct intervals during blockout.

### 0.3 Scale Calibration

Before sculpting anything, calibrate your sense of scale in UE5:

- The Vale is ~20 km² — roughly 5 km × 4.5 km oval (east-west elongated).
- Hollowford's walled city is ~0.5 km² (approximately 700m × 650m). In UE5 units (1 unit = 1 cm), that's 70,000 × 65,000 units. At 256m cell size, Hollowford occupies roughly a 3×3 grid of cells.
- River Serpentis is 30–50m wide (3,000–5,000 units) in the hills, 80m (8,000 units) near Hollowford.
- The 300–350m visual hook interval from SD-13 is 30,000–35,000 UE5 units — roughly 1–2 World Partition cells.

Place scale reference actors at key locations: a 1.8m capsule (human height), a 30m cube (tree height in border forest), a 100m cube (worldroot tree height in Verdantheart inner ring). Use these to gut-check everything.

---

## Phase 1 — Terrain Foundation (Weeks 3–6)

### 1.1 Heightmap Sculpting

This is the most consequential single task in world building. The terrain shape determines sightlines, river flow, settlement placement, and the player's moment-to-moment experience of traversal. Get this right before anything else.

**Elevation zones from the docs:**

| Zone | Elevation | Location |
|---|---|---|
| River valley (Hollowford) | 50–100m | SW quadrant |
| Rolling hills (farmland) | 100–200m | Central, NE |
| Northern foothills | 150–300m | N edge, rising toward Highwinter |
| Eastern ridge | 200–400m | E edge, overlooks Verdantheart |
| Southern borderlands | 75–150m | SE, gradual slope toward Crimson Flats |
| Verdantheart border forest | 200–350m | E of Vale |
| Verdantheart inner ring | 400–500m | Deep forest, ancient groves |
| Wellspring basin | 450m (10m depression) | Center of Verdantheart |

**Sculpting priorities (in order):**

1. **River Serpentis valley first** — carve the main river channel from NE to SW. This is the lowest point in the map and everything drains toward it. The channel should be narrow and steep-sided in the NE hills (V-shaped), then broaden into a wide floodplain in the lowlands near Hollowford (U-shaped, lazy meanders).

2. **Eastern ridge second** — the 200–400m elevation spine along the eastern edge. This ridge is the dramatic backdrop visible from most of the Vale and the overlook point where players see Verdantheart's canopy below. Make it steep on the Verdantheart (east) side, rolling on the Vale (west) side.

3. **Settlement plateaus** — flatten areas where each settlement sits. Hollowford needs a ~0.5 km² flat area at 85m elevation on the river. Grainfell needs a gentle rolling area at 120m. Ashford needs a higher shelf at 240m near rocky terrain. Ironwood needs a forest clearing at 180m. Southwatch needs flat borderlands at 90m.

4. **Northern foothills** — gentle rising terrain toward the N edge where Highwinter's mountains would be (off-map, but the foothills are playable).

5. **Tributary valleys** — 12+ creek channels feeding into the Serpentis. These don't need to be deep, but they should be visible depressions in the terrain that guide water flow logically.

6. **Mistwater Lake basin** — a natural depression at north-central (~445, 285 in map coords) large enough for an 800m diameter lake.

### 1.2 Sightline Validation (Critical Gate)

Before proceeding, validate the three sightlines identified in the earlier thread by placing the camera at each point and confirming:

1. **From Hollowford's north gate** — Mistwater Lake area visible as a low depression on the horizon. In the final game, fog fills this depression. At blockout stage, just confirm the terrain doesn't block the view.

2. **From Sunspear Ridge (eastern hills, ~400m)** — clear line of sight downward into the Verdantheart canopy zone to the east and back westward across the Vale to Hollowford. This must be a panoramic moment. If terrain blocks either view, re-sculpt.

3. **From the eastern ridge path (any point at ~300m)** — Hollowford visible in the river valley below. The player should feel the "I came from there" moment looking back at where they started.

Additionally, validate SD-13's road corridor hooks: stand at each road junction and confirm you can see at least one horizon-line feature in a non-road direction. At blockout stage, these are terrain features (ridge, hill, depression) that will later get content placed on them.

**Do not proceed to Phase 2 until all three sightlines work.** Reshaping terrain is cheap now and catastrophically expensive later.

### 1.3 World Boundary Treatment

The playable area needs boundaries that feel natural, not like invisible walls. The docs specify:

- **North:** Terrain rises steeply toward impassable mountain foothills (Highwinter). Slopes above 45° with snow-dusted rock.
- **West:** Canyon walls and fog-choked highland approaches (Hollow Crown). Dense fog volume + steep terrain.
- **South:** Heat-hazed volcanic borderlands (Crimson Flats). Increasing heat distortion + toxic corruption zone preventing passage.
- **East:** Verdantheart's dense forest serves as a soft boundary where you can enter the playable Verdantheart region but not pass through to the far east.

At blockout stage, sculpt the terrain for these boundaries. The atmospheric effects come later in Phase 5.

---

## Phase 2 — Water System (Weeks 5–8, overlaps with Phase 1)

### 2.1 River Serpentis Implementation

The river is the second most important terrain feature after the heightmap itself. It defines the Vale's character.

**UE5 approach:** Use UE5's Water system (Water Body River actor) for the Serpentis. This provides:
- Automatic spline-based river mesh that follows terrain
- Built-in water shader with flow direction, depth coloring, and surface reflection
- Buoyancy support for future gameplay (boats, floating objects)
- Automatic landscape deformation along the river path

**River character changes along its length (from SD docs):**

| Section | Width | Character | UE5 Treatment |
|---|---|---|---|
| NE source (from Verdantheart) | 30m | Straighter, whitewater over rocks | Fast flow speed, foam particles, narrow spline width |
| Mid-vale transition | 40m | Beginning to meander | Moderate flow, wider spline, some S-curves |
| Near Hollowford | 80m | Wide, lazy, pronounced meanders | Slow flow speed, wide spline, dramatic S-curves, oxbow hints |
| Past Hollowford SW | 50–60m | Continued lazy flow | Moderate width, continued meandering |

**Spline placement:** Follow the river path from the world map. Place spline control points every 200–300m. In the hills, fewer points (straighter). In the lowlands, many more points with offset to create natural S-curves. Reference real rivers at similar scales — the River Severn or River Wye in the UK are good analogs for the lowland sections.

### 2.2 Tributaries

12 named streams feed into the Serpentis. Use Water Body River actors at smaller scale for the larger ones (Highland Brook, Mistwater Creek, Ironwood Run, Ridge Run). Use simple spline meshes with a water material for the smaller ones (Spring Creek, Memorial Brook, etc.).

Each tributary should follow the terrain's natural drainage — water flows downhill. If a creek path doesn't follow terrain slope, either adjust the creek path or adjust the terrain.

### 2.3 Mistwater Lake

Use a Water Body Lake actor. 800m diameter, positioned in the north-central depression. The corruption zone around it (Mistwater Shores) will be implemented in Phase 4, but the lake itself goes in now because it affects terrain and drainage.

### 2.4 Seasonal Ponds and Marshland

**Seasonal ponds (7):** Small Water Body Lake actors scattered in the lowlands. These can be toggled visible/invisible based on the in-game season system if implemented, or left permanent for the MVP.

**SE Marshland near Southwatch:** This is a distinct sub-biome. Create a low-lying flat area (elevation 50–75m) with poor drainage. Multiple standing water pools. The terrain here should be nearly flat with slight depressions for each pool. This area will get distinct material layers (mud, wet ground) and foliage (reeds, cattails) in Phase 3.

### 2.5 Verdantheart Water Features

Five streams radiate outward from the Wellspring position. The West Fork is the most important — it exits the forest at the western border and feeds the River Serpentis. Implement this as a Water Body River actor that connects to the main Serpentis spline.

The Wellspring pool itself (100m diameter, center of Verdantheart) is a special case — it's described as "liquid arcane energy, not water" with unique visual properties (mirror-smooth, blue-green glow, 37°C). This needs a custom water material, not the default river shader. Defer the custom material to Phase 5; for now, place a Water Body Lake actor as a placeholder.

---

## Phase 3 — Biome Foundation and Landscape Materials (Weeks 7–12)

### 3.1 Landscape Material Setup

UE5's Landscape material system uses layer blending to paint different terrain types. You need material layers for each biome:

| Layer | Biome Coverage | Key Visual Properties |
|---|---|---|
| Farmland soil | 40% of Vale | Rich dark earth, high fertility look |
| Grass meadow | Blended with farmland | Tall grasses, wildflowers |
| Forest floor | 35% of Vale | Leaf litter, moss, roots, dark |
| Rocky ground | 15% of Vale | Exposed granite/limestone, lichen |
| Wetland mud | 7% of Vale | Wet, dark, unstable-looking |
| Corruption ground | 3% of Vale | Black-veined, crystallized, dead |
| Verdantheart forest floor | Verdantheart | Dense moss, bioluminescent undertone |
| Snow/frost | N boundary only | Permafrost, dusted snow on rock |

**Implementation note:** Start with 4–5 material layers (farmland, forest, rock, wetland, corruption) and add the rest as needed. Each additional layer increases the material's shader complexity. Nanite-compatible landscape materials have specific constraints — test performance early.

### 3.2 Material Painting Pass

Paint the landscape material layers following the biome distribution from the docs and the world map:

- **River valley and SW quadrant:** Farmland soil + grass meadow
- **N and NE hills:** Forest floor (deciduous/conifer mix)
- **Eastern ridge:** Rocky ground transitioning to forest floor
- **SE near Southwatch:** Wetland mud, dry grass
- **Corruption zone positions:** Corruption ground (initially small, matching Act I sizes)

This is a rough first pass. Fine detail comes in Phase 6.

### 3.3 Foliage Foundation

UE5's Procedural Foliage System can scatter trees, bushes, and ground cover based on landscape layers. Set up foliage types:

**Trees (priority order for blockout):**
1. Deciduous oak/ash (farmland borders, forest biome)
2. Coniferous pine/fir (northern areas, higher elevation)
3. Willow (riverbanks only)
4. Birch (scattered, lighter forest areas)
5. Dead/corrupted tree variants (corruption zones)

**Understory:**
1. Ferns and shrubs (forest biome)
2. Tall grasses (farmland, meadows)
3. Reeds and cattails (wetlands, riverbanks)

**For blockout:** Use UE5's starter content trees or Quixel Megascans trees. Do not invest in custom tree assets yet. The blockout needs to establish density, canopy coverage, and visual character — not final art quality.

**Density targets from docs:**
- Farmland: Low to medium vegetation density
- Forest: Medium to high (visibility 10–30m in dense areas)
- Rocky hills: Very low (rock dominates)
- Wetlands: High (reeds limit visibility)
- Corruption: Dead trees, fungal growths, sparse

### 3.4 Verdantheart Foliage (Special Case)

Verdantheart's concentric ring structure requires dramatically different tree scales:

| Ring | Tree Height | Trunk Diameter | Foliage Approach |
|---|---|---|---|
| Border (outer) | 20–30m | 1–2m | Standard forest foliage, dense |
| Deep forest (middle) | 40–60m | 3–5m | Scaled-up trees, canopy blocks sky |
| Ancient grove (inner) | 80–100m | 8–12m | Hero tree assets (custom later), massive scale |
| Corrupted Deepwood | 30–50m (dying) | Variable | Dead/twisted variants, fungal meshes |

**For blockout:** Use scaled-up versions of standard trees for the middle and inner rings. The scale alone communicates the concentric ring concept. Custom worldroot tree meshes are a Phase 6 (or later) task.

---

## Phase 4 — Infrastructure and Settlement Blockout (Weeks 10–16)

### 4.1 Road Network

Place the four primary road corridors as spline actors:

- **Corridor A:** Hollowford → Ironwood (SW to NW, ~3 km)
- **Corridor B:** Hollowford → Grainfell (SW to NE, ~2.5 km)
- **Corridor C:** Hollowford → Ashford (SW to NW, ~2.2 km)
- **Corridor D:** Hollowford → Southwatch (SW to SE, ~2.5 km)

Roads should follow terrain contours naturally — they don't go straight up hills, they switchback. They should be wider near settlements (6–8m, wagon traffic) and narrower in wilderness (3–4m, foot traffic).

Use a road spline mesh with a dirt/gravel material. Add stone bridges at river crossings.

### 4.2 Settlement Blockout (Greybox)

**Hollowford** is the largest and most complex. At blockout stage:
- Place the city wall perimeter (8m high, ~0.5 km² / 700m × 650m)
- Place the 4 gates (North, South, East, West)
- Block out the 5 district boundaries using simple geometry
- Place the River Serpentis passing through the city
- Place the refugee camp area outside the south gate

Do NOT detail interiors yet. The goal is spatial relationships and scale validation.

**Frontier settlements** (Ironwood, Ashford, Grainfell, Southwatch):
- Place 5–10 simple building volumes per settlement
- Place the settlement's defining feature (Ironwood: lumber yard; Ashford: mine entrance; Grainfell: farm plots; Southwatch: fortified walls + tent camp)
- Validate that the settlement is visible from the nearest road corridor at the distance the design docs specify

### 4.3 Dungeon Entrance Placement

Place entrance markers (not full dungeons) at:
- **The Sepulcher** — SW, underground vault entrance in a hillside
- **Verdant Temple** — NE, overgrown stone entrance near Verdantheart border
- **Sunken Hollow Vault** — South-central, sinkhole in terrain
- **Ashenveil Archive** — NE mountains, carved into cliff face at high elevation

These are just entrance points for now. Dungeon interiors are separate sub-levels that get built later.

### 4.4 Corruption Zone Initial Placement

Place the five corruption zones at their Act I sizes:

1. **Ashfield Scar** — NE near Grainfell, ~0.15 km²
2. **Mistwater Shores** — Around Mistwater Lake, ~0.4 km²
3. **Broken Road** — ~400m linear strip on Hollowford–Ashford road
4. **Sunken Hollow** — South-central, ~0.3 km² circular
5. **Corruption Front** — Eastern Vale, ~0.8 km² (largest)

At blockout, these are post-process volumes with the purple-pink color grade override, plus the corruption ground material layer painted on the landscape within their bounds. Full corruption VFX (crystal growths, floating motes, energy tendrils) come in Phase 6.

### 4.5 Refugee Camp Placement

Place tent cluster blockouts at:
- **Emberhaven** — Near Southwatch, SE
- **Greenwatch** — Near Verdantheart border, east
- **Frostborn Camp** — NW area, military tent layout

---

## Phase 5 — Atmospheric Systems (Weeks 14–18)

### 5.1 Time of Day and Weather

Set up UE5's Directional Light + Sky Atmosphere for a day/night cycle. The Vale's lighting moods from the docs:

- **Dawn:** Soft, warm, mist in river valley
- **Midday:** Bright, open (farmland), dappled shade (forest), harsh direct (rocky hills)
- **Dusk:** Golden hour, dramatic light shafts through trees, Wellspring begins to glow
- **Night:** Dark (torches essential in forest), Mistwater Lake fog glows faintly, aurora effects in sky

**Post-Severance weather additions:**
- Arcane storms (purple lightning, unnatural wind)
- Sudden frosts (frost shader overlay on ground materials)
- Aurora effects from lingering lattice energy (sky particle system)

### 5.2 Zone-Specific Atmosphere

Each area needs its own atmospheric treatment using UE5's Exponential Height Fog and Post Process Volumes:

| Zone | Fog Treatment | Post-Process |
|---|---|---|
| Vale valley floor | Low-lying morning mist, burns off by 10am game-time | Default, warm tint |
| Forest biome | Light haze, humidity | Slightly cooler tint, reduced contrast |
| Corruption zones | Dense purple-tinted fog | Purple-pink color grade, reduced saturation |
| Mistwater Lake | Permanent dense fog volume, does not dissipate | Cool desaturation, slight vignette |
| Verdantheart border | Constant canopy haze, greenish diffusion | Green tint, reduced exposure |
| Verdantheart deep | Perpetual twilight, blue-green bioluminescence | Dark, high contrast, blue-green tint |
| Verdantheart Wellspring | Mist from pool, 1m thick layer | Bright, ethereal, blown highlights |
| Southern borderlands | Heat haze distortion | Warm orange tint, slight blur at distance |

### 5.3 Ambient Sound Zones

Place audio volumes for ambient sound per biome. The docs specify distinct soundscapes:

- **Farmland:** Wind through grass, distant animal calls, creaking fences
- **Forest:** Bird calls, rustling leaves, snapping twigs, distant streams
- **Rocky hills:** Wind, echoes, raptor cries
- **Wetlands:** Frogs, insects, water lapping, reed rustling
- **Corruption zones:** Low-frequency hum, crackle, whispers, silence (natural sounds absent)
- **Verdantheart:** Layered canopy sounds, birdsong above, root creaks below
- **Wellspring:** Harmonic hum, water resonance

---

## Phase 6 — Vertical Slice Corridor (Weeks 16–24)

### 6.1 Why a Vertical Slice Before Full Population

SD-10 explicitly calls for a vertical slice at the end of Phase 1 Pre-Production: the Human Frontier Settler origin tutorial sequence (15–20 minutes), The Sepulcher first level, Kael's first meeting, and the Vanguard first quest.

For world building specifically, the vertical slice should fully realize **one road corridor** at final quality. This proves:
- The visual hook system works at 500m intervals
- The biome transitions feel natural
- The atmospheric treatments create the right mood
- The discovery tier system is rewarding
- The scale feels right for traversal timing

**Recommended corridor:** Hollowford → Ironwood (Corridor A from SD-13). This corridor has 6 visual hooks already specified, passes through farmland and forest biomes, includes a Tier 3 hidden location (Glasswater Shrine), and connects to the origin tutorial area.

### 6.2 Corridor A Full Realization

For this one corridor (~5 km), bring everything to near-final quality:

1. **Terrain detail pass** — refine terrain sculpting along the road. Add small-scale variation: eroded banks, rocky outcrops, natural clearings.
2. **Foliage detail pass** — hand-place hero trees at key sightline points. Ensure forest density matches the "visibility 10–30m" spec.
3. **Road detail** — add wear patterns, wheel ruts, stone markers, broken fences.
4. **6 visual hooks placed and payoff content built:**
   - 500m: Ruined Watchtower (Tier 2 POI with Firstborn survey station)
   - 1.0 km: Abandoned Farm (Tier 1 micro-discovery, journal)
   - 1.5 km: Crystal Falls / Glasswater Shrine (Tier 3 hidden location)
   - 2.0 km: Blue Ground Glow (Tier 2, buried lattice node)
   - 2.5 km: Stone Arch logging road (Tier 1, dead logging camp)
   - 3.5 km: Ironwood secondary smoke (Tier 2, creature attack aftermath)
5. **Atmospheric detail** — morning mist in valley, forest haze, dappled light shafts.
6. **Playtest** — walk the corridor multiple times at different times of day. Is there ever a moment where you look around and see nothing interesting? If yes, fix it.

### 6.3 Vertical Slice Evaluation Gate

When the corridor is complete, evaluate honestly:

- Does traversal between Hollowford and Ironwood take 8–12 minutes of real-time walking? (This is the target for a 5 km walk at ~7 km/h player speed.) If it's too fast, the world is too small. If it's too slow, the world is too big.
- Does the player encounter a visual hook roughly every 60–90 seconds of walking?
- Is there at least one "I didn't expect to find this" moment?
- Does the biome transition from farmland to forest feel gradual and natural?
- Do the atmospheric effects enhance the mood without being distracting?

If the answer to any of these is "no," fix the corridor before proceeding. This corridor is the template for all other world content.

---

## Phase 7 — Full World Population (Weeks 22–40)

### 7.1 Remaining Road Corridors

Apply the vertical slice template to the other three corridors, using the visual hook tables from SD-13:

- **Corridor B:** Hollowford → Grainfell (6 hooks specified)
- **Corridor C:** Hollowford → Ashford (6 hooks specified)
- **Corridor D:** Hollowford → Southwatch (6 hooks specified)

### 7.2 Off-Road Content

Between the corridors, place the remaining authored content:

- **60–80 micro-discoveries** (SD-08 §3.2) distributed per the placement rules: cluster near corruption zones and between hubs, thin inside settlements, no two visible from each other
- **6 Tier 3 hidden locations** (SD-13 §2.3) — full realization of each
- **Named wilderness landmarks:** Sunspear Ridge, Blackstone Quarry, The Old Ford, Remembrance Field
- **Faction footprints:** Reaver dead drops, Verdant Flame purification attempts, Hollow Crown survey flags, Vanguard requisition notices

### 7.3 Hollowford Full Build

Hollowford is the largest single content item in the world and deserves its own sub-phase. Build each district to playable quality:

1. Market Quarter (central) — 400m × 400m, dense buildings, central plaza
2. Noble Quarter (NW) — 300m × 300m, wide boulevards, walled estates
3. Vanguard Garrison (NE) — military compound
4. Forge District (E) — industrial, communal forge
5. Refugee Camps (outside south gate) — tent clusters, processing area
6. Undercity Layer 1 (below Market Quarter) — sewer/cellar network

### 7.4 Verdantheart Full Build

Build the concentric ring structure with increasing tree scale and decreasing light. Key locations:

- 3 border camps (NW, W, SW entry points)
- Wellspring Shrine (center hub, fast travel)
- Eldergrove (NW inner, hero worldroot tree)
- Newgrowth Glade (E inner, clearing with camps)
- Shattered Bloom (S inner, corrupted chrysalises)
- Ironbark Hold (N middle, canopy fortress)
- Corrupted Deepwood (N, dying trees, boss area)

---

## Phase 8 — Polish and Iteration (Weeks 36–48+)

### 8.1 Lighting Polish Pass

Walk every area at every time of day. Adjust:
- Light shaft angles through forest canopy
- Corruption zone glow intensity
- Night darkness levels (is torch/magic light actually necessary?)
- Golden hour quality on farmland
- Wellspring glow visibility from surrounding areas

### 8.2 Performance Optimization

- Run performance profiling on minimum-spec hardware in all areas
- Identify hotspots (likely: Verdantheart deep forest foliage density, Ashenveil Archive Firstborn materials, Hollowford crowd density)
- Set aggressive LOD distances for foliage
- Use instanced static meshes for repeated elements (fences, stone walls, market stalls)
- Optimize draw calls per World Partition cell

### 8.3 Audio Polish Pass

- Layer ambient sound zones (sounds should crossfade at biome boundaries, not cut)
- Add reverb zones (forest echo, cave reverb, city reverb)
- Validate that corruption zone silence effect works (all natural sounds removed)
- Add one-shot ambient sounds (distant bird call, branch snap, water splash)

---

## Appendix A — Asset Priority List

Assets needed earliest, organized by phase. Marketplace or Megascans assets are acceptable for all environment items during development. Custom hero assets can be commissioned later.

**Phase 1–2 (terrain and water):**
- Landscape materials (5 base layers minimum)
- Water materials (river, lake, marsh)
- Rock meshes for terrain detail (granite, limestone, slate per docs)

**Phase 3 (biome foundation):**
- Tree meshes: oak, pine, birch, willow, dead variants (5 types minimum)
- Understory: ferns, shrubs, grasses, reeds
- Ground cover: leaf litter, moss, flowers

**Phase 4 (infrastructure):**
- Modular medieval building kit (stone/timber) for settlements
- Wall/gate kit for Hollowford
- Road materials (dirt, stone, gravel)
- Bridge meshes (stone, wooden)
- Tent meshes for refugee camps
- Agricultural props: fences, plows, carts, scarecrows, wells

**Phase 5 (atmosphere):**
- Particle systems: mist, fog, dust motes, fireflies, arcane particles
- Corruption VFX: black veins, purple glow, crystal growths, energy tendrils
- Sky materials: aurora effects, arcane storms

**Phase 6+ (content population):**
- Firstborn stone material (custom — SD-10 Risk 3)
- Firstborn ruin architectural kit
- Corrupted tree/plant variants
- Interior props for buildings
- NPC placeholder meshes

---

## Appendix B — What This Plan Does Not Cover

This plan covers world building (terrain, biomes, water, infrastructure, atmosphere, content placement). It does not cover:

- **Core systems implementation** (combat, inventory, factions, economy) — see SD-10 Phase 1 engineering milestones
- **Character/enemy implementation** — separate workstream per SD-10
- **Quest scripting** — requires systems to be functional first
- **Narrative implementation** — requires quest system + dialogue system
- **UI/HUD** — separate workstream
- **Audio recording** — separate workstream (voice, music)

These workstreams run in parallel with world building. The key synchronization points are:
- Proto-2 (world state) and Proto-7 (corruption zones) must pass before Phase 4
- Combat must be functional before dungeon interiors can be built
- Quest system must be functional before visual hooks with quest connections can be fully implemented
- NPC schedule system must exist before Hollowford NPCs are placed with routines
