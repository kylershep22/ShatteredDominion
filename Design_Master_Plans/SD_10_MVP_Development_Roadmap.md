# THE SHATTERED DOMINION — MVP DEVELOPMENT ROADMAP
## Document 10 of 10 | Version 1.0 | Depends on: All preceding documents

**Purpose:** This document translates the full design vision of The Shattered Dominion into a structured development plan. It covers the complete scope of the designed game, a realistic phased development approach, a minimum viable core for resource-constrained scenarios, technical risk identification and mitigation, and a post-launch expansion roadmap.

**Framing:** This roadmap is a design bible document — aspirational, comprehensive, and explicitly dependent on appropriate funding and team size to execute as written. The full scope described across Documents 1–9 represents a AAA-adjacent production requiring a well-resourced team and timeline. Two versions of the plan are presented: the **Full Vision** (what the game should be with appropriate resources) and the **Constrained Core** (what the game must be to deliver its identity even with limited resources). Every production decision should be made with clarity about which version is being pursued.

**Scope note:** The design documents collectively describe a game of significant ambition — comparable in content scope to The Witcher 3: Wild Hunt or Dragon Age: Origins. Productions of that scale required 200–240 person teams over 3.5–4 years. A 10–25 person team cannot execute the full scope in any timeline without cuts. A 50–80 person team with 4–5 years can execute it with discipline. This document presents the full vision; the Constrained Core section identifies what a smaller team must protect.

---

# SECTION 1: SCOPE AUDIT — WHAT HAS BEEN DESIGNED

## 1.1 Complete Content Inventory

Before planning production, the full scope must be understood explicitly. This audit pulls directly from Documents 1–9.

### Narrative Content
| Category | Quantity |
|---|---|
| Main story acts | 4 (Acts I–IV) |
| Companion characters (full arcs) | 4 (Kael, Aelira, Maren, Seraphine) |
| Companion personal quests | 12 (3 per companion) |
| Faction quest lines | 4 complete lines (Act I + Act II per faction = 24 quests) |
| Vale side quests (formal) | ~33 |
| Origin-exclusive side quests | 12 (1–2 per origin × 6 origins) |
| Total formal quests at launch | ~81 |
| Authored micro-discoveries | 60–80 |
| Total voiced dialogue lines (estimate) | 35,000–50,000 |
| Companion voiced lines alone | 8,000–16,000 |
| Act III alignment world states | 4 × all Vale locations |
| Game endings | 3–4 (base + optional Integration ending) |
| Companion ending epilogues | 36 minimum |

### World Content
| Category | Quantity |
|---|---|
| Primary playable region | Severant Vale (40–45 km²) |
| Secondary playable region | Verdantheart Wilds (referenced in story) |
| Hollowford districts | 5 + Undercity (3 layers) |
| Frontier settlements (full) | 4 |
| Named dungeons | 4 (The Sepulcher, Verdant Temple, Sunken Hollow Vault, Ashenveil Archive) |
| Corruption zones | 5 (Vale) |
| Named wilderness landmarks | 6+ |
| Fast travel hub nodes | 12–13 |

### Systems Content
| Category | Quantity |
|---|---|
| Playable races | 3 (Human, Vaelari, Aetherborn) |
| Origins | 6 (2 per race) |
| Attributes | 6 (with 8 thresholds each = 48 total threshold unlocks) |
| Weapon types | 15 base categories, ~45 subtypes |
| Skill trees | 20+ (weapon, defense, magic, relic, utility) |
| Convergence Abilities | 6 |
| Crafting disciplines | 6 (10 tiers each) |
| Item quality tiers | 5 |
| Relic Shard types | 9 |
| Shard Combinations | 20+ at launch |
| Faction sets | 4 (5 pieces each = 20 pieces) |
| Firstborn sets | 3 (16 pieces total) |
| Remnant items (named) | 40+ |
| Crafting material tiers | 4 (Common through Legendary) |
| Armor weight classes | 3 + Unarmored |
| Enemy categories | 6 |
| Named enemy types | 45+ across all categories |
| Economic system (trade routes, property, production chains) | Full system |
| Faction reputation system (Fame/Infamy per faction) | 4 factions × 2 tracks |

### Art and Technical Content
| Category | Estimate |
|---|---|
| Character models (playable) | 3 races × customization variants |
| Character models (major NPCs) | 25–30 named characters |
| Enemy models | 45+ types with variant states |
| Environment biomes | 5 (farmland, forest, rocky hills, corruption, Firstborn) |
| Dungeon tile sets | 3 (human/medieval, Firstborn, corrupted hybrid) |
| Firstborn stone material | Custom engineered material |
| Voiced NPC characters | 35+ with unique voice performances |
| Music tracks | Full dynamic score |

## 1.2 Honest Scope Assessment

This game, as fully designed, is a **4–5 year, 60–80 person production** at minimum. It is not a solo or micro-team project. It is not a 2–3 year project at any team size. The content volume (35,000–50,000 voiced lines alone represents 18–24 months of voice production pipeline work at a typical pace), the systems complexity (the economic system, dynamic world states, and crafting disciplines each represent significant engineering work), and the art requirements (custom Firstborn materials, 45+ enemy types, 40–45 km² of authored environment) combine to create a production scope that demands appropriate resourcing.

This is stated plainly, not as a discouragement, but because the most common cause of ambitious game projects failing is underestimating scope at the outset and making irrevocable decisions based on that underestimate.

---

# SECTION 2: FULL VISION DEVELOPMENT PLAN

## 2.1 Team Structure Assumption (Full Vision)

**Recommended team size:** 55–75 people across all disciplines
**Recommended timeline:** 4.5–5 years from pre-production start to gold master

### Department Breakdown (approximate)

| Department | Headcount | Primary Responsibility |
|---|---|---|
| Design | 8–10 | Systems, quest, level, and combat design |
| Engineering | 12–15 | Core systems, tools, AI, UI, engine |
| Art — Environment | 10–12 | World building, biomes, dungeons, lighting |
| Art — Characters | 6–8 | Character models, animation, VFX |
| Art — UI/UX | 2–3 | HUD, menus, map, inventory |
| Narrative | 4–5 | Writing, dialogue, quest scripting |
| Audio | 3–4 | Music, SFX, voice direction |
| QA | 6–8 | Testing, bug tracking, balance |
| Production | 3–4 | Project management, milestones, external coordination |

---

## 2.2 Phase 1 — Pre-Production (Months 1–8)

**Objective:** Prove the game works before committing full team resources. Exit criteria: a playable vertical slice demonstrating core combat, one dungeon, one companion, one faction arc starter, and the world's visual identity.

### Core Deliverables

**Technical foundation:**
- [ ] UE5 project structure established, source control configured
- [ ] Core movement system (walk, run, sprint, dodge, climb) — weighted action RPG feel validated
- [ ] Basic combat loop (attack, block, parry, dodge, stamina system) — 3-attack combo, recovery frames
- [ ] One weapon type fully implemented (Broadsword — the design benchmark)
- [ ] Enemy AI prototype (one standard, one elite enemy type) — telegraph system validated
- [ ] Basic inventory and equipment system

**Milestone-gated technical prototypes (must pass before Phase 2):**
- [ ] **Proto-1: Combat feel validation** — Broadsword combat against one enemy type. Does it feel weighted and deliberate? Does the recovery frame system create the intended read-and-react loop? Go/No-Go gate.
- [ ] **Proto-2: World state system** — Two locations with three Act state variants each. Does the flag system correctly trigger visual and NPC behavioral changes? Performance acceptable? Go/No-Go gate.
- [ ] **Proto-3: Faction reputation integration** — Fame/Infamy dual track affecting NPC behavior in real time. Does the system feel invisible to players while working correctly? Go/No-Go gate.
- [ ] **Proto-4: Dynamic economy prototype** — One trade route, one property, one production chain. Does the system produce readable economic outcomes? Is it fun to engage with at this minimal scale? Go/No-Go gate.

**Design:**
- [ ] All 9 completed documents reviewed for internal consistency — flag any contradictions
- [ ] Level design blockout for Act I — Hollowford, Frontier Settler origin sequence, The Sepulcher
- [ ] Combat skill tree structure finalized (all trees listed, nodes defined — not implemented)
- [ ] Quest dependency graph for all 81+ quests mapped (what requires what, in what order)

**Art:**
- [ ] Art direction document approved by all department leads
- [ ] Vale environment visual test (one 500m² section of farmland, one corruption zone edge)
- [ ] Firstborn stone material created and approved — this is a pre-production critical path item
- [ ] Human character base model created (male/female variants, relic mark implementation)

**Audio:**
- [ ] Musical identity established — 3 theme sketches for approval (main theme, combat theme, corruption zone ambient)
- [ ] Voice direction brief written

**Vertical Slice target (end of Phase 1):**
- Human Frontier Settler origin tutorial sequence (fully playable, 15–20 minutes)
- The Sepulcher dungeon first level (fully playable, combat validated, visual identity established)
- Kael Thornwright first meeting and one dialogue scene (character feel validated)
- Vanguard faction first quest (systems integration tested end-to-end)

---

## 2.3 Phase 2 — Alpha (Months 9–30)

**Objective:** Build the complete game in greybox/first-pass state. Everything exists and works; nothing is final. Exit criteria: the full game is playable from start to finish, all systems functional, all content present in some form.

**Duration note:** This is the longest phase and the one most commonly underestimated. 22 months is not excessive — it reflects the content volume honestly.

### Engineering Milestones

**Months 9–15 (Core Systems):**
- [ ] Full attribute system (6 attributes, 48 thresholds, partial bonus below threshold)
- [ ] Full skill tree system (all 20+ trees, Proficiency Bonus system, use-rank growth)
- [ ] Full combat system (all 15 weapon categories, all skill interactions, all race systems)
- [ ] Convergence Abilities system (dual-threshold detection, 6 launch abilities)
- [ ] Full loot system (5 quality tiers, Shard system, socket mechanic, item identification)
- [ ] Full crafting system (6 disciplines, all stations, refinement system, material tiers)
- [ ] Faction reputation system (Fame/Infamy, 6 standing states, ideology sub-scores)
- [ ] Economic system (trade routes, property, production chains, faction economic warfare)
- [ ] NPC schedule system (cross-district movement, daily routines)

**Months 16–24 (World and Content Systems):**
- [ ] Full hub-and-spoke fast travel (12 nodes, faction travel layer — all three systems)
- [ ] Zone-locked enemy scaling (level ranges per zone implemented)
- [ ] Dynamic world state system (Act I/II/III transitions, player-deviation flags)
- [ ] All 6 enemy categories implemented (AI behaviors per category, scaling variants)
- [ ] Undercity progression system (3-layer unlock logic)
- [ ] Corruption zone expansion/contraction system
- [ ] Respec system (Voss NPC, skill reset, material cost scaling)
- [ ] Economic investment visual change system (property appearance updates)

**Months 25–30 (Integration and Stability):**
- [ ] All systems integrated and communicating correctly
- [ ] Save/load system (multiple save slots, autosave at key points)
- [ ] Performance baseline established (target platform minimum specs met in all areas)
- [ ] Memory management validated (no leaks in any 4-hour play session)

### Content Milestones

**Act I complete (greybox) — Month 18 target:**
- [ ] All 6 origin tutorial sequences playable
- [ ] Hollowford fully blockout (all districts, all NPCs in place, all Act I quests triggerable)
- [ ] All 4 frontier settlements blockout
- [ ] The Sepulcher dungeon complete (all 3 levels, boss, narrative payoff)
- [ ] Verdant Temple first pass
- [ ] All Act I faction quests scripted and triggerable
- [ ] Act I → Act II transition functional

**Act II complete (greybox) — Month 24 target:**
- [ ] Ashenveil Archive dungeon complete (all 7 levels — largest single content item in the game)
- [ ] Sunken Hollow Vault complete
- [ ] All Act II faction quests scripted
- [ ] Ashenveil revelation trigger and world state change functional
- [ ] All companion personal quests Act II content complete
- [ ] Act II → Act III transition functional

**Act III/IV complete (greybox) — Month 30 target:**
- [ ] All 4 Act III alignment world states implemented
- [ ] All faction Act III quest lines complete
- [ ] Heart of the Lattice final sequence complete
- [ ] All 3–4 endings functional
- [ ] All companion endings and epilogues implemented

---

## 2.4 Phase 3 — Beta (Months 31–44)

**Objective:** Polish, balance, and complete all content to ship quality. Exit criteria: game passes first-party certification, all major bugs resolved, performance targets met on all platforms, player testing validates the experience.

### Content Completion

**Months 31–36 (Content Polish — First Pass):**
- [ ] All 35,000–50,000 dialogue lines recorded, implemented, and tested
- [ ] All 40+ Remnant items named, written (lore entries), and implemented
- [ ] All 60–80 micro-discoveries authored, placed, and tested
- [ ] All companion voiced ambient dialogue (300–500 lines per companion) recorded and implemented
- [ ] All NPC schedule routines validated (cross-district movement working correctly)
- [ ] All 3 texture characters (The Singer, The Waiting Man, The Patrol) fully implemented with Act-reactive states
- [ ] All first-impression beats scripted and positioned at correct entry points per location
- [ ] Economic investment visual changes implemented for all investment types

**Months 37–42 (Systems Balance and Tuning):**
- [ ] Combat balance pass — all 20+ skill trees, all weapon types, all enemy types
- [ ] Convergence Abilities balance — specialist vs. spread player power parity validated
- [ ] Economic system balance — trade route profitability, property ROI, faction economic warfare impact
- [ ] Crafting discipline balance — Blacksmithing Tier 10 output vs. found Remnant equivalence tested
- [ ] Corruption Herald self-damage loop validated (aggressive play funds the self-damage net-neutral target)
- [ ] Zone-locked enemy scaling validated across all zones (no level band exploits, no difficulty cliffs)
- [ ] Act III alignment world state consequences balanced (no alignment feels like a bad ending)

**Months 43–44 (Polish and Performance):**
- [ ] Visual polish pass — all biomes, all dungeons, all lighting states
- [ ] Audio mix complete — all music layers, all ambient sound, all voice levels balanced
- [ ] Performance optimization — target 60fps on minimum spec hardware in all areas including Ashenveil Archive
- [ ] Accessibility options implemented (subtitle sizing, UI scaling, colorblind modes, difficulty settings)
- [ ] First-party certification requirements met

### QA Milestones

**Month 31:** Full game playable for QA — dedicated testing begins
**Month 35:** Critical bug backlog cleared (no Severity 1 issues)
**Month 40:** Major bug backlog cleared (no Severity 2 issues above threshold)
**Month 43:** Gold candidate build submitted
**Month 44:** Gold master — ship

---

## 2.5 Phase 4 — Post-Launch Support (Months 45–52)

**Objective:** Address launch issues, complete anything that shipped incomplete, and deliver the first content update.

**Months 45–47 (Launch Support):**
- [ ] Day-one patch addressing any critical issues discovered post-certification
- [ ] Performance patches for edge cases not caught in testing
- [ ] Balance patches from player feedback (first 30 days of live data)
- [ ] Any quest scripting issues that shipped

**Months 48–52 (Content Completion Update):**
Content identified during Beta as stretch goals that didn't reach ship quality:
- [ ] Additional Shard Combinations (bring total from 20 to 30+)
- [ ] Additional Remnant items (bring total from 40 to 55+)
- [ ] Echo Interface Full Resonance dialogue expansion (Voice of the Architect contextual lines — flagged as expensive in Doc 7)
- [ ] Additional origin-specific dialogue distribution across the game
- [ ] Additional micro-discoveries in areas that tested below density targets

---

# SECTION 3: THE CONSTRAINED CORE

## 3.1 What Must Ship for This Game to Exist

If resources are constrained — smaller team, shorter timeline, reduced budget — some things can be cut, deferred, or reduced without destroying the game's identity. Others cannot. This section identifies the non-negotiable core.

**The game's identity rests on four pillars:**
1. A morally complex world with no obvious good guys and a central mystery worth solving
2. A combat system where build commitment feels meaningful and spread feels like a choice with trade-offs
3. A world that visibly changes based on what the player does
4. Companions who feel like people, not quest dispensers

Everything in the Constrained Core must serve at least one of these four pillars. Everything outside it can be examined for deferral.

## 3.2 Non-Negotiable — Must Ship

**Narrative:**
- Main story Acts I–IV — start to finish, fully voiced. The narrative is the product. A version of this game without a complete story is not this game.
- All 4 companions with full arcs, personal quests, and ending epilogues. The companion system is the emotional heart. Reducing to 2 companions would halve the relationship system's richness beyond recovery.
- All 4 faction quest lines — Act I content minimum, Act II content strongly preferred. The faction system without all four factions is not the faction system.

**World:**
- Hollowford — all 5 districts, the Undercity (at least Layers 1 and 2 at launch). This is where most of the game is experienced.
- All 4 frontier settlements — at minimum the "outpost with purpose" version (defined mechanical role, 3–5 key NPCs, 1–2 quest hooks). Full version strongly preferred.
- The Sepulcher and Ashenveil Archive — these are the Act I and Act II narrative dungeons. They cannot be cut.
- Act III alignment world state changes — all 4 alignments must produce visible, felt consequences. This is the payoff for everything the player did. Cutting any alignment breaks the faction system's promise.

**Systems:**
- Combat system — all 6 attributes, skill trees, the weighted action RPG feel, Proficiency Bonus system. This is the primary play loop.
- Convergence Abilities — 6 at launch. These are what give the spread build a reason to exist. Cutting them makes the spread player a failed specialist.
- Loot system — all 5 quality tiers, Relic Shard system with Shard Combinations (minimum 12 at launch), color coding. The loot system and the combat system are the game loop.
- Faction reputation system — Fame/Infamy dual track. This is what makes the faction system feel alive.
- Dynamic world state — Act I/II/III transitions. The world must change. A static world cannot deliver the game's promise.

## 3.3 Deferrable — Can Ship in Version 1.1 or Expansion

**Content that can be deferred without breaking the core experience:**

*Quests:* The 33 Vale side quests can be reduced to ~20 at launch (the most narratively significant per location) with the remainder shipping in a free content update. The game is completable and rich at 20 side quests. At 33, it is denser. Neither version is broken.

*Micro-discoveries:* Launch with 30–40. Reach 60–80 in the first content update. Players who explore thoroughly at launch will find discovery density somewhat lower than designed; this is acceptable as long as the authored ones present are high quality.

*Crafting disciplines:* Blacksmithing, Alchemy, and Tailoring ship at launch (covering the most common player needs). Woodworking, Jewelcrafting, and Runecarving ship in Version 1.1. Runecarving in particular is identified as high complexity and Hollow Crown-dependent — it is the most deferrable of the six.

*Economic system depth:* Trade routes and property ownership ship at launch. Production chains and faction economic warfare ship in Version 1.1. The economic system is meaningful at the shallow layer; the depth is an enrichment, not a foundation.

*Verdant Temple:* The alternate resolution path (purification instead of combat) can be deferred to Version 1.1 if the full dungeon content without it ships complete. The dungeon must ship; the alternate path is a significant enrichment, not a critical path.

*Additional Convergence Abilities:* 6 ship at launch. 4–6 more ship in Version 1.1. The system's concept is proven at 6.

## 3.4 Reducible — Ship a Simpler Version

**Systems that can ship at reduced scope without identity damage:**

*Shard Combinations:* 12 at launch (down from 20) is sufficient to establish the Builder's Track. Players will find them meaningful at 12. Ship the remaining 8+ in Version 1.1.

*Enemy variety:* 6 categories ship at launch. Within each category, launch with the 4–5 most mechanically distinct types; add rarer variants in Version 1.1. The six categories themselves are non-negotiable — removing Arcane Anomalies or Undead would thin the game's enemy variety below acceptable.

*Faction faction sets:* All 4 faction sets must ship. Firstborn sets can be reduced to 2 (Sentinel's Array and Erevos Fragment are most story-critical) with the third (Pathfinder's Kit) shipping in Version 1.1.

*Companion ambient dialogue:* 200 lines per companion at launch (vs. the designed 300–500). This is audible but not game-breaking. Reach full count in Version 1.1.

---

# SECTION 4: TECHNICAL RISK REGISTER

## 4.1 Top 10 Technical Risks — Milestone-Gated Approach

Each risk below has a required prototype milestone that must pass a Go/No-Go evaluation before full implementation begins. If a prototype fails, the team evaluates whether to solve the technical problem, reduce scope, or change the design before committing full implementation resources.

---

**RISK 1 — Dynamic World State System**
*Description:* The Act I/II/III transition system requires tracking 15+ player-deviation flags per location, maintaining 4 alignment world states, and triggering visual/NPC behavioral changes at correct moments without save-state corruption.
*Risk level:* HIGH
*Prototype gate:* Phase 1, Month 6. Two locations, three Act states each, five player flags. Validates the data architecture before world state is implemented across all 15+ locations.
*Mitigation:* If the system performs poorly, reduce to three states (Act I, Act II, one combined Act III state) and move per-alignment NPC dialogue to the companion system rather than the world state system.

---

**RISK 2 — Voiced Dialogue Volume**
*Description:* 35,000–50,000 voiced lines is a major production pipeline undertaking. Voice recording, direction, implementation, and localization at this volume requires external contractors and careful pipeline management.
*Risk level:* HIGH
*Prototype gate:* Phase 1, Month 4. Record and implement 500 test lines across 3 NPCs. Validate the recording pipeline, implementation tools, and QA workflow at small scale before committing to full production.
*Mitigation:* If pipeline is slower than projected, prioritize: main story lines first, companion lines second, faction quest lines third. Side quest ambient lines are the last priority and can be reduced or shipped without full voice in the Constrained Core version.

---

**RISK 3 — Firstborn Stone Custom Material**
*Description:* The Firstborn stone material (iridescent blue-gray, specific weathering behavior, different moss-growth patterns from organic stone) does not exist in UE5's standard material library. It requires custom material engineering.
*Risk level:* MEDIUM-HIGH
*Prototype gate:* Phase 1, Month 3. Create the material, apply to test geometry, validate performance in a scene with 50+ Firstborn surfaces. Confirm it meets visual targets and performance budget.
*Mitigation:* If custom material is too performance-expensive, simplify to a standard stone with a post-process iridescence layer applied only in high-quality settings. Visual target is reduced but performance is preserved.

---

**RISK 4 — Economic System Integration**
*Description:* The trade route, property ownership, and production chain system must integrate with the faction reputation system, the dynamic world state system, and the economic investment visual change system simultaneously. Integration bugs in one system can cascade through all three.
*Risk level:* HIGH
*Prototype gate:* Phase 1, Month 7. One trade route, one property, one production chain, in one zone with one faction alignment state. Validate that all three systems communicate correctly before scaling.
*Mitigation:* If integration proves too complex, launch with a simplified economic system (trade routes and property only; production chains deferred to Version 1.1). The economic identity of the game is preserved; the depth is reduced.

---

**RISK 5 — Echo Interface "Full Resonance" Contextual Dialogue**
*Description:* The Voice of the Architect capstone (Doc 7) requires the Echo to speak contextually to the player's specific situation — combat context, location, and recent choices — at the highest Echo Interface investment level. This requires a branching dialogue system that reads multiple game state variables simultaneously.
*Risk level:* MEDIUM-HIGH
*Prototype gate:* Phase 2, Month 20. Implement for one specific situation (The Sepulcher, player in combat, Echo at high rank). Validate that the contextual read works correctly and produces believable non-repetitive responses.
*Mitigation:* If contextual dialogue system is too complex, reduce Full Resonance to a curated set of 20 high-quality lines that cover common combat situations, rather than true contextual generation. Less dynamic, still impactful.

---

**RISK 6 — Enemy Echo Phantom (Mirrors Last 3 Abilities)**
*Description:* The Echo Phantom enemy (Arcane Anomaly category, Doc 7) mirrors the player's last 3 ability uses. This requires tracking and storing recent player input state and applying it to an enemy AI system — a non-standard AI architecture.
*Risk level:* MEDIUM
*Prototype gate:* Phase 2, Month 22. Build the Echo Phantom in isolation, validate that input tracking works correctly across all 20+ ability types and does not produce exploitable edge cases.
*Mitigation:* If the system is too buggy or exploitable, replace with a simpler mirroring system (mirrors one ability type — the player's most-used in the current combat) rather than the last 3. Reduces impressiveness but eliminates the edge case problem.

---

**RISK 7 — Corruption Zone Dynamic Expansion**
*Description:* Corruption zones must expand and contract based on Act transitions and player actions, with visual changes applied to the world geometry itself (not just a post-process overlay).
*Risk level:* MEDIUM
*Prototype gate:* Phase 1, Month 6 (validated alongside Risk 1). Corruption zone expansion applied to Zone 1 (Ashfield Scar). Confirm that geometry/material changes at zone boundaries work in real time and perform within budget.
*Mitigation:* If real-time geometry changes are too performance-expensive, implement as a scene reload (loading screen transition to new zone state) rather than real-time change. Less seamless, functionally equivalent.

---

**RISK 8 — Undercity Progression System**
*Description:* Three-layer Undercity with distinct discovery gates, standing requirements, and physical space unlocks requires careful state management to avoid the player accessing deeper layers before requirements are met.
*Risk level:* MEDIUM-LOW
*Prototype gate:* Phase 2, Month 14. Implement Undercity Layers 1 and 2, validate that standing gate correctly prevents early access and that the transition between layers is visually clean.
*Mitigation:* If gate system is buggy, simplify Layer 2 access to a quest-gated door rather than the standing-based system. Less elegant, fully functional.

---

**RISK 9 — Act III World State Multiplied by Four Alignments**
*Description:* Every major location needs 4 alignment variants of its Act III state. At 15+ major locations, this is 60+ variant states requiring unique art assets, NPC dialogue, and behavioral flags. Asset budget multiplier is significant.
*Risk level:* HIGH
*Prototype gate:* Phase 2, Month 24. Implement all 4 alignment states for Hollowford Market Quarter. Validate the asset production pipeline, establish per-variant asset reuse ratio, and confirm the total scope is achievable.
*Mitigation:* If asset production is too slow, reduce to two visually distinct alignment states (Vanguard and Verdant Flame as the most visually distinct) with Reaver and Hollow Crown changes delivered primarily through NPC behavior and dialogue rather than environment art changes. Full art changes ship in Version 1.1.

---

**RISK 10 — Performance in Ashenveil Archive**
*Description:* The Ashenveil Archive is a 7-level mega-dungeon with Firstborn architecture, custom materials, active construct enemies (particle effects), and complex lighting. It is the game's densest content area and its most performance-demanding.
*Risk level:* HIGH
*Prototype gate:* Phase 2, Month 26. Level 1 of the Archive at full visual quality on minimum spec hardware. Target: 60fps. If target is not met, begin optimization before Levels 2–7 are built to this standard.
*Mitigation:* If performance cannot reach 60fps at full quality, ship with reduced texture quality in the Archive and a performance mode option. The Archive is a critical narrative location — it cannot be simplified architecturally, but visual quality can be tiered.

---

# SECTION 5: POST-LAUNCH EXPANSION ROADMAP

## 5.1 Expansion Philosophy

The game's world is built with expansion in mind. The seven regions of Aethercrown are established in the World Bible with enough lore, political context, and narrative hooks to support three full expansions without contradicting the base game's events. Each expansion adds a new playable region, a new playable race, and a new storyline that connects to the base game's consequences without requiring it.

## 5.2 Expansion 1 — The Forge Covenant (Highwinter Expanse)

**Timing:** 12–18 months post-launch
**New playable race:** Ironkin (full implementation — Tank/Heavy Warrior/Crafter identity, Firstborn Forge mastery, Iron Will system)
**New origins:** Covenant Smith, Forge Warden (2 Ironkin origins)
**New region:** Highwinter Expanse (~35 km² — volcanic tundra, forge-temple cities, Vanguard High Command)
**New faction:** The Covenant of Forges (Ironkin religious-industrial leadership — distinct from but politically entangled with the Vanguard)
**Narrative hook:** The forge-temples are destabilizing as their lattice-powered furnaces fail. The Ironkin's Tempering Rite — the coming-of-age ritual that creates Ironkin identity — is producing increasing numbers of Hollow Ones (failed Temperings). Return to Highwinter to stabilize the Covenant before the north collapses into civil war between Traditionalists and Unbound.
**Connection to base game:** Kael Thornwright's homeland. His personal quest's full resolution requires Expansion 1 content. Vanguard High Command — referenced but never seen in the base game — becomes a location.
**New systems:** Ironkin Crafting System (Firstborn Forge mastery — expands on the base game's Firstborn Forge station), Iron Will system (defensive power spike below 25% HP), Cold Environment mechanics (Ironkin advantage in Highwinter; other races face cold exposure challenges)
**Scope estimate:** 60% of base game content volume. Manageable as a paid expansion.

## 5.3 Expansion 2 — The Ashen Exodus (Crimson Flats or Sunscar Coast)

**Timing:** 24–30 months post-launch
**New playable race:** Drakelings (full implementation — Heat Meter system, fire magic, berserker identity)
**New origins:** Flame Prophet (fire zealot, trauma of homeland), Ember Scout (pragmatic survivor, refugee experience)
**New region:** Crimson Flats (volcanic wasteland, reclamation story) OR Sunscar Coast (diaspora story, maritime setting) — one at expansion launch, one in a subsequent content update
**Narrative hook:** The volcanic cascade that destroyed the Drakeling homeland during the Severance has stabilized enough to return — but what's waiting in the Crimson Flats is not what anyone expected. Something survived. Or something arrived.
**Connection to base game:** Drakeling refugee communities in the Vale (Emberhaven, Southwatch camp) are the starting point. Characters introduced in the base game's Southwatch content appear in Expansion 2. Pyra Flameheart's questline, if resolved in the base game, has direct consequences here.
**New systems:** Heat Meter (builds through combat, enhances fire abilities, risks uncontrolled ignition), fire environment interactions (flammable objects, heat-sensitive NPCs, fire-immunity zones — the content complexity reason this race wasn't in the base game), Cold Vulnerability (opposite of Ironkin)
**Scope estimate:** 75% of base game content volume.

## 5.4 Expansion 3 — The Severed Capital (Severantis / Unknown)

**Timing:** 36–42 months post-launch
**Nature:** The Dominion's capital city of Severantis vanished during the Severance — its fate was deliberately left as a mystery in the base game. Expansion 3 answers the question.
**New playable content:** Whatever Severantis became. A city displaced into an adjacent plane, or a city frozen in the moment of the Severance, or something else entirely — the design of this expansion follows from what the story demands, not from a predetermined concept. This is intentionally unspecified.
**New race (optional):** Dependent on what Severantis contains. If it was inhabited by people who survived in a changed form, a fourth playable race emerges naturally.
**Design philosophy:** This expansion should feel like the culmination of everything the base game's mystery established. Players who completed the base game and both previous expansions will bring significant context. The writing can assume that context.
**Scope estimate:** Equivalent to base game in ambition. Budget accordingly.

---

# SECTION 6: MILESTONE SUMMARY

## 6.1 Key Development Gates

| Milestone | Phase | Target Month | Go/No-Go Criteria |
|---|---|---|---|
| Combat feel validated | Pre-Production | Month 3 | Weighted action RPG feel confirmed by blind playtest; recovery frames producing intended read-and-react loop |
| Firstborn stone material approved | Pre-Production | Month 3 | Visual target met, performance within budget |
| World state prototype validated | Pre-Production | Month 6 | Two locations, three states each, five flags — no corruption, correct triggers |
| Economic system prototype validated | Pre-Production | Month 7 | One trade route + property + production chain integrated without cascade bugs |
| Vertical slice complete | Pre-Production | Month 8 | Origin tutorial + Sepulcher L1 + Kael intro + one Vanguard quest — all playable end-to-end |
| Core systems complete | Alpha | Month 15 | All 6 attributes, all skill trees, full combat, full loot, full crafting — integrated and stable |
| Act I greybox complete | Alpha | Month 18 | Full Act I playable, all systems triggering correctly, no narrative blockers |
| Act II greybox complete | Alpha | Month 24 | Ashenveil Archive playable, all Act II content in place |
| Full game greybox complete | Alpha | Month 30 | All four Acts, all endings, all companion arcs — playable start to finish |
| Dialogue recording complete | Beta | Month 36 | All 35,000–50,000 lines recorded, implemented, and tested |
| Content polish complete | Beta | Month 42 | All systems balanced, all content at ship quality |
| Gold master | Beta | Month 44 | Certification passed, all critical/major bugs resolved |
| Expansion 1 gold | Post-Launch | Month 56 | The Forge Covenant complete |

---

# SECTION 7: CONTENT PRODUCTION PRIORITIES

## 7.1 The Hierarchy of What Gets Built First

When production time is constrained, this is the order in which content should be built:

**Tier 1 — Must be working to evaluate anything else:**
1. Core movement and combat (Phase 1)
2. One companion relationship and one faction quest (Phase 1 vertical slice)
3. Dynamic world state system (Phase 1 prototype)

**Tier 2 — Must be complete for Alpha to be meaningful:**
4. All 6 character origins with tutorial sequences
5. Hollowford in full (the game's hub — everything depends on it)
6. The Sepulcher (Act I narrative payoff)
7. All 4 faction quest lines through Act I

**Tier 3 — Must be complete before Beta begins:**
8. Ashenveil Archive (Act II narrative payoff — the game's most expensive single content item)
9. All 4 companion personal quests
10. Complete Act III alignment world states

**Tier 4 — Beta phase priorities:**
11. All voiced dialogue (pipeline running from month 15 onward — not a batch at the end)
12. All 33 side quests
13. All micro-discoveries
14. Economic system depth

**What this hierarchy means practically:** If a team is behind schedule at Month 24 (end of Act II greybox), the correct decision is to complete Tier 2 and Tier 3 content to high quality before touching Tier 4 content at all. A game with complete Act I–IV, four compelling companions, and all four faction arcs — but 15 side quests instead of 33 and 30 micro-discoveries instead of 60 — is a better shipped game than a game with all 33 side quests but a broken Act III.

---

# SECTION 8: BUDGET CONSIDERATIONS

## 8.1 Major Cost Drivers

The five largest cost drivers in this production, in order of magnitude:

**1. Voice acting production (~18–22% of total budget):**
35,000–50,000 lines across 35+ voice performers, with recording sessions, direction, implementation engineering, and QA. This is the single largest variable cost in the production. Planning the voice pipeline from Month 6 onward (not as a late-stage production item) is critical to managing this cost.

**2. World art and environment (~20–25% of total budget):**
40–45 km² of authored environment at grounded realism standard, custom Firstborn materials, 4 dungeon tile sets, dynamic corruption zone visual states. The environment art team is the largest single art department and the one with the longest lead time per asset.

**3. Animation (~12–15% of total budget):**
45+ enemy types with full attack/death/idle animation sets, all weapon types with distinct combat animations, companion facial animation systems, cutscene animation for major narrative moments. Animation is chronically underestimated in RPG productions.

**4. Narrative writing and scripting (~8–10% of total budget):**
81+ quests with branching outcomes, 35,000–50,000 dialogue lines, 60–80 micro-discovery scenes, Act III world state variant dialogue per NPC per location. Writing takes longer than it looks at this volume.

**5. QA (~10–12% of total budget):**
A game with dynamic world states, 81+ quests, 4 Act III alignment states, and an economic system requires sustained dedicated QA from Month 31 onward. Undertesting a game of this complexity produces an embarrassing launch.

## 8.2 Budget Reallocation Principle

If budget must be cut, cut content before cutting quality. A game with fewer side quests that are all excellent is better than a game with all designed side quests at reduced quality. The Constrained Core section defines the floor. Within that floor, every cut should preserve quality over quantity.

---

# SECTION 9: THE DESIGN BIBLE AS A LIVING DOCUMENT

## 9.1 Document Maintenance

The ten documents of this design bible were written in sequence, building on each other. As production proceeds, decisions made in implementation will require updates to the design documents. This is normal and expected.

**Update protocol:**
- Any change to SD_01 (World Bible) requires review of all nine subsequent documents for contradictions
- Any change to SD_07 (Combat) requires review of SD_06 (Loot) for affix/ability compatibility
- Any change to SD_05 (Faction Playbook) requires review of SD_08 (Region Guide) for world state implications
- SD_01 remains the canonical source of truth — if any document contradicts it, SD_01 wins

**Version control:** All design documents should be version-controlled alongside the codebase. Design changes should be documented with the same rigor as code changes — what changed, why, who approved it.

## 9.2 What This Document Set Does Not Cover

Explicitly out of scope for this design bible, requiring separate documentation:
- Detailed quest scripts (separate quest design documents per quest)
- Specific NPC dialogue scripts (separate narrative production documents)
- Technical engineering specifications (separate technical design documents)
- Sound design specification (separate audio design document)
- Marketing and publishing strategy
- Platform certification requirements
- Localization planning
- Multiplayer or co-op considerations (this game is single-player only as designed)

---

# SECTION 10: FINAL SCOPE SUMMARY

## What This Game Is, At Its Core

The Shattered Dominion is a single-player action RPG about a world four weeks past a catastrophe, told through the eyes of someone marked by a Firstborn relic who must decide the fate of a failing magical infrastructure — not by being special, but by becoming informed enough to make an intelligent choice.

The game's identity is not its combat system, its loot system, its crafting system, or its economic system — though all of these are well-designed. Its identity is the combination of a morally complex world with no obvious villains, companions who push back against the player's choices, factions whose conflicts feel genuinely unsettled, and an ending that depends on what the player understood and chose rather than which faction they were loyal to.

Every production decision should be evaluated against this identity. If a system, quest, or feature reinforces one of those four things — moral complexity, companion agency, faction authenticity, meaningful ending — it belongs in the Constrained Core. If it enriches the experience without reinforcing those things, it belongs in Tier 4 or post-launch. If it contradicts them, it should be cut regardless of how much work went into it.

**The game succeeds if a player finishes it, looks back at their choices, and genuinely wonders whether they made the right ones.** Everything in these ten documents exists in service of that moment.

---

*End of Document 10: MVP Development Roadmap*
*End of The Shattered Dominion Design Bible — Documents 1 through 10*
*Version 1.0 | Complete*
