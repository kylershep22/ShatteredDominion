# THE SHATTERED DOMINION
## World Partition & World Building Technical Reference
**Document SD-15 | Version 1.0 | Depends on: SD-01, SD-08, SD-10, SD-13, SD UE5 Architecture**

---

### Document Purpose

This document specifies the UE5 World Partition configuration, HLOD strategy, Data Layer architecture, Level Instance workflow, streaming optimisation approach, and editor workflow conventions for The Shattered Dominion.

It is derived from Epic's official World Building Guide v3 (updated for UE 5.5/5.6), cross-referenced against existing SD design documents. Every specification here overrides any conflicting World Partition values stated in earlier documents (notably SD-13 §4.2 cell size and SD Playable Area Detail streaming distances), which were preliminary and are now superseded by this validated configuration.

> **Derived document policy:** Any implementation document, world detail file, or UE5 plan that specifies values also defined in SD-08 (map scale, content density, settlement dimensions) or SD-15 (cell size, loading range, heightmap resolution, HLOD config) is a derived document. Derived documents must include this header: *"Derived from: [parent doc IDs and versions]. Do not modify terrain scale, cell size, content density targets, or streaming configuration without updating parent documents first."* If a derived document contradicts its parent, the parent is authoritative until the parent is explicitly updated.

| System | Status | Depends On |
|---|---|---|
| World Partition Grid Config | Specified — ready for project setup | SD-08 map scale |
| Runtime Hash Selection | Specified — RuntimeHashSet + LHGrid | UE 5.4+ required |
| HLOD Layer Strategy | Specified — 3 layers defined | SD-08 biomes, SD-09 art direction |
| Data Layer Architecture | Specified — requires WorldStateSubsystem | SD-10 Act system, SD-05 factions |
| Level Instance Workflow | Specified — ready for content production | SD Playable Area Detail |
| Sub-World Partition (Verdantheart) | Specified — requires 5.4+ | SD Playable Area Detail |
| FastGeo Streaming | Flagged for evaluation — experimental | UE 5.6 |
| OFPA & Source Control | Specified — workflow defined | Team tooling |
| Streaming Source Strategy | Specified — vista points identified | SD-08, SD-13 sightlines |

---

## Section 1 — World Partition Configuration

### 1.1 Runtime Hash Type

**Use `WorldPartitionRuntimeHashSet` with `RuntimePartitionLHGrid` (Loose Hierarchical Grid).**

Do NOT use the legacy `WorldPartitionRuntimeSpatialHash`. The Loose Hierarchical Grid (introduced in 5.4) solves critical problems for our mixed-density world:

- **Variable cell sizing.** Actor bounds determine the streaming cell scale within up to 1.5× of the defined grid size before promotion. Dense areas (Hollowford interior, ~4000 population) and sparse areas (eastern farmland) coexist without manual micro-management.
- **Reduced grid promotion issues.** The old spatial hash promoted actors to persistent when their bounds crossed the grid origin axis. The LHGrid eliminates this through its hierarchical approach.
- **Removed advanced CVAR complexity.** The old spatial hash required careful tuning of placement rules, grid alignment, and promotion CVARs. The LHGrid does not require any of these.

Configuration location: World Settings → World Partition Setup → Runtime Hash Class → `WorldPartitionRuntimeHashSet`. Under Runtime Settings → Runtime Partitions → Index[0], set Class to `RuntimePartitionLHGrid`.

### 1.2 Grid Size and Loading Range

**Starting values (subject to profiling):**

| Parameter | Value | Rationale |
|---|---|---|
| Grid Cell Size | 128m (12800 UU) | Matches Fortnite/City Sample. Validated for ~100k actor worlds. |
| Loading Range | 256m (25600 UU) | 2× cell size. Provides 2-cell look-ahead for the player. |

These values are starting points. The guide is explicit: grid size and loading range must be re-evaluated as content is added through constant profiling. The Loose Hierarchical Grid reduces the impact of an imperfect starting cell size, but loading range directly affects memory pressure and should be profiled per-platform once blockout content exists.

**Validation checkpoints:**
- After SW quadrant blockout (SD-13 §4.2 step 6): profile actor count per cell, streaming churn during traversal at player walk/sprint speed.
- After Hollowford district population: profile peak actor count in the densest cell. If any cell exceeds ~2000 actors, evaluate Packed Level Actors or ISM consolidation before adjusting grid size.
- After Verdantheart border content: profile memory with Verdantheart's foliage density. Adjust loading range downward if memory budget is exceeded.

### 1.3 Single Grid Policy

**Use a single grid.** The guide is unambiguous: start with one grid, and the fewer grids in the final product the better. Each additional grid multiplies streaming levels (every cell of every grid containing at least one actor produces a streaming level, compounded by Data Layer combinations). Adding a second grid should only occur after profiling demonstrates a clear benefit that outweighs the streaming level multiplication cost.

### 1.4 Landscape Configuration

- Landscape is **always loaded** (not spatially streamed). This matches Fortnite's approach and ensures terrain is never missing under the player.
- Landscape partitioned actors (proxies) use their own internal grid. If the streaming grid is reconfigured later, the landscape proxy grid does NOT automatically update — a commandlet rebuild is required. The World Partition Landscape Builder commandlet is planned by Epic but not yet implemented; manual reconstruction may be necessary.
- Landscape HLOD settings (available in 5.4+) should be configured: specify which LOD level feeds HLOD generation, set maximum texture size (project default 1024, evaluate whether 512 is sufficient for our art style), and control mesh complexity.

---

## Section 2 — HLOD Strategy

### 2.1 Layer Architecture

Three HLOD layers, defined in the RuntimePartitionLHGrid's HLODSetups array:

| Layer | Type | Cell Size | Range | Spatially Loaded? | Purpose |
|---|---|---|---|---|---|
| HLOD0 | Instanced (Nanite-enabled) | 256m | 512m | Yes | Near-distance replacement for structures, rocks, hero trees |
| HLOD1 | Simplified mesh | 512m | 2048m | Yes | Mid-distance simplified geometry for buildings, landmarks |
| Tree Imposters | Instanced | — | — | **No (always loaded)** | Foliage imposters visible at all distances |

**Rationale by layer:**

**HLOD0 — Instanced, Nanite-enabled, spatially loaded.** This follows the City Sample / Matrix Awaken pattern. Nanite-enabled instanced HLODs provide visually indistinguishable results from loaded assets at distance, while reducing actor count from N to 1 per cell. This layer handles structures (Hollowford buildings, settlement structures, Firstborn ruins, fortifications), environmental hero assets (large rock formations, bridge geometry, wall sections), and significant environmental props.

**HLOD1 — Simplified mesh, spatially loaded.** For distances beyond HLOD0, a simplified mesh provides the silhouette representation needed for horizon composition. This is critical for: Hollowford's city silhouette visible from eastern approaches, the Ashenveil Archive structure visible from surrounding terrain, and settlement outlines visible from roads. Build time for simplified mesh HLODs is significant (Epic reports hours on build machines for complex worlds) — plan for nightly automated builds once content reaches production density.

**Tree Imposters — Instanced, always loaded.** Foliage cannot pop in at distance without destroying the world's visual coherence. Fortnite uses this exact pattern: an always-loaded instanced layer of tree imposters that provides forest coverage across the entire map regardless of streaming state. For our project this is essential because: Verdantheart's canopy must be visible from Sunspear Ridge (~2.5km direct distance; imposters still required for visual coherence across all approaches), the Ironwood forest in NW must read from Hollowford approaches, and tree density is a primary biome identifier for player orientation.

### 2.2 HLOD Build Pipeline

- HLOD generation runs via the `WorldPartitionBuilderCommandlet`. Plan for automated nightly builds once content density increases.
- Use the HLOD Relevant Color actor coloration mode (`Show → Actor Coloration → HLOD Relevant Color`) to identify actors incorrectly included in or excluded from HLODs. Small actors, interiors, underground content, and non-significant props should have `bIncludeInHLOD = false`.
- Individual HLOD sections can be rebuilt from the Details panel (5.4+) for local iteration without triggering a full world rebuild.
- Track HLOD stats between builds using `wp.Editor.HLOD.DumpStats`, which outputs a CSV with per-HLOD texture sizes, triangle/vertex counts, and disk sizes.

### 2.3 Actors That Should NOT Be in HLODs

- Interior geometry (building insides, dungeon rooms, Undercity)
- Underground content (Root Layer, Undercity passages, mine interiors)
- Small decorative props (market stall items, table objects, wall-mounted items)
- Gameplay actors (loot containers, interaction points, trigger volumes)
- NPCs and enemies
- VFX actors (particle systems, corruption zone effects, lattice energy flows)

### 2.4 Horizon Landmark Handling

Our SD-01 §6 and SD Map V1 define horizon landmarks visible at 30-50km (Highwinter Peaks, Hollow Crown Plateau, Crimson Flats glow, Stormwoven Isles). These are far beyond any streaming range and require special treatment:

- **Non-spatially loaded HLOD actors placed in the persistent world.** These are hand-authored simplified meshes or ISM clusters that are always loaded, following the Fortnite pattern for cliffs and large statues.
- **Not generated from World Partition grid cells.** They exist outside the streaming grid as bespoke visual anchors.
- The Crimson Flats glow and Stormwoven storm effects are skybox/atmospheric elements, not HLOD geometry — handle through post-process and sky atmosphere materials.

---

## Section 3 — Data Layer Architecture

### 3.1 Data Layer Fundamentals

Data Layers are the system for conditionally loading world data at runtime. They act as a filter on top of World Partition's spatial streaming — actors assigned to a Data Layer only stream when both their spatial cell is in range AND the Data Layer state permits it.

**Critical understanding:** Activating a Data Layer does NOT instantly load all its content everywhere. Spatial streaming still applies. Content on an activated Data Layer loads only within the streaming source's loading range. Plan accordingly for Act transitions — the player will see changes around them first, with distant changes loading as they approach.

Data Layer states: **Unloaded** (not in memory, not visible), **Loaded** (in memory, not visible), **Activated** (in memory, visible).

### 3.2 Runtime Data Layers for World State

Define the following Runtime Data Layer Assets. Each is a `UDataLayerAsset` with type `Runtime`.

**Act State Layers:**

| Data Layer Asset | Initial State | Purpose |
|---|---|---|
| `DL_Act1_Crisis` | Activated | Crisis-state environmental markers: fresh damage, arriving refugees, intact faction banners |
| `DL_Act2_Conflict` | Unloaded | Conflict-state changes: faction control markers, expanded corruption, fortified positions |
| `DL_Act3_Resolution_Base` | Unloaded | Resolution-state base changes shared across all alignments |

**Alignment Variant Layers (Act III/IV, mutually exclusive):**

| Data Layer Asset | Initial State | Purpose |
|---|---|---|
| `DL_Alignment_Vanguard` | Unloaded | Vanguard-aligned resolution: military order, rebuilt structures, Vanguard banners |
| `DL_Alignment_HollowCrown` | Unloaded | Hollow Crown-aligned resolution: noble restoration, political signage |
| `DL_Alignment_VerdantFlame` | Unloaded | Verdant Flame-aligned resolution: nature reclamation, lattice growth |
| `DL_Alignment_Independent` | Unloaded | Independent resolution: mixed recovery, community-driven repairs |

**Corruption Layers:**

| Data Layer Asset | Initial State | Purpose |
|---|---|---|
| `DL_Corruption_Stage1` | Activated | Initial corruption zones: Ashfield Scar, Mistwater Lake edge |
| `DL_Corruption_Stage2` | Unloaded | Expanded corruption: larger zones, new incursion points |
| `DL_Corruption_Stage3` | Unloaded | Peak corruption: maximum spread before resolution |
| `DL_Corruption_Cleansed` | Unloaded | Post-cleansing state: healed terrain, residual scarring |

**Gameplay Event Layers:**

| Data Layer Asset | Initial State | Purpose |
|---|---|---|
| `DL_Event_SeasonalStorm` | Unloaded | Arcane storm environmental changes |
| `DL_Event_RefugeeSurge` | Unloaded | Additional refugee camp content, NPC population increase |
| `DL_Event_FactionClash` | Unloaded | Battlefield debris, fortification damage, aftermath content |

### 3.3 Integration with USDWorldStateSubsystem

Data Layer state changes are driven exclusively by `USDWorldStateSubsystem`. When an Act transition occurs:

1. `USDWorldStateSubsystem` calls `UDataLayerManager::SetDataLayerRuntimeState()` to **Load** (not Activate) the incoming Act's Data Layer.
2. A brief delay allows streaming to bring content into memory within the player's vicinity.
3. The subsystem then **Activates** the new layer and **Unloads** the outgoing layer.
4. This sequence prevents visible pop-in during the transition moment.

For alignment layers in Act III: only one alignment layer is ever activated. The subsystem validates mutual exclusivity — setting any alignment layer first unloads all other alignment layers.

### 3.4 Editor Data Layers

Define the following Editor-Only Data Layers for production workflow:

| Data Layer Asset | Purpose |
|---|---|
| `DL_Editor_Cinematics` | Cinematic-specific actors, camera rigs, sequence props |
| `DL_Editor_Debug` | Debug visualization actors, test triggers, profiling markers |
| `DL_Editor_ProceduralOutput` | PCG-generated content isolation |
| `DL_Editor_Lighting` | Lighting-specific actors for isolated lighting work |

### 3.5 Data Layer Logic Operator

Set the project-wide default Data Layer logic operator to **OR** (Project Settings → Engine → World Partition → Default Data Layer Operator). This means an actor loads when ANY of its assigned Data Layers is active. This is the correct default for our use case — an actor belonging to both `DL_Act2_Conflict` and `DL_Corruption_Stage2` should load when either layer is activated.

If specific actors require AND logic (load only when ALL assigned layers are active), override per-level in World Settings.

### 3.6 Data Layers and Streaming Level Multiplication

**Warning from the guide:** Each unique combination of Data Layers assigned to actors within a grid cell creates an additional streaming level. Monitor the total streaming level count as content production progresses. Keep the number of simultaneously active Runtime Data Layers as low as practical. The Fortnite reference scenario has 50+ Data Layers but only a handful active at any given time.

---

## Section 4 — Level Instance & Packed Level Actor Workflow

### 4.1 Level Instance Strategy

All discrete locations are authored as Level Instances with the following conventions:

| Location Type | Level Instance? | OFPA? | Level Behavior | Example |
|---|---|---|---|---|
| Settlement / Town | Yes | Yes | Embedded | Hollowford, Ironwood, Grainfell, Ashford, Southwatch |
| Building / POI | Yes | Yes | Embedded | The Broken Chalice, Vanguard Garrison, Market Stalls |
| Dungeon | Yes | Yes | Embedded | Ashenveil Archive, Sepulcher, Verdant Temple |
| Natural Landmark | No (direct placement) | N/A | N/A | Mistwater Lake, Sunspear Ridge, River Serpentis |
| Verdantheart Region | Yes | Yes | **Standalone** | Sub-World Partition (see §5) |

**Why Embedded for most Level Instances:** With OFPA enabled and Level Behavior set to Embedded, Level Instance content is broken down into the persistent world's streaming grid during PIE and Cook. Level Instances do not exist as discrete units at runtime — their actors integrate into the main world's cell-based streaming. This gives full HLOD support and optimal streaming behavior.

**Production playground:** Create an empty reference level (`L_SD_Playground`) containing the game's standard world lighting, post-process, and sky atmosphere. Artists and designers build Level Instances here, outside the complexity of the main world. Use the `IsMainWorldOnly` flag on a lighting sub-Level Instance within templates so it only appears in the editor, not in the game world.

### 4.2 Packed Level Actor Strategy

Use Packed Level Actors inside Level Instances for visual-only static geometry clusters:

- Building facades (repeated wall sections, window frames, structural elements)
- Rock groupings at Point of Interest sites
- Market stall assemblies (structural frames, canopy meshes — NOT interactive goods)
- Fortification sections (wall runs, tower segments)
- Interior decoration sets (static furniture groupings, shelf assemblies)

**Constraints to respect:**
- PLA bounds determine streaming cell assignment. Keep PLA bounds smaller than the streaming cell size (128m). A building facade PLA spanning 200m would cause streaming issues.
- PLA outputs only SM/ISM/HISM components. Any actor with gameplay logic, Blueprint scripting, or collision requirements beyond what ISM supports must remain as individual actors.
- PLA content streams as a single unit. If a PLA is too large, the entire cluster loads/unloads as a block, defeating granular streaming.

### 4.3 Non-OFPA Level Instance Strategy (File Count Reduction)

For small, self-contained Level Instances where source control contention is unlikely (a single artist owns the content), consider using non-OFPA levels with Level Behavior set to Embedded (supported in 5.6+). This reduces external actor file count at the cost of per-actor source control granularity.

Candidates: small decoration sets, individual building interiors, standalone puzzle rooms.

Do NOT use non-OFPA for: any Level Instance where multiple team members may edit simultaneously, any Level Instance containing Data Layered actors (Data Layers on actors within non-OFPA levels are not supported when embedded).

---

## Section 5 — Sub-World Partition: Verdantheart

### 5.1 Rationale

Verdantheart Wilds has fundamentally different streaming requirements from Severant Vale:

- **Foliage density:** Highest in the game. Millions of instanced foliage actors. Multiple nav mesh layers (ground, root, canopy).
- **Distinct cell layout:** The existing design specifies a ring-based cell structure (10 border, 20 middle, 10 inner, 1 Wellspring) that differs from the Vale's quadrant-based layout.
- **Independent streaming range:** Dense canopy allows shorter loading ranges than the Vale's open terrain.

Sub-World Partitions (5.4+) were designed for exactly this scenario: areas with distinct density and streaming needs within a larger environment.

### 5.2 Configuration

- Create Verdantheart as a separate World Partition-enabled level.
- In the main Severant Vale world, place a Level Instance Actor referencing the Verdantheart level.
- Set the Level Instance Actor's **Level Behavior** to **Standalone**.
- The Standalone Level Instance becomes a Sub-World Partition, managing its own streaming grid independently.

**Verdantheart-specific grid settings:**

| Parameter | Value | Rationale |
|---|---|---|
| Grid Cell Size | 64m (6400 UU) | Smaller cells for dense foliage — reduces per-cell memory load |
| Loading Range | 128m (12800 UU) | Shorter range acceptable due to dense canopy occluding distance |

### 5.3 Sub-World Partition HLODs

As of 5.6, Sub-World Partition HLODs are supported without requiring the base level to be loaded. Enable via World Settings → World Partition Setup → **Build Standalone HLOD** on the Verdantheart level, and toggle **Enable Standalone HLOD** in Editor Preferences → Experimental.

This is critical for our design: Verdantheart's distant canopy must be visible from Sunspear Ridge and the Vale's eastern approaches. Without standalone HLOD support, the forest would only appear once the player crosses into Verdantheart's streaming range.

---

## Section 6 — Streaming Optimisation

### 6.1 Streaming Source Components

The default streaming source is the PlayerController. Add `UWorldPartitionStreamingSourceComponent` to the following actors for pre-loading and cinematic support:

| Actor / Location | Purpose | Priority | Target State |
|---|---|---|---|
| Sunspear Ridge vista trigger | Pre-load Verdantheart HLOD view for cinematic moment | Medium | Activated |
| Hollowford approach road (SW) | Pre-load Hollowford cells before the player rounds the final hill | High | Loaded |
| Cinematic camera actors | Load content at cinematic locations during cutscenes | High | Activated |
| Fast travel system | Pre-load destination cells during the fast travel transition screen | High | Activated |
| Dungeon entrance triggers | Begin loading dungeon interior cells as player approaches exterior | Medium | Loaded |

Streaming source shapes, priority, target grids, and target state can all be configured per-component.

### 6.2 Block On Slow Streaming

Enable Block On Slow Streaming for the main gameplay grid. This forces a frame stall if streaming falls behind, preventing the player from ever seeing unloaded terrain. The blocking load triggers based on a ratio of distance-to-cell / loading-range, controlled by `wp.Runtime.BlockOnSlowStreamingRatio`.

For a secondary non-gameplay grid (if one is ever added for ambient effects or decorative content), disable blocking to avoid stalls from non-essential content.

### 6.3 FastGeo Streaming (5.6 — Experimental, Evaluate During Production)

FastGeo Streaming targets immutable static geometry and achieves dramatic streaming performance improvements (Epic's internal tests showed 90%+ reduction in streaming overhead on City Sample at 215 km/h). Our Verdantheart region (dense static foliage, rocks, tree trunks) and the Vale's environmental dressing are strong candidates.

**Prerequisites for evaluation:**
1. Enable FastGeo Streaming plugin
2. Add `FastGeoWorldPartitionRuntimeCellTransformer` to World Settings → World Partition Setup → Runtime Cells Transformer Stack
3. Set `p.Chaos.EnableAsyncInitBody = true`
4. Profile with and without using the provided console variables

**Actors that will NOT be FastGeo-compatible (by design):**
- Blueprint actors with gameplay logic (interactive objects, quest triggers, NPCs)
- Replicated actors (not applicable — single player)
- Non-static mobility actors (moving platforms, corruption tendrils, dynamic obstacles)
- Actors with child actors

**Actors that should be candidates:**
- Static mesh environment props (rocks, walls, fences, ruins)
- Packed Level Actor output (buildings, decoration clusters)
- PCG-spawned partitioned foliage

Use the FastGeo Actor Coloration debug mode (`show ActorColoration FastGeo`) to visualise what was and was not transformed. Use `FastGeo.Show 0` to hide all FastGeo content and see what remained as standard actors.

### 6.4 Runtime Cell Transformers (ISM Optimisation)

Even without FastGeo, enable the base `WorldPartitionRuntimeCellTransformerISM` (introduced 5.5). This non-destructive process gathers StaticMeshActors and Partitioned Actors (PCG foliage, etc.) into Instanced Static Mesh components at PIE/Cook time, reducing actor count per cell without affecting editor data.

Configuration: World Settings → Runtime Cells Transformer Stack → Add `WorldPartitionRuntimeCellTransformerISM`. Set Allowed Classes to include `PartitionActor` and `StaticMeshActor` with Min Num Instances at 2.

Use `Show ActorColoration CellTransformerISM` to verify transformation results in PIE.

**Note from the guide:** Pre-packing content via Packed Level Actors or PCG partitioned spawning is always preferred over relying on automatic Cell Transformer optimisation. Both strategies should be combined: authored content uses PLA/PCG instancing, and the Cell Transformer catches any remaining un-optimised static meshes.

---

## Section 7 — OFPA & Source Control Workflow

### 7.1 Core Rules

- **All source control operations go through Unreal's View Changelist window.** External actor files are named with GUIDs and cannot be meaningfully identified in P4V or other external SC clients. Unreal displays actor display names, types, and paths.
- **Use Uncontrolled Changelists** for local experimentation, debugging, and testing. Move edits back to controlled CLs when ready to submit. This prevents locking files unnecessarily.
- **Enable the source control column in the Scene Outliner.** This provides async status display for every actor, making file contention visible at a glance.
- **Enable the Unsaved Items button monitoring.** Source control conflicts appear immediately as warnings.
- **Do NOT use P4V to submit content.** This is explicitly warned against in the guide. The validation that runs on submit within Unreal (reference checking, missing file detection) is bypassed by external tools.

### 7.2 Submit Validation

Extend the built-in submit validation with project-specific checks:

- Verify that no actors reference unsubmitted DataAssets
- Verify that no actors in corruption zones are missing corruption material layer assignments
- Verify that Level Instance actors have the correct Level Behavior setting
- Verify that gameplay actors (quest triggers, interaction points) are not flagged for HLOD inclusion

### 7.3 File Count Management

With a ~20 km² world at our target content density, OFPA will generate thousands of external actor files. Monitor file count growth and consider the following mitigation strategies (from the guide's Strategies section):

- Use non-OFPA Level Instances (Embedded, 5.6+) for small, single-owner content
- Avoid unnecessary world copies — use Data Layers or Level Instances for test configurations
- Favour instancing strategies (PLA, PCG, ISM) which reduce the number of individual actors and therefore individual files

---

## Section 8 — Editor Workflow Conventions

### 8.1 Location Volumes

Create named Location Volumes in the World Partition Editor for each major area. These persist as actors and are visible to all team members.

| Location Volume | Approximate Bounds | Purpose |
|---|---|---|
| `LOC_Hollowford` | 1.0km × 1.0km around city | City content loading |
| `LOC_Ironwood` | 800m × 800m around settlement | Settlement + surrounding forest |
| `LOC_Grainfell` | 800m × 800m around settlement | Settlement + farmland |
| `LOC_Ashford` | 800m × 800m around settlement | Settlement + bridge area |
| `LOC_Southwatch` | 800m × 800m around settlement | Settlement + refugee camps |
| `LOC_AshenveilArchive` | 500m × 500m around dungeon | Dungeon + exterior |
| `LOC_VerdanthearBorder` | 1.5km × 500m along border | Transition zone |
| `LOC_CorruptionZones` | Variable per zone | Corruption area loading |

### 8.2 World Bookmarks (5.6+)

Create and share World Bookmarks for key development contexts:

- **Default level bookmark:** Opens at Hollowford North Gate with surrounding 2km loaded
- **Per-developer home bookmarks:** Each team member sets their current working area
- **Categorised bookmarks:** Art, Bug, Cinematics, Level Design, Personal (configure categories in Project Settings → Editor → World Bookmark)
- Use `WorldBookmark.CaptureToClipboard` to share exact editor states in bug reports

### 8.3 Actor Editor Context

Use the Actor Editor Context (Make Current on Data Layers) when placing content for specific Act states or event layers. All actors placed with a Data Layer set as Current automatically receive that Data Layer assignment, preventing the common error of placing Act-specific content without the correct layer assignment.

### 8.4 Show Grid Preview

Use the Show Grid Preview option in the World Partition Editor to visualise streaming grid cells and approximate loading range directly in the editor. This does not replace in-game profiling but catches obvious spacing and density issues during content placement.

---

## Section 9 — Useful Console Commands

### World Partition Debug
- `wp.Runtime.ToggleDrawRuntimeHash2D` — Toggle streaming grid debug overlay
- `wp.Runtime.OverrideRuntimeLoadingRange -grid=[index] -range=[value]` — Override loading range at runtime for testing
- `wp.runtime.hlod` — Toggle HLOD display
- `wp.Runtime.BlockOnSlowStreamingRatio` — Control when blocking load triggers

### Data Layers Debug
- `wp.DumpDatalayers` — Dump all Data Layer states to log
- `wp.Runtime.SetDataLayerRuntimeState [state] [layer]` — Force a Data Layer state
- `wp.Runtime.ToggleDrawDataLayers` — Show Data Layer states in viewport
- `wp.Runtime.DebugFilerByDatalayer` — Filter runtime hash debug by Data Layer

### HLOD Debug
- `wp.Editor.HLOD.DumpStats` — Export HLOD stats CSV to Saved/Logs/WorldPartition/
- `show ActorColoration HLODRelevant` — Highlight HLOD-included vs excluded actors

### FastGeo Debug (when evaluating)
- `show ActorColoration FastGeo` — Highlight transformed vs non-transformed actors
- `FastGeo.Show 0/1` — Hide/show all FastGeo content
- `FastGeo.EnableTransformerDebugMode=1` — Log transformation failures during cook

### Actor Coloration
- `show ActorColoration LevelColor` — Color actors by source Level Instance
- `show ActorColoration PropertyColor` — Color actors by shared property value (Ctrl+Click a property first)
- `show ActorColoration CellTransformerISM` — Visualise ISM Cell Transformer results

---

## Section 10 — Reference Scenarios from Epic

These shipped configurations from the guide provide validated reference points for our decisions:

### Fortnite Chapter 6 (most relevant comparison)
- Map: 2km × 2km, ~100k actors
- Hash: RuntimeHashSet + Loose Hierarchical Grid (2D)
- Single grid: 128m cell, 256m range
- HLODs: 2 layers for buildings (merged + simplified), 1 always-loaded instanced layer for tree imposters, non-spatially-loaded HLODs for cliffs/statues in persistent world
- Level Instances: All POIs and locations
- Data Layers: 50+ runtime for event/season changes + External Data Layers via Game Feature Plugins
- Landscape: Always loaded
- Server: Everything loaded (server streaming used in PIE only for dev iteration)

### City Sample (UE 5.6 update)
- Map: 4km × 4km, ~107k actors
- Hash: RuntimeHashSet + Loose Hierarchical Grid (2D)
- Single grid: 128m cell, 128m range
- FastGeo Streaming enabled with Cell Transformers
- HLODs: 2 layers (HLOD0 Nanite instanced 256m/768m spatially loaded, HLOD1 simplified always loaded)
- 35 runtime Data Layers, 21 editor Data Layers
- All buildings/roads/props as Packed Level Actors with ISM

### Ancient Game (UE5 Preview — simplest reference)
- Map: 2km × 2km, ~14k actors
- Single grid: 64m cell, 64m range
- HLODs: 1 layer, instanced, always loaded
- Packed Level Actors for rock groupings with merged collision
- 2 runtime Data Layers (one for full world state swap), 1 editor

### Our Project (The Shattered Dominion — target)
- Map: ~20 km² (Severant Vale) + ~15 km² (Verdantheart as Sub-World Partition)
- Hash: RuntimeHashSet + Loose Hierarchical Grid (2D)
- Single grid: 128m cell, 256m range (subject to profiling)
- HLODs: 3 layers (instanced Nanite, simplified mesh, always-loaded tree imposters)
- Level Instances: All settlements, POIs, dungeons (Embedded). Verdantheart as Standalone Sub-World Partition.
- Data Layers: ~15-20 runtime (Act states, alignment variants, corruption stages, events), ~4 editor
- Landscape: Always loaded
- Heightmap resolution: 2017×2017 (per SD-08 v3.0)
- Cell Transformers: ISM transformer baseline, FastGeo evaluation during production

---

## Appendix A — Build Order Update (Supersedes SD-13 §4.2 Steps 1-2)

The build order from SD-13 §4.2 is updated to incorporate this document's specifications. Steps 3+ in SD-13 remain valid.

1. **World Partition enabled** at project level. Runtime Hash Class set to `WorldPartitionRuntimeHashSet`. Runtime Partition set to `RuntimePartitionLHGrid`. Cell size 128m (12800 UU). Loading range 256m (25600 UU). Enable `p.Chaos.EnableAsyncInitBody = true` in DefaultEngine.ini.

2. **ISM Cell Transformer enabled.** Add `WorldPartitionRuntimeCellTransformerISM` to Runtime Cells Transformer Stack. Allowed Classes: `PartitionActor`, `StaticMeshActor`. Min Num Instances: 2.

3. **Data Layer Assets created** for Act states, alignment variants, corruption stages, and editor isolation layers per Section 3. Data Layer Instances added to `WorldDataLayers` actor with correct initial states. Enable `Use External Package Data Layer Instances` on the WorldDataLayers actor to reduce file contention.

4. **Location Volumes created** per Section 8.1 for all major areas.

5. **Landscape created** at correct scale: 2017×2017 heightmap resolution, X/Y scale 100. Set to always loaded (not spatially streamed). Heightmap imported, manual sculpting limited per SD-13 §4.2 step 2.

6. *Continue with SD-13 §4.2 steps 3-7 (landscape material, River Serpentis, POI system, blockout, discovery testing).*

---

## Appendix B — Decisions Deferred to Profiling

The following decisions cannot be finalised until content exists at sufficient density for meaningful profiling:

| Decision | When to Evaluate | Data Needed |
|---|---|---|
| Final cell size (128m vs 96m vs 64m) | After SW quadrant blockout | Actor count per cell, streaming churn at player speed |
| Final loading range | After Hollowford population | Memory budget per platform, peak loaded cell count |
| Verdantheart cell size (64m proposed) | After Verdantheart border biome content | Foliage instance count per cell, memory under canopy |
| FastGeo Streaming adoption | Mid-production | A/B profiling with and without, on target hardware |
| HLOD1 always-loaded vs spatially-loaded | After initial HLOD build | Memory impact of always-loaded simplified mesh layer |
| Need for second streaming grid | If profiling shows specific category of actors causing streaming issues | Per-actor-type streaming cost analysis |
