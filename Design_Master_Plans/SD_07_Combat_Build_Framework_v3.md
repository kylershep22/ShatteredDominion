# THE SHATTERED DOMINION — COMBAT & BUILD FRAMEWORK
## Document 7 of 10 | Version 3.0 | Depends on: World Bible, Race & Origin System, Loot & Itemization Bible, Faction Playbook

**Revision Notes (v2.0 → v3.0):**
- Intuition attribute removed — back to 6 attributes. Bonuses redistributed into Awareness and Survival. Dialogue checks moved to reputation system.
- Convergence Abilities added: spread builds hitting Tier 2 thresholds in multiple stats unlock exclusive cross-tree abilities unavailable to specialists
- Proficiency Bonus added: at use-rank 25/50/75/100, one free Tier 1 passive auto-unlocks in that skill (does not reintroduce gating — active nodes and higher tiers still require points)
- Weakpoint System revised: combat-mode acquisition flash (3+ consecutive hits briefly shows overlay), Sniper's Patience trigger changed from "completely stationary" to "not been hit for 3 seconds"
- Echo Interface tree expanded: Echo's Wrath offensive node added, defensive reflex passive added (Echo auto-manifests when player is staggered at low HP)
- Zone scaling Act II entry floor adjusted: first 20% of Act II content is level-ranged 25–40, not 20–45

---

# SECTION 1: DESIGN PHILOSOPHY

## 1.1 What "Weighted Action RPG" Means in Practice

Every attack has three phases: **startup** (committed but no damage yet), **active** (damage window), and **recovery** (follow-through — no cancel into dodge or block until complete). This is a **read system**, not a punishment system. Enemies telegraph attacks clearly. The game rewards pattern recognition and timing, not reaction speed alone.

Combat feels deliberate. A well-placed swing matters. A staggered enemy is earned. Players who spam attacks die. Players who read fights win. Recovery duration varies significantly by weapon — a Short Sword recovers in 0.3 seconds; a War Hammer in 1.2 seconds. Choosing a weapon means choosing a rhythm.

## 1.2 Two Progression Systems

**System 1 — Attributes:** Gate access to skill tree tiers. Earn 2 per level-up. Spent across 6 attributes.

**System 2 — Skill Tree Points:** Buy every node — active abilities AND passives alike. Nothing auto-unlocks through attributes. Earn 3 per level-up.

**Use-based growth:** Using a skill improves its effectiveness rank (0–100). This improves output of what the player already has — damage, effect speed, timing windows. It does not unlock new nodes or gate abilities. At use-rank milestones (25/50/75/100), one **Proficiency Bonus** triggers: a single Tier 1 passive in that skill auto-unlocks for free. This bonus applies only to the lowest-cost passive in the tree at each milestone. All active nodes, higher-tier passives, and capstones still require skill tree points. This keeps early-game feel alive without reintroducing gating.

**The Proficiency Bonus is not a gate bypass.** It is a reward for practice that gives players small felt power growth between level-ups, particularly in levels 1–15 where point scarcity is most felt.

## 1.3 Spread Builds — Convergence Abilities

Hard thresholds give partial bonuses below the threshold. A player who spreads 5 points across every stat gets the derived stat benefits linearly — they are never getting zero value, just no unlock. That softens the penalty.

But spread builds now have something more: **Convergence Abilities**. These are exclusive cross-tree abilities that only activate when the player has hit the Tier 2 threshold (or higher) in two or more different stats simultaneously. Specialist builds — by definition — don't spread enough to unlock them. The spread player's breadth is not accidental and compromised. It is an intentional choice with a unique reward.

Convergence Abilities are designed so a specialist cannot access them regardless of level. They require genuine multi-stat commitment. Full catalogue in Section 4.6.

## 1.4 Zone-Locked Enemy Scaling

Enemies do not scale globally. Each zone has a fixed level range. Over-leveling old zones feels powerful — this is intentional and rewarding on replays.

| Act | Zone Level Range | Notes |
|---|---|---|
| Act I — Entry zones | 1–15 | |
| Act I — Deeper zones | 10–25 | |
| Act II — Entry zones | **25–40** | Floor adjusted from v2.0 — prevents difficulty valley for thorough Act I players |
| Act II — Main zones | 30–55 | |
| Act III — Conflict zones, deep ruins | 45–70 | |
| Act IV — Heart approach, endgame | 65–85 | |
| Post-game / Challenge content | 80–100 | |

---

# SECTION 2: THE ATTRIBUTE SYSTEM

Six core attributes. Two points per level-up. Maximum value: 50. **Dialogue checks are no longer stat-gated** — they are governed by the reputation system (faction Fame, racial standing, origin background). Stats do not determine social outcomes. Reputation does.

**Threshold design:** Every threshold gives a full unlock. Below threshold, derived stats scale linearly — the player is never getting zero value from any point spent.

---

## STRENGTH
*"The capacity to impose your will on the physical world."*

**Derived stats:** +1% melee damage per point, +5 carry weight, +3 armor weight tolerance.

| Threshold | Full Unlock |
|---|---|
| **STR 10** | Medium armor without trade-off penalty |
| **STR 15** | Weapon Master Tier 2 nodes purchasable |
| **STR 20** | Heavy armor without trade-off penalty. Two-hand mastery node available. |
| **STR 25** | Warden Tier 2 nodes. Power Attack charge time −20%. |
| **STR 30** | Weapon Master Tier 3 nodes. Cleave hits one additional target. |
| **STR 35** | Warden Tier 3 nodes. Heavy armor movement penalty eliminated. |
| **STR 40** | **Iron Dominance** capstone node: damage bonus becomes +1.5% per point above 40. |
| **STR 50** | **Titan's Frame**: Once per combat, a hit that would stagger you does not. |

---

## AGILITY
*"Speed, precision, and the capacity to be somewhere else when danger arrives."*

**Derived stats:** +0.5% attack speed per point, +0.3% critical strike chance per point (base 5%), dodge distance scales with Agility.

**Ranged scaling:** Agility is the primary stat for **Bow** damage and attack speed. Higher Agility increases draw speed, arrow velocity, and bow critical strike chance.

| Threshold | Full Unlock |
|---|---|
| **AGI 10** | Dodge becomes a full roll. Detection radius reduced. |
| **AGI 15** | Shadow Operative Tier 2 nodes. Dual-wield penalty −15%. |
| **AGI 20** | Stealth kills available. Bow Tier 2 nodes purchasable. |
| **AGI 25** | Shadow Operative Tier 3 nodes. Parry window widened by 20%. |
| **AGI 30** | Dodge can cancel ability recovery frames — the most powerful mobility unlock. |
| **AGI 35** | Critical strike bonus damage +50% on top of base multiplier. |
| **AGI 40** | **Ghost Step** capstone node: movement produces no sound. |
| **AGI 50** | **Phantom**: After a successful dodge, next attack deals +100% damage. 8-second cooldown. |

---

## INTELLIGENCE
*"Understanding of the arcane, the lattice, and the systems that underpin reality."*

**Derived stats:** +1.2% spell damage per point, +8 mana pool per point (base 100), +0.8% relic ability effectiveness per point.

| Threshold | Full Unlock |
|---|---|
| **INT 10** | Spellweaver Tier 2 nodes. Can identify Touched items without scrolls. |
| **INT 15** | Battlemage Tier 2 nodes. Spell-melee combo attacks available. |
| **INT 20** | Spellweaver Tier 3 nodes. Aetherborn Overload window widens. |
| **INT 25** | Corruption Herald Tier 2 nodes. Wild magic events more likely to benefit you. |
| **INT 30** | Spellweaver Tier 3 capstone nodes. Mana regeneration doubles in combat. |
| **INT 35** | Corruption Herald Tier 3 nodes. Can modify Relic Slot Shards without a workbench. |
| **INT 40** | **Arcane Reservoir** capstone: mana pool increases by additional 50% of current total. |
| **INT 50** | **Lattice Sight**: Passively see all hidden Firstborn mechanisms, traps, and enemy weak points without ability activation. |

---

## AWARENESS
*"Combat sharpness — reading threats, spotting weaknesses, placing shots. Reading the world."*

In v3.0, Awareness absorbs the world-exploration bonuses previously held by Intuition. It now governs both combat sharpness and environmental reading — the unifying logic is that Awareness is about what you notice, whether in a fight or moving through the world.

**Derived stats:** +1% ranged accuracy per point, +2m enemy detection range per point (base 8m), +0.4% critical strike chance with ranged weapons per point.

**Crossbow scaling:** Awareness is the secondary stat for Crossbow (primary: Strength). Crossbow accuracy, weakpoint identification, and critical windows all improve with Awareness.

**Weakpoint System:** Awareness directly governs the ranged Weakpoint system (see Section 4.3). Higher Awareness = faster identification, more armor exposure visibility, and larger critical windows.

**World exploration bonuses (absorbed from Intuition):**
- Hidden rooms and concealed doors become faintly detectable through walls (AWA 15 threshold)
- Faction agent NPCs become identifiable in crowds (AWA 20 threshold)
- All enemies in detection radius visible on minimap regardless of line of sight (AWA 30 threshold)
- Rare reagent and material deposit locations highlighted on map within detection range (AWA 35 threshold)

| Threshold | Full Unlock |
|---|---|
| **AWA 10** | Traps visible before triggering. Ambush warning activates (audio/visual cue). |
| **AWA 15** | Crossbow Tier 2 nodes. Enemy weak points visible after 2 seconds of observation. Hidden rooms faintly detectable within 10m. |
| **AWA 20** | Weakpoint System fully unlocked. Headshot critical multiplier activates. Faction agents identifiable in crowds. |
| **AWA 25** | Crossbow Tier 3 nodes. Enemy ability telegraphs shown on HUD before activation. |
| **AWA 30** | All enemies in detection radius on minimap regardless of line of sight. |
| **AWA 35** | Alchemist Tier 3 combat nodes. Ricochet hits additional targets. Rare material deposits highlighted on map. |
| **AWA 40** | **Eagle's Clarity** capstone: critical strike chance with ranged weapons doubles. |
| **AWA 50** | **Sixth Sense**: Cannot be surprised. All stealth attacks against the player converted to normal attacks. |

---

## ENDURANCE
*"The capacity to absorb punishment and keep fighting."*

**Derived stats:** +12 max HP per point (base 100), +6 stamina pool per point (base 100), +0.4% stamina regen per point.

| Threshold | Full Unlock |
|---|---|
| **END 10** | Stagger resistance +20%. Fight at low HP without speed penalty. |
| **END 15** | Warden Tier 2 nodes. Block stamina cost −15%. |
| **END 20** | Second Wind: once per combat, HP drops to 25% → restore 30% max HP automatically. |
| **END 25** | Warden Tier 3 nodes. Stamina regenerates 30% faster in combat. |
| **END 30** | Immunity to standard poison and disease. |
| **END 35** | Cannot be staggered by standard attacks (boss-level impacts only). |
| **END 40** | **Iron Constitution** capstone: HP regenerates 1% per second out of combat, 0.2% in combat. |
| **END 50** | **Unbroken**: HP cannot be reduced below 1 by any single hit. Once per combat. |

---

## SURVIVAL
*"Practical mastery of the living world — crafting, tracking, foraging, and reading the land. Also: finding what others miss."*

In v3.0, Survival absorbs the world-reward bonuses previously held by Intuition. The logic: you find better things because you know the land, read the terrain, and understand how people and creatures move through the world — not because of abstract perception.

**Derived stats:** +1% wilderness crafting potency per point, +0.5 foraging yield per 10 points, animal encounter hostility reduced with Survival investment. **Container loot quality softly scales with Survival** (absorbed from Intuition — higher Survival means you know where to look, and you look in the right places).

| Threshold | Full Unlock |
|---|---|
| **SUR 10** | Alchemy Tier 1 combat recipes. Can identify edible vs. poisonous plants and fungi. |
| **SUR 15** | Animal companions available (passive animals tamed for scouting). |
| **SUR 20** | Alchemy Tier 2 fully unlocked. Wilderness crafting produces Touched-equivalent items. Container loot quality improvement becomes meaningful (noticeable roll improvement). |
| **SUR 25** | Tracking: enemy footprints visible up to 10 minutes after passage. |
| **SUR 30** | Alchemy Tier 3 unlocked. Field-crafted consumables have 40% extended duration. |
| **SUR 35** | Trapper mastery: field traps deal 50% more damage, wider trigger radius. Economic property income improves by 15% (you manage your assets like you manage the land — efficiently). |
| **SUR 40** | **One With the Land** capstone: in natural environments, HP and Stamina regenerate at double rate. Container loot quality improvement becomes significant. |
| **SUR 50** | **Apex Tracker**: all enemy types leave detectable traces. Cannot be tracked by enemies in natural environments. |

---

# SECTION 3: THE SKILL SYSTEM

## 3.1 Architecture Summary

**Attributes:** Gate tier access. 2 per level-up.
**Skill Tree Points:** Buy all nodes (actives and passives). 3 per level-up. Nothing auto-unlocks through attributes.
**Use-rank growth (0–100):** Improves effectiveness of existing abilities. At Rank 25/50/75/100: Proficiency Bonus triggers (1 free Tier 1 passive, automatic, lowest-cost passive in that tree).

## 3.2 Proficiency Bonus — How It Works

When a skill's use-rank reaches 25, 50, 75, or 100:
- The game automatically identifies the lowest-cost Tier 1 passive in that skill's tree that the player has not yet purchased
- That passive is granted for free, with a brief notification ("Your practice with the Broadsword has sharpened your instincts — *Swordsman's Rhythm* unlocked")
- If the player has already purchased all Tier 1 passives through skill tree points, the Proficiency Bonus grants a small flat stat bonus instead (+2% effectiveness with that skill)
- This bonus does **not** apply to Tier 2 or higher nodes, capstones, or active abilities — those remain point-purchased only

Result: A player who exclusively uses daggers for the first 10 levels will have Predator's Instinct and Poison Mastery unlocked through practice before they've spent a single skill tree point. Their point budget goes entirely toward active abilities. Early game feels alive. The system stays clean.

## 3.3 Skill Categories

| Category | Skills |
|---|---|
| **Weapon Skills** | One-Hand Sword, Two-Hand Sword, One-Hand Axe, Two-Hand Axe, One-Hand Blunt, Two-Hand Blunt, Polearms, Bow, Crossbow, Dagger, Thrown, Wand/Staff/Focus, Dual-Wield |
| **Defense Skills** | Block, Dodge, Parry, Heavy Armor, Medium Armor, Light Armor |
| **Magic Skills** | Battlemage, Nature Magic, Shadow Magic (Corruption Herald), Arcane Magic (Spellweaver), Restoration |
| **Relic Skills** | Echo Interface, Lattice Reading, Shard Attunement |
| **Utility Skills** | Stealth, Alchemy (combat), Trapping, Tracking |

---

# SECTION 4: SKILL TREES

## 4.1 Weapon Skill Trees (Selected)

### ONE-HAND SWORD TREE

**Proficiency Bonuses (auto at use-rank milestones):**
- Rank 25: *Swordsman's Rhythm* (passive) — every third consecutive hit deals +20% damage, resets on target switch
- Rank 50: *Keen Edge* (passive) — bleed chance on all one-hand sword attacks +15%
- Rank 75: *Fluid Guard* (passive) — transitioning from block into one-hand sword attack costs no stamina for the first hit
- Rank 100: *Master Swordsman* (passive) — one-hand sword attacks cannot be deflected by enemy guards or constructs

**Tier 1 Nodes** (no attribute gate, 1 point each — actives and additional passives):
- *Pommel Strike* (active): Quick pommel follow-up after any combo. Low damage, high stagger buildup. Cannot be interrupted.
- *Riposte* (active): Within 0.5s of successful block, counter-attack for +60% damage.
- *Sweep* (active): 120-degree horizontal slash hitting all targets in arc.

**Tier 2 Nodes** (STR 15, 1 point each):
- *Lunge* (active): 4m forward dash-attack, +40% damage. Longer recovery.
- *Disarm* (active): On successful Parry, chance to knock enemy weapon free (scales with Agility). Disarmed enemy drops weapon as loot.
- *Whirlwind* (active): 360-degree spin hitting all surrounding enemies. High stamina cost.

**Tier 3 Nodes** (STR 20, 2 points each):
- *Steel Tempest* (active): 5-hit combo (80/90/100/110/130% damage). All five connecting applies guaranteed stagger.
- *Bladestorm* (active): 6 seconds, +30% damage, no recovery frames on attacks. Cannot dodge during. High mana cost.

**Capstone** (STR 25, 3 points, requires 4+ One-Hand Sword nodes purchased):
- *Sword Saint*: All One-Hand Sword abilities −25% stamina cost. Swordsman's Rhythm resets only on target switch, not on taking a hit. Riposte damage +100%.

---

### DAGGER TREE

**Proficiency Bonuses:**
- Rank 25: *Predator's Instinct* — flanking bonus increases from +25% to +40%
- Rank 50: *Poison Mastery* — dagger-applied poison ticks twice as frequently
- Rank 75: *Ghost's Grace* — after a stealth kill, stamina fully restored instantly
- Rank 100: *Phantom Blade* — 15% chance for dagger attacks to ignore all armor and mitigation

**Tier 1 Nodes** (no gate, 1 point each):
- *Hemorrhage* (active): Precise slash with +200% bleed buildup. Slower but devastating DoT.
- *Fan of Knives* (active): Three daggers in a fan, 60% weapon damage each.

**Tier 2 Nodes** (AGI 15, 1 point each):
- *Shadowstep* (active): Teleport 3m behind targeted enemy. Automatically triggers flanking bonus. **Stacking stamina cost: 30/50/75 per sequential use. Resets to 30 on taking a hit.** Cannot be reduced below 20/40/65 even with Capstone investment.
- *Smoke Screen* (active): Deploy smoke bomb (consumes crafted item). 4m cloud, 6 seconds, breaks targeting.

**Tier 3 Nodes** (AGI 25, 2 points each):
- *Marked for Death* (active): Tag enemy. +50% damage for 15s, all attacks count as flanking regardless of position.
- *Death Blossom* (active): Rapid spin, 5 hits on all surrounding enemies at 70% damage. Requires dual-wield.

**Capstone** (AGI 30, 3 points, requires 4+ Dagger nodes):
- *Assassin's Art*: Stealth kill range doubles to 4m. Shadowstep stacking stamina starts at 20 (escalates 20/40/65). Marked for Death duration: 30 seconds.

---

### BOW TREE
*Primary stat: Agility | Secondary stat: Awareness*

**Proficiency Bonuses:**
- Rank 25: *Hunter's Stance* — moving while firing Short Bow or Hunting Bow incurs no accuracy penalty
- Rank 50: *Instinctive Shot* — firing within 0.5s of drawing (no aim hold) grants +20% critical strike chance
- Rank 75: *Marksman's Eye* — holding aim beyond 1.5 seconds grants guaranteed critical strike on release
- Rank 100: *Arrow Whisperer* (passive) — all bow draw times reduced by 25%; quiver can hold two special arrow types simultaneously

**Tier 1 Nodes** (no gate, 1 point each):
- *Rapid Nock* (active): Immediately fire a second arrow after the first without draw animation. 50% damage, extra stamina.
- *Bleed Arrow* (active): Special shot applies heavy bleed regardless of hit location. Does not trigger Weakpoint bonuses — pure DoT.
- *Quiver Mastery* (passive): Can carry special arrow types (Fire, Silence, Scatter). One type at a time.

**Tier 2 Nodes** (AGI 20, AWA 15, 1 point each):
- *Weakpoint Arrow* (active): Aimed shot that applies a 10-second debuff to the targeted weakpoint — all subsequent hits to that zone deal +40% damage.
- *Pinning Shot* (active): Arrow pins target to surface for 2 seconds (hard root, no damage emphasis).

**Tier 3 Nodes** (AGI 30, AWA 20, 2 points each):
- *Rain of Arrows* (active): 5 rapid arrows in spread across a target area, 70% damage each. Area saturation, not precision.
- *Quiver Expansion* (passive): Quiver holds two special arrow types simultaneously, hotkey-switched. Synergizes with Rank 100 Proficiency Bonus.

**Capstone** (AGI 35, AWA 25, 3 points, requires 4+ Bow nodes):
- *Apex Hunter*: Weakpoint Arrow debuff window extends to 20 seconds. Hunter's Stance expands to all bow types. Rain of Arrows arrow count increases to 8.

---

### CROSSBOW TREE
*Primary stat: Strength | Secondary stat: Awareness*

**Proficiency Bonuses:**
- Rank 25: *Bolt Driver* — all crossbow attacks gain +10% armor penetration
- Rank 50: *Steady Aim* — while stationary, headshot critical window widens 30%
- Rank 75: *Reload Efficiency* — reload time reduced by 35%
- Rank 100: *Armor Seeker* — weakpoint identification speed with crossbows doubled; at AWA 20+, instant identification

**Tier 1 Nodes** (no gate, 1 point each):
- *Impact Shot* (active): Charged bolt (+80% damage, staggers target). 1.5 second charge, high stamina.
- *Suppressive Fire* (active): Volley at target area — enemies suppressed (cannot advance, −30% accuracy for 4 seconds).

**Tier 2 Nodes** (STR 15, AWA 15, 1 point each):
- *Penetrating Bolt* (active): Bolt travels through target, hits up to 3 in line (100%/70%/50% damage).
- *Exploit Weakness* (active): After weakpoint identification, mark it — all ranged attacks against that target from any source deal +25% damage for 12 seconds. **Shares bonus with companions** — Kael's hammer benefits too.

**Tier 3 Nodes** (STR 25, AWA 25, 2 points each):
- *Sniper's Patience* (passive): After **not being hit for 3 seconds** (revised from "completely stationary" — allows crouching, cautious movement, position-holding), next shot ignores ALL armor and mitigation. The most powerful single shot in the game. **Fully functional mid-combat** during defensive positioning, not just pre-combat stealth.
- *Siege Bolt* (active): Oversized bolt — deals 200% weapon damage and knocks back target 5m. Single bolt capacity before reload, but the shot is an event.

**Capstone** (STR 30, AWA 30, 3 points, requires 4+ Crossbow nodes):
- *Master Marksman*: Impact Shot charge time halved. Penetrating Bolt secondary/tertiary damage increases to 85%/70%. Exploit Weakness duration doubles to 24 seconds. Sniper's Patience not-hit window reduced to 2 seconds.

---

## 4.2 Defense Skill Trees

### BLOCK TREE

**Proficiency Bonuses:**
- Rank 25: *Steady Guard* — blocking stamina drain −20%
- Rank 50: *Counter Stance* — blocking an attack generates 10% of blocked damage as bonus damage on next attack
- Rank 75: *Iron Wall* — while blocking, incoming elemental damage −25%
- Rank 100: *Immovable* — blocks cannot be broken by standard attacks (only boss-tier smash attacks and magic)

**Tier 1 Nodes** (no gate, 1 point each):
- *Shield Bash* (active): Thrust shield forward — moderate damage, guaranteed 0.8-second stun.
- *Brace* (active): −40% all incoming damage for 2 seconds. Cannot attack or move while Braced.

**Tier 2 Nodes** (END 15, 1 point each):
- *Reflect Projectile* (passive): 30% chance to reflect blocked ranged attack back at attacker for 80% original damage.
- *Guardian's Aura* (passive): Companions within 5m take 15% less damage while you are blocking.

**Tier 3 Nodes** (END 20, 2 points each):
- *Perfect Guard* (active): Block timed within 0.3 seconds of attack landing — consumes no stamina, opens free counter-attack window (next attack +80% damage, 0.5-second window).
- *Fortress* (active): 10 seconds — cannot be moved, knocked back, or staggered. Damage taken −30%. Movement speed: 0. The definitive defensive ability.

**Capstone** (END 25, 3 points, requires 4+ Block nodes):
- *Unbreakable Guard*: Perfect Guard window extends to 0.5 seconds. Guardian's Aura radius doubles. Shield Bash stun doubles to 1.6 seconds.

---

### DODGE TREE

**Proficiency Bonuses:**
- Rank 25: *Fluid Motion* — dodge costs 10% less stamina
- Rank 50: *Evasion* — successful dodge increases movement speed +15% for 3 seconds
- Rank 75: *Ghost's Weave* — dodging through an enemy hitbox deals 20% weapon damage
- Rank 100: *Perfect Evasion* — at or below 25% HP, dodge costs no stamina

**Tier 1 Nodes** (no gate, 1 point each):
- *Combat Roll* (active): Extended dodge, twice the distance, passes through hitboxes.
- *Sidestep* (active): Minimal distance, near-instant recovery. Best in close-range fights.

**Tier 2 Nodes** (AGI 15, 1 point each):
- *Counter-Dodge* (active): Dodge timed within 0.4s of attack landing — next attack +50% damage, briefly slows enemy 30%.
- *Acrobatic Strike* (active): Jump attack clearing obstacles. +30% damage falling more than 2m.

**Tier 3 Nodes** (AGI 25, 2 points each):
- *Phase Dodge* (active): 3 seconds untargetable by standard attacks. High mana cost. (Echo-assisted temporal displacement — narratively significant.)
- *Whiplash* (active): Immediately after a dodge, kinetic burst at nearest enemy for moderate damage. No weapon required.

**Capstone** (AGI 30, 3 points):
- *Untouchable*: Counter-Dodge window extends to 0.6 seconds. Phase Dodge cooldown −40%. Fluid Motion doubles to 20%.

---

## 4.3 The Weakpoint System — Revised

### Core Mechanic

All enemies have body models divided into **Exposure Zones** — logical based on armor type. Weakpoints are not random UI elements; they reflect physical reality.

**Standard identification:** Hold aim on an enemy. After a duration scaled inversely with Awareness (high AWA = faster), the **Weakpoint Overlay** appears as a subtle visual highlight on exposed areas. At AWA 30: instant identification on aim. At AWA 50 (INT 50 threshold): the overlay also shows critical weakpoints — unique one-time discoveries.

**Combat-mode acquisition (new in v3.0):** When the player lands **3 or more consecutive hits** on an enemy without interruption, the Weakpoint Overlay briefly flashes on the target even without holding aim. The flash lasts 1.5 seconds — enough to register a target weakpoint during an active melee-adjacent engagement without requiring the player to stop and aim. High-Awareness players see the flash longer and more clearly. This keeps the Weakpoint System present in fast fights without demanding the player exit the combat rhythm to access it.

### Armor Exposure by Type

| Armor Type | Exposed Areas | Damage Bonus |
|---|---|---|
| **Unarmored** | Entire body | No bonus (already full effectiveness) |
| **Light armor** | Joints (elbows, knees), neck, face, hands | +25% to these areas |
| **Medium armor** | Armpits, inner thighs, neck | +35% |
| **Heavy armor** | Visor slit, back of knee, armpit, groin (if unplated) | +50% |
| **Constructs** | Glowing energy conduits | +100% (the only effective ranged attack path) |

### Headshots

Always deal +75% damage regardless of armor type. Helmeted enemies reduce headshot bonus to +30% (hitting the head through a helm still counts). No helmet: full +75%.

### Critical Weakpoints

Unique to specific enemies — an existing injury, a visible corruption wound, an embedded relic fragment. Never shown on the standard overlay. Discovered only through observation before engagement. Deal massive damage. One-time use per encounter. These are the moments that reward players who read the fight before it starts.

---

## 4.4 Magic Skill Trees

### ARCANE MAGIC (SPELLWEAVER) TREE

**Proficiency Bonuses:**
- Rank 25: *Arcane Affinity* — Lattice-damage spells cost 10% less mana
- Rank 50: *Resonant Casting* — consecutive spell casts (no melee between) increase spell damage by 5% per cast (max 5 stacks)
- Rank 75: *Mana Surge* — when mana drops below 20%, all spell damage +30% until mana regenerates above 50%
- Rank 100: *Lattice Conductor* — Resonant Casting stacks no longer reset on taking damage, only on switching to melee

**Tier 1 Nodes** (no gate, 1 point each):
- *Lattice Bolt* (active): Fast direct arcane projectile. Low mana, reliable damage.
- *Arcane Shield* (active): Mana-powered barrier absorbing set damage. Lasts 10 seconds or until depleted.

**Tier 2 Nodes** (INT 15, 1 point each):
- *Lattice Pulse* (active): AoE arcane burst, knocks back nearby enemies. Melee escape tool.
- *Mana Siphon* (active): Drain mana from magical creatures and lattice constructs. Restores caster mana.

**Tier 3 Nodes** (INT 25, 2 points each):
- *Arcane Storm* (active): 6m radius storm for 8 seconds. Continuous damage. Channeled — player cannot move.
- *Lattice Collapse* (active): Charge 1.5 seconds, then massive damage to all enemies within 5m of target point. Highest single-spell damage in this tree.

**Capstone** (INT 35, 3 points, requires 4+ Spellweaver nodes):
- *Archmage's Domain*: Resonant Casting max stacks increase to 10. Arcane Storm no longer requires channeling (70% damage, fire and forget). Lattice Collapse charge time −50%.

---

### CORRUPTION HERALD TREE — FIXED

**Self-damage loop:** Corruption Drain (baseline passive, no purchase required) returns 1% max HP per corruption stack applied to any enemy. Aggressive play funds the self-damage. A Herald who applies 10 stacks recovers 10% HP from ability costs — net neutral or positive in sustained engagements. Against single targets or fast fights, self-damage still costs.

**Revised HP costs:** Tier 1: 3%. Tier 2: 6%. Tier 3: Void Rift 8%, Cascade 12%.

**Proficiency Bonuses:**
- Rank 25: *Tainted Conduit* — Corruption spell HP costs −15%
- Rank 50: *Corrupted Aura* — Enemies within 3m accumulate 1 corruption stack per second; at 5 stacks they take bonus shadow damage from all sources
- Rank 75: *Void Resonance* — Each corruption spell cast increases next corruption spell damage by 10% (resets after 5s without casting)
- Rank 100: *Abyss Walker* — Immune to environmental corruption damage entirely

**Tier 1 Nodes** (no gate, 1 point each):
- *Corruption Bolt* (active): Shadow damage + 2 stacks. Mana + 3% HP.
- *Void Grasp* (active): Spectral hand, shadow damage + 2s immobilize. Mana only — entry ability.

**Tier 2 Nodes** (INT 20, 1 point each):
- *Corruption Burst* (active): AoE shadow explosion, 3 stacks on all targets. Mana + 6% HP.
- *Consume Weakness* (active): Drain a corruption stack from nearby enemy, convert to HP restoration. Supplementary recovery on top of Corruption Drain passive.

**Tier 3 Nodes** (INT 30, END 20, 2 points each):
- *Void Rift* (active): 6-second rift, constant shadow damage, draws enemies toward it. Mana + 8% HP.
- *Corruption Cascade* (active): Enemy with 5+ stacks explodes — corruption damage to all within 6m radius, 3 stacks each. Chains possible. Mana + 12% HP.

**Capstone** (INT 35, END 25, 3 points, requires 4+ Herald nodes):
- *Herald of the Void*: Corrupted Aura radius doubles to 6m. Corruption Cascade chains once (one chain only — no infinite loops). Tainted Conduit HP reduction combined: 30%. Corruption Drain returns 1.5% HP per stack applied instead of 1%.

---

### NATURE MAGIC (DRUID), RESTORATION, BATTLEMAGE

*Structurally intact from v2.0 with Proficiency Bonus system applied. All auto-unlock passives converted to Proficiency Bonuses at Rank 25/50/75/100. All other nodes require skill tree points. Full tree listings in Skill Tree Appendix.*

---

### ECHO INTERFACE TREE — EXPANDED

The Echo Interface tree now has a genuine offensive identity alongside its defensive and utility roles. Playing an Echo Interface build feels like fighting alongside a partner who shares your body — one who covers your blind spots, responds to your danger, and occasionally acts independently.

**Proficiency Bonuses:**
- Rank 25: *Resonance* — Echo abilities recharge 15% faster
- Rank 50: *Shared Consciousness* — when an Echo ability is active, the player gains the Echo's passive perception — attacker's next strike is briefly telegraphed (faint shimmer 0.5s before the hit)
- Rank 75: *Lattice Sight* — nearby Firstborn inscriptions, hidden mechanisms, and conduit activity become faintly visible without active ability use
- Rank 100: *Full Resonance* — the Echo's fragmented speech becomes fully coherent during combat, providing real-time tactical commentary. Narratively the most significant passive in the game: the player hears Erevos thinking alongside them in every fight.

**Tier 1 Nodes** (no gate, 1 point each):
- *Echo Pulse* (active): Burst of relic energy — Lattice damage to all nearby enemies, brief stagger.
- *Lattice Read* (active): Passive scan highlights all interactive Firstborn objects, hidden doors, and active conduits within 20m for 30 seconds.

**Tier 2 Nodes** (INT 15, 1 point each):
- *Echo Shield* (active): Relic projects a protective barrier for 1.5 seconds (absorbs significant damage). 30-second cooldown — the Echo is exerting itself to protect you. That cost is real.
- *Resonant Strike* (active): Channel weapon attack through the relic — next melee hit deals bonus Lattice damage equal to 50% of physical damage, briefly interrupts construct abilities.
- *Echo's Wrath* (active) **[New in v3.0]**: Direct the Echo to attack independently for 6 seconds. The Echo manifests partially and strikes the nearest enemy autonomously each second, dealing moderate arcane damage. The player and Echo attack simultaneously — not a mirror, not a clone, but a partner acting on their own judgment. The Echo targets differently than the player (prioritizes spellcasters, Constructs, and corrupted enemies). The Echo appears briefly visible during this ability — companions react to it.

**Tier 3 Nodes** (INT 25, 2 points each):
- *Echo Manifestation* (active): Echo partially materializes as a spectral duplicate for 8 seconds, mirroring the player's attacks at 60% damage. The Echo appears visibly distressed by full manifestation — companion dialogue acknowledges this.
- *Echo's Reflex* (passive) **[New in v3.0]**: When the player is staggered while at or below 35% HP, the Echo automatically manifests for 3 seconds to cover them — attacking the staggering enemy and drawing its attention. No cost, no activation — it happens because the Echo is protecting the player. This is not a tool. It is a relationship. First time this triggers, the Echo says something. What it says depends on how the player has treated the Echo throughout the game.
- *Lattice Surge* (active): Massive burst of lattice energy — heavy damage to all enemies in 10m radius. After use, the relic goes silent for 30 seconds. The Echo doesn't speak. Only static. The silence is intentional and unsettling.

**Capstone** (INT 30, 3 points, requires 4+ Echo Interface nodes):
- *Voice of the Architect*: Echo Manifestation lasts 16 seconds. Lattice Surge cooldown reduced to 20 seconds. Echo Shield cooldown reduced to 15 seconds. Echo's Wrath duration extended to 10 seconds. When Erevos speaks during Echo abilities at Full Resonance rank, their words are relevant to the specific situation — combat, location, or the player's recent choices. This is the most expensive per-ability narrative scripting in the game and should be flagged as such.

---

## 4.5 Build Archetypes

| Archetype | Primary Attributes | Signature Abilities |
|---|---|---|
| **Weapon Master** | STR 30+, END 20+ | Titan's Blow, Steel Tempest, Fortress |
| **Spellweaver** | INT 35+, AWA 15+ | Arcane Storm, Lattice Collapse, Phase Dodge |
| **Battlemage** | INT 20+, STR 20+ | Bladestorm, Resonant Strike, Lattice Pulse |
| **Shadow Operative** | AGI 30+, AWA 20+ | Shadowstep, Marked for Death, Death Blossom |
| **Corruption Herald** | INT 30+, END 25+ | Corruption Cascade, Void Rift, Herald of the Void |
| **Warden** | STR 30+, END 30+ | Fortress, Unbreakable, War Cry |
| **Mobile Archer** | AGI 30+, AWA 20+ | Arrow Whisperer, Pinning Shot, Weakpoint Arrow |
| **Precision Marksman** | AWA 30+, STR 20+ | Master Marksman, Sniper's Patience, Exploit Weakness |
| **Druid** | INT 25+, SUR 25+ | Grove Sentinel, Verdant Surge, Nature's Mending |
| **Echo Channeler** | INT 30+, END 20+ | Echo's Wrath, Echo Manifestation, Voice of the Architect |

---

## 4.6 CONVERGENCE ABILITIES

Convergence Abilities are the spread player's exclusive toolkit. They activate only when the player has reached the Tier 2 threshold (or higher) in **two or more different stats simultaneously**. Specialist builds — by definition investing deeply in one or two stats — will not have spread enough to access them. These are not consolation prizes. They are a distinct archetype with abilities that cannot be replicated through any single-path investment.

**How they work:** Convergence Abilities appear as a separate node category in the skill tree UI — visible but grayed out until both required thresholds are met. They cost skill tree points like any other node (1–2 points each). Once both thresholds are hit, the node becomes purchasable. The player must still buy them — they do not auto-unlock. Meeting the threshold is the gate; the point is the commitment.

---

**RUNIC BLADE**
*Requires: STR 15 (Tier 2) + INT 15 (Tier 2)*
*Cost: 1 skill tree point*

Infuse your equipped weapon with lattice energy on demand. For 10 seconds, all melee attacks deal bonus Lattice damage equal to 30% of physical damage dealt. Recharge: 30 seconds. This is not a spell — it is a weapon enhancement. A Weapon Master who invested only in STR never touched INT 15. A pure Spellweaver who invested only in INT never touched STR 15. Only the player who did both gets this.

The fantasy: the warrior who knows more than warriors are supposed to know.

---

**SWIFT READING**
*Requires: AGI 15 (Tier 2) + INT 15 (Tier 2)*
*Cost: 1 skill tree point*

While in stealth, automatically identify enemy weakpoints without holding aim. The overlay appears instantly on any enemy within detection range when crouching. No Awareness investment required for the identification itself — this is instinct, not patience. A pure Shadow Operative at AGI 30 but minimal INT never gets this. A pure Spellweaver at INT 30 but minimal AGI never gets this. The agile magic-user who moves through shadows with arcane insight gets it.

The fantasy: the infiltrator who reads every room before they enter it.

---

**IRONHIDE DODGE**
*Requires: STR 15 (Tier 2) + END 15 (Tier 2)*
*Cost: 2 skill tree points*

After a successful dodge while wearing Medium or Heavy armor (at least 3 armor slots filled with Medium or Heavy pieces), the next hit the player receives deals 0 damage. The armor's momentum, carried through the dodge, absorbs the impact. Cooldown: 20 seconds. This enables a heavy-armor-dodge build identity that should not exist by conventional RPG logic — and that is precisely why it is a Convergence Ability. A Warden (STR 30+, END 30+) invested too deeply to also invest in AGI 15 for full dodge capability. A dodge specialist (AGI 30+) does not wear heavy armor. The spread player who touches both unlocks this specific hybrid moment.

The fantasy: the armored fighter who hits you wearing a juggernaut's armor and ghosts out of your counter like they aren't wearing it.

---

**VOID CONDUIT**
*Requires: INT 20 (Tier 3) + END 20 (Tier 2)*
*Cost: 2 skill tree points*

Corruption Herald abilities cost no HP for 8 seconds after the player falls below 40% HP. The body's survival instinct suppresses the self-damage mechanism — the corruption flows outward without cost because there is nothing left to protect. Recharge: 60 seconds. This ability is designed for the near-death power spike fantasy. It requires INT 20 to access Spellweaver Tier 3 AND END 20 for Warden Tier 2 — a player who invested in both survivability and magic chaos. A pure Corruption Herald (INT 30+ but minimal END) hits the INT requirement but not END 20.

The fantasy: the moment you should die being the moment you become the most dangerous thing in the room.

---

**BLOOD AND STONE**
*Requires: STR 20 (Tier 3) + AWA 20 (Tier 2)*
*Cost: 2 skill tree points*

While wielding a two-handed weapon, enemy weakpoints are highlighted by the combat-mode acquisition flash (see Section 4.3) after only **1 hit** instead of 3. The physical intuition of heavy weapons — understanding where force lands, where armor gives — creates a combat awareness that replaces the patience of a ranged Marksman. A pure Weapon Master (STR 30+) rarely invested AWA to 20. A pure Marksman (AWA 30+) does not use two-handed weapons. The heavy melee fighter who studied their targets gets this.

The fantasy: the berserker who hits precisely because they understand exactly where the armor ends.

---

**LATTICE GHOST**
*Requires: AGI 20 (Tier 3) + INT 15 (Tier 2)*
*Cost: 2 skill tree points*

Phase Dodge (the Dodge Tier 3 ability requiring AGI 25 to access normally) can be triggered without the AGI 25 requirement — but only by spending both Stamina AND Mana simultaneously (30 Stamina + 30 Mana per use). The player trades resource economy for capability above their attribute investment. A pure Shadow Operative investing toward AGI 25 can just wait for the threshold — they don't need this. A player who spread toward magic and agility but never reached AGI 25 gets a harder version of the same capability.

The fantasy: the magic-touched rogue who can slip between moments at the cost of burning both their physical and arcane reserves.

---

# SECTION 5: RESOURCE MANAGEMENT

## 5.1 Stamina

**Pool:** Base 100. +6 per Endurance point. Practical maximum: ~340.

**Costs:**
- Standard attacks: 8–20 (Short Sword 8, War Hammer 20, scales by weapon weight)
- Power attacks: 25–50
- Dodge: 15–25 (inversely scales with Agility)
- Block held: 5 per second
- Sprint: 10 per second
- Shadowstep: 30/50/75 stacking (resets on taking a hit; Capstone starts at 20/40/65)
- Bow draw hold: 5 per second (incentivizes firing, punishes indefinite hold)

**Regeneration:**
- Out of combat: Full regen in 4 seconds
- In combat, not attacking: 15 per second
- Blocking: 5 per second
- Actively attacking: 0

**Depletion consequences:** −40% damage, dodge becomes a stumble, blocks can be broken through. The player is visibly exhausted — animation changes.

## 5.2 Mana

**Pool:** Base 100. +8 per Intelligence point. Practical maximum: ~420.

**Costs:**
- Tier 1 spells: 15–25
- Tier 2 spells: 30–50
- Tier 3 spells: 60–100
- Echo abilities: 20–80

**Regeneration:**
- Out of combat: Full regen in 6 seconds
- In combat: 8 per second baseline, scales with Intelligence

**Depletion consequences:** No spells or Echo abilities. Pure physical combat only.

---

# SECTION 6: CORE COMBAT MECHANICS

*Attack framework (startup/active/recovery), stagger system, block, parry, dodge, and stealth are unchanged from v2.0. See Section 6 of v2.0 for full descriptions.*

Key rules:
- All attacks have startup/active/recovery. No mid-recovery cancelling.
- Stagger builds on enemies; depletes over time if pressure stops.
- Block drains stamina; guard breaks at 0 stamina.
- Parry window: 0.3 seconds (0.5 with Parry investment). Staggers attacker, opens counter.
- Dodge: directional, invincibility frames in first 0.3 seconds.
- Stealth: two-stage detection (Suspicion → Detection). Stealth kills at AGI 20.

---

# SECTION 7: ENEMY CATEGORIES

*All six enemy categories from v2.0 are retained with full rosters: Corrupted, Undead, Faction Enemies, Firstborn Constructs, Wildlands Creatures, Arcane Anomalies.*

**One addition:** The **Corrupted post-death burst** (30% chance on Corrupted enemy death to release a small AoE explosion) is explicitly retained and flagged as a core behavioral feature. Players learn to fight away from their kills. This creates natural kinetic flow to engagements that changes how players navigate post-combat cleanup. Do not remove this in implementation QA without design discussion.

*Full enemy rosters, behavioral profiles, and faction enemy sub-profiles from v2.0 Section 7 remain authoritative.*

---

# SECTION 8: THE RESPEC SYSTEM

**Voss and the Unmade Path** questline are unchanged from v2.0.

**What resets:**
- All attribute points (fully returned, default)
- All skill tree points (fully returned, default)
- Skill use-rank: **opt-in only, additional cost** — a player who has practiced daggers for 40 hours is not forced to re-grind that practice. If they want to unlearn it, that option exists at extra cost.
- Proficiency Bonuses: if skill use-rank is reset, the Proficiency Bonus auto-unlocks associated with that rank reset too.

**Respec costs:** Unchanged from v2.0. First respec: accessible (Silverite Ingots + Wellspring Concentrate). Repeated respecs escalate.

---

# SECTION 9: RACE-SPECIFIC COMBAT SYSTEMS

*Human Jury-Rigging, Vaelari Wellspring Communion, and Aetherborn Overload are unchanged from v2.0.*

**Convergence Ability interaction with race systems:**

- **Aetherborn + Runic Blade**: The Overload Meter accelerates while Runic Blade is active — the lattice infusion excites the Overload system. High-risk, extremely high-reward combination.
- **Vaelari + Swift Reading**: In natural environments with high Communion, Swift Reading weakpoint identification range extends beyond stealth (activates within 8m of any enemy, not just those the player is directly approaching). The most potent combination for Vaelari stealth builds.
- **Human + Blood and Stone**: The Human's Relic Jury-Rigging bonus applies to the combat-mode weakpoint flash — successfully jury-rigging a relic mid-combat triggers a full 3-second Weakpoint Overlay on all enemies in range (not just the current target).

---

# SECTION 10: COMPANION COMBAT INTEGRATION

*AI presets, direct command system, and synergy abilities unchanged from v2.0.*

**Convergence Ability companions note:** Companions do not use Convergence Abilities — they are player-exclusive. However, Maren and Kael have ambient dialogue lines that react if they see the player use specific Convergence Abilities:

- Maren on *Swift Reading*: "You see the gaps before the fight starts. That's actually impressive."
- Kael on *Ironhide Dodge*: He says nothing. He just watches. Later, at camp, he asks to spar.
- Aelira on *Runic Blade*: Her reaction depends on the player's ideology track with the Verdant Flame.

---

# SECTION 11: IMPLEMENTATION CHECKLIST

**From v3.0 revisions:**
- [ ] Intuition attribute removed from all systems
- [ ] Awareness updated to include world-exploration bonuses (hidden rooms, faction agent ID, material deposits)
- [ ] Survival updated to include loot quality scaling and trade outcome bonuses
- [ ] All dialogue skill checks removed from attribute system — confirmed as reputation system outputs
- [ ] 6-attribute total confirmed and attribute allocation math recalibrated (200 points across 6 stats)
- [ ] Convergence Abilities system implemented (6 abilities at launch, expandable)
- [ ] Convergence Ability unlock conditions implemented (dual-threshold detection logic)
- [ ] Convergence Ability UI implemented (visible but grayed until both thresholds met)
- [ ] Proficiency Bonus system implemented (use-rank 25/50/75/100 → auto Tier 1 passive)
- [ ] Proficiency Bonus fallback implemented (flat bonus if all Tier 1 passives already purchased)
- [ ] Weakpoint System: combat-mode acquisition flash implemented (3+ consecutive hits → 1.5s overlay)
- [ ] Sniper's Patience trigger changed from "stationary" to "not been hit for 3 seconds"
- [ ] Echo's Wrath node implemented (6-second autonomous Echo attack)
- [ ] Echo's Reflex passive implemented (auto-manifest on stagger at ≤35% HP)
- [ ] Echo's Reflex dialogue written (content depends on player's Echo relationship history — 5+ variations)
- [ ] Act II entry zone floor confirmed at level 25–40 (not 20–45)
- [ ] Corrupted post-death burst confirmed and flagged as non-removable behavior

**From v2.0 (carried forward, confirm implementation):**
- [ ] All weapon/defense/magic/relic/utility skill trees implemented with Proficiency Bonuses replacing auto-unlock passives
- [ ] All attribute thresholds implemented (8 per attribute, 48 total)
- [ ] Partial bonus below threshold implemented (linear derived stats at all investment levels)
- [ ] Zone-locked enemy scaling implemented per Act level ranges
- [ ] All 6 enemy categories with full rosters implemented
- [ ] Corruption Herald: Corruption Drain passive implemented, revised HP costs confirmed
- [ ] Shadowstep stacking stamina cost implemented (30/50/75, resets on hit)
- [ ] Zone-locked Act II floor adjustment confirmed (25–40 entry zones)
- [ ] Voss respec system with optional skill rank reset implemented
