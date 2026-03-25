# THE SHATTERED DOMINION — SETTLEMENT & HOMESTEAD SYSTEM
## Document 12 | Version 3.0 | Depends on: SD_01 World Bible, SD_08 Severant Vale Region Guide, SD_11 Economy System

**Revision Notes (v2.0 → v3.0):**
- Section 4.2: Faction Envoy transition mechanic fully specified (cost, timeline, act-specific behavior)
- Section 4.3: Veslan Ohr full specification added (stock categories, rotation logic, information system, authored first-visit dialogue direction)
- Section 6.1: Guard Barracks removed from Residential catalog; cross-reference to Defense section added
- Section 6.5: Guard Barracks canonical home confirmed as Defense; housing function noted explicitly
- Section 9.5: New subsection added — Equipment Policy Production Tradeoff; Blacksmith dual-consumption demand documented with planning guidance
- Section 10.1: First-raid tutorial design decision added — first organized raid is always minimum-strength Organized Bandit Crew regardless of homestead tier
- Section 11.1: Partial Breach recovery session description added (Phase 4) as sixth session scenario
- Section 11.2: Personal Harvest and Site Improvement micro-activities revised to produce categorically unique rewards unavailable through passive means
- Checklist updated throughout

**Revision Notes (v1.0 → v2.0):**
- Worker needs system overhauled with buffer mechanics; Steward auto-resolution logic expanded
- Section 10 (Defense) substantially redesigned: Notable Threshold trigger, worker equipment system, absent vs. present attack resolution, five typed attack categories, destruction/theft matrix, faction awareness progression
- Township tier rewards expanded with three exclusive features (Merchant Circuit, Faction Envoy, Resonance Spire)
- Cassian Aelveth arc defined with three resolution endpoints and Act II deadline
- Phase 3–5 day-to-day session descriptions added to Section 11
- Player-driven micro-activity system added
- Township world-acknowledgment events authored (five specific events)
- Section 1.1 "world notices" language grounded with specific authored content

**Authority Note:** This document is the authoritative specification for the Homestead and Settlement Building System. It supersedes and replaces SD_11 Section 6 (Property and Business Ownership) **for the Homestead system only**. SD_11 Section 6 commercial property types (Storefronts, Warehouses, Information Broker Offices, Taverns) remain valid and are a separate, complementary system. Where this document contradicts SD_11 Section 6, SD_12 takes precedence. SD_11 should be updated to reference SD_12 for homestead content.

**Design Reference:** The Shattered Dominion is a game about rebuilding something in a world that just broke. The homestead system is that idea made physical. It is not a distraction from the main game — it is a place the player makes real over time, and then wants to come back to.

---

# SECTION 1: DESIGN PHILOSOPHY

## 1.1 Core Principles

**It is a home, not a menu.** Every upgrade to the homestead should be visible, spatial, and felt. The player should be able to stand at the edge of their land after twenty hours of play and see what they built — not read a stat screen. The difference between a freshly claimed plot and a fully developed settlement should be visually dramatic. When this system tempts design toward abstract numerical upgrades, push back and ask what the player can see change. That question is the north star.

**Complexity comes from options, not from learning requirements.** The building system must be learnable in under ten minutes and offer hundreds of hours of depth. The solution: snap-point placement with Blueprint shortcuts. Players who want granular control get it. Players who want to place a pre-designed building and move on can do that. The system never forces one mode on the other.

**Build it because you want to, not because the game makes you.** Settlement building is entirely optional. The main story does not gate behind homestead milestones. However, players who build deeply receive genuine advantages: material production, passive income, crafting access, and a population of workers whose labor compounds over time.

**Every building does something.** There are no decorative-only structures in the functional tier. Decorative items and furnishings exist for personalization, but every building category provides either production, economic output, population support, or crafting access. Players are never building inert scenery unless they choose to.

**The system runs itself at scale. The player intervenes with meaning, not with maintenance.** A Village-tier homestead with 20+ workers cannot become a second job. Worker needs, production cycles, and morale incidents should self-manage at the routine level — the Steward handles the ordinary, and only genuinely interesting decisions escalate to the player. The goal is proportionate friction: player attention has value because it is reserved for things that matter, not consumed by daily upkeep.

**The world notices a large settlement — specifically and concretely.** A Township-tier homestead is a small town in a post-Severance world. This is not a footnote; it is a significant thing. The world's acknowledgment of this must be authored, not assumed to emerge from ambient dialogue. Five specific world-acknowledgment events fire at Township tier (see Section 11.3). Named NPCs across the Vale reference the settlement by name. Faction leaders treat it as a political entity. Players who invest forty hours in building something deserve to feel that the world noticed.

## 1.2 Relationship to SD_11 Commercial Properties

The homestead system and the SD_11 commercial property system are **two separate systems that integrate but do not overlap**.

| System | What It Is | Scope | Location |
|---|---|---|---|
| **Homestead** (SD_12) | Player's primary land holding. Physical building, farming, crafting, community. | One primary site; potentially one secondary | Player-claimed rural or semi-rural land |
| **Commercial Properties** (SD_11) | Business investments in existing settlements. Storefronts, warehouses, workshops, info broker offices. | Multiple; spread across the Vale's towns | Inside or adjacent to existing settlements |

A player can own both. They serve different functions. Commercial properties are investment and passive income inside existing economies. The homestead is where the player lives, farms, crafts, and builds a community. Production from the homestead can feed commercial properties — that is the intended integration point.

## 1.3 Design Reference Games and Lessons Applied

**Fallout 4 (Bethesda)**
- ✅ Adopted: NPC settlers with assigned roles; supply lines feeding shared inventory; modular building pieces + prefab options; workshop as management hub; scalable investment (minimal or maximal)
- ❌ Avoided: Clunky first-person-only build camera; confusing power wiring (SD uses proximity-based utility zones); 37 equal settlements spreading investment too thin; mandatory faction integration; short departure windows that punish players mid-quest (SD uses a buffer tolerance system)

**Valheim (Iron Gate)**
- ✅ Adopted: Color-coded structural feedback during placement; snap points that make placement feel satisfying; material tier progression that mirrors game progression; earned sense of permanence
- ❌ Avoided: True structural integrity simulation (too complex for an RPG not primarily a builder — SD uses simplified visual feedback without collapse risk); no NPC population

**No Man's Sky (Hello Games)**
- ✅ Adopted: Blueprint/template system for placing whole pre-designed buildings instantly; clean build mode UI with clear categories; the feeling that every location produces a different-feeling base

**Kenshi (Lo-Fi Games)**
- ✅ Adopted: Building-by-building placement for functional tier; the feeling that a settlement is a meaningful faction-scale operation at high development; worker assignment to buildings

**Stardew Valley (ConcernedApe)**
- ✅ Adopted: Farm layout with genuine spatial strategy; seasonal production rhythms; satisfaction of a well-organized working farm; player-driven optional engagement between passive cycles

---

# SECTION 2: HOMESTEAD LOCATIONS

## 2.1 System Overview

The player chooses one primary homestead location from a set of designated sites across the Severant Vale. Each site is a physical piece of land already present in the world — the player is not generating terrain, they are claiming and developing an existing location with its own character, history, and starting conditions.

All homestead sites share the same building system and progression potential. They are differentiated by starting terrain and aesthetic, proximity to major settlements, pre-existing structures, adjacency bonuses and complications, and the story of prior occupants — every site has one.

## 2.2 Available Homestead Sites

### SITE 1 — The Thornfield
**Location:** NE quadrant, Grainfell region. Open farmland on the Verdantheart border, river tributary nearby.
**Starting Condition:** Abandoned farmstead. Collapsed barn, partial stone fence, overgrown field rows still visible. Prior family fled to Hollowford after the Severance.
**Size Class:** Medium-large
**Adjacency Bonuses:**
- Fertile soil: Farm yield +15% base
- River tributary: Water access eliminates irrigation cost
- Grainfell proximity: Farm output sells at slightly higher prices due to local grain shortage; community standing with Grainfell residents builds faster
**Adjacency Complications:**
- Corruption zone creep from Verdantheart border is a late-game threat — soil quality degrades, crop yields drop, Corruption Breach raids become possible
- Verdant Flame scouts pass through; their attitude is faction-dependent
**Starting Resources:** Scrappable barn wood, partial stone foundation
**Aesthetic Identity:** Working farmland. Fields, orchards, modest stone buildings. The kind of place that existed for generations and looks it.
**Prior History:** The Aldenmoor family ran this land for three generations. Mira Aldenmoor, now in Grainfell, cares deeply what happens to it. She visits when the player reaches Farmstead tier. If the player builds an orchard, she recognizes the heritage apple trees her grandmother planted and says so — a moment with no mechanical weight that players will remember. The Broken Mill in Grainfell (SD_11) belonged to a family the Aldenmoors knew; these two NPC threads exist in the same neighborhood and are worth developing as a Grainfell character cluster.

---

### SITE 2 — The Ironwood Clearing
**Location:** NW quadrant, northern Vale, Ironwood region. Forest-edge clearing, mixed pine and oak around the perimeter.
**Starting Condition:** Old logging camp. Equipment shed, fire pit, rough-hewn bunkhouse frame.
**Size Class:** Medium (forest constrains expansion on three sides; can be cleared for a cost)
**Adjacency Bonuses:**
- Forest access: Timber production requires no wood import
- Ironwood proximity: Ironkin crafters available for hire at reduced cost
- Natural defensive perimeter: Forest on three sides forces attackers through a single corridor; reduces Opportunistic Bandit frequency
**Adjacency Complications:**
- Hollow Crown Highlands to the northwest — tensions bleed into this area during Act II, increasing raid risk
- Agricultural output requires clearing forest (irreversible; forest adjacency bonus diminishes per cleared plot)
**Starting Resources:** Rough-hewn structural lumber, iron salvage from logging equipment
**Aesthetic Identity:** Fortified forest outpost. Timber construction, high walls, functional over beautiful.
**Prior History:** Crew foreman Harrek Dunweld still drinks at the Broken Axe in Ironwood. He sells the player original camp layout plans (Blueprint unlock) at Friendly standing. He visits at Manor Estate tier and comments gruffly on what has been built — approving if the timber work is solid, critical if the player has replaced all the wood with stone.

---

### SITE 3 — The Ashford Ridgeline
**Location:** SW quadrant, Ashford region. Elevated ridge overlooking the western Vale.
**Starting Condition:** Abandoned noble minor holding. Stone foundations, collapsed tower, small chapel ruin.
**Size Class:** Medium (ridge limits lateral expansion; vertical construction viable)
**Adjacency Bonuses:**
- Elevated position: Watchtower detection range doubled at this site; all raid events receive advance warning regardless of tower count
- Stone quarry nearby: Stone construction costs 20% reduced
- Hollow Crown Highlands trade routes proximity: Trade income bonus from Trading Post
**Adjacency Complications:**
- Vanguard-controlled mine in Ashford; faction politics affect labor availability
- Exposed to arcane storms; buildings require weatherproofing investment at higher tiers
**Starting Resources:** Stone foundation (reusable), chapel ruin with hidden cache (brief quest hook)
**Aesthetic Identity:** Fortified stone manor. High walls, tower option, formal layout.

**Prior History and the Cassian Aelveth Arc:**
The Ashford Ridgeline belonged to the minor Hollow Crown noble house Aelveth. The heir, Cassian Aelveth, is in Hollowford, dispossessed. He believes — with some legal basis — that the player occupies his family's land. This thread has three resolution endpoints and closes at the start of Act III regardless of player choices.

**Resolution A — Bought Out:** 40 silver; Cassian agrees after two conversations, leaves Hollowford for the Highlands. Clean exit; no relationship built. Chapel cache is the player's without complication.

**Resolution B — Cassian as Steward:** A three-stage quest chain — locating his family's deed documents, recovering a personal item from the chapel ruin, and offering him a formal role. Cassian becomes a named Steward with site-specific historical knowledge, Hollow Crown social network access that improves trade income on Highlands-adjacent routes, and personal investment in the homestead's success. A dispossessed noble finding purpose as steward of his own family's land, rebuilt by someone else — thematically coherent with SD's broader subject matter.

**Resolution C — Unresolved (Default):** Cassian periodically tips off bandit crews to the homestead's schedule, adding a small frequency modifier to Organized Bandit raids. He surfaces in one Act III faction negotiation as a hostile witness if the player is formalizing Hollow Crown standing.

**Timeline:** First encounter triggers on site claim. All three paths are available Act I through Act II. At Act III start, unresolved threads freeze: Cassian either commits to ongoing (minor) hostility or disappears from the narrative. Players are not chased by this indefinitely.

---

### SITE 4 — The Southwatch Flats Outpost
**Location:** SE quadrant, near Southwatch, facing the Crimson Flats border.
**Starting Condition:** Decommissioned Vanguard waystation. Solid stone building, perimeter wall in good repair, functioning well.
**Size Class:** Small-medium (flat terrain allows expansion in all directions)
**Adjacency Bonuses:**
- Existing structure: Player starts with one free functional Stone Building
- Southwatch proximity: Refugee labor pool in high numbers
- Crimson Flats access: Rare materials locally; unique crafting recipes unavailable elsewhere
**Adjacency Complications:**
- Highest baseline raid frequency of all five sites; defense investment is near-mandatory from Farmstead tier, not Village tier
- Drakeling refugee proximity: faction dynamics affect worker availability and morale during Act II
- Furthest from Hollowford: Highest trade route overhead
**Starting Resources:** Functional stone building, perimeter wall, working well
**Aesthetic Identity:** Frontier outpost. Practical, fortified, rough-edged.
**Prior History:** Sergeant Lena Croft, who was stationed here, returns periodically to check on "her post." Not hostile, but clearly unresolved. She cannot be recruited as a worker — still technically Vanguard — but can become a named contact who provides advance intelligence on Crimson Flats raid activity based on how the player treats her across several visits.

---

### SITE 5 — Mistwater Lakeshore
**Location:** Central Vale, Mistwater Lake shore. Accessible but somewhat isolated.
**Starting Condition:** Seasonal fishing post. Dock frame, smoking shed, minimal structure.
**Size Class:** Large (lakeshore offers wide flat expansion; dock expansion into shallow water possible — unique to this site)
**Adjacency Bonuses:**
- Fishing: Unique food production type; smoked fish is a consistently high-value trade good
- Water adjacency: All irrigation costs eliminated; water-powered Watermill possible
- Aesthetic premium: Workers' morale has a persistent passive bonus — turnover lower than any other site without additional investment
**Adjacency Complications:**
- Isolated: No settlement adjacency bonus; all goods must be transported further
- Mistwater Lake has its own quest (Sentinel boss); early development may intersect
- Arcane water contamination in Act II affects fishing yield if the lake's corruption arc is not addressed
**Starting Resources:** Dock frame, smoking shed
**Aesthetic Identity:** Lakeside village. Organic, scenic, spread along the water. The only site where buildings can be constructed over water.
**Prior History:** The fisherman who owned this post died in the first week after the Severance. His adult son Deven, in Hollowford, sold the land out of grief. If the player develops the site substantially, Deven visits unprompted. He does not want work or money. He just wants to sit by the water for a while. The player can let him, or ask him to leave.

---

## 2.3 Secondary Site

At Township tier, the player unlocks the option to establish a second, smaller outpost — not a full homestead, but a functional working camp. The secondary site uses a subset of the building system: no housing beyond a minimal bunkhouse, maximum 8 workers, full production buildings available. It is an operational extension of the primary homestead, not an emotional one. Secondary site locations are smaller, undeveloped parcels in other parts of the Vale with no prior history NPCs or named complications.

---

# SECTION 3: THE BUILDING SYSTEM

## 3.1 Core Mechanics Overview

The player enters Build Mode by interacting with the Homestead Stone (see Section 5). Build Mode changes the camera to a free-roaming third-person overhead perspective, allowing the player to survey and interact with their land from above, or drop to ground level for detailed placement.

The building system operates in two layers:
1. **Blueprint Placement** — Place a complete, pre-designed building as a single object. Fast, clean, no assembly required. The building spawns as a construction site and completes after time or worker assignment.
2. **Custom Placement** — Place individual structural pieces (walls, floors, roofs, windows, doors) to compose custom structures from scratch. Full creative control. Pieces snap to a grid.

Both modes are always available. No mechanical penalty exists for using either mode for any structure.

## 3.2 Snap-Point Grid System

All building pieces operate on a **snap-point system**. The grid is **2-meter-unit-based**. Standard rooms are 4m × 4m, 4m × 6m, or 6m × 6m. Walls are 2m wide, 2.5m or 3m tall. Floors and ceilings snap to wall tops automatically. Players can override snap-alignment with manual rotation in 45-degree increments, or hold a modifier key for freeform rotation.

**Terrain Adaptation:** Pieces placed on uneven terrain automatically adapt within a 0.5m tolerance. Beyond that, the player is notified the terrain needs leveling.

## 3.3 Color Feedback System

| Color | Meaning |
|---|---|
| **Green** | Valid placement; can be placed now |
| **Blue** | Valid placement; snapping to existing structure |
| **Yellow** | Valid but adjacency warning (near plot boundary; may interfere with another structure) |
| **Orange** | Placement requires a prerequisite (needs foundation; needs specific worker unlocked) |
| **Red** | Invalid placement (terrain conflict, outside plot boundary, no materials) |

There is **no structural integrity collapse system** in SD. Structural coherence is enforced through snap-point logic — pieces that cannot meaningfully connect to existing structures will not snap. Coherent buildings are produced without engineering homework.

## 3.4 Material Tiers

| Tier | Name | Primary Materials | Unlock Condition | Visual Identity |
|---|---|---|---|---|
| **T1** | Timber | Rough-cut lumber, thatch, clay | Available from start | Rough-hewn farmstead; exposed wood, low roofs, practical |
| **T2** | Dressed Stone | Cut stone, fired brick, iron fittings | Act I mid-game; requires Stonecutting Station | Solid, permanent-looking; mortar lines, arched doorways |
| **T3** | Ironbound | Iron-reinforced stone, hardwood beams, quality glass | Act II; requires Iron Forge on site | Manor-quality; fortified, imposing, ornate detail |
| **T4** | Firstborn-Infused | Ironbound + Lattice-treated stone, arcane glass | Act II–III; requires Lattice Workbench + Vaelari/Aetherborn worker | Faint iridescent glow at joins; elegant, slightly uncanny |

Players can mix tiers across buildings. Tier Upgrade: existing buildings can be upgraded; costs material difference, takes worker time, preserves function and assigned workers.

## 3.5 Terrain Tools

Shovel Tool in Build Mode provides: **Level Ground** (flattens 4m × 4m area; costs worker-hours), **Raise Foundation** (raised earthwork platform), **Clear Vegetation** (removes trees and brush; trees produce lumber). Terrain modification consumes worker time and, for large-scale leveling, material cost.

## 3.6 Build Mode UI Structure

1. **Structures** — Walls, floors, roofs, doors, windows, stairs, foundations
2. **Buildings** (Blueprints) — Complete functional buildings as single-placement objects
3. **Farm** — Crop plots, irrigation channels, animal pens, barns
4. **Crafting** — Workbenches, forges, alchemy tables, Lattice Workbenches
5. **Utility** — Wells, storage buildings, roads, fences, gates
6. **Furnishings** — Interior decoration, lighting, furniture, trophy displays
7. **Defense** — Walls, palisades, guard towers, reinforced gates (unlocks at Notable Threshold only)

Each category shows currently unlocked options; locked options are visible but not selectable, with unlock requirement shown on hover. The **Defense tab** does not appear in the UI until Notable Threshold is crossed (see Section 10.1). Its appearance is the first explicit signal to the player that the world has noticed.

---

# SECTION 4: PLOT ACQUISITION AND PROGRESSION

## 4.1 Plot Size Tiers

| Tier | Name | Approximate Size | Gold Cost (cumulative) | Faction Standing Gate | Building Capacity |
|---|---|---|---|---|---|
| **1** | Small Holding | ~0.5 acres / 2,000 m² | 15 silver (claim fee) | None | 6 buildings + personal residence |
| **2** | Farmstead | ~2 acres / 8,000 m² | +40 silver | Neutral with any major faction | 18 buildings + residence |
| **3** | Manor Estate | ~6 acres / 24,000 m² | +120 silver | Friendly with any major faction | 40 buildings + residence |
| **4** | Village | ~15 acres / 60,000 m² | +300 silver | Honored with any major faction | 80 buildings + residence |
| **5** | Township | ~40 acres / 160,000 m² | +800 silver | Exalted with any major faction OR combined Honored standing across two | 160 buildings + residence + secondary site unlocked |

**Faction standing gate logic:** Vanguard bureaucratic legitimacy, Hollow Crown land patent, and Verdant Flame community recognition are three paths to the same outcome. Reaver standing does not satisfy this gate directly — but high Reaver standing combined with Neutral Vanguard can be negotiated through a quest chain ("The Irregular Deed") that produces a forged but functional land claim.

## 4.2 Township-Exclusive Features

Township unlocks three exclusive features unavailable at any earlier tier, in addition to maximum building capacity and the secondary site:

**The Merchant Circuit**
Veslan Ohr begins visiting the homestead every 10–14 in-game days. Full specification in Section 4.3 below.

**The Faction Envoy**
One allied faction (player's choice; must be Honored+) semi-permanently stations a representative at the Township. The Envoy provides weekly faction intelligence updates, a standing bonus to interactions with that faction conducted from the homestead, on-site faction supply delivery confirmation, and unique dialogue reflecting their personal reaction to the homestead's development over time.

**Envoy Transition — Full Specification:**
The player can dismiss the current Envoy and invite a different faction's representative. The transition works as follows:

1. The player initiates dismissal through the Homestead Stone management interface. This triggers a single conversation with the current Envoy — they respond based on the faction's standing with the player (formally if relations are good; coldly if the player is pivoting away from their faction).
2. Dismissing the Envoy costs a **small Infamy tick with the departing faction** — equivalent to a minor slight, not a standing-tier loss. The departing faction interprets this as a political signal, not a diplomatic incident. This cost is the same regardless of whether the player is pivoting to another faction or simply removing the Envoy.
3. A **3-day vacancy** follows before a new Envoy can be invited. The homestead operates without Envoy benefits during this window. This is intentional — switching should feel like a real transition, not an instant swap.
4. The player invites the new Envoy through the Homestead Stone, requiring the new faction to be Honored+. The new Envoy arrives within 1 in-game day of the invitation and begins providing their faction's benefits immediately.

**Act III behavior:** In Act III, when faction relationships shift rapidly around the alignment lock (SD_05), the Envoy transition system is likely to be used. The 3-day vacancy window means that a player switching allegiance at the critical moment loses Envoy benefits during the transition. This is correct — it reflects that diplomatic relationships take time to renegotiate. Players who anticipate their Act III alignment and transition the Envoy early avoid this gap.

**Only one Envoy at a time.** This is a hard constraint, not a soft preference.

**The Resonance Spire**
A unique structure available only at Township scale, requiring a Lattice Workbench, Aetherborn or Vaelari Lattice Crafter at Skill 4+, and T4 Firstborn-Infused building materials.

Functional effects:
- All Lattice Workbench output at the homestead gains a 20% quality bonus
- The Spire acts as a weak Lattice node — the Echo (SD_07) can sense it from anywhere in the Vale, providing the player a persistent ambient awareness of homestead status without opening the Ledger
- At high Echo Interface investment, the Echo provides more specific homestead observations when near the Spire
- Visually: the Spire is the most impressive single structure the player can build. It is visible from a significant distance. A Township with a Resonance Spire looks like something.

## 4.3 Veslan Ohr — Full Specification

Veslan Ohr appears four times in this document (Sections 4.2, 9.3, 11.1, 11.3) and is central enough to require a dedicated specification before content work begins.

**Who He Is**
Veslan Ohr is a veteran caravan master, approximately 55, who has been moving goods across the Vale and beyond for thirty years. He survived the Severance not by luck but by competence — he was on the road when it happened, adapted faster than anyone else, and has been running circuits between the Vale's largest economic nodes ever since. He is not charming. He is dry, direct, and observant. He has an opinion about everything and shares it unsolicited. He is one of the few people in the game who treats the player's economic achievements with professional respect rather than political interest.

**Why He Only Visits Township Homesteads**
Veslan runs a route based on supply volume. He has made the calculation that small homesteads don't produce enough concentrated inventory to make the detour worthwhile. A Township-tier homestead producing at volume across multiple output categories crosses his threshold. His arrival is not a reward the game gives — it is a business decision he makes. This framing matters: Veslan should feel like a person who showed up, not a feature that unlocked.

**Stock Categories**
Veslan's inventory on each visit is drawn from five categories, with 2–3 items from each:

1. **Rare Reagents** — Alchemical and Lattice materials unavailable from fixed merchants. Examples: distilled corruption extract (used in advanced Shard Combinations), deep-forest spore clusters (Verdantheart-origin, only accessible post-Severance through his network), pre-Severance mineral compounds from Ironkin stockpiles.

2. **Pre-Severance Equipment** — Recovered gear from distant sites. These are individual authored items, not category loot. Each has a brief provenance note (where he found it, who owned it). Quality is high but not narrative-essential — powerful tools, not story beats.

3. **Faction-Adjacent Goods** — Goods that faction members would ordinarily handle through official channels but which Veslan has acquired through his network: Hollow Crown household items of genuine value, Vanguard surplus equipment, Verdant Flame preserved seed varieties. These are not contraband — they are goods that exist at the edges of faction supply chains.

4. **Regional Specialties** — Goods from parts of the continent the player cannot reach in this game: Highwinter Ironkin metalwork (superior to anything producible in the Vale), Stormwoven Island dried herbs, Crimson Flats mineral goods. Each has a story attached. Veslan will tell it if asked.

5. **Information** — Veslan sells what he knows. Information purchases are offered as dialogue options and cost Crown Marks. Information categories:
   - *Trade Intelligence*: current price movements in markets across the Vale (valuable for timing trade route shipments)
   - *Faction Intelligence*: what he has observed about faction movements (overlaps with, but is distinct from, Envoy intelligence — his is less faction-filtered)
   - *Site Intelligence*: things he has seen near specific locations — ruins, wandering threats, potential secondary site locations. Some of this information exists nowhere else in the game.

**Stock Rotation Logic**
Veslan's stock is **semi-authored, not fully randomized**. Each visit, 60% of his inventory is drawn from a fixed authored pool that rotates on a predetermined schedule (so players who visit every circuit will see different things over time without encountering pure RNG). 40% is procedurally selected from his five categories based on what the player's homestead has been producing — he carries what complements what the player is making, not what they already have in abundance. This makes his visits feel personally relevant without requiring deep player-behavior tracking.

**First Visit Dialogue Direction**
Veslan's opening dialogue on his first visit is not generic merchant patter. He references the settlement by name, names what it's known for (drawn from the player's primary production output), and says something specific about the journey he took to get here. He does not compliment the settlement effusively. He observes it. He might say the road in needs work, or that the placement of the storage warehouse is smart given the prevailing wind, or that he heard about this place from a carter in Grainfell who seemed personally invested in what happened here (a reference to the Mira Aldenmoor thread, if the Thornfield is chosen). The first visit should feel like meeting someone who already knows more about you than you expected.

**Veslan's Return Dialogue**
On subsequent visits, Veslan's dialogue reflects accumulated history with the player and the homestead. At minimum, three scripted return-visit dialogue trees exist: one for a player who has bought information from him before (he mentions something relevant to what they purchased); one for a player who has been building aggressively between visits (he comments on what's changed); and one for a player who has had a raid since his last visit (he noticed the repair work and asks what happened). These are brief — two to four lines each — but they make him feel like a person who pays attention.

## 4.4 Plot Boundary Visualization

The current plot boundary is always visible as a faint luminous marker at ground level when in Build Mode. The next tier boundary shows as a dashed line, allowing the player to plan toward expansion.

## 4.5 Building Capacity

Building capacity is counted by **Building Slots**. Custom-placed structures consume slots based on footprint (approximately 1 slot per 4m × 4m). Blueprint buildings each consume a defined slot count. The system ensures performance management and gives the player meaningful decisions about what to build.

---

# SECTION 5: CLAIMING A HOMESTEAD SITE

## 5.1 The Claim Process

Homestead sites are discovered through exploration. No map marker reveals them. Each site has visible contextual cues (ruins, abandoned structures, Claim Post markers) that signal it is claimable.

To claim a site: find the site and examine the Claim Post → return to Hollowford's Registry Office or any Settlement Broker NPC → pay the initial claim fee (15 silver) and receive the Deed → return to the site and plant the **Homestead Stone**, activating Build Mode.

The Homestead Stone is the management hub for the site. Interacting with it opens the full management interface.

## 5.2 Claiming Conflicts

Two sites have pre-existing claim complications:
- **The Ashford Ridgeline** — Cassian Aelveth's contested claim (full arc in Section 2.2). Player must purchase the claim, resolve the quest chain, or proceed without his signature (Infamy tick with Hollow Crown).
- **The Southwatch Flats Outpost** — technically still Vanguard property. Requires formal decommissioning through Vanguard administrative interaction (Neutral+ standing) or Reaver assistance (produces a less legally clean deed with small future complication risk).

Neither takes more than 15–20 minutes to resolve. Both affect faction relationship in a small, non-trivial way.

## 5.3 Relocation

The player can relocate their homestead to a different site at any point.

**Relocation Process:**
1. Purchase a new site deed (standard claim fee)
2. Plant a temporary Homestead Stone at the new site
3. A 3-day Relocation Window opens: all workers and stored goods transfer automatically; functional buildings marked for Salvage (60% material recovery); custom structures salvage at 50%; Blueprint buildings store as "packed blueprints" re-placeable at 25% material cost
4. After the window closes, the old Homestead Stone is removed

Terrain modifications, pre-existing ruins, and site-specific adjacency bonuses belong to the land and do not transfer.

---

# SECTION 6: BUILDING CATALOG

## 6.1 Residential Buildings

Every worker requires an assigned bed. Housing capacity is the primary limiting factor on population.

| Building | Blueprint Slots | Capacity | Material Tier | Notes |
|---|---|---|---|---|
| **Bedroll Shelter** | 1 | 2 workers | T1 | Minimal. Workers here have slightly lower morale. |
| **Bunkhouse (Small)** | 1 | 4 workers | T1 | Standard early-game housing. |
| **Bunkhouse (Large)** | 2 | 8 workers | T1–T2 | Efficient. Common in mid-game homesteads. |
| **Worker Cottage** | 1 | 2 workers | T2 | Private housing; improves morale and reduces turnover. |
| **Worker Longhouse** | 3 | 12 workers | T2 | Community housing; morale bonus from proximity to others. |
| **Manor House (Player Residence)** | 4 | 0 workers (player only) | T3 | Required for Township tier claim. Fully customizable interior. |
| **Steward's Quarters** | 1 | 1 worker (Steward role) | T2 | Dedicated housing for Steward; activates Steward management bonus. |

**Note on Guard Barracks:** Guard housing is handled by the Guard Barracks building, cataloged in Section 6.5 (Defense Buildings). It is a defense structure that also provides housing — its canonical location in the building catalog is the Defense tab, not Residential.

**Player Residence Note:** The player does not require a bed at their homestead — but sleeping in their own building restores health/mana. The quality of the residence affects ambient worker dialogue. Workers who feel their employer lives alongside them have better morale than workers who feel the employer is absent.

## 6.2 Agricultural Buildings

| Building | Slots | Function | Worker Req. | Notes |
|---|---|---|---|---|
| **Crop Plot (Small)** | 1 | Grows one crop type; 4 plant rows | 1 farmer | Base unit of farm production |
| **Crop Plot (Large)** | 2 | Grows one crop type; 10 plant rows | 2 farmers | More efficient per slot |
| **Orchard Plot** | 2 | Seasonal fruit production | 1 farmer | Slower cycle; higher value output |
| **Herb Garden** | 1 | Grows alchemical/cooking reagents | 1 farmer | Output feeds Alchemy Table |
| **Irrigation Channel** | 0.5 | Connects water source to adjacent farm plots; +20% yield | 0 (passive) | Requires water source nearby |
| **Animal Pen** | 2 | Houses 4 animals of one type | 1 handler | Produces secondary goods (milk, wool, eggs) |
| **Stable** | 2 | Houses 2 horses; player mount storage | 1 stable hand | Horses can be assigned to trade route caravans for modest speed increase |
| **Barn** | 2 | Stores agricultural output; up to 500 units | 0 (passive) | Required at Farmstead+ to prevent spoilage loss |
| **Root Cellar** | 1 | Extends stored food shelf-life by 200%; raid-resistant storage | 0 (passive) | Pairs with Barn; stored goods here cannot be looted during raids |
| **Windmill / Watermill** | 3 | Processes grain into flour | 1 miller | Watermill requires river/stream adjacency; unique to Thornfield and Mistwater sites |

**Crop Types Available:**
- Wheat, rye, root vegetables, legumes — standard yield staples; Tier 1 farming
- Medicinal herbs, Shadowbloom, Thornweed — alchemical inputs; Tier 2 farming
- Verdant Flame-blessed seeds (Honored+ Verdant Flame standing) — standard yield with bonus properties for certain recipes
- Post-corruption varieties — unique seeds found in Verdantheart; high yield, require soil treatment, produce goods unavailable elsewhere

## 6.3 Production and Crafting Buildings

| Building | Slots | Function | Worker Req. | Output Category | Notes |
|---|---|---|---|---|---|
| **Carpenter's Workshop** | 2 | Converts lumber to furniture, building components | 1 carpenter | T2 crafting materials | Required to unlock T2 building pieces |
| **Blacksmith's Forge** | 3 | Smelts metal; produces weapons, armor, tools | 1 blacksmith | Weapons/armor/tools | Ironkin blacksmith increases output quality; also primary source feeding Armory stockpile |
| **Alchemy Table** | 2 | Combines reagents into potions, poisons, salves | 1 alchemist | Consumables | Vaelari alchemist unlocks advanced recipes |
| **Tannery** | 2 | Processes animal hides into leather goods | 1 tanner | Leather goods, armor components | Requires Animal Pen adjacency for bonus |
| **Stonecutting Station** | 2 | Dresses raw stone; unlocks T2 building materials | 1 mason | T2/T3 building materials | Required for Manor Estate tier |
| **Weaving Loom** | 1 | Produces cloth, rope, textile goods | 1 weaver | Cloth goods | Lower value but high-volume trade good |
| **Brewhouse** | 2 | Produces ale, mead, spirits | 1 brewer | Beverages | High-value trade good; worker morale bonus |
| **Preservation Kitchen** | 2 | Processes raw food into smoked, pickled, dried goods | 1 cook | Preserved food | Critical for trade route cargo — preserved food does not spoil |
| **Lattice Workbench** | 3 | Combines standard materials with arcane components; produces T4 building materials and Firstborn-resonant items | 1 Lattice-trained craftsperson | Arcane-enhanced goods | Requires Vaelari or Aetherborn worker with Lattice skill |

## 6.4 Utility Buildings

| Building | Slots | Function | Notes |
|---|---|---|---|
| **Storage Warehouse** | 2 | 1,000 unit general storage | Strongly recommended before Farmstead tier |
| **Well** | 0.5 | Water access; enables irrigation within 20m radius | Multiple wells extend coverage |
| **Trading Post** | 2 | Enables visiting merchants to stop at homestead | Visiting merchants every 5–7 in-game days; Veslan Ohr at Township |
| **Messenger Post** | 1 | Enables remote Ledger management | Homestead management without physical travel |
| **Road (per segment)** | 0.5 | Improves worker efficiency; aesthetic | Well-roaded homesteads look like real settlements |
| **Perimeter Fence (Timber)** | 0.5 per section | Basic boundary marker; minor raid deterrent | Visual impact; minimal defense value |
| **Armory** | 2 | Stores worker equipment; enables equipment policy assignment | Required to implement equipment policy at Village scale; draws from Blacksmith output |

## 6.5 Defense Buildings

Defense buildings are unlocked when the homestead crosses Notable Threshold (Section 10.1). They appear in the Defense tab of the Build Mode UI, which is not present until that threshold is crossed.

| Building | Slots | Defense Value | Notes |
|---|---|---|---|
| **Guard Post** | 1 | Low | 1 guard assigned; reduces raid severity when player is away |
| **Watchtower** | 2 | Low + warning | 1 guard with extended detection; advance warning of all raid types |
| **Palisade Wall** | 1 per section | Medium | Blocks raid unit pathfinding; forces attackers to longer routes |
| **Stone Wall** | 1.5 per section | High | Significantly increases attacker difficulty; T2+ material required |
| **Reinforced Gate** | 2 | High + chokepoint | Single controlled entry point; best force-multiplication structure |
| **Guard Barracks** | 2 | Housing + readiness | Houses 6 guards; guards quartered here gain morale and readiness bonus. Required to efficiently maintain Guard-Equipped status at scale. *This is the canonical catalog location for Guard Barracks. It is a defense structure that also provides housing — it is not listed in the Residential catalog.* |
| **Archer Platform** | 1 | Medium | Positioned atop walls or towers; increases guard effectiveness during absent raids |

**Defense Score** is calculated from the combination of all defense buildings and equipped workers (see Section 10.3 for full calculation).

---

# SECTION 7: FARMING SYSTEM

## 7.1 Farm Cycle Design

Farming operates on **in-game seasonal cycles**. Each cycle represents approximately one in-game season. Crops planted at the start of a cycle are harvestable by cycle end. The player does not manually water or tend crops — the farmer worker handles this. The player's role: plan the layout, plant the initial crop type, assign the worker, and harvest (or set to auto-harvest, the default).

**Four Crop States:** Fallow → Growing (progress bar visible on inspection; no player action needed) → Ready (auto-harvest if set; remains harvestable for 1 additional cycle before spoiling without barn storage) → Depleted (fallow again or rotate to new crop)

## 7.2 Soil Quality

- **Base soil quality** — Site-dependent (Thornfield highest; Southwatch Flats lowest)
- **Composting** (buildable, T1) — Slow improvement to adjacent plot quality over multiple cycles
- **Verdant Flame Soil Treatment** (Friendly+ standing; material cost) — Rapid boost; works even near corruption zones
- **Corruption contamination** — Corruption zone expansion degrades adjacent soil quality, connecting the narrative threat directly to the farming economy

## 7.3 Animal Husbandry

| Animal | Output | Cycle Time | Notes |
|---|---|---|---|
| **Chickens** | Eggs | Short (daily) | Low-value, high-frequency; good for feeding workers |
| **Pigs** | Meat, rendered fat | Medium | Fat is a crafting reagent (alchemy, tanning) |
| **Cows** | Milk, leather (slaughter) | Medium-long | Milk feeds workers or produces cheese (high-value trade good) |
| **Sheep** | Wool, leather (slaughter) | Medium-long | Wool feeds Weaving Loom |
| **Horses** | Draft labor, mount | Passive | Travel speed bonus on homestead roads; assignable to trade route caravans |

Animals require feed (hay from crop plots or purchased). Starved animals produce nothing and eventually die. Maintaining feed supply is the one active management requirement of the farm system.

---

# SECTION 8: STAFFING SYSTEM

## 8.1 Worker Acquisition

1. **Open Hire** — Hollowford Labor Board, settlement job boards, occasional wandering recruits. Generic workers; fill functional roles.
2. **Named Recruit** — Specific named NPCs across the Vale recruitable through dialogue at relationship threshold. Unique skills, dialogue, sometimes side quest hooks.
3. **Faction-Referred Workers** — At Friendly+ standing, factions offer specialized workers: Ironkin blacksmiths (Vanguard network), Vaelari alchemists (Verdant Flame), Reaver-affiliated scavengers. Slightly better base skill than Open Hire.
4. **Refugees** — Drakeling and other refugees at Southwatch camps. Higher availability, lower initial cost, lower starting skill. Treatment has small ripple effects in the refugee camp dynamic.

## 8.2 Worker Roles

| Role | Assigned Building | Production |
|---|---|---|
| **Farmer** | Crop Plots, Herb Garden, Orchard | Agricultural goods |
| **Animal Handler** | Animal Pen, Stable | Animal goods |
| **Carpenter** | Carpenter's Workshop | Processed lumber, furniture, components |
| **Blacksmith** | Blacksmith's Forge | Weapons, armor, tools, metal goods |
| **Alchemist** | Alchemy Table | Potions, salves, reagent compounds |
| **Tanner** | Tannery | Leather goods, armor components |
| **Mason** | Stonecutting Station | Dressed stone, T2/T3 building materials |
| **Weaver** | Weaving Loom | Cloth, rope, textile goods |
| **Brewer** | Brewhouse | Ales, meads, spirits |
| **Cook** | Preservation Kitchen | Preserved foods |
| **Lattice Crafter** | Lattice Workbench | Arcane-enhanced goods |
| **Guard** | Guard Post, Watchtower, Perimeter, Barracks | Defense, raid response |
| **Steward** | Steward's Quarters | Management (see Section 8.4) |
| **Trader** | Trading Post | Merchant relations, sell pricing |

Workers can be re-assigned at any time. Re-assignment is immediate but the worker takes 1 in-game day to reach full productivity in the new role.

## 8.3 Worker Skills and Specialization

**Skill Level 1–5:**
- Skill 1: Basic output; 100% cycle time
- Skill 2: Competent; 85% cycle time
- Skill 3: Skilled; 70% cycle time; quality upgrade chance begins
- Skill 4: Expert; 60% cycle time; quality upgrade chance increased
- Skill 5: Master; 50% cycle time; unique output variants unlocked

Workers gain skill through experience. No player-initiated training mechanic.

**Racial Skill Bonuses:**
- Ironkin in Blacksmith roles: start at Skill 2; gain skill faster; combat effectiveness bonus in defense events
- Vaelari in Alchemist or Lattice Crafter roles: start at Skill 2; unlock unique recipe options
- Aetherborn in Lattice Crafter roles: only workers capable of reaching Skill 5 in that role
- Human workers: no racial specialty; widest role flexibility

## 8.4 The Steward Role

Available at Manor Estate tier or higher. Requirements: worker must have Skill 3+ in any production role; Steward's Quarters must be built; player must have spoken to the worker directly (cannot be assigned remotely).

**Steward Effects:**
- Manages all worker assignments while player is away
- **Auto-resolves routine morale incidents** — supply shortages below buffer threshold, minor worker disputes, ordinary maintenance. Only escalated incidents (Overrun raid aftermath, faction hostility events, named worker departure risk) reach the player
- Provides daily briefing accessible through the Ledger
- Does not replace the player — makes the player more efficient by reserving their attention for what matters

Named Stewards are more capable than generic workers elevated to the role. Cassian Aelveth (Ashford Ridgeline, Resolution B) is the only named Steward with site-specific historical knowledge and Hollow Crown network access.

## 8.5 Worker Needs, Morale, and the Buffer System

**Three worker needs:** Housing (a bed), Food (consumed daily from homestead stores), Wages (paid weekly in Crown Marks).

**Buffer System — Critical Design Principle:**
A large homestead cannot hold the player hostage to daily upkeep while they are deep in an Act II quest chain. Ordinary shortages give the player adequate time to respond.

| Shortage Type | Buffer Duration | During Buffer | After Buffer |
|---|---|---|---|
| **Food shortage** | 7 in-game days | No morale change; Steward notes in Ledger | Morale degrades at Uncomfortable rate |
| **Wage delay** | 5 in-game days | No morale change; workers grumble but stay | Morale degrades; Discontent at 10+ days |
| **Housing deficit** (new worker, no bed) | 3 in-game days | Worker sleeps rough; slight discomfort | Worker leaves if not housed |

**Morale states:**
- **Satisfied** — +10% productivity (good housing, food surplus, paid on time)
- **Content** — Normal productivity
- **Uncomfortable** — -10% productivity (shortage within buffer; minor issues)
- **Discontent** — -25% productivity; turnover risk flagged in Ledger
- **Leaving** — Worker departs within 5 in-game days if not addressed

**Steward auto-resolution scope:** With a Steward in place, routine incidents are resolved automatically. The player is not notified of routine resolutions — only of situations the Steward cannot handle. A player with a competent Steward and adequate stores who returns after a week of main quest work should find their homestead running, not a disaster area.

---

# SECTION 9: ECONOMIC INTEGRATION

## 9.1 Homestead as Production Source

The homestead's primary economic function is as a **Tier 1 and Tier 2 production source** feeding into the broader SD_11 economy. Goods produced at the homestead enter the same economic system as goods sourced elsewhere — sold directly, shipped via trade routes, or consumed internally.

**Practical Example:**
A Thornfield homestead running 3 Crop Plots (Wheat) → 1 Windmill (Grain to Flour) → 1 Preservation Kitchen (Hardtack and Preserved Bread). Hardtack and Preserved Bread are Tier 2 goods: higher sale prices, non-spoiling in trade route cargo, always in demand. Players who process before selling earn substantially more than those who sell raw output.

## 9.2 Trade Route Integration

At Farmstead tier or higher, the player can establish a trade route originating from the homestead using SD_11 Section 4's system. Requires a Trading Post, Barn or Warehouse, and a hired Caravan Master. Fully integrated into the SD_11 route disruption and upgrade system.

## 9.3 Faction Economic Support

Each major faction has a Supply Request list. Delivering regularly earns standing bonuses and unlocks specific benefits. Optional — not a faction alignment gate. Players can supply all four factions simultaneously.

| Faction | Preferred Supply | Standing Reward | Sustained Supply Effect |
|---|---|---|---|
| **The Vanguard** | Weapons, armor, field rations, iron goods | +Fame per delivery; checkpoint friction reduced | Vanguard assigns a patrol to the homestead road (reduces all raid event frequency) |
| **Verdant Flame** | Medicinal herbs, preserved food, alchemical goods | +Fame per delivery; soil treatment available | Verdant Flame scout warns of corruption expansion before it reaches homestead soil |
| **Hollow Crown** | Luxury goods, quality cloth, fine spirits, carved stone | +Fame per delivery; Highlands trade network access | Hollow Crown merchant visits with rare goods (precursor to Veslan Ohr's circuit at Township) |
| **The Reavers** | No formal request — offer goods at fair price preemptively | Informal standing; reduced Reaver raid frequency | Reaver protection agreement available at reduced Favor Marker cost |

Faction supply relationships are severed by Act III alignment lock (SD_05). Economic relationships are not immune to political reality.

## 9.4 Local Economic Footprint

At Village and Township tier, the homestead produces enough volume to affect local prices in adjacent settlements — large grain output depresses Grainfell grain prices; consistent weapon output compresses local weapon prices. Players who diversify production maintain better margins than those who maximize a single output.

## 9.5 Equipment Policy Production Tradeoff

**This section exists because players reading Section 9 while planning production chains need to know about a competing consumption demand they will encounter in Section 10.**

At Village tier, when the defense system activates and the player implements an equipment policy, the Blacksmith's Forge output is split between two uses: **trade goods** (sold externally for income) and **Armory stockpile** (consumed internally to equip workers). This is a genuine tradeoff, not a bug or an oversight. It is the correct design — a self-sustaining defended settlement is more economically resilient than one that exports everything and has no defensive capacity.

**Planning guidance for Village tier production:**
- A single Skill 3 blacksmith produces approximately enough output to maintain the Armory at "Guards only: Guard-Equipped" policy with moderate surplus for trade
- Expanding to "Guards: Guard-Equipped; all workers: Armed" at 20+ workers will consume most of a single Skill 3 blacksmith's output, leaving little for trade
- The break-even point for keeping both the Armory supplied and maintaining a meaningful trade good output requires either a Skill 4–5 blacksmith or two Blacksmith's Forges
- Players who reach Village tier and want both serious defense and meaningful weapons/armor trade should plan for two Forges as their first Village-tier production expansion

**The tradeoff in practice:** A player who redirects all Forge output to internal defense is running a more secure but less profitable homestead. A player who exports all Forge output is running a more profitable but more vulnerable one. This is an intentional design tension that makes the equipment policy decision feel economically real, not just mechanically convenient.

---

# SECTION 10: DEFENSE SYSTEM

## 10.1 Notable Threshold — When the World Starts Watching

The homestead crosses **Notable Threshold** — the point at which factions and organized groups begin treating it as a meaningful target — when all three conditions are simultaneously true:

1. **Village tier plot unlocked** (Plot Tier 4)
2. **At least 3 production buildings operational**
3. **8 or more workers present**

All three must be true. A player who bought the Village plot but hasn't developed it does not trigger defense events. The threshold requires that the homestead look, to an outside observer, like something worth taking.

When Notable Threshold is crossed:
- The Defense tab appears in the Build Mode UI with the notification: *"Your settlement has grown large enough to draw attention. Consider its defense."*
- The homestead enters faction awareness
- Defense events become possible
- The player receives ambient warning signals (a scout observed at the treeline; workers comment on strangers watching the road) before the first real raid

**At Notable Threshold, the player has roughly 3–5 in-game days before the first organized raid event is possible.** This is a grace window during which the warning signs are legible.

**First Raid Design Decision — Tutorial Sequencing:**
The first organized raid event after Notable Threshold is crossed is **always an Organized Bandit Crew of minimum strength, regardless of homestead tier, site location, or faction standing.** This is a hardcoded design rule.

The rationale: a player crossing Notable Threshold for the first time encounters the Defense tab, the equipment policy system, the Defense Score calculation, the five raid type taxonomy, and the stolen vs. destroyed matrix simultaneously. Throwing a Reaver Raid or Corruption Breach at them as their first defense encounter would fail the "complexity comes from options, not learning requirements" principle. The first Organized Bandit Crew teaches the player: raid events exist, Watchtowers provide warning, guards matter, the equipment policy affects outcomes, and the Repelled/Partial Breach/Overrun outcome system is real. After this encounter, all raid types are available per their standard trigger conditions.

## 10.2 Worker Combat and Equipment

Every worker has a hidden **Combat Readiness** value separate from production skill. Guards are the designated combat role with meaningful base Combat Readiness. Other workers are civilians who will defend themselves but are not fighters.

**Worker Equipment Policy**
Set through the Armory building (required at Village tier). The homestead auto-draws from stockpile. This is a strategic decision, not inventory management.

| Equipment Tier | What It Means | Combat Effect |
|---|---|---|
| **Unequipped** | Default civilian | Defends self; takes heavy casualties |
| **Armed** | Basic weapons from Armory stockpile | Fights effectively; reduced casualties |
| **Light Armored** | Weapons + light armor | Fights well; significantly reduced casualties |
| **Guard-Equipped** | Full weapons + medium armor; guard role | Full combat effectiveness; can hold against most attacks without player |

Equipment is consumed from the homestead stockpile. See Section 9.5 for the Blacksmith dual-consumption tradeoff this creates.

**Equipment policy options:**
- All workers: Unequipped (default, no cost)
- Guards only: Guard-Equipped; all others Unequipped
- Guards: Guard-Equipped; production workers: Armed
- All workers: Armed or Light Armored (maximum defense; highest cost)

Players can change policy at any time. The Armory distributes or reclaims equipment over the following in-game day.

**Ironkin workers in combat:** Regardless of production role, Ironkin workers have a racial combat bonus in defense events. Minor bonus, not decisive — but a homestead with several Ironkin workers has meaningfully better passive defense.

## 10.3 Defense Score

When the player is absent during a raid, outcome is determined by **Defense Score vs. Attack Strength**.

| Factor | Defense Contribution |
|---|---|
| Each Guard-Equipped guard | High |
| Each Light Armored worker | Medium |
| Each Armed worker | Low |
| Each Unequipped worker | Negligible |
| Palisade Wall coverage (%) | Medium (scales with perimeter coverage) |
| Stone Wall coverage (%) | High (scales with perimeter coverage) |
| Reinforced Gate | High (single chokepoint multiplier) |
| Watchtower (per tower) | Warning only; no direct Defense Score contribution |
| Archer Platform (per platform) | Medium |
| Elevated site (Ashford Ridgeline only) | Constant bonus |

**Three outcomes:**

| Outcome | Trigger | What It Means |
|---|---|---|
| **Repelled** | Defense Score > Attack Strength | Attackers driven off. Minor worker injuries possible. Small repair costs. Workers who fought gain experience. |
| **Partial Breach** | Defense Score roughly matches Attack Strength | Attackers breached but eventually stopped. Goods stolen from accessible storage. Some building damage. Several workers injured; brief recovery time. |
| **Overrun** | Defense Score significantly < Attack Strength | Defenses failed. Significant goods stolen. Multiple buildings damaged or destroyed. Workers injured or killed. Named workers can be permanently lost. |

Killed workers in an Overrun are permanent losses. The player had advance warning through the Watchtower system and chose not to respond — the consequence is proportionate to the neglect.

## 10.4 Raids With the Player Present

When the player is at the homestead during a raid, it becomes a **real-time combat encounter** in the homestead environment. The player's personal combat capability is the single largest factor in any raid's outcome.

**During a player-present attack:**
- Guards actively engage from assigned posts
- Non-combat workers attempt to reach shelter (barn, residence, root cellar)
- Armed and Light Armored workers form a secondary defensive line
- The player can direct guards with three context-sensitive commands: *Hold Gate*, *Defend Storage*, *Protect Workers*

**Post-combat:** Victory scatters the attacking group (will not return for an extended period, varying by raid type). The player personally fighting for their homestead produces small morale gains in workers who witnessed it.

**Raid as authored environment:** The homestead is a space the player designed. Fights in it should feel different from fights elsewhere — familiar, personal, with stakes attached to specific buildings and specific people.

## 10.5 Raid Types

---

**Opportunistic Bandits** *(all tiers; below Notable Threshold)*
- **Goal:** Steal food and portable goods. Quick raid, grab and go.
- **Attack Strength:** Very Low; 2–4 individuals, no tactical coordination
- **What they take:** Stored food, small portable goods
- **Defeated by:** Basic fencing + 1–2 armed workers; player presence trivially ends it
- **Frequency:** Low baseline; not faction-driven; present at all homestead tiers

---

**Organized Bandit Crew** *(Village tier and above; post-Notable Threshold; first raid is always this type at minimum strength — see Section 10.1)*
- **Goal:** Loot storage and take animals. Planned approach.
- **Attack Strength:** Medium; 8–15 fighters with basic tactical planning; identify weak points in perimeter
- **What they take:** Stored goods, animals, portable equipment
- **Defeated by:** Palisade perimeter + 4+ equipped workers; Watchtower warning gives player time to respond
- **Note:** Some crews are loosely Reaver-affiliated. Negotiating Reaver protection significantly reduces this raid type's frequency.

---

**Reaver Raid** *(Village tier and above; no Reaver protection agreement in place)*
- **Goal:** Tribute extraction — a cut of what the homestead produces, ongoing.
- **Attack Strength:** Medium-High
- **Method:** Professional, organized, deliberate. Will issue a **Demand Notice** (delivered by messenger, appearing as a Ledger notification) before attacking. The Demand Notice is a business communication, not a threat.
- **What they take:** A percentage of stored goods; if seriously resisted, damage buildings as a message
- **Special behavior:** Reavers **do not kill workers** unless workers attack them first. They are running a protection racket, not a war. Killing workers is bad for business.
- **Resolution options:** Fight (possible but escalates — next raid will be stronger); pay tribute (ongoing cost, no violence); establish formal Reaver Protection Agreement (Favor Markers; eliminates this raid type entirely)

---

**Corruption Breach** *(Village tier and above; corruption zone expands to homestead boundary)*
- **Goal:** None — corrupted creatures are not intelligent attackers
- **Attack Strength:** Medium-High; scales with corruption advancement
- **What they do:** Kill animals, destroy growing crops, injure workers, contaminate soil. Do not steal or make demands.
- **Defeated by:** Defense structures contain temporarily; the real solution is addressing the corruption source
- **Special behavior:** If the player has an active Verdant Flame supply relationship (Section 9.3), the Verdant Flame scout warns the player **before** this raid type triggers — detecting corruption expansion in the days before creatures breach the boundary. This is the most concrete payoff for that supply relationship made real.

---

**Faction Hostile Seizure Attempt** *(Village tier and above; player at open hostility with zone's controlling faction)*
- **Goal:** Reclaim or destroy the settlement. This is a military operation, not a raid.
- **Attack Strength:** Very High; organized soldiers or faction enforcers; multiple coordinated squads
- **What they do:** Damage and destroy buildings; expel or kill guards; attempt to remove the Homestead Stone (which would effectively end the player's claim)
- **Defeated by:** Cannot be purely defended. Requires political resolution, player-present combat of sufficient skill, or genuine military investment
- **Preceded by:** Always preceded by multiple warning stages in the faction relationship arc. Should never feel like it came from nowhere.
- **Frequency:** Rare. Requires open hostility, not mild disagreement.

---

## 10.6 What Gets Stolen vs. Destroyed

| Category | Can Be Stolen? | Can Be Destroyed? | Recovery |
|---|---|---|---|
| **Stored goods (accessible storage)** | Yes (Partial Breach or worse) | No | Permanent loss |
| **Stored goods (Root Cellar / locked Armory)** | No | No | Raid-resistant; cannot be looted |
| **Animals** | Yes (Bandits, Reavers) | Yes (Corruption Breach kills them) | Permanent; new animals purchasable |
| **Growing crops** | No | Yes (trampled/burned; Corruption Breach) | Lost cycle; replant next season |
| **Buildings (partial damage)** | No | Yes | Repair cost in materials + worker time; functional during repair |
| **Buildings (destruction)** | No | Yes (Overrun and Seizure Attempt only) | Full rebuild cost; structure lost |
| **Workers (injured)** | No | No | Out of action 2–5 days; recover without player intervention |
| **Workers (killed)** | No | Yes (Overrun and Seizure Attempt only) | Permanent; named workers irreplaceable |
| **Homestead Stone** | No | No (only Seizure Attempt threatens it) | If Seizure succeeds: claim contested (quest to reclaim) |

Outright destruction is the exception. Most raids result in stolen goods and partial building damage — repairable, costly, but not catastrophic. Catastrophic outcomes require genuine neglect at scale. The system punishes inattention proportionately, not randomly.

## 10.7 Faction Awareness Progression

**Stage 1 — Below Notable Threshold:** Private property claim. No faction takes operational interest. Only Opportunistic Bandits.

**Stage 2 — Notable Threshold Crossed:** Homestead appears in faction intelligence. Ambient signals of interest begin. Organized raid types become possible. Defense tab unlocks.

**Stage 3 — First Faction Supply Delivery:** Supplying faction has a positive relationship; they will not raid something they depend on. Sustained supply benefits begin accumulating.

**Stage 4 — Act II Faction Conflict Escalation:** Homestead's faction zone tag actively contested. Factions the player has opposed treat the homestead as a pressure point — cutting supply relationships, escalating Reaver-affiliated raids, issuing formal demands.

**Stage 5 — Township Tier:** Factions treat the homestead as a small political entity. A faction that has been neither supplied nor negotiated with sends a formal messenger with an explicit demand before any escalation to force. This demand is a quest hook requiring a player decision with faction relationship consequences.

---

# SECTION 11: HOMESTEAD PROGRESSION PATH

## 11.1 Recommended Progression Arc

### Phase 1 — The Claim (Act I, Early)
**Player State:** Just claimed the site. 15 silver spent. Small Holding plot.
**First Actions:** Place Homestead Stone; clear and level a small area; build Bunkhouse (Small); build Crop Plot (Small); build Well; hire 2 workers (one farmer, one general).
**State of Homestead:** A rough camp with a working garden and beds. Functional but visually minimal.

**What a 30-minute session looks like:** The player arrives at the site. They enter Build Mode and work out where to put the first bunkhouse — terrain matters here, and they're making actual spatial decisions. They clear some brush. They hire a worker at the Grainfell job board on their way back. They plant the first crop. They leave. There is nothing to manage yet. The session is entirely construction and planning.

---

### Phase 2 — The Working Farm (Act I, Late to Act II, Early)
**Player State:** Farmstead tier. Small income flowing. 3–6 workers.
**Key Additions:** 3–4 Crop Plots; Animal Pen; Carpenter's Workshop (unlocks T2 pieces); upgrade to T2 Dressed Stone; Storage Warehouse; Trading Post; first homestead trade route.
**State of Homestead:** A credible working farm. Multiple buildings, visible field rows, animals. Begins to feel like a place someone lives, not a camp.

**What a 30-minute session looks like:** The player arrives to find the crop ready. They harvest (auto-harvest handles it if set). A worker mentions a merchant passed through and asked about grain prices. They check the Ledger — the trade route had a minor disruption but resolved. They decide whether to upgrade the bunkhouse to stone or save materials for a second crop plot. They spend 15 minutes in Build Mode laying the foundations of the next expansion. They leave having made a real decision and seen the farm running. No incidents required their attention.

---

### Phase 3 — The Manor Estate (Act II)
**Player State:** Full economic engagement. 8–15 workers. Multiple production chains.
**Key Additions:** Blacksmith's Forge; Alchemy Table; hire a Steward (single most important mid-game homestead decision); Player Residence; upgrade primary buildings to T3 Ironbound; begin faction supply deliveries.
**State of Homestead:** A substantial estate. Visitors would recognize it as a prosperous, managed property. The Steward is handling routine incidents without escalation.

**What a 30-minute session looks like:** The player arrives. The Steward gives a brief update — production is running, a minor supply dispute was handled, the trade route returned 18 silver this cycle. The player walks the grounds. A named Vaelari alchemist mentions she has been experimenting with a new reagent combination and shows the player a potion variant the standard recipe doesn't produce — a small discovery that only happens because the player visits. The player decides to expand toward the Blacksmith's Forge footprint they've been planning. They enter Build Mode and place the foundation. Total active decisions: 2. Time spent in the world: meaningful. Nothing felt like maintenance.

---

### Phase 4 — The Village (Act II–III)
**Player State:** Major economic operation. 16–35 workers. Notable Threshold crossed; defense system active.
**Key Additions:** Lattice Workbench; Brewhouse; Watchtower network and first palisade sections; Worker Longhouses for efficiency; equipment policy set; begin T4 Firstborn-Infused building materials; Reaver Demand Notice arrives — requires decision.
**State of Homestead:** A village. People call it by its name. The road in is worn. Travelers stop. The economy is real and visible. So is the risk.

**What a 30-minute session looks like (good session):** The player fast-travels in. There is a Watchtower alert from last night — an Organized Bandit crew was spotted at the eastern treeline but didn't approach (the palisade deterred them). The Steward flagged it. The player notes the eastern wall coverage is incomplete and goes into Build Mode to finish the palisade run — a direct spatial response to a real threat. While building, they see that the Brewhouse output has stacked to 80 units and set a trade route pickup. A worker they've had since Phase 1 has hit Skill 4. They visit him. He's been here longer than anyone else and his dialogue reflects that. The player leaves. The session felt like owning something.

**What a 30-minute session looks like (recovery session — Partial Breach while away):**

The player fast-travels in. Something is visually different before they reach the Homestead Stone — a section of palisade is damaged and there are repair scaffolds that weren't there before. Workers are moving with visible purpose. The Ledger notification from two days ago (which the player hadn't read mid-quest) summarizes: Organized Bandit Crew; Partial Breach outcome; eastern palisade section damaged; Warehouse storage partially looted (specific goods listed); three workers injured, now recovering; the Steward managed the immediate aftermath.

**What the player does first:** They walk to the breach. They can see exactly where the palisade failed — it was the incomplete eastern run they knew about and hadn't finished yet. The breach is not random. It is the consequence of a decision they made, now physically present in the space they built. They talk to the Steward, who gives a composed account: what happened in sequence, which goods were taken, how the guards responded. The Steward is not accusatory. They are practical: the breach is partially repaired; full repair requires 15 stone and 2 worker-days; the looted goods represent 22 silver of loss; the equipment policy held, no workers were killed.

**What the player decides:** They enter Build Mode and complete the eastern palisade. They do it now, not later, because the cost of not doing it is concrete and visible. They check the three injured workers — recovery in progress, no intervention needed. They look at the stolen goods list and decide whether to replenish the stockpile from the next trade route or buy directly from a Hollowford merchant. They consider upgrading the eastern palisade section to Stone Wall. They have a real decision about production planning — the Blacksmith Forge output needs to be split differently now.

**Why this session matters:** The recovery session is the defense system's most important moment. A Partial Breach that feels fair — where the breach happened at a known weak point, the loss is specific and proportionate, the Steward handled what they could, and the player's response is a series of concrete spatial decisions — builds trust. A Partial Breach that feels random, opaque, or excessive destroys it. The session described above should be the design target for what Partial Breach recovery feels like. If a playtest produces a recovery session that doesn't resemble this description, something in the system is wrong.

---

### Phase 5 — The Township (Act III)
**Player State:** Maximum development. 40–80+ workers. Secondary site operational. Resonance Spire under construction or complete.
**Key Additions:** Full stone perimeter wall with towers; Watermill (if water access available); secondary site with up to 8 workers; comprehensive T4 presence; Resonance Spire; Veslan Ohr's circuit begins; Faction Envoy stationed; settlement named — exists on the map as a labeled location.
**State of Homestead:** A small town in a world trying to rebuild. Named workers have been here for the whole game. The player's choices about faction supply have shaped relationships. The Steward has a personality. The place has a history.

**What a 30-minute session looks like:** The player arrives. Veslan Ohr is at the Trading Post — he arrived yesterday. The player browses his stock and finds a pre-Severance piece of equipment they've been looking for. They buy it. The Faction Envoy (Verdant Flame) pulls them aside — there is intelligence about a Corruption expansion event near the eastern border that will be relevant to the main quest within a day or two. This is information the player has because they built what they built. They inspect the Resonance Spire's construction progress. Two more days. They spend 10 minutes in Build Mode placing decorative elements in the Manor courtyard — entirely optional, entirely personal. A visiting NPC from Grainfell mentions having heard of this place. The player is in Act III. The homestead has become context for everything else.

---

## 11.2 Player-Driven Micro-Activities

Between major build sessions and passive production cycles, the homestead offers **optional micro-activities** — player-driven actions that produce something categorically unavailable through passive means. The design test for each activity: *what does doing this yourself give you that the system cannot produce without you?* Activities that only offer a percentage bonus fail this test. All five activities listed here pass it.

| Micro-Activity | What the Player Does | What Only the Player Can Get |
|---|---|---|
| **Forge Work** | The player spends time at the Blacksmith's Forge alongside the assigned blacksmith | The blacksmith teaches the player a recipe variant (unique item variant) at Skill 3+; cannot be crafted through normal production; exists nowhere else in the system |
| **Guard Rounds** | The player walks the perimeter with the guards | Guards share specific observations about patrol activity — locations of observed scouts, timing patterns, an approach route they noticed — that constitutes informal intelligence unavailable in any interface. This information is perishable; it reflects the current situation only. |
| **Evening with Workers** | The player sleeps at the homestead and chooses to eat with workers rather than alone | Workers share gossip, local observations, and personal details that do not appear in any Ledger or briefing. Named workers may share something about themselves that opens or advances a relationship thread. Generic workers occasionally share information that reveals a market condition, local event, or approaching threat. This is an information channel that exists only through physical presence. |
| **Personal Harvest** | The player harvests a crop plot manually rather than using auto-harvest, then takes the raw output to the Preservation Kitchen and processes it personally alongside the cook | The cook, watching the player work, describes a variant preservation technique they learned before the Severance. This unlocks a single unique Preserved Food variant (a named recipe with superior properties) that the automated Preservation Kitchen will never produce. |
| **Soil Work** | The player personally tends the soil on degraded or corruption-affected crop plots — clearing contaminants, turning the earth, applying compost manually | Accelerates soil quality recovery by 50% on affected plots, bypassing the standard cycle-over-cycle improvement rate. Also: the farmer assigned to the plot has a distinct dialogue response the next time the player visits — they noticed what the player did, and they say so. This is a relationship moment that the automated soil treatment system cannot produce. |

None of these are optimized paths. A player who only uses auto-harvest and the Ledger is not missing mechanical value. They are missing the information channels and relationship moments that exist only through presence — and that is the correct tradeoff to offer.

---

## 11.3 Township World-Acknowledgment Events

Five authored events fire when Township tier is reached and sustained for 5 in-game days. These are specific and scripted — not ambient. The player should feel unmistakably that something meaningful has been noticed.

**Event 1 — The Faction Letter**
The player's allied faction leader sends a formal written communication — not a Ledger notification, but a physical letter delivered to the Homestead Stone. The letter acknowledges the settlement by name, notes its economic significance, and offers a named formal title: "Provisioner of the Vale" (Vanguard), "Groundkeeper of the Restoration" (Verdant Flame), "Holder of the Western Trade" (Hollow Crown). The title appears in faction dialogue when the player interacts with faction-specific NPCs.

**Event 2 — The Hollowford Mention**
During an unrelated conversation with a named NPC in Hollowford (a civilian the player has spoken to before — the Broken Chalice proprietor, the market square vendor), the NPC mentions having heard of the player's settlement by name. They ask about it. This NPC has nothing to do with the homestead system. Their knowledge of it is purely social — the way news travels in a small region.

**Event 3 — Veslan Ohr's First Visit**
Veslan arrives for the first time. His opening dialogue is not generic merchant patter — he references the settlement by name, names what it's known for (drawn from the player's primary production output), and says something specific about the journey to get here. He has an opinion about the place. This event introduces the Merchant Circuit and is a concrete reward that feels like the world responding rather than a system activating. Full dialogue direction in Section 4.3.

**Event 4 — The Returning Worker**
The player's earliest generic worker — the first one hired, if still employed — has new dialogue at Township tier. They stand in the settlement and comment on what it has become since they arrived. They use the homestead's name. They speak in past and present tense. The contrast between then and now is the entire point.

**Event 5 — The Hostile Notice**
If the player has any faction at hostile standing, that faction's representative sends a message acknowledging the settlement's scale. The tone is a warning. They are not afraid of it — but they are no longer ignoring it. This is a pressure event, not a reward. Things built at scale become politically real.

---

# SECTION 12: MANAGEMENT INTERFACE

## 12.1 The Homestead Ledger Entry

Displayed at the top of the SD_11 Ledger screen. Shows: current plot tier and worker count/capacity; last cycle production summary; stored goods totals by category; active workers with current role and morale state; pending incidents (yellow/red flagging); projected trade route income; defense status summary (equipment policy, guard count, last raid outcome if applicable).

Accessible anywhere without physically visiting the homestead.

## 12.2 The Physical Management Hub

The Homestead Stone opens the full management screen, adding: Build Mode entry; plot expansion purchase; worker assignment interface (drag/drop); stockpile management (sell thresholds, reserve amounts, faction supply quotas); equipment policy assignment (requires Armory); deed and ownership information.

Worker assignment is better done physically — visiting workers directly unlocks morale dialogue and relationship events. Players who visit regularly have a genuine information advantage the Ledger cannot replicate.

## 12.3 Homestead Notifications

Notifications appear in the same system as SD_11 trade route disruption events:
- Raid event initiated (advance warning if Watchtower present)
- Raid event resolved while away (outcome summary)
- Escalated worker morale incident (Steward cannot resolve)
- Production cycle complete (optional; can be disabled)
- Faction supply threshold reached
- Named worker skill level up
- Food or wage shortage warning (appears at start of buffer window, not at morale impact)
- Notable Threshold crossed (first occurrence only)
- Township world-acknowledgment events (five specific authored events, Section 11.3)

Notifications are informational. The player addresses them at their next convenience.

---

# SECTION 13: SD_11 CROSS-REFERENCE AND RECONCILIATION

## 13.1 SD_11 Section 6 Status

SD_11 Section 6 commercial property types (Storefront, Warehouse, Farm Plot, Workshop, Information Broker Office, Tavern/Inn) remain fully valid. Homestead acquisition is governed by SD_12 Section 5. Property incident events apply to commercial properties; homestead incidents are governed by SD_12 Sections 8.5 and 10.

**The Broken Mill adjacency note:** The Broken Mill in Grainfell (SD_11 named property) belongs to a family connected to the Aldenmoor family of the Thornfield homestead site. These two NPC threads exist in the same neighborhood and are worth developing as a Grainfell character cluster.

## 13.2 Farm Plot Distinction

SD_11's Farm Plot is an investment asset at an existing settlement, managed abstractly. SD_12's homestead farm is a hands-on, player-built, directly managed agricultural operation. They are different experiences. SD_11 Farm Plot should be updated to clarify this distinction.

## 13.3 Terminology Alignment

Consistent with SD_01 canonical terminology:
- Arcane crafting components: **Relic Shards** and **Shard Combinations** (canonical terminology per SD_06/SD_07, resolved 2026-03-20)
- Playable races: **Human, Vaelari, Aetherborn**
- Ironkin appear as NPC workers; not playable per SD_02; confirmed Vale presence

---

# SECTION 14: IMPLEMENTATION CHECKLIST

**Core Building System:**
- [ ] Build Mode camera implemented (overhead + ground-level)
- [ ] Snap-point grid system implemented (2m base unit)
- [ ] Color feedback system implemented (green/blue/yellow/orange/red)
- [ ] Material tier system implemented (T1–T4) with visual differentiation
- [ ] Blueprint placement mode implemented
- [ ] Custom placement mode implemented
- [ ] Terrain tools implemented (Level Ground, Raise Foundation, Clear Vegetation)
- [ ] Build Mode UI implemented with 7 category tabs
- [ ] Defense tab locked until Notable Threshold; unlock notification implemented
- [ ] Guard Barracks confirmed in Defense tab only (not Residential tab)

**Homestead Sites:**
- [ ] All 5 sites physically present at correct map locations
- [ ] Claim Post markers placed at each site
- [ ] Site-specific starting conditions implemented
- [ ] Site adjacency bonuses implemented (including Ashford Ridgeline doubled Watchtower range)
- [ ] Prior history NPC interactions implemented (Mira Aldenmoor, Harrek Dunweld, Lena Croft, Deven)
- [ ] Cassian Aelveth three-resolution arc implemented with Act II deadline and Act III freeze
- [ ] Claiming conflict interactions implemented (Ashford Ridgeline, Southwatch Outpost)

**Plot Progression:**
- [ ] All 5 plot tiers implemented with correct size, cost, and faction gate
- [ ] Township-exclusive features implemented:
  - [ ] Merchant Circuit: Veslan Ohr with full specification per Section 4.3
  - [ ] Faction Envoy: transition mechanic fully implemented (conversation, Infamy tick, 3-day vacancy, Act III behavior)
  - [ ] Resonance Spire: Skill 4+ Lattice Crafter gate, T4 material requirement, Echo integration
- [ ] Plot boundary visualization implemented
- [ ] Building Slot cap enforced per tier
- [ ] Secondary site unlock at Township (8 worker cap, full production buildings)

**Veslan Ohr (per Section 4.3 specification):**
- [ ] 5 stock categories implemented (Rare Reagents, Pre-Severance Equipment, Faction-Adjacent Goods, Regional Specialties, Information)
- [ ] Semi-authored rotation logic implemented (60% authored pool rotating on schedule; 40% complement-based procedural)
- [ ] Information purchase dialogue options implemented (3 categories: Trade, Faction, Site)
- [ ] First visit dialogue implemented with production-output-aware specifics
- [ ] Three return-visit dialogue trees implemented (prior information purchase; post-construction; post-raid)
- [ ] Visits conditioned on Township tier; does not appear at smaller homesteads

**Staffing System:**
- [ ] Worker acquisition via all four channels implemented
- [ ] All 14 worker roles implemented
- [ ] Skill Level 1–5 with productivity scaling implemented
- [ ] Racial skill and combat bonuses implemented (including Ironkin combat bonus)
- [ ] Steward role with auto-resolution AI implemented
- [ ] Buffer system implemented (food 7-day, wage 5-day, housing 3-day)
- [ ] Extended departure window implemented (5 days)
- [ ] Morale state system (5 states) with Steward auto-resolution for routine incidents

**Farming:**
- [ ] Seasonal cycle system (4 crop states) implemented
- [ ] All crop type varieties implemented
- [ ] Soil quality system with improvement methods implemented
- [ ] Corruption contamination of soil implemented
- [ ] Animal husbandry implemented (5 types, feed requirement)

**Defense System:**
- [ ] Notable Threshold trigger implemented (Village tier + 3 production buildings + 8 workers)
- [ ] Defense tab UI unlock on Notable Threshold crossing
- [ ] **First raid hardcoded as minimum-strength Organized Bandit Crew (tutorial sequencing rule)**
- [ ] Worker equipment policy system implemented (4 tiers, Armory-gated)
- [ ] Equipment auto-draw from Armory stockpile implemented
- [ ] Ironkin combat bonus in defense events implemented
- [ ] Defense Score calculation implemented
- [ ] Absent raid resolution system implemented (3 outcomes: Repelled, Partial Breach, Overrun)
- [ ] All 5 raid types implemented with correct triggers and behaviors:
  - [ ] Opportunistic Bandits (all tiers)
  - [ ] Organized Bandit Crew (Notable Threshold+; first raid always this type at minimum strength)
  - [ ] Reaver Raid with Demand Notice system (Notable Threshold+)
  - [ ] Corruption Breach (Notable Threshold+, corruption-zone-adjacent sites)
  - [ ] Faction Hostile Seizure Attempt (hostile faction standing)
- [ ] Reaver "no worker kills" behavior implemented
- [ ] Raid-resistant storage (Root Cellar, locked Armory) implemented
- [ ] What gets stolen vs. destroyed matrix implemented correctly
- [ ] Player-present raid as real-time combat encounter implemented
- [ ] Three tactical commands implemented (Hold Gate, Defend Storage, Protect Workers)
- [ ] Workers seeking shelter behavior during player-present raids implemented
- [ ] Post-raid scatter timer implemented
- [ ] Player-present fight morale bonus for workers implemented
- [ ] 3–5 day grace window before first organized raid post-Notable Threshold
- [ ] Watchtower advance warning notification system implemented
- [ ] Faction awareness progression (5 stages) implemented
- [ ] Township faction formal demand system (Stage 5) implemented
- [ ] Partial Breach visual state implemented (visible damage, scaffolding, worker activity) to match recovery session design intent

**Economic Integration:**
- [ ] Homestead goods enter SD_11 price index
- [ ] Trade route from homestead origin implemented
- [ ] Faction supply request system implemented (4 factions)
- [ ] Faction supply sustained-relationship effects implemented
- [ ] Local price impact from high-volume production implemented
- [ ] Blacksmith Forge → Armory internal equipment supply chain implemented
- [ ] **Equipment policy production tradeoff balanced against Forge output rates per Section 9.5 guidance**
- [ ] Two-Forge configuration confirmed viable for Village+ players wanting both defense and trade

**Progression and World Acknowledgment:**
- [ ] Phase 1–5 progression arc supported by all systems
- [ ] All five micro-activities implemented with categorically unique rewards:
  - [ ] Forge Work: unique recipe variant unlock (not available through automated production)
  - [ ] Guard Rounds: perishable intelligence not available in any interface
  - [ ] Evening with Workers: named-worker relationship thread advancement; generic worker information channel
  - [ ] Personal Harvest: unique Preserved Food variant recipe unlock (cook dialogue trigger)
  - [ ] Soil Work: accelerated soil recovery (50% faster); distinct farmer dialogue on next visit
- [ ] Five Township world-acknowledgment events authored and implemented (Section 11.3)
- [ ] Partial Breach recovery experience designed to match Phase 4 recovery session description (Section 11.1)

**Management Interface:**
- [ ] Homestead Ledger entry with defense status summary implemented
- [ ] Homestead Stone management hub implemented
- [ ] Worker assignment interface implemented
- [ ] Stockpile management implemented
- [ ] Equipment policy assignment interface implemented (requires Armory)
- [ ] Notification system implemented (buffer-window shortage warning; all events listed in Section 12.3)
- [ ] Homestead naming implemented (map label, ambient dialogue)

**Relocation:**
- [ ] Relocation system implemented (3-day window, 60% salvage, Blueprint packing at 25% re-placement)

**SD_11 Reconciliation:**
- [ ] SD_11 Section 6 updated with reference to SD_12
- [ ] SD_11 Farm Plot clarified as commercial investment only
- [ ] SD_11 Broken Mill NPC adjacency with Thornfield documented for Grainfell character cluster development

---

*End of Document 12: Settlement & Homestead System (v3.0)*
*v3.0 supersedes v2.0 entirely. v2.0 supersedes v1.0 entirely.*
*Reviewer assessment: document is ready to guide system development. Content development on Veslan Ohr, Envoy transitions, and Cassian quest chain detail can now proceed against this specification.*
*Known cross-references requiring attention: SD_11 Section 6 update (Farm Plot vs. homestead farm distinction). Terminology and Act IV corrections completed 2026-03-20 — no further action needed.*
