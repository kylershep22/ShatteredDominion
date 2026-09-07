# THE SHATTERED DOMINION — ONBOARDING & SYSTEM INTRODUCTION SCHEDULE
## Document SD_18 | Version 1.0
## Depends on: SD_02 Race & Origin System, SD_07 Combat & Build Framework, SD_11 Economy System, SD_12 Homestead System

---

# SECTION 1: PHILOSOPHY

## 1.1 The Problem

The Shattered Dominion has, at launch, the following systems a player must eventually understand:

- Combat (weighted action, recovery frames, stamina, stagger)
- Dodge mechanics (basic roll → full roll at AGI 10 → dodge-cancel at AGI 30)
- The attribute system (6 attributes, 8 thresholds each)
- The skill tree system (20+ trees, use-rank growth, Proficiency Bonuses)
- The Echo interface and relic abilities
- Convergence Abilities (spread-build unlocks)
- The weakpoint system
- The socket system (two distinct purposes: Combinations on Common items; individual bonuses on Touched+)
- Five item quality tiers and identification
- Nine relic shard types and 20+ Combinations
- Crafting (six disciplines, three at launch)
- The faction Fame/Infamy dual-track system (4 factions × 2 tracks)
- The ideology sub-score within each faction's Fame track
- The economy (four currency types, trade routes, caravan masters, production chains)
- Companion relationship management (invisible score, threshold behaviors)
- The homestead system (Farmstead through Manor Estate at launch)
- Race-specific mechanics (Jury-Rigging / Wellspring Communion / Overload)

That is an enormous learning surface. The game's systems are individually well-designed and collectively coherent. They are not, however, self-explanatory. A player who hits ten of these systems in their first five hours will not engage with any of them meaningfully.

## 1.2 The Solution: Tiered Introduction with Staggered Revelation

Every system in the game is assigned to one of three introduction tiers:

**Tier 1 — Survival Knowledge:** Must be understood in hours 1-5 or players fail. Introduced through authored tutorial moments — the game stops, shows you, makes you do it. Approximately 8 systems.

**Tier 2 — Engagement Knowledge:** Should be introduced hours 5-25 but players won't hit a wall without them. Introduced through soft contextual teaching — an NPC explains it when the situation naturally calls for it. Players who ignore the explanation can keep playing; they'll hit the system eventually through natural play. Approximately 6 systems.

**Tier 3 — Depth Knowledge:** Available from hour 1 but mastery is optional. Available through discovery — the system exists in the world before it's explained; players who look find it. Players who don't find it when they're ready. Approximately 5 systems.

## 1.3 The Echo as Primary Tier 1-2 Teaching Agent

The Echo is inside the player's head. It has access to the player's sensory experience. It can provide contextual instruction at exactly the right moment without breaking immersion, because the Echo *noticing* something the player hasn't is characterfully appropriate — it was built as a guide.

**Echo teaching principles:**
- The Echo teaches through observation, not instruction. *"That soldier telegraphed that swing for half a second before it landed. You'll learn to see it."* Not: *"Tip: Enemies have a startup frame before attacks."*
- The Echo does not repeat itself. If a player has already demonstrated understanding (executed a successful dodge, used the identification scroll), the Echo acknowledges it once and moves on.
- The Echo's teaching voice evolves with its overall arc. In Act I (early), it's broken and directive. By Act I (late), it's more conversational. Teaching lines should match the Echo's current arc state.
- The Echo is not a help menu. If a player is confused about a system that was already taught, they can access a codex entry. The Echo is for first introductions only.

---

# SECTION 2: TIER 1 — SURVIVAL KNOWLEDGE

*Introduced in hours 1-5, through authored moments. These systems must be understood for basic play.*

---

## T1-01: Movement and Camera

**When:** First 60 seconds of origin sequence
**Who:** Environmental (player discovers through control)
**Method:** The game simply starts. Movement, camera, and sprint are discovered through necessity. No popup.
**Reinforcement:** Sprint is naturally tested in the first chase/escape sequence in every origin opening.

---

## T1-02: Basic Combat (Attack, Startup, Recovery)

**When:** First combat encounter in origin sequence (hours 1-2)
**Who:** Echo (broken, directive form)
**Method:** The Echo fires on the first enemy encounter: *"Strike. Wait for it to finish. Strike again."* This is not a popup — it's a voiced line. The player makes the attempt. If the first strike lands without the player understanding recovery and they get hit, the Echo adds: *"...Too soon. Let it complete."*
**Reinforcement:** The origin tutorial fights are designed specifically to punish button-mashing (the enemy's counter-attack arrives during recovery frames). Players learn by getting hit, not by reading.

---

## T1-03: Dodge and Blocking

**When:** Second combat encounter in origin sequence; or first named enemy encounter
**Who:** Echo
**Method:** When a large, clearly telegraphed attack is incoming, the Echo: *"That one — move."* The player dodges or blocks. If they take the hit: *"The tell was the shoulder drop. You'll learn its patterns."* If they dodge successfully: *"Yes. Like that."* No further explanation of dodge mechanics — the basic functionality is established. Dodge-cancel and roll upgrades are Tier 2.
**Reinforcement:** Consistent enemy telegraph design — startup frames are always visually distinct (posture change, wind-up animation, glow if magical).

---

## T1-04: Stamina

**When:** First time the player runs out of stamina during combat (usually within the first two enemy encounters)
**Who:** Echo
**Method:** Stamina bar depletes visibly. If the player attempts to attack at zero stamina: *"You're spent. Breathe."* The stamina bar pulses. The player waits. It refills. *"There. Stamina comes back. It always comes back — but not if you push past empty."*
**Reinforcement:** Early enemies are designed with windows that require players to manage stamina (attack, pause, attack) rather than spam. This is taught through enemy behavior, not tooltips.

---

## T1-05: The Echo and Relic Abilities

**When:** Origin-specific relic introduction moment (hours 1-2, varies by origin)
**Who:** Echo (the introduction of this ability IS the Echo becoming present)
**Method:** Each origin has a scripted relic activation moment (the Frontier Settler's Echo activates after finding the family item; the Relic Hunter's activates in the collapsing ruin; etc.). The Echo's first coherent instruction is to use the relic ability. The player does it. The ability works. The Echo: *"There. That's what you are now. I'll explain more when I can. Move."*
**Reinforcement:** Relic abilities are available from the start. Players who experiment with them discover additional effects through use-rank growth.

---

## T1-06: Healing and Consumables

**When:** First near-death experience in origin sequence
**Who:** Echo
**Method:** When player HP drops below 30%: *"You're bleeding. Use the [salve/herb/potion] — there, in your belt."* A brief visual pulse highlights the consumable slot. If the player uses it: *"Good."* If they don't: *[after the fight or death]* *"You had supplies. You didn't use them. Keep them in mind."*
**Note:** This is the only system where a UI highlight is acceptable — the consumable slot pulse is non-intrusive and resolves immediately.

---

## T1-07: Item Identification (Basic)

**When:** First Touched-tier item found (usually during the origin sequence or first hour in Hollowford)
**Who:** NPC vendor or the first identification station the player encounters
**Method:** The Touched item is visually distinct (blue tint, question marks on affixes). The first vendor the player sells to says: *"Hold on — that one's sealed. You'll want to identify it before you decide what to do with it. The workbench at the market does it for free."* This is not a popup. It's a merchant line. The player can ignore it, follow it immediately, or return to it.
**Reinforcement:** The first identification is free and produces a clearly better item than anything found before it — reward is immediate.

---

## T1-08: Fast Travel

**When:** First time the player tries to return to a previously visited location (usually around hour 4-5, after the first faction quest)
**Who:** Hollowford notice board or Vanguard gate guard
**Method:** A gate guard: *"Heading out again? The Vanguard maintains waypoints on the main roads — ask any gate soldier to arrange transit."* This is soft — players can walk. Fast travel is available. The game doesn't force you to discover it; it lets you know it exists.

---

# SECTION 3: TIER 2 — ENGAGEMENT KNOWLEDGE

*Introduced hours 5-25, through contextual NPC dialogue. Players who miss these introductions encounter the systems naturally through play.*

---

## T2-01: Attribute Thresholds

**When:** Hour 8-10, when the player earns their first 4+ attribute points and visits a trainer or the Hollowford general workbench
**Who:** A Vanguard weapons trainer named Sergeant Orin (available Act I in the Market Quarter)
**Method:** Orin: *"A word of advice — don't spread yourself thin. Pick a direction early. When your Strength hits ten, you'll feel it — medium armor stops costing you. At fifteen, more options open up. Every threshold's a gate. Which gates matter depends on what you're building."* The player can ask follow-up questions. Orin knows the STR and END thresholds in detail; other attributes are summarized as "talk to someone who knows those."
**Reinforcement:** The threshold system feedback is mechanical — players who hit STR 10 feel the armor weight change immediately. The system teaches itself once players know to look for thresholds.

---

## T2-02: Faction Fame and Infamy

**When:** Hour 6-8, after the player completes their first faction quest
**Who:** Maren Duskwell (if recruited) or a Reaver contact in the Undercity (if not)
**Method:** *"You know the difference between the Vanguard liking you and the Vanguard fearing you? Fame gets you through checkpoints with a smile. Infamy gets you through checkpoints without a search. High enough of both and they don't know what to do with you. That's actually the most useful state."* This is Tier 2 because the player has already built some reputation before it's explained — the explanation contextualizes what they've been doing.
**Reinforcement:** The Standing State system (Unknown, Trusted, Notorious, etc.) is labeled in the faction menu — players who open it after this conversation understand what the labels mean.

---

## T2-03: Companion Relationship (Invisible Score)

**When:** Hour 8-12, after a significant companion moment (Kael's confession, Aelira's first node survey, Maren's first personal disclosure)
**Who:** The companion themselves, in ambient dialogue after the moment
**Method:** Kael, after the confession: *"I don't share that with most people. I notice what you do with it."* This is not an explanation of the relationship system. It's a character line that implicitly tells the player that what they do matters to this person. Players who are paying attention understand: this is tracked. Players who aren't will figure it out when companion behavior changes.
**Note:** The relationship score is never, under any circumstances, shown as a number or a bar. The companion's dialogue tone and willingness to share are the only indicators. This is intentional and should not be overridden.

---

## T2-04: The Socket System (Basic — Individual Shard Bonuses)

**When:** Hour 10-15, when the player finds their first socketed Touched item and first Relic Shard
**Who:** A Verdant Flame researcher named Senna (introduced at Hollowford gate in Act I) or Aelira
**Method:** *"You've got a slotted piece there. Relic Shards go in those slots — they add their own effects on top of whatever the item already does. Simple combination. The more interesting thing is what happens when you socket Common items instead — but that's a different conversation."* The researcher offers to show the player the basic socket process. This introduces individual shard bonuses. The Combination system is flagged as "different" — Tier 3 discovery.

---

## T2-05: Trade Routes and the Economy (Basic)

**When:** Hour 12-18, when the player first has enough Crown Marks to consider investment (usually after completing several faction quests)
**Who:** A caravan master named Aldene Whitpath, based in the Hollowford Market Quarter
**Method:** Aldene is visible in the market with a large cart and an invitation to talk. She introduces herself and offers a first route at minimal investment. *"You put in six silver, I take your goods south, I come back with eleven — minus my cut, you see eight. Takes eight days. Want to know more, or shall we just shake hands?"* Players who engage learn more. Players who walk away can return. The game does not prompt them to return.

---

## T2-06: Homestead (Basic Claim)

**When:** Hour 14-20, when the player first passes near one of the four homestead sites (each has a visible "For Claim" marker on approach)
**Who:** A Vanguard land registrar NPC at the nearest settlement
**Method:** The claim marker on the abandoned site is visible without any NPC direction. Players who approach get a contextual prompt: "Unclaimed land — register at the Grainfell Land Office." At the registrar: *"Fifteen silver to file the claim. Land's yours after that. What you do with it is your business. Most people put a roof up first."* If the player asks about building: *"The homestead guide's in the welcome packet. It's not complicated."* A codex entry unlocks covering the basic building options.

---

# SECTION 4: TIER 3 — DEPTH KNOWLEDGE

*Available from hour 1 but discovered through player-initiated exploration. Not explained through NPC dialogue until the player demonstrates awareness of the system.*

---

## T3-01: The Shard Combination System

**When:** Player-discovered; a Reaver fence in the Undercity (Hollowford) has a copy of a partial Shard Combination schema as ambient inventory decoration — visible on their wall, readable if examined
**Discovery path:** Player examines the wall decoration → finds a Firstborn manufacturing schematic → partially translated → it lists a socket sequence (4 shards, specific types, specific order) with a named result: "The Hollow Blade — tested effective against constructs"
**Explanation available:** Maren (if recruited) can explain it if asked after the player finds the schematic: *"Socket those specific shards in that order in a Common item, and something else happens — something the individual shards don't do alone. Reaver network's been trading these schemas for a year. Some of them are actually worth the price."*

---

## T3-02: Convergence Abilities

**When:** Player-discovered; the ability description appears in the skill tree UI when the player reaches Tier 2 in two different attributes simultaneously
**Discovery path:** Player opens the skill tree → sees a new highlighted node they haven't seen before → tooltip reads "Convergence Ability: [Name] — requires [Attribute A] 15 and [Attribute B] 15"
**Explanation available:** No NPC explains this. The system is self-explaining through the UI. The tooltip is sufficient.

---

## T3-03: Crafting Disciplines (Advanced)

**When:** Player-discovered after basic identification and socket use are established
**Discovery path:** The Hollowford general workbench has a "Crafting" tab that is unlocked from hour 1. The basic options (identification, socket insertion) are visible. Advanced crafting (Alchemy, Forgework, Runecarving) requires finding a discipline-specific station in the world. The first stations are in Grainfell (Forgework) and near the Verdant Flame camp (Alchemy).
**Explanation available:** Each discipline station has a craftsperson NPC who offers a first lesson for free.

---

## T3-04: Relic Jury-Rigging (Human Only)

**When:** Player-discovered through encountering a damaged relic in the world (first occurs in the origin sequence for Frontier Settler and Relic Hunter; first occurs around hour 4-6 for humans who took other paths)
**Discovery path:** Damaged relic item in inventory → UI prompt "Attempt jury-rig?" → success or failure result → Echo: *"Hm. I didn't know you could do that. Interesting."*

---

## T3-05: Economy Production Chains

**When:** Player-discovered after establishing their first trade route and basic homestead farm
**Discovery path:** Aldene Whitpath (the caravan master) mentions that her best-paying runs are for processed goods, not raw materials: *"Refined iron ships better than ore. Brewed goods hold value better than grain. Something to think about if you're producing."* This is a hint, not a tutorial. Players who investigate find the production chain mechanics in the homestead Ledger tab.

---

# SECTION 5: MASTER INTRODUCTION TABLE

| System | Tier | Hour Window | Agent | Method |
|---|---|---|---|---|
| Movement and camera | 1 | 1 | Environmental | Discovery |
| Basic combat | 1 | 1–2 | Echo | Authored moment |
| Dodge and blocking | 1 | 1–2 | Echo | Authored moment |
| Stamina | 1 | 1–2 | Echo | Authored moment |
| Relic abilities | 1 | 1–2 | Echo | Origin script |
| Healing/consumables | 1 | 1–3 | Echo | First near-death |
| Item identification | 1 | 2–4 | Merchant NPC | Contextual dialogue |
| Fast travel | 1 | 4–5 | Gate guard | Contextual dialogue |
| Attribute thresholds | 2 | 8–10 | Sergeant Orin | Trainer conversation |
| Faction Fame/Infamy | 2 | 6–8 | Maren/Reaver contact | Post-quest debrief |
| Companion relationship | 2 | 8–12 | Companion | Character moment |
| Socket system (basic) | 2 | 10–15 | Verdant Flame researcher | Item encounter |
| Trade routes | 2 | 12–18 | Aldene Whitpath | Market approach |
| Homestead (basic claim) | 2 | 14–20 | Land registrar | Site approach |
| Shard Combination system | 3 | Any (hint at hour 6+) | Reaver fence display | Environmental discovery |
| Convergence Abilities | 3 | Any (when available) | UI tooltip | Self-revealing |
| Advanced crafting | 3 | Any (after basic) | Discipline NPC | Station discovery |
| Jury-Rigging (Human) | 3 | Origin or 4–6 | Echo reaction | Damaged relic |
| Production chains | 3 | 20+ | Aldene Whitpath hint | Trade conversation |

---

# SECTION 6: SYSTEMS THE ECHO SHOULD NEVER EXPLAIN

The following systems are **deliberately unexplained** — they reward curiosity and experimentation and should not be handed to the player:

- Specific Shard Combination effects and recipes (the player finds schemas, trades for them, experiments)
- Specific ideology sub-score implications within faction tracks (players infer this from NPC dialogue changes)
- Enemy specific weakpoints and patterns (the combat system is designed to teach these through play)
- The full depth of companion relationship states (players observe changes in behavior)
- The Overload system's mastery ceiling (Aetherborn players discover this through experimentation)
- The specifics of what the Echo actually is (this is a narrative mystery — the Echo's teaching function should never reveal its nature prematurely)

**Rule:** If explaining a system would reduce the satisfaction of discovering it, do not explain it.

---

*End of Document SD_18 v1.0*
