# THE SHATTERED DOMINION — ENEMY DESIGN & ENCOUNTER VOCABULARY
## Document SD_17 | Version 1.0
## Depends on: SD_07 Combat & Build Framework, SD_01 World Bible, SD_08 Severant Vale Region Guide

---

# SECTION 1: DESIGN PHILOSOPHY

## 1.1 What This Document Is For

SD_07 defines the combat system — attributes, skill trees, stamina, convergence abilities, the weighted action framework. It defines *how players fight*. This document defines *what players fight* — the behavioral vocabulary, encounter design rules, and teaching objectives for every enemy category in the game.

These two things are distinct. A combat system without specified enemy design is a grammar without sentences. The weighted action RPG promise — *"enemies telegraph clearly, players who read fights win"* — requires that enemies have clear, distinct, learnable patterns. This document is the specification for those patterns.

**Use this document when:**
- Designing a new enemy type
- Designing an encounter (room, corridor, or open world)
- Evaluating whether a dungeon combat section is working
- Writing AI behavior specifications for any enemy category

## 1.2 Core Enemy Design Principles

**Every enemy teaches something.** Not every enemy needs to be complex. A basic enemy teaches the player one thing, clearly. An elite enemy teaches two things in combination. A boss teaches the player to apply everything they've learned in a specific order under pressure.

**Enemies have behavioral vocabulary, not stat sheets.** The difference between a Bloodhound Knight (Elden Ring) and a generic "strong melee enemy" is behavioral specificity — the Bloodhound Knight has recognizable attack patterns, tells, and a specific counter-strategy. SD enemies must have equivalent specificity.

**Encounters are teaching moments, not obstacle courses.** Every significant encounter should be designed so the player comes out the other side knowing something they didn't know going in — about the enemy, about their own build, about the environment.

**Corrupted variants are not reskins.** A corrupted wolf and a normal wolf share a visual language but fight differently — corruption changes behavior, not just appearance. Every corrupted variant must have at least one new behavioral element that the uncorrupted version doesn't have.

---

# SECTION 2: THE SIX ENEMY CATEGORIES

*Per SD_07 §7. This section defines the behavioral vocabulary, teaching objective, and encounter design rule for each category. Individual enemy specifications are in Section 3.*

---

## Category 1: CORRUPTED WILDLIFE
**World Grounding:** Animals and creatures warped by lattice failure — the most common enemy type in the open Vale.
**Teaching Objective:** Resource management and threat assessment. Corrupted wildlife teaches the player to prioritize targets, conserve stamina against fast enemies, and read corrupt animation tells (which are faster and less telegraph-heavy than construct or human enemies).

**Behavioral Vocabulary:**
- Fast, aggressive, commit-heavy attacks (animals don't second-guess)
- Low HP but high pressure — they keep attacking even while staggered
- Pack behavior: often encountered in groups of 3-5; AI designed so they don't all attack simultaneously (they form a loose rotation)
- Environment-aware: use cover, high ground, narrow corridors to their advantage
- **Corruption tell:** All corrupted wildlife has a specific animation state (a brief "charge-up" that normal animals don't have) before their most dangerous attack. This tell is fast (0.4-0.6 seconds). The game is designed so players learn to read it, not react to it.

**Encounter Design Rule:** Corrupted wildlife is never the main threat in an encounter — it's the ambient pressure that makes the main threat harder to deal with. A corrupted wolf pack in a room with a corrupted bear: the bear is the encounter; the wolves are why you can't focus entirely on the bear.

**Corrupted Variants (behavioral changes):**
- Base animals: normal behavior, normal telegraph speed
- Partially corrupted: same attacks, faster, one new attack type unique to corruption
- Fully corrupted: transformed appearance, entirely new attack set, pack coordination is more sophisticated

---

## Category 2: IRONBOUND VANGUARD SOLDIERS
**World Grounding:** Human military trained by the Dominion, now operating under fragmented command structure in the Vale.
**Teaching Objective:** Formation combat and target prioritization. Vanguard soldiers teach the player to manage groups of coordinated human enemies who use cover, call reinforcements, and have individual specializations.

**Behavioral Vocabulary:**
- Formation-aware: two or more Vanguard soldiers will naturally position to flank the player. Single Vanguard soldiers are significantly less dangerous.
- Specialization types: Shield-bearer (high defense, crowd control function), Crossbowman (ranged harassment, soft target), Captain (buffs nearby soldiers, priority target)
- Morale system: Vanguard soldiers at low HP will retreat to cover and call reinforcements rather than fight to death. This teaches players to finish priority targets quickly.
- Non-lethal options: Some Vanguard encounters can be ended through intimidation (high Fame/Infamy with Vanguard), bribery (Crown Marks), or tactical withdrawal (stealth exit from combat area). These options close when players are Notorious with the Vanguard.
- **Unique mechanic:** Vanguard Captains can issue commands that alter nearby soldiers' behavior (shield-bearers raise shields on command, crossbowmen relocate on command). Eliminating the Captain first disrupts formation.

**Encounter Design Rule:** Vanguard encounters should always present the player with a clear priority hierarchy. Captain → Crossbowman → Shield-bearer → Infantry is the standard. Players who understand this dismantle Vanguard groups efficiently; players who attack the nearest target instead are punished by the formation adapting around them.

**Hostile vs. Neutral:** Not all Vanguard encounters are combat. Checkpoint Vanguard soldiers are non-combat (see SD_18 for checkpoint interaction mechanics). Combat Vanguard encounters are flagged by their armor variant — red crest means hostile, grey crest means neutral.

---

## Category 3: ASHMAR REAVER OPERATIVES
**World Grounding:** Smugglers, mercenaries, and opportunists operating outside faction control.
**Teaching Objective:** Threat identification under ambiguity. Reavers teach the player that not all human enemies have obvious roles — Reaver groups are deliberately miscellaneous, and the "leader" may not be visually distinct.

**Behavioral Vocabulary:**
- Opportunistic: Reavers flee when the fight turns against them. High morale at 3-on-1; low morale when outnumbered or when an ally falls. Players who kill one Reaver quickly may watch the others run.
- No formation: they fight individually with loose coordination. Less disciplined than Vanguard but harder to predict.
- Traps and ambushes: Reaver encounters often begin with an environmental trap (tripwire, oil fire, falling debris) that the player walks into. Awareness stat and Vaelari's Wellspring Sense detect these.
- Specialization types: Knife specialist (fast, high-damage on flanks), Torch-and-oil (area denial), Bruiser (tanky, slow, ignores player attempts to disengage), Informant (hangs back, calls reinforcements — must be neutralized before they escape)
- **Unique mechanic:** Some Reaver encounters have a "pay to leave" option — the player can throw a purse of Crown Marks (25-100 depending on Reaver size) and the group disengages. High Reaver Fame makes this cheaper. High Infamy means they'll take the money and then attack anyway.

**Encounter Design Rule:** Every Reaver encounter should have an Informant in it, positioned at the back. Eliminating the Informant first is always the correct play but players must identify them first. Informants look like any other Reaver but move toward exits rather than toward the player.

---

## Category 4: FIRSTBORN CONSTRUCTS
**World Grounding:** Automated Firstborn machines reactivated by the Severance, running defense protocols in ruins and lattice infrastructure.
**Teaching Objective:** Pattern patience and deliberate combat. Constructs teach the player to slow down, read long attack sequences, and find specific openings rather than looking for general weaknesses.

**Behavioral Vocabulary:**
- High HP, high defense — cannot be quickly overwhelmed
- Strictly patterned: each construct type has 2-4 attack sequences it cycles through. The sequences are always the same, in the same order. Veteran players know the pattern before the construct completes its first cycle.
- Clear telegraphing: Constructs have the longest startup frames of any enemy category (0.8-1.5 seconds depending on attack). The telegraph is always visual — a specific limb position, a glow effect, a gear sound.
- Openings only on recovery: Unlike wildlife (which has brief openings mid-combo), constructs have attack windows only during their post-attack recovery phase. Players who understand this pace their attacks correctly; players who don't take constant damage.
- **Unique mechanic:** Construct Weakpoints (per SD_07 combat revision). Accumulating 3+ consecutive hits without taking damage activates the weakpoint flash. Different construct types have different weakpoint locations — players who know the type can target immediately; players who don't have to earn it.
- **Relic interaction:** The Echo can briefly "confuse" a construct's targeting system once per combat — a 3-second window where the construct ignores the player. This is introduced in the Relic Hunter origin and the Thornveil Undercroft dungeon.

**Encounter Design Rule:** Construct encounters should always be duels or near-duels. Constructs are designed for 1-on-1 combat with a player. Paired constructs (two in the same room) represent a significant difficulty spike and should be used deliberately, not as ambient challenge increase. A room with four constructs is a puzzle, not a fair fight — the solution is environmental (activate a control panel, use a construct against another) not combat-direct.

**Construct Tiers:**
- Maintenance drone (minor): 1-2 attack sequences, simple pattern, low HP. Tutorial constructs.
- Guard construct (standard): 3-4 attack sequences, two weakpoint phases. Core construct encounter.
- Warden construct (elite): 5-6 attack sequences, phase transitions at 60% and 30% HP where new sequences unlock. Boss-adjacent.
- Seal Warden (boss, unique): See SD_03 §5.3.

---

## Category 5: HOLLOW CROWN AGENTS AND ENFORCERS
**World Grounding:** Political operatives and hired muscle working for House Eltaryn and the Hollow Crown's agenda.
**Teaching Objective:** Combat-adjacent problem solving. Hollow Crown encounters are designed to be solvable through combat, social leverage, or information — players who only fight miss solutions that cost less.

**Behavioral Vocabulary:**
- Enforcers fight like Vanguard soldiers but without formation discipline — they're hired muscle, not trained military. Less coordinated, more aggressive.
- Agents do not fight if they can avoid it. They flee to alert others, use environmental levers (collapsing walls, locked doors, summoning reinforcements through signal devices), and will surrender if cornered and the player's reputation makes surrender seem survivable.
- **Non-combat resolution:** Hollow Crown encounters (Agents specifically) can be resolved through: revealing information the Agent values more than loyalty (requires Archive knowledge); bribing (Hollow Crown agents respond to Crown Marks specifically, not Lattice Chips — their loyalty is transactional); demonstrating that the player's cause aligns with Eltaryn survival (requires Hollow Crown Fame); or simply having Seraphine present and functional (if she is, most Agent encounters deescalate automatically with a word from her).
- **Unique mechanic:** Hollow Crown Agents always carry written instructions — an item that can be looted from their body or pickpocketed while alive. These instructions provide intelligence about Hollow Crown operations and occasionally serve as quest items or faction leverage.

**Encounter Design Rule:** At least one in three Hollow Crown encounters should have a visible non-combat solution before combat begins. The player should see the solution, choose to ignore it, and accept the consequences — or choose it and bypass the fight. Never hide non-combat solutions behind a wall the player might not find.

---

## Category 6: ARCANE ANOMALIES (CORRUPTION-SPAWNED ENTITIES)
**World Grounding:** Entities that exist only in or near corruption zones — not wildlife, not human, not construct. The Severance created them.
**Teaching Objective:** Adaptation and unconventional thinking. Anomalies break the rules established by other categories — they don't respond to standard stagger, they have behaviors no previous enemy has demonstrated, and they often require environment interaction rather than direct damage.

**Behavioral Vocabulary:**
- Resistant to standard physical damage — full damage is only achievable through Relic abilities, magic, or specific environmental interactions (lattice conduit discharge, purified materials)
- Unpredictable: unlike constructs (fully patterned) or wildlife (semi-patterned), Anomalies have randomized attack selection within a defined set. Players cannot learn a fixed sequence — they must learn the full set and react to each instance.
- Environment-integrated: Anomalies use corruption zone elements as part of combat — they emerge from corrupted surfaces, retreat into corruption pools (which damage the player), and recharge by touching corrupted objects. Removing or neutralizing environmental corruption objects changes the encounter.
- **Unique mechanic — Echo Phantom (specific Anomaly subtype):** This Anomaly mirrors the player's last 3 ability uses and deploys them against the player. Players who understand this can manipulate what it mirrors; players who don't will fight a distorted version of themselves. See SD_10 Risk 6 for implementation notes.
- HP bar: Anomalies display HP bars that count up rather than down — the bar fills as the Anomaly absorbs damage without a source that affects it. Players who hit it with normal attacks watch the bar fill (they're feeding it, not hurting it). Players who switch to relic or magic attacks see the bar drop normally. This is the clearest possible telegraph for "you're doing this wrong."

**Encounter Design Rule:** Anomaly encounters must never be the player's introduction to a new mechanic. If a player encounters their first Echo Phantom before they've used 3 distinct abilities in a single combat, the Phantom cannot mirror anything and the mechanic is wasted. Place first Anomaly encounters only after the player has demonstrated the abilities the encounter is designed to test.

---

# SECTION 3: FIVE ENCOUNTER ARCHETYPES

*Named templates that level designers apply to any enemy combination. Each archetype has a specific teaching objective and specific rules.*

---

## Archetype 1: THE DUEL
**Enemy configuration:** One enemy. No other threats. Full arena.
**Teaching:** Pattern reading and sustained combat. Duels are where players learn individual enemy types.
**Rules:** The enemy must have at least 3 attack sequences. The arena must have enough space to dodge all attacks. There must be a recovery item available (on a body, in a chest) before the fight begins — players who nearly die learn to prepare.
**Used for:** Warden construct encounters, Named enemy introductions, Boss fights (always a Duel structure).

---

## Archetype 2: THE PRESSURE COOKER
**Enemy configuration:** 1-2 high-priority targets + 3-5 low-priority ambient threats.
**Teaching:** Target prioritization under constant harassment.
**Rules:** The ambient threats must be killable in 1-2 hits. The high-priority targets must require sustained attention. The player should feel the difference between "dealing with the pressure" and "dealing with the problem."
**Used for:** Standard dungeon rooms, open world corruption zone encounters, Reaver ambushes.

---

## Archetype 3: THE PUZZLE FIGHT
**Enemy configuration:** Multiple enemies that cannot all be engaged simultaneously; environmental elements that change the encounter.
**Teaching:** Problem identification before problem-solving. The player must understand why the fight is hard before they can make it easy.
**Rules:** The puzzle solution must be discoverable through observation (not prior knowledge). The puzzle must have at least two valid solutions. Solving the puzzle should feel like insight, not luck.
**Used for:** Construct pairs, Anomaly encounters, Hollow Crown compound interiors.

---

## Archetype 4: THE GAUNTLET
**Enemy configuration:** Sequential waves with brief recovery windows between waves.
**Teaching:** Stamina economy over sustained combat. The Gauntlet punishes players who spend everything on wave 1.
**Rules:** Recovery windows must be long enough to heal and identify incoming threats. Wave 3+ must introduce a new enemy type the player hasn't seen in this encounter. Final wave must include at least one high-priority target (Captain, Warden, Agent).
**Used for:** Dungeon defense sequences, faction assault missions, Act III surface conflicts.

---

## Archetype 5: THE SOCIAL COMBAT
**Enemy configuration:** Human enemies (Vanguard, Reavers, or Hollow Crown) in a context where non-combat resolution is explicitly available.
**Teaching:** That combat is always optional and sometimes suboptimal.
**Rules:** The non-combat solution must be discoverable without prior knowledge of the encounter. Choosing non-combat must produce a meaningfully different outcome (not just "same result, less fighting"). Players who choose combat should not be penalized — but players who choose the social solution should feel they've outplayed the encounter.
**Used for:** Checkpoint encounters, Hollow Crown Agent confrontations, Reaver negotiation moments.

---

# SECTION 4: ENEMY INTRODUCTION SCHEDULE

*No enemy type should appear before the player has the tools to engage it. This table specifies when each category is first encountered and what the player needs to handle it.*

| Category | First Encounter | Player Prerequisites | Teaching Encounter Design |
|---|---|---|---|
| Corrupted Wildlife | Origin sequence (hour 1) | Basic combat only | Small pack, open area, slow wildlife variants |
| Vanguard Soldiers | Hour 3-5 (Hollowford patrol encounter) | Basic dodge and block | Single Vanguard soldier, no flanking |
| Reaver Operatives | Hour 6-10 (Undercity or supply road) | Target prioritization basics | Small group, Informant visible, retreat option present |
| Firstborn Constructs | Hour 10-13 (Thornveil Undercroft) | Stamina management, recovery window awareness | Maintenance drone pair — low HP, simple patterns |
| Hollow Crown Agents | Hour 8-15 (faction quest context) | Social options awareness | Agent + 1 Enforcer; social solution available |
| Arcane Anomalies | Hour 20-25 (first corruption zone deep area) | Relic ability comfort, magic awareness | Single Anomaly in open space; Echo narrates the HP bar behavior |

---

*End of Document SD_17 v1.0*
