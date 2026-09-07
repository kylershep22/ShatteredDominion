# THE SHATTERED DOMINION
## World Exploration & Puzzle Design Specification
**Document SD-13 | Version 1.0 | Depends on: SD-01, SD-08, SD-09, SD-10**

---

### Document Purpose

This document specifies the wilderness traversal design, the three-tier discovery system, all six puzzle types, and the six Tier 3 hidden locations for the Severant Vale playable region.

It is the design authority for all off-road exploration content. Any content placed in the Vale wilderness must conform to the visual hook system in Section 1, the discovery tier rules in Section 2, and the puzzle design rules in Section 3.

UE5 implementation notes are provided in Section 4. The data architecture (`USDPointOfInterestData`, `USDDiscoverySubsystem`) is specified there and must be built before any exploration content is placed in the editor.

| System | Status | Depends On |
|---|---|---|
| Traversal Visual Hooks | Specified — ready for blockout | SD-08 micro-discovery list |
| Discovery Tier System | Specified — requires UE5 POI actor | SD-08 §3, SD-06 loot tiers |
| Tier 3 Hidden Locations (6) | Specified — ready for level design | SD-06 loot, SD-07 combat |
| Puzzle Types 1–6 | Specified — requires Echo system | SD-07 Echo, SD-01 lattice lore |
| UE5 Data Architecture | Partially specified — see Section 4 | SD UE5 Architecture doc |

---

## Section 1 — Wilderness Traversal Design

### 1.1 Core Philosophy

Player perception of world size is driven by discovery density, not raw terrain. The Severant Vale is ~20 km² by deliberate choice. A map this size with maximum authored content density will feel larger than a 120 km² map with sparse content because something meaningful happens every minute of travel.

The specific problem this section addresses: the design documents contain excellent internal detail for named locations and micro-discoveries, but the connective tissue between them is undefined. A player following any road between two settlements must encounter deliberate visual hooks — things visible from the road that reward leaving it — at intervals no greater than 350m.

If a player looks left, right, and ahead at any road junction and sees only trees, there is a design failure at that location. The fix is not always more content — it may be terrain shaping, a light anomaly, a sound cue, or a silhouette visible on the horizon. The hook need not be large. It must be unignorable.

---

### 1.2 Visual Hook Rules

> **Non-Negotiable Rules for All Road Corridors**
>
> 1. Maximum 350m between visual hooks. No road segment longer than 350m offers no off-road pull.
> 2. No two hooks of the same type consecutively. Smoke plume followed by smoke plume is invisible on the second occurrence.
> 3. Every hook must be identifiable from the road. The player should be able to see it without leaving the road and make a conscious choice to investigate.
> 4. Hooks must be honest. If a distant silhouette looks like a structure, there must be a structure there.
> 5. Hooks are not quest markers. No UI element, no map pin, no journal entry is triggered by seeing a hook from the road. The hook is visual only.
> 6. Sound hooks are valid. A mill creak, running water from an unexpected direction, an unnatural silence — these are hooks that do not require line of sight.

**Visual hook categories:**

- **Silhouette hooks** — a structure, cairn, or ruined tower visible on the skyline or tree line. Effective at long range (200–600m). Require a payoff when reached.
- **Light anomalies** — a glow, reflection, or absence of light that is wrong for the environment. Lattice blue-white at night; fire where fire should not be; the Mistwater Lake fog column; a reflection showing the wrong sky.
- **Sound hooks** — running water from an unexpected direction; rhythmic mechanical sound (the mill); the road silence zone; distant drums from Ironbark Hold in Verdantheart.
- **Smoke/particle hooks** — a smoke column suggesting habitation or fire where neither is expected. Always honest: investigation finds an actual source.
- **Pattern hooks** — something in the landscape that has wrong geometry. The half-corrupted field stopping at a perfect diagonal. The pond reflection. A crop field in the shape of a Firstborn character.
- **Movement hooks** — a creature, a person, or a swinging object visible from the road. The still-turning mill wheel. A figure standing motionless at a corruption zone edge. A scarecrow that moves on second glance.

---

### 1.3 Road Corridor Specifications

Four primary road corridors connect Hollowford to the frontier settlements. Each is specified below with hooks at 500m intervals. Distances are approximate from Hollowford's gate or from the nearest named settlement.

#### Corridor A — Hollowford to Ironwood (SW to NW, ~3km)

| Distance | Visual Hook | What the Player Finds | Reward Tier |
|---|---|---|---|
| 300m | Ruined Watchtower | Collapsed stone tower on ridge to the left of the road. Asymmetric broken profile visible over tree line. Close approach: Tier 2 POI — Firstborn survey station still running, data fragment inside. Elevation: 180m. | Tier 2 |
| 600m | Smoke Plume (Abandoned Farm) | Thin smoke rising from treeline gap — structure not visible from road. Investigation: Tier 1 micro-discovery. Farmhouse with journal, sentence stops mid-word on the night of the Severance. Smoke from a still-burning hearth lit days ago. | Tier 1 |
| 900m | Crystal Falls (Glimpse) | White vertical line visible 3 seconds through forest canopy gap — a 60m waterfall catching light. Sound audible from 80m. Tier 3 Hidden Location: HL-03 Glasswater Shrine. Firstborn observation post at cliff top; permanent minor stamina restoration at base pool. | Tier 3 |
| 1.2km | Blue Ground Glow | Visible at dusk/night: steady blue pulse in undergrowth (not flicker — lattice not fire). 40m off road. Tier 2 POI: buried lattice node. Echo Interface reacts. Map fragment revealing unlisted location. Node cannot be deactivated. | Tier 2 |
| 1.5km | Stone Arch (Logging Road) | A worked stone archway at the entrance of an overgrown logging road — clearly Firstborn construction repurposed by human loggers. The road beyond leads 400m into forest. At its end: a logging camp where the workers died at their stations. | Tier 1 |
| 2.5km | Ironwood Palisade (Final Hook) | Settlement palisade visible through trees. Smoke and activity audible. Direct approach leads to Ironwood gate. | Tier 2 |

#### Corridor B — Hollowford to Grainfell (SW to NE, ~2.5km)

| Distance | Visual Hook | What the Player Finds | Reward Tier |
|---|---|---|---|
| 300m | Split Corruption Field | Crop field visible from road where corruption stops in a perfect diagonal — half green, half crystallized black. Wrong geometry for natural spread. Tier 1 micro-discovery: corruption follows a buried Firstborn conduit. Verdant Flame tools at field edge, still warm. | Tier 1 |
| 625m | Still-Turning Mill Wheel | Mill wheel rotating despite abandoned, damaged building. Sound: rhythmic creak audible from 80m. Tier 2 POI: mill grinding grain into sealed Firstborn storage mechanism beneath floor. Functional Firstborn tech + loot cache. Links to Grainfell food supply questline. | Tier 2 |
| 950m | Standing Stones on Hillside | Three tall stones on northern hilltop, visible from 600m. Glow faintly at night. Tier 2 POI: Firstborn triangulation array still functional. Echo Interface: 10-second memory — Wellspring was destabilising 400 years before the Severance. Critical lore. | Tier 2 |
| 1.25km | Crystallized Dead Tree | Single tree crystallized by corruption — catches light like glass, visible 300m in daylight. Unique silhouette. Investigation: hollow interior contains compromised Reaver dead drop. Empty container, calling card left. Internal Reaver faction tension. | Tier 1 |
| 1.6km | Verdantheart Canopy Looms | Road bends; Verdantheart tree line becomes visible for the first time — the canopy is above 40m, visibly moving despite no wind. Not a hook to investigate but a mood shift. First time players should feel the forest watching. | N/A — atmosphere |
| 2.2km | Smoke from Within Forest | Thin smoke rising from inside Verdantheart border. No safe entry here. Thornwalker camp (discovered in Verdantheart questline). Functions as horizon threat signal. | Tier 1 |

#### Corridor C — Hollowford to Ashford (SW to W, ~2.2km)

| Distance | Visual Hook | What the Player Finds | Reward Tier |
|---|---|---|---|
| 300m | Hollow Crown Survey Flag | Yellow pennant flag on iron stake, 40m off road. Back of flag: geological notation. Survey predates Severance by two years — they knew about the lattice fracture. Tier 1 micro-discovery — no loot, high faction lore value. Can trigger player suspicion of Hollow Crown timeline. | Tier 1 |
| 750m | Quarry Scar on Hillside | Large pale gash in hillside to the north — exposed limestone visible from 800m. Clearly worked, not natural. Leads to HL-02: The Quarryman's Rest. Miners broke into a Firstborn chamber. Construct enemy. Remnant-tier loot. | Tier 3 |
| 1.25km | Dry Creek Bridge Ruins | Old stone bridge over a creek that is completely dry — water table changed since Severance. Under the bridge: a Firstborn drainage channel still trying to move water that no longer exists. Echo Interface: 5-second fragment of the Firstborn hydrologist noting the original water table. | Tier 1 |
| 1.75km | Ashford Light at Night | Ashford visible in daylight; at night, the forge fires make it glow orange. Players approaching at night see the glow before they see the settlement. No hook payoff — navigational landmark and atmosphere. | N/A — atmosphere |

#### Corridor D — Hollowford to Southwatch (SW to S, ~2.5km)

| Distance | Visual Hook | What the Player Finds | Reward Tier |
|---|---|---|---|
| 300m | Red Horizon Glow | Crimson Flats visible on southern horizon from earliest point on this road — constant red-orange glow, intensifying at dusk. Ash clouds occasionally drift north. Environmental horror establishing the scale of the refugee crisis. No investigation needed. | N/A — atmosphere |
| 750m | Drakeling Roadside Shrine | Small shrine of salvaged materials, fresh daily offering at base. Investigation: keeper is a Drakeling elder camping 60m into the marshland. No quest. If engaged: location of a hidden orchard that survived the ash storms revealed. Merchant access. | Tier 2 |
| 1.25km | Marsh Fog Column | Unnaturally vertical fog column rising from marshland east of road — density and vertical coherence wrong for natural fog. Investigation leads to HL-06: The Fen Hollow. Drakeling settlement of 12 people, unique merchant goods, questline not in main journal. | Tier 3 |
| 1.75km | Sunken Cart (Vanguard Markings) | Vanguard supply cart half-submerged in marshland 30m from road. Recent — markings still visible. Tier 1 micro-discovery: cart manifest inside waterproof case. Manifest shows supplies destined for a garrison post that no longer exists. | Tier 1 |
| 2.2km | Southwatch Watch-Fire | Southwatch's elevated watch-fire visible from 1km on clear nights. Players approaching at night can navigate by it. By day, a dust cloud from Flats creature activity sometimes visible south of the outpost. | N/A — atmosphere |

---

### 1.4 Elevation as Design Tool

The Vale's elevation range (50m valley floor to 400m Sunspear Ridge) is a content distribution tool, not just geography. Every significant high point visible from a lower area must have a reason to climb it.

| Elevation Band | Terrain Type | Design Obligation |
|---|---|---|
| 50–100m | River valley, Hollowford | Dense authored NPC content, quests — no wilderness hooks needed |
| 100–200m | Rolling farmland, roads | Micro-discoveries and Tier 2 hooks at 400–600m intervals |
| 200–300m | Forest hills, ruins | Named locations, Tier 2 and Tier 3 POIs — at least 2 per km² |
| 300–400m | Eastern Ridge, cliff faces | Rare crafting materials + 1 hidden location per km — effort justified by reward |
| 400m | Sunspear, mountain approaches | Breathtaking panoramic vista, endgame-tier discovery, star map puzzle anchor |

Slope as a design signal: every 30–45° slope must have a navigable path if the player looks carefully. The trained response is to stop at a cliff face; the design obligation is to reward players who look for the foothold, the ledge, the switchback trail. Verdantheart uses root systems as natural staircases — the same logic applies to the Vale's eastern ridge.

> **Heightmap resolution note (v3.0):** The reduction from 4033×4033 to 2017×2017 heightmap resolution means each sample covers ~4× the area. Terrain interpolation will smooth gentle undulation but steepen transitions between elevation bands. This is acceptable and may improve the Vale's terrain character — sharper ridges and more defined cliff faces create better exploration texture than uniform gentle slopes. However, the number of 30–45° slopes may increase, which increases the number of required navigable paths. During blockout, run a slope analysis pass (Landscape debug visualization → slope angle overlay) before committing to asset placement. If 30°+ terrain coverage exceeds expectations, use manual sculpting to soften critical traversal corridors rather than relaxing the navigable path rule. AI navmesh generation should also be validated after heightmap import — steeper terrain may require additional NavLink proxies on ridge approaches.

---

### 1.5 Sightlines That Must Be Preserved

The following sightlines are load-bearing for the Vale's sense of scale. They must be verified in UE5 blockout before any assets are locked.

| From | To | Distance | Design Function |
|---|---|---|---|
| Hollowford North Gate | Mistwater Lake fog | 2km | "I should investigate that" |
| Hollowford North Gate | Sunspear Ridge peak | 2.5km | Establishes world scale, pulls player east |
| Sunspear Ridge | Verdantheart canopy below | 2km | Jaw-drop moment — looking down into 600m trees |
| Eastern ridge path | Hollowford in river valley | 2.5km | "I came from there" — scale of journey |
| Southwatch road | Crimson Flats red glow | On southern horizon | Environmental horror — constant reminder |
| Any northern elevation | Highwinter peaks on horizon | 40km+ | World larger than playable area — lore signal |

---

## Section 2 — Discovery Tier System

### 2.1 Overview

The existing design documents define two discovery layers: micro-discoveries (SD-08 §3, no marker, no journal) and major named locations (quest-relevant). This section formalises the three-tier system that fills the gap between them.

| Tier | Name | Map Mark | Journal | Loot | Count Target |
|---|---|---|---|---|---|
| 1 | Micro-Discovery | Never | Never | None | 60–80 across Vale |
| 2 | Unmarked POI | Yes (on find) | Never | Tier 2–3 items | 30–40 across Vale |
| 3 | Hidden Location | Yes (on find) | One-line note | Tier 3–4 + Remnant possible | 8–12 across Vale |

---

### 2.2 Tier 1 — Micro-Discoveries

Fully specified in SD-08 §3. Reproduced here for completeness:

- No journal entry. No map mark. No loot spawn.
- Pure environmental storytelling — evidence of people, history, or world-state anomaly.
- Companion reactions count as a Tier 1 reward. Aelira commenting on a lattice harmonic is a discovery payoff.
- Must not require any game system to engage with — player approaches, observes, moves on.
- 60–80 total. Distribution weighted toward corruption zone edges, spaces between hub locations, and areas visible from road that require a short detour.

---

### 2.3 Tier 2 — Unmarked Points of Interest

This tier does not currently exist in the design documents. It is defined here.

> **Tier 2 Definition**
>
> An Unmarked POI appears on the player's map as a greyed icon only after the player physically enters its discovery radius. Before discovery it does not appear at all. It has no quest marker and no journal entry.
>
> Each Tier 2 POI contains: a readable (journal fragment, inscription, or Echo Interface reading), a minor loot spawn (Tier 2–3 items from SD-06), and at least one piece of information that makes the world feel larger or more real.
>
> Tier 2 POIs are authored — each one is hand-placed with a specific story reason. They are not procedurally generated.

**Example Tier 2 POIs from corridor specifications:**

- Ruined watchtower on Corridor A — Firstborn survey station, data fragment, map extension.
- Still-turning mill on Corridor B — Firstborn grain storage, loot cache, Grainfell supply link.
- Standing stones on Corridor B — Firstborn triangulation array, Wellspring destabilisation lore.
- Blue ground glow on Corridor A — buried lattice node, Echo reaction, map fragment.
- Drakeling shrine on Corridor D — keeper NPC, hidden orchard merchant access.

---

### 2.4 Tier 3 — Hidden Locations

Hidden Locations are full-scale discoverable areas not on the fast travel list and not pointed to by any quest marker. They have meaningful loot (Tier 3–4 items, Remnant possible), a full enemy encounter or significant NPC interaction, and something worth knowing. They are the highest reward for off-road exploration.

Eight to twelve exist across the Vale. Six are fully specified below. Two to four additional locations are reserved for Act II/III content and are not specified in this document.

---

#### HL-01 — The Drowned Archive
**Location:** River Serpentis, near widest point (~85m) — NE quadrant

| | |
|---|---|
| **Access** | Accessible only during summer (low water reveals submerged entry) OR via a Reaver tunnel whose entrance is a Tier 2 POI on the riverbank. Both entry methods require players to know the location exists. |
| **Description** | A pre-Dominion Firstborn structure partially submerged in the River Serpentis. The structure predates all known Firstborn records in Ashenveil Archive — it appears in no catalogue. Interior: two dry upper chambers (partial collapse, navigable) and one flooded lower chamber (swimming required, 60-second breath limit without END 20 threshold or water-breathing consumable). |
| **Encounter** | Flooded chamber guardian: an automated Construct in maintenance mode, hostile to perceived intruders. Not a boss — a standard elite Construct encounter. The Construct is repairable (INT 25 threshold + Firstborn components) rather than destroyable; repaired Constructs stand down and activate the chamber's preserved contents. |
| **Loot** | Flooded chamber: one Remnant-tier item (weapon or armour, build-aware LootSubsystem resolution). Upper chambers: Tier 3 item cache, one Firstborn data fragment. |
| **Lore Value** | Data fragment reveals the Night of Severance was not the first lattice failure — an identical event occurred 800 years earlier and was suppressed. The Firstborn covered it up. This recontextualises the entire main story's framing of the Severance as unprecedented. |

---

#### HL-02 — The Quarryman's Rest
**Location:** Eastern hillside, Corridor C (Ashford road) — visible from road as quarry scar

| | |
|---|---|
| **Access** | Quarry scar on hillside is the visual hook (visible 800m from road). The quarry entrance is unguarded. Interior path follows worked stone for 200m before reaching the sealed Firstborn chamber the miners broke into. |
| **Description** | An active limestone quarry, abandoned mid-operation. Miners' tools are still in place. Evidence of panic in the final moments — one miner's journal describes the chamber opening behind the face, something moving inside. The Firstborn chamber is intact: intact storage alcoves, intact lighting, intact one Construct that reactivated when the chamber was breached. The miners' bodies are still inside the chamber — some partially preserved by the chamber's climate control. |
| **Encounter** | One reactivated Construct (standard combat encounter, not a boss). The Construct is protecting storage alcoves — it stops engaging if the player moves away from them. Players who figure out the Construct is territorial (not aggressive to the entire space) can navigate around it. |
| **Loot** | Construct drop: Tier 3 weapon component. Storage alcoves: Firstborn components (valuable Runecarving crafting materials) plus 600–900 Crown Marks in salvageable metal parts. One Tier 4 armour piece. |
| **Lore Value** | Miner's journal — final entry: "The thing inside doesn't want us dead. It wants us out. It's been herding us toward the entrance." Recontextualises Firstborn Construct behaviour across the whole game: they are guardians, not weapons. |

---

#### HL-03 — The Glasswater Shrine
**Location:** Northern Ironwood forest edge — 280m elevation, northeast quadrant

| | |
|---|---|
| **Access** | No road leads directly to it. Discoverable via: following running water sound uphill from Corridor A; a map fragment in the Drowned Archive (HL-01) that marks a water source; Aelira dialogue if recruited and taken into the northern forest (she mentions sensing something "clean" to the northeast). |
| **Description** | A natural spring at 280m elevation whose water pre-dates the corruption of the region entirely. The spring's output has never been affected by lattice fractures — it flows from a geological formation that predates the Firstborn's arrival on the continent. The Verdant Flame know of it but have not publicised its location. No enemy presence. No threat. A quiet, beautiful place. |
| **Encounter** | No combat encounter. The only challenge is finding it. One NPC: a Verdant Flame elder in meditation who is startled but not hostile. She has been here for three days. She will not say why. |
| **Loot** | One-time consumable from the spring: a permanent minor stamina buff (+8 base stamina, non-removable, appears as a passive labelled "Glasswater Memory"). Aelira has a unique, extended reaction scene here if in the party — one of her most personal companion moments. |
| **Lore Value** | No explicit lore delivery. The place communicates through absence of corruption and the elder's presence. Players who engage with the elder across multiple dialogue trees learn she is performing a memory ritual for someone who died at this spring before the Severance. The person's name matches a name encountered later in Ashenveil Archive. |

---

#### HL-04 — The Broken Spire
**Location:** Southern borderlands, near Crimson Flats edge — SE quadrant

| | |
|---|---|
| **Access** | Visible from Corridor D as a distant broken tower silhouette. Approach requires crossing 800m of rough southern borderlands terrain and then climbing a partially collapsed structure. Rope item useful but not required — alternate path exists via interior staircase if players find the ground-level entrance. |
| **Description** | A collapsed Firstborn observation tower. The base is structurally sound; floors 2–4 are partially collapsed and require navigation through weight-bearing paths. Floor 5 is intact and open to the sky on one side — the wall collapsed outward, creating an open observation deck at 35m elevation. From here: panoramic view of the Vale and the Crimson Flats heat haze. |
| **Encounter** | No enemy encounter at the tower. One enemy patrol of 3 Vanguard soldiers on the approach path — not hostile unless attacked, but are looking for someone and will question the player. |
| **Loot** | Top floor: one Remnant-tier weapon leaning against the wall as if left by the last person to stand here. Weapon is rolled by LootSubsystem — placement is deliberate. Crafting note tucked into the weapon's wrappings: a Firstborn smith's signature, 400 years old. |
| **Lore Value** | The Vanguard patrol is searching for a deserter. If the player has previously encountered a specific NPC in Hollowford, the description the patrol gives matches that NPC exactly. No quest triggers. Players carry the knowledge. The connection may or may not become relevant depending on their choices. |

---

#### HL-05 — The Undertow Cave
**Location:** Beneath Mistwater Lake — accessible via underwater entrance on lake's north shore

| | |
|---|---|
| **Access** | Underwater entrance visible from shore if player explores Mistwater Lake's north bank (corruption zone edge, hostile). Requires: 45 seconds of breath-holding (without END 15 threshold), a light source (cave is completely dark below the waterline), and willingness to swim into a corruption-adjacent location. |
| **Description** | A natural cave system beneath Mistwater Lake. The cave is not corrupted — it predates the lake's corruption and is geologically sealed from it. Inside: two dry chambers accessible by climbing from the submerged entry. The source of Mistwater Lake's corruption is here: a saturated lattice fragment lodged in the cave wall. It is not a Firstborn device — it is a piece of raw lattice energy crystallised by the Severance into a physical form. This has never happened before. |
| **Encounter** | No boss encounter. Two standard corrupted creature spawns (guardians drawn to the fragment's energy). The fragment itself is the puzzle: removing it stops corruption spreading, leaving it maintains the status quo, taking it (requires Relic Mark interaction at SUR 20 threshold) stops the corruption but gives the player an ongoing debuff that pulses every 90 seconds for the remainder of the Act. |
| **Loot** | Option A (remove, leave it): corruption zone shrinks 40% over two in-game weeks. No item. Verdant Flame reputation gain. Option B (leave): status quo. Option C (take): fragment is a rare Runecarving component — Hollow Crown agents send a buyer to Hollowford within 5 in-game days. |
| **Lore Value** | The fragment's existence — raw lattice energy crystallising into physical form — is evidence the lattice is not failing, it is transforming. The Echo Interface's reaction to the fragment (if used) produces the clearest direct statement the Echo has ever made: "This should not be possible. And yet." |

---

#### HL-06 — The Fen Hollow
**Location:** Southeast marshland — depression in reeds 300m east of Corridor D

| | |
|---|---|
| **Access** | Marsh fog column on Corridor D is the visual hook. Reeds surrounding the depression are 3m tall — the hollow is invisible from outside. Entry requires wading through 80m of ankle-deep marsh water. No map marker. No path. |
| **Description** | A natural depression in the marshland containing a small Drakeling settlement of 12 people who declined the Hollowford refugee camps. The settlement is semi-permanent: canvas structures, a fire, a small herb garden. The 12 people are not hiding — they simply chose not to go north. Spokesperson: Elder Keth-Mara. |
| **Encounter** | No combat encounter. The settlement is wary of outsiders but not hostile. One threat: Vanguard patrol that comes within 200m of the hollow twice per in-game week and has not yet noticed it. Players can warn the settlement, help conceal it, or say nothing. |
| **Loot** | Merchant: Deth-Ara. Sells southern Flats salvage goods (obsidian fragments, drake-scale scraps, heat-resistant alloys) unavailable from any other Act I merchant. Questline: 3-part, not in main journal. Rewards: permanent safe house in the marshland, access to Deth-Ara's full inventory. |
| **Lore Value** | The Fen Hollow people know the Caldera is not purely volcanic — something is directing the eruptions. They have a word for it in their dialect. When translated via Echo Interface, the word matches a Firstborn engineering term from Ashenveil Archive: "controlled demolition." |

---

## Section 3 — Puzzle Design Framework

### 3.1 Design Principles

These principles are derived from player research on what makes RPG puzzles memorable versus frustrating. They are non-negotiable. Puzzles that violate them should be redesigned, not shipped.

> **The Five Principles**
>
> 1. **The solution must be visible in the problem.** Every clue needed to solve a puzzle exists within the same space as the puzzle. No external knowledge required.
>
> 2. **Multiple valid approaches beat a single intended solution.** Players who brute-force, find the elegant path, or discover an unintended method all feel the same pride. Design for at least two valid approaches per puzzle.
>
> 3. **Difficulty comes from insight, not complexity.** A puzzle with two elements and a non-obvious solution beats a puzzle with eight elements and a mechanical solution. The "aha" moment is the reward.
>
> 4. **Puzzles must fit the world's logic.** A puzzle that feels arbitrary breaks immersion permanently. Every puzzle type below is grounded in the game's existing lore systems.
>
> 5. **Failure must be visible and reversible.** Wrong configurations produce visible signals. No puzzle dead-ends silently. No puzzle failure permanently locks a reward.

---

### 3.2 The Six Puzzle Types

---

#### Type 1 — Lattice Redirection
*Player feels: understanding a broken system and restoring it — infrastructure problem-solving*

**Lore basis:** The Firstborn built the lattice as literal infrastructure — pipes, conduits, nodes. Post-Severance, energy flows incorrectly: backing up, leaking, blocked. Players physically reroute flow using Firstborn components (moveable pylons, reflective crystal panels, conduit connectors).

**Visual language:** Active conduits glow pale blue-white (per SD-09). Blocked conduits are dark. Incorrect flow produces a faint purple-pink tinge (corruption precursor). Correct flow: clean sustained tone. Wrong configurations arc visibly — players see they are wrong without being told.

| Tier | Nodes | Visibility | Time Pressure | Location |
|---|---|---|---|---|
| 1 — Entry | 2 nodes, 1 junction | Direct line of sight | None | Ashenveil Archive upper levels, wilderness ruins |
| 2 — Standard | 3–4 nodes, branching | Partially obscured | Optional (corruption) | Tier 2 and Tier 3 POIs |
| 3 — Advanced | 5+ nodes, multi-path | Some nodes hidden | Mild zone timer | Ashenveil Archive trials |
| 4 — Mastery | 6+ nodes, destructive wrong paths | Deliberately hidden | Hard pressure | Ashenveil Archive core chamber |

**Alternate solutions:** A player who cannot solve the puzzle can break a conduit by force (less efficient, causes corruption damage, but works). A Verdant Flame-aligned player with a purification tool can bypass lattice puzzles entirely. The puzzle rewards elegance; it does not permanently punish non-elegance.

---

#### Type 2 — Echo Memory
*Player feels: investigation and archaeology — piecing together what happened in a space*

**Lore basis:** Locations with strong emotional imprints leave residue the Echo Interface can read — but the Echo is broken. Receiving a memory requires physical action first: standing in the right position, interacting with objects in sequence, or reaching a location at a specific in-game time.

This is the only puzzle type where the reward is always lore, never loot. The lore has mechanical utility — it reveals a combination, identifies a weakness, exposes a hidden path, or recontextualises a major story event.

**Constraints:**
- Echo Memory puzzles must be solvable entirely through observation of the space where they are found. External information can enrich the solution — it cannot be required for it.
- The physical action required to trigger a memory must be discoverable through environmental observation, not stated by any NPC or UI element.
- The memory itself must be legible without prior lore knowledge — context clues within the memory explain what it means.

---

#### Type 3 — Sealed Firstborn Structures
*Player feels: the detective's satisfaction of understanding a security system*

**Lore basis:** Firstborn security uses biological-lattice resonance authentication. Sealed structures respond to specific energy configurations — not keys in the traditional sense.

| Seal Type | Solution | Alternate Solution |
|---|---|---|
| Type A — Construct Signature | Construct energy field opens door (alive or recently killed — 60s death-echo window) | Kill the Construct adjacent to the door; reach the door within 60 seconds |
| Type B — Relic Shard Configuration | Specific shard combination in relic socket (pattern encoded above door) | Trial-and-error if player can read the encoding; alternate physical entrance always exists |
| Type C — Purification Intensity | Verdant Flame purification at specific calibrated level | Multiple purification sources at different intensities in same space — players improvise |

Every sealed structure has a bypass. No puzzle should hard-gate a Tier 3 location. Standard bypasses: collapsed wall section, ventilation shaft, underwater approach. The bypass is harder or more dangerous than the elegant solution — but it exists.

---

#### Type 4 — Corruption Load-Bearing
*Player feels: ethical cost-benefit — not "how do I solve this" but "how much am I willing to pay"*

**Lore basis:** Corruption has crystallised around objects of value. Three approaches produce different costs and yields — establishing a pattern consistent with the game's core design rule: no faction is right, choices have consequences but not binary ones.

| Approach | Speed | Player Cost | Item Yield | World Effect |
|---|---|---|---|---|
| Purify (Verdant Flame tools) | Slow — 30–90 sec exposure | Combat exposure risk | Full quality | Local corruption reduces; VF reputation gain if witnessed |
| Break Through (force) | Fast | Corruption damage (temp debuff) | Item damaged (minor stat loss) | None |
| Lateral Solution | Variable | Observation investment | Full quality + minor XP bonus | Varies by specific puzzle |

**Design requirement:** Every corruption puzzle must visually telegraph all three approaches. The violence option is the most obvious. The purification option requires tool knowledge. The lateral option requires looking at the full room, not just the obstacle.

---

#### Type 5 — Firstborn Observation
*Player feels: being rewarded for paying attention — the detective's quiet satisfaction*

These puzzles have no UI indicator. No glow, no prompt, no marker. The puzzle exists in the world and players either notice it or they do not. Players who notice feel genuinely smart. Players who do not are not punished — they simply do not get the reward.

| Name | Observation Required | Payoff |
|---|---|---|
| Star Map Cairn (Sunspear Ridge) | At summit at sunrise — shadow pattern from cairn stones matches Firstborn star map etched on nearby flat rock | Pattern points to Ashenveil Archive's hidden entrance — accessible without any quest directing there |
| Pond Reflection (Wilderness) | Reflection shows pre-Severance sky AND pre-Severance structure no longer standing above ground | Mapping reflection architecture against terrain locates buried Firstborn foundations — Tier 2 POI beneath |
| Mill Rhythm (Grainfell approach) | Still-turning mill wheel produces rhythmic sound that is a Firstborn coordinate encoding (INT 25 + Echo translate) | Coordinates point to Firstborn storage vault beneath mill — accessible only via this knowledge |
| Road Silence Zone (Wilderness) | Silence zone boundary follows outline of buried Firstborn structure — mappable by walking the edge | Structure footprint reveals entrance location — discoverable only by tracing the silence |

---

#### Type 6 — Moral Trial Chambers
*Player feels: genuine uncertainty and weight — no answer feels fully right*

**Lore basis:** The Firstborn designed trial chambers to evaluate candidates for lattice access. The trials were designed to reveal character, not to be winnable. The chambers still function.

**Ashenveil Archive's three trials (Act II):**

**Combat Trial:** Waves of Constructs. Not a puzzle — a combat encounter. The puzzle is what happens after: the player can destroy every Construct, destroy only enough to pass, or find a specific Construct that disables the others when interacted with rather than killed. The chamber observes the player's approach and echoes it in the lore fragment unlocked at the end. A player who destroyed everything receives a fragment about Firstborn who destroyed everything. A player who found the disable method receives a fragment about Firstborn who looked for alternatives. The fragment differs — never the reward amount.

**Lattice Trial:** A Type 1 lattice redirection puzzle with a specific feature: one valid solution is significantly more efficient than another. The efficient solution powers the chamber's central memory node. The less efficient solution powers a secondary system the player has not seen before — a hologram of a Firstborn argument about the lattice's true purpose. Both solutions pass the trial. Only one reveals the hidden lore.

**Moral Trial:** A situation with no right answer. Two Firstborn recordings play — two Firstborn who disagreed about what to do in a crisis. The player must side with one. No immediate mechanical consequence. Delayed consequence: the faction aligned with the player's choice in the trial offers a specific quest in Act III that the other faction never does. The connection is never made explicit. No loot reward attached to any choice. Companions react — Aelira has a strong opinion, Kael has a different strong opinion. Neither lectures.

---

### 3.3 Puzzle Difficulty Curve

| Act | Primary Types | Complexity Ceiling | Primary Reward |
|---|---|---|---|
| Act I | 1 (basic), 5 (observation) | 2-node redirection, single-observation puzzles | Lore + Tier 2 loot |
| Act II | 1 (advanced), 2, 3 | 5-node redirection, multi-stage Echo Memory, seal types A–C | Tier 3 loot + story recontextualisation |
| Act III | 4, 6, 1 (mastery) | Corruption cost-weighting, full moral trials, 6-node redirection | Hidden location access + ending flags |
| Wilderness (all acts) | 5, 2 (light) | Observation-only, no manipulation required | Micro-discovery lore, Tier 2 POI flags |

---

### 3.4 Anti-Patterns — What Not to Build

> **Prohibited Puzzle Patterns**
>
> **No number-sequence puzzles without world grounding.** "Pull lever 2, then 5, then 1" with no in-world reason for the sequence is arbitrary and breaks immersion permanently. Every sequence must be derivable from the environment's own logic.
>
> **No puzzles requiring a specific companion.** Aelira enriches lattice puzzles; Kael enriches combat trials. Neither is mandatory. A player without companions must be able to solve every puzzle.
>
> **No build-gated Tier 1 puzzles.** 6 INT and 30 INT should both solve Tier 1 puzzles. Higher INT may reveal additional layers; it must not be required for the core solution.
>
> **No permanent failure.** Wrong configurations, corrupted items, wrong moral trial choices — all produce a different version of the reward or a harder path to the same reward. The game never tells a player "you cannot have this because you got it wrong."
>
> **No tutorial text for puzzle mechanics.** The game teaches puzzle types through scaled experience. A simple version always comes first. The first lattice puzzle teaches the mechanic for the Ashenveil Archive's complex version.

---

## Section 4 — UE5 Implementation Priorities

### 4.1 Data Architecture Required

All exploration content specified in this document depends on the following UE5 components. None of this content can be placed in the editor until these systems exist and are tested end-to-end.

| Component | Type | Status | Description |
|---|---|---|---|
| `USDPointOfInterestData` | `UPrimaryDataAsset` subclass | Specified in prev. session | DataAsset defining tier, category, discovery tag, world state gates, loot table ref, map appearance flags |
| `ASDPointOfInterestActor` | `AActor` subclass | Specified in prev. session | In-world actor with discovery radius sphere, condition evaluation, loot spawn trigger, discovery event delegate |
| `USDDiscoverySubsystem` | `UGameInstanceSubsystem` | Needs implementation | Tracks all discovered POIs by tag, provides query API (`HasDiscovered`, `GetCountByCategory`), handles save/load serialisation |
| `USDMapSubsystem` | `UWorldSubsystem` | Not yet specified | Receives discovery events from `USDDiscoverySubsystem`, updates map icons for Tier 2 and Tier 3 POIs only |
| Landscape Material (8-layer) | `UMaterial` | Architecture specified | Farmland fertile/dry, forest floor, rocky hills, riverbank mud, wetlands, corruption ground, snow/frost — corruption layer driven by `USDCorruptionSubsystem` at runtime |

---

### 4.2 Build Order — Exploration Systems

Follow this sequence exactly. Building out-of-order creates rework.

1. World Partition enabled at project level. Cell size 12800 UU. Loading range 25600 UU. Do not proceed without this — World Partition cannot be added to an existing level without reconstruction.
2. Landscape created at correct scale: 2017×2017 heightmap resolution, X/Y scale 100. Heightmap imported, not hand-sculpted — manual sculpting used only for River Serpentis channel, Mistwater Lake basin, ford crossing, and cliff face sharpening.
2a. Slope validation pass: enable landscape slope debug visualization. Verify 30°+ slope distribution against Section 1.4 expectations. If ridge transitions or road corridors show excessive steepness from heightmap compression, manually sculpt to soften before proceeding. Validate AI navmesh builds cleanly on eastern ridge and Sunspear approaches — add NavLink proxies where needed.
3. 8-layer landscape material created, painted to base biome state. Macro variation texture applied to break tiling at distance (verify from Sunspear Ridge elevation — tile pattern is visible at 3km without this).
4. River Serpentis placed using UE5 Water Body River plugin. Width 30–80m, clear-to-murky shader variant. Ford crossing at Hollowford verified at 1m below surrounding bank.
5. `USDPointOfInterestData`, `ASDPointOfInterestActor`, and `USDDiscoverySubsystem` implemented and unit tested. Verify: discovery fires correctly, tag granted to player, Tier 1 produces no map mark, Tier 2 produces greyed icon, state saves across session boundary.
6. SW quadrant blockout — full SW quadrant (~5 km²) including Hollowford and river approach. No final assets. Verify all sightlines from Section 1.5 before committing to any asset placement.
7. One complete Tier 1 micro-discovery placed, end-to-end tested. One Tier 2 POI placed, end-to-end tested. Verify map appearance logic. Only after both pass: begin content placement for remaining POIs.

---

### 4.3 Corridor Blockout Checklist

Before placing any assets on any road corridor, verify the following from UE5 viewport at player eye level (175cm camera height):

- At every 500m point on the road: is there a visual hook? Stand at the point, rotate 360°. If the answer is "only trees" — add a hook or reshape terrain before proceeding.
- At every hook location: walk to the road and verify the hook is visible. If it is not visible from the road, it is not a hook — it is a secret. Secrets require a different design reason to exist.
- At every hook location: verify the "honest" test. If the hook suggests a structure, there is a structure. If it suggests fire, there is fire. No misleading environmental geometry.
- Sightlines from Section 1.5: verify each from the listed origin point. If any sightline fails due to terrain obstruction, fix terrain before placing assets in the blocked area.
- At Sunspear Ridge summit: verify the star map shadow puzzle is achievable. The flat stone and cairn must produce a readable shadow pattern at the correct in-game sunrise angle.

---

### 4.4 Puzzle Implementation Notes

#### Type 1 — Lattice Redirection
- Lattice energy flow is a visual effect system, not a gameplay system. Puzzle state is tracked in Blueprint (or C++ LevelScript) per-dungeon. Do not route puzzle state through `USDWorldStateSubsystem` — it is local, not global.
- Energy flow direction: use Niagara ribbon emitters with direction vectors. Do not use particle systems with no directional logic — players must be able to read which way energy is flowing.
- Wrong configuration arc effect: Niagara system with spawn rate tied to puzzle error state. Purple-pink tinge on conduit material: material parameter set by Blueprint puzzle state.

#### Type 2 — Echo Memory
- Echo trigger volumes: `BoxComponent` or `SphereComponent` with overlap events. Multiple overlapping volumes can define a "sequence" — all must be activated in order within a time window.
- Memory playback: Sequencer cinematic, not cutscene. Player retains control during playback. Memory is a visual overlay (post-process + Niagara), not a full-screen cinematic.
- In-game time gate: query `USDWorldStateSubsystem` for current in-game time. Do not hardcode time checks — use the subsystem's time API.

#### Type 5 — Observation Puzzles
- Star Map Cairn shadow puzzle: use a decal projected from a directional light parented to the in-game sun. Shadow decal reveals pattern only at correct sun angle. No Blueprint logic required — purely lighting-driven. Test at multiple in-game time values to confirm the pattern is only readable at sunrise.
- Road silence zone: use Audio Volume with attenuation override set to zero. The silence boundary must follow the buried structure's footprint exactly — use a custom collision shape, not a sphere or box.
- Mill rhythm encoding: audio cue is authored in Wwise/MetaSounds as a specific rhythmic pattern. The translation output (visible to INT 25+ players via Echo Interface) is a separate UI element, not a subtitle — it should feel like the player's character translating, not the game explaining.

---

## Appendix A — Visual Hook Quick Reference

| Corridor | Distance | Hook Name | Type | Reward Tier |
|---|---|---|---|---|
| A (→Ironwood) | 300m | Ruined Watchtower | Silhouette | Tier 2 |
| A (→Ironwood) | 600m | Smoke Plume / Abandoned Farm | Smoke/particle | Tier 1 |
| A (→Ironwood) | 900m | Crystal Falls glimpse | Light + sound | Tier 3 |
| A (→Ironwood) | 1.2km | Blue Ground Glow (lattice node) | Light anomaly | Tier 2 |
| A (→Ironwood) | 1.5km | Stone Arch (logging road) | Silhouette | Tier 1 |
| B (→Grainfell) | 300m | Split Corruption Field | Pattern | Tier 1 |
| B (→Grainfell) | 625m | Still-Turning Mill Wheel | Movement + sound | Tier 2 |
| B (→Grainfell) | 950m | Standing Stones on Hillside | Silhouette | Tier 2 |
| B (→Grainfell) | 1.25km | Crystallized Dead Tree | Silhouette + light | Tier 1 |
| C (→Ashford) | 300m | Hollow Crown Survey Flag | Object | Tier 1 |
| C (→Ashford) | 750m | Quarry Scar on Hillside | Silhouette | Tier 3 |
| C (→Ashford) | 1.25km | Dry Creek Bridge Ruins | Pattern + sound | Tier 1 |
| D (→Southwatch) | 750m | Drakeling Roadside Shrine | Object | Tier 2 |
| D (→Southwatch) | 1.25km | Marsh Fog Column | Light anomaly | Tier 3 |
| D (→Southwatch) | 1.75km | Sunken Vanguard Cart | Object | Tier 1 |

---

## Appendix B — Puzzle Type Quick Reference

| Type | Name | Core Mechanic | Reward Type | Acts Active |
|---|---|---|---|---|
| 1 | Lattice Redirection | Reroute energy flow using moveable Firstborn components | Loot + lore | I, II, III |
| 2 | Echo Memory | Physical positioning/sequencing to trigger Echo memory fragments | Lore only (high utility) | I, II, III |
| 3 | Sealed Firstborn Structures | Construct signature, shard config, or purification intensity | Location access + loot | II, III |
| 4 | Corruption Load-Bearing | Choose approach (purify/force/lateral) with different cost-benefit | Loot (quality varies by approach) | II, III |
| 5 | Firstborn Observation | Notice environmental detail with no UI prompt — no mechanic required | Hidden location access, lore | I, II, III |
| 6 | Moral Trial Chambers | Choose between Firstborn positions with no correct answer | Delayed narrative consequence | II |

---

## Appendix C — Tier 3 Hidden Location Summary

| ID | Name | Quadrant | Access Method | Key Loot | Core Lore Value |
|---|---|---|---|---|---|
| HL-01 | The Drowned Archive | NE — River Serpentis | Summer low water OR Reaver tunnel | Remnant item + data fragment | Severance has happened before — covered up |
| HL-02 | The Quarryman's Rest | W — Corridor C hillside | Quarry scar hook → interior path | Remnant weapon + Tier 4 armour | Constructs are guardians, not weapons |
| HL-03 | The Glasswater Shrine | NW — Northern forest | Water sound, map fragment, Aelira | Permanent stamina buff (unique) | Pre-Firstborn geology — world older than lore states |
| HL-04 | The Broken Spire | SE — Southern borderlands | Visible silhouette, terrain cross, climb | Remnant weapon at summit | Vanguard patrol mystery + Firstborn smith lineage |
| HL-05 | The Undertow Cave | N — Mistwater Lake | Underwater swim from north shore | Triple-choice resolution (no single item) | Lattice transforming, not failing — key to endgame |
| HL-06 | The Fen Hollow | SE — Marshland | Fog column hook → wade through reeds | Unique merchant access (all Acts) | Crimson Flats eruptions are directed — not natural |

---

*SD-12 World Exploration & Puzzle Design Specification — v1.0*
*Next document: SD-13 Hidden Location Full Specifications (HL-01 through HL-12)*
