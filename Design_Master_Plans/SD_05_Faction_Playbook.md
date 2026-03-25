# THE SHATTERED DOMINION — FACTION PLAYBOOK
## Document 5 of 10 | Version 1.0 | Depends on: World Bible & Lore Foundation, Race & Origin System, Main Story Arc, Companion Design

**Purpose:** This document defines the mechanical architecture of the faction system — how reputation is tracked, how affiliation evolves across the game's three acts, how faction conflict reshapes the world state, and how the economic layer integrates with political standing. Every other document that references faction interaction, merchant access, quest availability, or world state variables defers to this one.

**Design Reference:** Flexible affiliation early, forced alignment late (Fallout: New Vegas model). Independent Fame/Infamy tracking per faction (The Outer Worlds model). World state changes activate in Act II/III escalation. Economic system operates as a parallel mini-game with deep faction entanglement.

---

# SECTION 1: DESIGN PHILOSOPHY

## 1.1 Core Principles

**Factions are political entities, not quest dispensers.** Each faction has goals, internal tensions, and limited resources. They are not waiting for the player — they are actively pursuing their agendas in the world regardless of player involvement. The player's choices determine whether they become assets, liabilities, or enemies to each faction.

**Reputation is earned and lost through behavior, not checklist completion.** The system tracks *what* the player did and *how*, not just whether a quest was completed. A player who completes a Vanguard mission by bribing the captain builds a different reputation than one who follows orders to the letter — and the faction reacts accordingly.

**The economic system is not optional flavor.** Trade routes, property ownership, and production chains are mechanical systems that intersect with faction power. A player who owns a warehouse in a district that falls under Reaver control faces real consequences. This is intentional — it gives the player *stakes* before the forced alignment in Act III, not just opinions.

**No faction is the hero faction.** The reward model is calibrated so that committing to any single faction is mechanically viable at the cost of specific trade-offs. There is no objectively optimal faction. Players who try to stay neutral past the Act III trigger will be penalized — neutrality is a position the world will not allow forever.

## 1.2 The Four Major Factions at a Glance

| Faction | Core Want | Method | Economic Strength | Economic Weakness |
|---|---|---|---|---|
| Ironbound Vanguard | Control the lattice permanently | Military authority, information suppression | Stable trade routes, low tariffs within garrison zones | High taxation, limited black market access |
| Circle of Verdant Flame | Manage the lattice's decline gracefully | Research, corruption purification, advocacy | Rare reagents, purified land, Wellspring-adjacent goods | No military production, poor luxury access |
| Ashmar Reavers | Exploit the transition for maximum gain | Intelligence, black markets, relic trafficking | Highest profit margins, unrestricted goods, relic economy | Unstable routes, extortion risk, no legal protection |
| House of the Hollow Crown | Restore the Dominion under Eltaryn authority | Political manipulation, archive knowledge, legitimacy claims | Archive access, noble luxury economy, political leverage | No military force, economically dependent on others |

---

# SECTION 2: THE FAME/INFAMY REPUTATION SYSTEM

## 2.1 Architecture

Each of the four major factions tracks two independent values for the player:

- **Fame** — How respected, trusted, and valued you are within the faction. Earned through completing quests that advance their goals, making choices aligned with their ideology, and protecting their people or assets.
- **Infamy** — How feared, resented, or dangerous you are perceived to be by the faction. Earned through opposing their operations, harming their members, exposing their secrets, or acting against their interests — even in service of another faction.

**These are not opposites.** A player can have high Fame *and* high Infamy with the same faction simultaneously. This produces the most nuanced standing states and the most interesting NPC reactions.

**Example — High Fame / High Infamy with the Vanguard:**
The player has saved Vanguard soldiers, shared intelligence, and helped suppress a riot — but also exposed a corrupt officer, freed prisoners from an illegal detention camp, and publicly contradicted Commander Hale's account of a massacre. Vanguard soldiers respect your effectiveness. Command despises your independence. Merchants give you discounts. Guards watch you carefully. Captain Kael asks you to stop making his job harder.

## 2.2 Standing States (Fame/Infamy Combinations)

Each faction has six readable standing states, determined by the relative levels of Fame and Infamy:

| State | Fame | Infamy | Faction Behavior |
|---|---|---|---|
| **Unknown** | Low | Low | Default. Neutral interaction. No special treatment. |
| **Trusted** | High | Low | Warmly received. Best prices. Quest access. Safe passage. |
| **Notorious** | Low | High | Hostile on sight in faction-controlled zones. Bounty possible. |
| **Controversial** | High | High | Mixed reactions. Some NPCs respect you, others are hostile. Unique dialogue. Access is unpredictable. |
| **Indispensable** | Very High | Low | Deep alignment. Faction perks unlock. Inner circle access. |
| **Dangerous Asset** | Very High | High | Faction uses you but doesn't trust you. High-risk, high-reward quest access. They may betray you. |

## 2.3 How Reputation Changes

**Direct actions (primary driver):**
- Completing faction quests: +Fame with that faction, variable Infamy with opposing factions
- Failing or betraying faction quests: +Infamy with that faction
- Observed behavior in faction-controlled zones: Guards, merchants, and civilians report to faction leadership
- Combat — who you fight and who you protect matters

**Ideological alignment (secondary driver):**
- Dialogue choices that reflect a faction's core philosophy earn Fame even without quest completion
- Choices that contradict their ideology add Infamy even when completing their quests
- Example: Completing a Vanguard mission by executing prisoners earns Fame with hardliners but Infamy with moderates — both tracked internally, expressed as a hidden ideology sub-score (see Section 2.4)

**Faction-to-faction bleed:**
- High Fame with the Reavers passively generates Infamy with the Vanguard over time (association guilt)
- High Fame with the Verdant Flame generates Infamy with the Hollow Crown (competing lore authority)
- The bleed rate accelerates in Act II when faction tensions become overt

## 2.4 The Ideology Sub-Score (Hidden)

Within each faction's Fame track, a hidden secondary variable tracks *how* the player built their reputation. This is not visible to the player directly but shapes faction NPC dialogue, inner-circle access, and which faction ending is available.

**Vanguard Ideology Score:**
- Order track: Built through following protocol, supporting martial law, prioritizing security
- Reform track: Built through protecting civilians, opposing corruption, supporting Kael's moderate position
- High Order: Commander Hale trusts you. Hardliner missions unlock. Brutal efficiency rewarded.
- High Reform: Kael advocates for you. Moderate officers open up. Some hardliner missions locked.

**Verdant Flame Ideology Score:**
- Preservation track: Built through purification work, protecting the Wellspring, managing decline patiently
- Radical track: Built through aggressive anti-civilization choices, supporting the faction's extremist wing
- High Preservation: Elder Thorn's inner circle. Diplomatic outcomes available. Aelira's trust.
- High Radical: Radical missions unlock. Some of the most destructive game outcomes available through this path.

**Reaver Ideology Score:**
- Opportunist track: Built through profit-driven choices, relic trafficking, pure pragmatism
- Idealist track: Built through protecting vulnerable people, Robin Hood-style operations, Varek's philosophical side
- High Opportunist: Varek's full operation network. Highest economic rewards. Morally dark.
- High Idealist: Access to Varek's rare honest moments. Alternative Reaver ending where the network becomes something better.

**Hollow Crown Ideology Score:**
- Loyalist track: Built through supporting Dominion restoration, accepting Eltaryn authority claims
- Truth track: Built through exposing Firstborn lore that contradicts divine right claims, pushing Seraphine toward honesty
- High Loyalist: Traditional Hollow Crown ending (restoration attempt, likely catastrophic).
- High Truth: Seraphine's redemption arc unlocks. Requires sustained investment.

---

# SECTION 3: THE AFFILIATION MODEL — THREE-ACT STRUCTURE

## 3.1 Act I: Open Field (No Affiliation)

**Duration:** Approximately the first 15–20 hours of play.

The player has no formal affiliation. All four factions are aware of the player's existence and are actively courting them — they know a relic-marked individual is significant, even if they don't fully understand why.

**Mechanical state:**
- All faction quests available
- No Fame/Infamy penalties for working with multiple factions simultaneously
- Factions are suspicious of each other but not openly hostile
- Economic system is available from the beginning — players can begin establishing trade routes and property

**Narrative framing:**
Each faction makes their pitch in Act I. The Vanguard through Kael (order, protection, purpose). The Verdant Flame through Aelira (understanding, responsibility, the truth about the lattice). The Reavers through Maren (survival, honesty about power, pragmatism). The Hollow Crown through Seraphine (knowledge, legitimacy, the weight of history).

The player is not choosing yet. They are listening.

## 3.2 Act II: Rising Tensions (Shadow Affiliation)

**Duration:** Middle act, roughly 20–35 hours in.

A significant crisis event — the Ashenveil Archive revelation — becomes public in different, distorted forms across the factions simultaneously. Each faction interprets the same information according to their ideology. The Vanguard treats it as a security threat. The Verdant Flame treats it as confirmation of their position. The Reavers treat it as the most valuable intelligence in history. The Hollow Crown sees their narrative either confirmed or threatened depending on which version reaches them first.

**Mechanical state:**
- Faction conflict becomes overt — joint operations are now politically costly
- Completing a quest for one faction generates a small automatic Infamy gain with its rivals (the bleed activates)
- Factions begin offering "shadow" alignment quests — deeper operations that hint at inner-circle access but aren't publicly attributable
- World state changes begin: faction-controlled zones start developing distinct characteristics
- Economic consequences become visible: trade routes through contested areas become more expensive and dangerous

**The Shadow Affiliation prompt:**
Late in Act II, each faction privately asks the player to make a choice — not a public declaration of alignment, but a shadow commitment. Accept one shadow alignment, and the inner circle opens. Accept none, and you remain a free agent — but at the cost of the deepest faction content and some economic protections.

Players can shadow-align with only one faction. This is the first real narrowing.

## 3.3 Act III: The Forced Alignment (Hard Choice)

**Trigger:** The Convergence — a faction-precipitated crisis where all four factions make simultaneous moves toward their endgame goals. The Vanguard attempts to seize the primary lattice node. The Verdant Flame activates a purification ritual that will accelerate the lattice's decline. The Reavers detonate a stolen storm engine fragment to destroy a rival faction's stronghold. The Hollow Crown broadcasts their claim to the Scepter and calls for popular support.

The world cannot absorb all four moves simultaneously. Something breaks. The player must choose a side.

**Mechanical consequences of alignment:**
- Chosen faction: Full inner-circle access, highest-tier rewards, faction ending available
- One rival faction: Standing can be partially preserved if ideology tracks align (e.g., a Reform-Vanguard player choosing the Verdant Flame won't be instantly hostile to moderate Vanguard officers)
- Two rival factions: Hostile to you. Bounties. Closed quest lines. Economic assets in their territory at risk.
- One faction (the most ideologically opposite): At war with you. Their forces are active enemies in the world.

**What cannot be undone:**
- The Act III alignment cannot be reversed
- Certain companions will leave based on your choice (see Companion Design Document for specific triggers)
- Economic assets in hostile faction territory are frozen, seized, or destroyed depending on how the conflict plays out

**The Fifth Option:**
Players who have built sufficient Fame with *all four* factions and completed at least one inner-circle quest for each are offered a fifth path: the Unaligned Gambit. This requires negotiating a temporary ceasefire between all four factions, forcing them to cooperate on the lattice crisis. It is mechanically the hardest path, narratively the most complex, and produces a unique ending unavailable through any single faction alignment. It is also unstable — two of the four factions will break the ceasefire by the endgame, and the player must manage the fallout.

---

# SECTION 4: THE FOUR FACTIONS — MECHANICAL PROFILES

## 4.1 Ironbound Vanguard

### Reputation Tiers (Fame)

| Tier | Name | Threshold | Unlocks |
|---|---|---|---|
| 0 | Unknown | Default | Basic guard neutrality |
| 1 | Recognized | 15 Fame | Reduced checkpoint friction, basic Vanguard merchants |
| 2 | Auxiliary | 35 Fame | Auxiliary designation, access to garrison quartermaster (Tier 1 gear) |
| 3 | Field Asset | 55 Fame | Full garrison access, Tier 2 gear, tactical briefings |
| 4 | Trusted Operative | 75 Fame | Commander Hale meeting, inner circle access, Tier 3 gear |
| 5 | Vanguard Sanctioned | 95 Fame | Vanguard endorsement (public reputation effect), highest-tier armory |

### Infamy Effects

| Infamy Level | Effect |
|---|---|
| Low | No effect |
| Medium | Additional scrutiny at checkpoints. Some guards ask for identification. |
| High | Detention risk at checkpoints. Warrants possible. Some missions closed. |
| Very High | Arrest on sight in garrison zones. Bounty active. Kael may be ordered to bring you in. |

### Faction Perks (Unlocked by Fame Tier)

- **Tier 2 — Military Training:** Access to Vanguard combat drills. Unlocks the Shield Wall and Suppressive Fire ability branches in the Combat Framework. +10% physical damage mitigation.
- **Tier 3 — Intelligence Network:** Access to Vanguard surveillance reports. Enemies in scouted areas are marked on the map. Can request patrol support for owned territory (economic protection — see Section 6).
- **Tier 4 — Garrison Authority:** Can deputize NPCs, issue warrants, and access sealed Vanguard archives. Unlocks Vanguard-aligned endings.
- **Tier 5 — Command Clearance:** Full access to Commander Hale's strategic plans. Vanguard forces defend player-owned property in their territory at no cost. Vanguard merchant prices at 15% below base.

### Faction Quests (Overview — Full quest designs in Severant Vale Region Guide)

**Act I:**
- *The Deserter Problem* — Track and retrieve (or protect) a Vanguard deserter who knows too much
- *Magic Suppression* — Assist in shutting down an unsanctioned Vaelari healing circle; choices determine how
- *Border Integrity* — Investigate corruption in the Drakeling refugee processing operation

**Act II:**
- *The Commander's Bargain* — Hale asks the player to surveil the Verdant Flame camp; what you report and what you omit shapes both faction standings
- *Archive Security* — Prevent the Hollow Crown from accessing Vanguard-seized Firstborn data
- *The Hollow Men* — Investigate Vanguard soldiers who've gone silent in a corruption zone — the truth implicates command

**Act III (Shadow/Inner Circle):**
- *Iron Protocol* — Assist in the seizure of the primary lattice node (or sabotage it)
- *The Purge Order* — Hale orders the arrest of all Verdant Flame operatives in Hollowford; how the player executes this (or refuses) determines the Reform/Order ideology split

### Economic Role
Vanguard-controlled zones have the most stable trade routes and lowest base tariffs. However, Vanguard taxation on goods produced in their territory is the highest of any faction. Best for players who want security over profit margins. Their garrison quartermaster is the primary source of military-grade equipment outside of crafting.

---

## 4.2 Circle of Verdant Flame

### Reputation Tiers (Fame)

| Tier | Name | Threshold | Unlocks |
|---|---|---|---|
| 0 | Unknown | Default | Basic neutrality at grove camp |
| 1 | Observer | 15 Fame | Verdant Flame scholars will speak openly. Basic reagent merchant. |
| 2 | Field Researcher | 35 Fame | Access to corruption purification side quests. Reagent Tier 2. Wellspring maps. |
| 3 | Circle Ally | 55 Fame | Elder Thorn meeting. Purification abilities unlock. Vaelari community trust increases. |
| 4 | Seer-Friend | 75 Fame | Aelira's personal quest unlocks fully. Inner archive access. Rare reagent merchant. |
| 5 | Voice of the Grove | 95 Fame | Verdant Flame public endorsement. Corruption zones partially passable. Highest reagent tier. |

### Infamy Effects

| Infamy Level | Effect |
|---|---|
| Low | No effect |
| Medium | Vaelari NPCs become cold. Some quests gated. Aelira becomes professionally distant. |
| High | Verdant Flame rangers are hostile. Vaelari community merchants close. |
| Very High | Branded as a desecrator. Active hostility in Wellspring-adjacent zones. Elder Thorn issues a formal warning to other factions. |

### Faction Perks (Unlocked by Fame Tier)

- **Tier 2 — Corruption Reading:** Can identify corruption zone intensity and safe paths through them on the minimap. Unlocks Purification Salve crafting recipe.
- **Tier 3 — Lattice Attunement:** Relic abilities have 10% reduced cooldown. Wellspring proximity generates passive relic charge. Unlocks the Natural Conduit ability branch.
- **Tier 4 — Grove Sanctuary:** Safe houses at Verdant Flame camps. Enemies will not pursue into marked grove territory. Aelira relationship unlocks deepen.
- **Tier 5 — Elder's Blessing:** All nature and lattice abilities at 15% increased effectiveness. Corruption zones within purified Verdant Flame territory deal no passive damage to the player.

### Faction Quests (Overview)

**Act I:**
- *The Pulse Readings* — Help Aelira map a destabilizing lattice node before it ruptures
- *The Radical's Fire* — A Verdant Flame extremist has begun burning farms near the border; stop them or not — and how you handle it shapes the Circle's internal dynamics
- *Greenwatch Crisis* — The Vaelari refugee camp (Greenwatch) faces a Thornwalker raid; the Circle wants protection without Vanguard involvement

**Act II:**
- *The Archive Truth* — Aelira has decoded Firstborn records that contradict both Vanguard and Hollow Crown narratives; decide who else learns this
- *Wellspring Contamination* — A lattice node is being deliberately overloaded; tracing the source implicates a surprising party
- *The Long Goodbye* — Elder Thorn proposes a managed lattice decommissioning timeline; getting other factions to sign on (or preventing them from sabotaging it) is the task

**Act III (Shadow/Inner Circle):**
- *The Purification Protocol* — The Circle activates their great ritual; the player chooses whether to accelerate it, modify it, or undermine it
- *Aelira's Final Argument* — Whether Aelira succeeds or fractures depends on the player's ideological track with the Circle

### Economic Role
Verdant Flame territory produces the rarest crafting materials in the game — reagents for advanced lattice-based abilities, purification components, and unique consumables unavailable elsewhere. Their merchants have the best stock for mage and relic-focused builds. However, they produce no weapons or armor and have no military infrastructure. Establishing a trade route through Verdant Flame territory is high-value but requires maintained standing — they will sever access if the player's Infamy rises.

---

## 4.3 Ashmar Reavers

### Reputation Tiers (Fame)

| Tier | Name | Threshold | Unlocks |
|---|---|---|---|
| 0 | Unknown | Default | Ignored or watched in Undercity |
| 1 | Known Face | 15 Fame | Black market vendors accessible. Basic fence services. |
| 2 | Crew-Adjacent | 35 Fame | Smuggling route access. Relic trafficker merchants. Better fence rates. |
| 3 | Trusted Runner | 55 Fame | Varek meeting. Reaver safe houses. Reaver intelligence network partially visible. |
| 4 | Captain's Confidence | 75 Fame | Full intelligence network. Relic modification services. Inner operation access. |
| 5 | Varek's Right Hand | 95 Fame | Highest-tier black market. Storm engine fragment knowledge. Varek's full arc. |

### Infamy Effects

| Infamy Level | Effect |
|---|---|
| Low | No effect |
| Medium | Some crew members are cold. Extortion risk increases on player-owned routes. |
| High | Reaver crews treat you as a mark. Random ambushes on travel routes. |
| Very High | Full Reaver network hostile. Varek puts a contract out. This is survivable but expensive. |

### Faction Perks (Unlocked by Fame Tier)

- **Tier 2 — Black Market Access:** Unlocks the Undercity merchant network. Items unavailable through legitimate channels (rare relic components, faction intelligence reports, contraband consumables) become purchasable.
- **Tier 3 — Smuggler's Routes:** Bypasses Vanguard checkpoints via Reaver smuggling tunnels. Travel through hostile zones at significantly reduced detection risk. Can use these routes for trade goods too — tariff-free but carrying risk of ambush.
- **Tier 4 — Intelligence Brokerage:** Purchase and sell information as a commodity. Reaver intelligence reports reveal hidden quest options, NPC vulnerabilities, and competitor weaknesses. Certain Vanguard and Hollow Crown missions become much easier.
- **Tier 5 — Storm Network:** Access to Varek's full continental operation awareness. Highest profit margin on all trade goods. Ability to commission Reaver crews for targeted operations (sabotage a competitor's trade route, extract a prisoner, acquire a specific relic).

### Faction Quests (Overview)

**Act I:**
- *The First Score* — Help Maren retrieve a stolen Reaver shipment; what's in the shipment complicates things
- *Undercity Diplomacy* — Two Reaver crews are on the edge of a gang war that will destabilize Hollowford's black market; mediate, back one side, or let it burn
- *Varek's Test* — Varek runs the player through an intelligence extraction job to see what they're made of

**Act II:**
- *The Storm Engine* — Varek is sitting on a piece of the device that helped cause the Severance; he hasn't told anyone; whether you expose this, exploit it, or help him reckon with it is one of the game's most significant moral choices
- *Hollowford Below* — The Reavers have built an entirely parallel city beneath Hollowford; the Vanguard is close to discovering it; options for how to protect it range from brutal to clever
- *The Idealist's Problem* — A Reaver crew has gone full bandit — attacking refugees; Varek quietly wants them stopped but won't move publicly; the player is the off-the-books solution

**Act III (Shadow/Inner Circle):**
- *The Controlled Burn* — Varek's endgame plan is to detonate the storm engine fragment to destroy the Hollow Crown's intelligence operation; help, redirect, or stop it
- *What Varek Wants* — If the player's ideology track is high on Idealist, Varek reveals what he actually wants the Reaver network to become; this conversation determines his ending

### Economic Role
The Reavers offer the highest profit margins of any faction but the highest risk. Their black market sells things no one else can get. Their smuggling routes bypass legitimate trade infrastructure but are subject to disruption, ambush, and Infamy-based extortion. Players who invest heavily in the Reaver economic network will become extremely wealthy but will carry persistent Infamy with the Vanguard. Best for players who want to maximize economic output and accept the political cost.

---

## 4.4 House of the Hollow Crown

### Reputation Tiers (Fame)

| Tier | Name | Threshold | Unlocks |
|---|---|---|---|
| 0 | Unknown | Default | Formal courtesy at the Eltaryn Vale Seat |
| 1 | Petitioner | 15 Fame | Access to Hollow Crown scholars. Basic archive reading permissions. |
| 2 | House-Friend | 35 Fame | Tier 1 archive access. Hollow Crown luxury merchant. Political intelligence sharing. |
| 3 | Sworn Associate | 55 Fame | Seraphine direct meetings. Tier 2 archive access. Hollow Crown legal protection (limited). |
| 4 | House Confidant | 75 Fame | Full archive. Seraphine's personal quest opens fully. Tier 3 gear from House armory. |
| 5 | Voice of the Crown | 95 Fame | Seraphine's inner council. Scepter of Ascension quest access. Highest archive tier. |

### Infamy Effects

| Infamy Level | Effect |
|---|---|
| Low | No effect |
| Medium | Formal coolness. Some archive sections closed. Seraphine becomes guarded. |
| High | House agents surveillance player. Attempts to discredit you with other factions. |
| Very High | Active intelligence operations against player. Attempts to neutralize you before you reach the Heart. |

### Faction Perks (Unlocked by Fame Tier)

- **Tier 2 — Firstborn Scholar:** Firstborn inscriptions provide 50% more lore information. Hidden rooms in Firstborn ruins identified through archive cross-referencing. +1 to all relic interaction skill checks.
- **Tier 3 — Political Cover:** One crime per Act can be legally expunged through Hollow Crown political influence. Access to noble NPC dialogue options unavailable by default.
- **Tier 4 — Archive Authority:** Can commission specific Firstborn historical research. Receive intelligence on other factions' operations that the Hollow Crown has gathered through their agent network.
- **Tier 5 — Eltaryn Legitimacy:** Hollow Crown endorsement carries significant NPC reaction weight. Certain quest resolutions available only through legitimate authority claims. Seraphine's full arc — including her potential redemption — accessible.

### Faction Quests (Overview)

**Act I:**
- *The Sealed Wing* — Access a section of the Eltaryn archive that Seraphine claims is irrelevant; it is not
- *The Pretender's Claim* — A minor noble is publicly challenging Eltaryn legitimacy; handle it through evidence, persuasion, or force
- *What the Records Say* — Retrieve Firstborn documentation from a ruin before the Vanguard seizes it

**Act II:**
- *The Inconvenient Truth* — The player has access to Firstborn records that directly contradict the divine right narrative; what they do with this information reshapes Seraphine's trajectory
- *Scepter of Ascension* — The search for the maintenance tool the Hollow Crown believes is a royal artifact; finding it first has significant consequences
- *The Betrayal Calculus* — Seraphine discovers an internal coup attempt by House loyalists who want to abandon her idealism for pure power; her response depends on what the player has built with her

**Act III (Shadow/Inner Circle):**
- *The Declaration* — Seraphine publicly broadcasts her claim and calls for support; the player chooses what role to play in it
- *Seraphine's Choice* — If the Truth ideology track is high, the player can be the catalyst for Seraphine's complete reorientation — the most dramatically significant outcome the Hollow Crown track offers

### Economic Role
The Hollow Crown controls the luxury economy — high-value goods, political intelligence, archive knowledge, and social capital. Their merchants are the best source of high-end equipment components and rare lore items. Their political leverage can reduce the player's Infamy with other factions (at a price). However, they produce nothing themselves — they are entirely dependent on buying influence and controlling information. Their economic power collapses if their political standing crumbles.

---

# SECTION 5: MINOR FACTION SYSTEM

## 5.1 Design Principle
Minor factions do not have full Fame/Infamy tracking. They operate on a simplified three-state system (Hostile / Neutral / Allied) that defaults based on the player's major faction standings, but can be shifted through specific quest actions independent of major faction alignment.

## 5.2 Minor Factions at Launch

### Emberhaven Drakeling Community
**Default State:** Determined by Vanguard standing (Vanguard Trusted = Drakeling Wary; Vanguard Notorious = Drakeling more open)
**Independent Shift:** Completing Emberhaven's three dynamic event quests (Food Shortage, Zealot Uprising, Human Mob) moves standing independently of major faction alignment.
**Allied Unlocks:** Drakeling cultural goods merchant, access to Pyra Flameheart's faction if she was deradicalized, unique fire-resistant crafting components.
**Quest Available (Allied):** *The Long March* — Elder Vorash asks the player to negotiate permanent settlement status for Emberhaven with whatever faction currently controls Hollowford. The approach and outcome depend heavily on the player's standing with that faction.

### Greenwatch Vaelari Community
**Default State:** Determined by Verdant Flame standing (strong positive correlation)
**Independent Shift:** Completing Wellspring Pulse, Thornwalker Raid events in the map document.
**Allied Unlocks:** Vaelari Wellspring reagents (unique tier), Aelira's community trust amplified, access to Thornwalker faction if allied.
**Quest Available (Allied):** *Rootless* — Liora, the Half-Formed outcast, has information about a Wellspring corruption source that she will only share with someone she trusts. Her personal quest is available only through Greenwatch Allied standing.

### The Undercity Residents (Hollowford)
**Default State:** Neutral to all players
**Independent Shift:** Determined by choices in Hollowford side quests independent of faction alignment
**Allied Unlocks:** Reduced black market prices, access to fences outside the Reaver network, civilian intelligence (rumors, patrol schedules, NPC whereabouts)
**Quest Available (Allied):** *Below the Floor* — The Undercity residents have discovered a sealed Firstborn chamber beneath Hollowford that none of the factions know about. What's in it, who finds out, and what the player does with the knowledge is one of the game's most freeform quests.

### The Relic-Marked (Other Survivors)
**Default State:** Cautiously neutral — they are aware the player exists and are watching
**Independent Shift:** Determined entirely by direct interaction when encountered
**Allied/Hostile:** Meeting other relic-marked individuals produces unique outcomes — potential alliance, ideological conflict, or combat. Their Echo fragments have different perspectives than the player's Echo.
**Quest Available:** Each relic-marked encounter is its own contained questline. Not a faction in the traditional sense but tracked as a minor faction for consistency.

---

# SECTION 6: THE ECONOMIC SYSTEM

## 6.1 Design Philosophy

The economic system functions as a parallel progression layer — a mini-game embedded in the political world. It is not mandatory for completing the main story, but it is the primary source of late-game wealth, creates personal stakes in faction conflicts, and produces some of the most memorable emergent gameplay moments when a trade route collapses or a business gets seized.

The system has three interlocking components: **Trade Routes**, **Property & Business Ownership**, and **Production Chains**. All three are entangled with faction standing.

---

## 6.2 Trade Routes

### What They Are
Trade routes are established connections between two settlements or production sites that automatically move goods over time. Once a route is established, it generates passive income and delivers goods to designated storage without requiring the player to physically transport them. Routes can be disrupted, taxed, seized, upgraded, or destroyed based on world events.

### Establishing a Route
1. Player must have physically traveled the route at least once (unlocks it as a known path)
2. Player hires a merchant caravan NPC from a settlement (cost scales with distance and danger)
3. Player assigns goods to transport (produced at origin, sold or stored at destination)
4. Route activates on a real-time cycle (one in-game day per trip)

### Route Variables

| Variable | Effect |
|---|---|
| **Distance** | Longer routes = more profit per trip, higher disruption risk, longer delivery time |
| **Faction Control** | Route passing through Vanguard territory = stable, taxed. Reaver territory = risky, untaxed. Contested = highest risk, lowest reliability |
| **Danger Rating** | Corruption zones, bandit activity, faction conflict events all raise danger |
| **Caravan Quality** | Cheap caravans have high failure rate. Upgraded caravans survive more disruption events |

### Route Disruption Events
When a route is disrupted, the player receives a notification and must respond:
- **Bandit Ambush:** Player can dispatch (investigate and clear the ambush site), pay extortion (Reaver-related option), or reroute (longer path, lower profit)
- **Faction Checkpoint:** Vanguard establishes a new checkpoint; player can pay the tariff, use Reaver tunnels (if available), or use political leverage to exempt their route
- **Corruption Surge:** A corruption zone expands across a route; player must either clear the node (combat) or reroute
- **Faction Seizure (Act III):** If a faction the player is at war with controls route territory, they can seize the goods in transit. Player must retake the route militarily, negotiate, or abandon it.

### Route Upgrades
| Upgrade | Cost | Effect |
|---|---|---|
| Armed Escort | Ongoing | Significantly reduces bandit ambush success rate |
| Vanguard Patrol Contract | Ongoing (high) | Near-immunity to bandit disruption; adds Vanguard tariff |
| Reaver Protection | Ongoing (medium) | Immunity to Reaver disruption; adds Infamy with Vanguard |
| Weather-Hardened Wagons | One-time | Reduces corruption zone damage to caravan |
| Insider Contact | One-time per settlement | Reduces checkpoint friction, better sell prices at destination |

---

## 6.3 Property Ownership

### Property Types

| Type | Base Cost | Primary Function | Faction Interaction |
|---|---|---|---|
| **Storefront** | Low | Sells player-produced goods automatically. Generates passive income. | Faction-controlled district affects clientele, prices, and risk |
| **Warehouse** | Medium | Stores goods, components, and trade inventory. Route terminus point. | Can be seized by hostile faction. Can be fortified. |
| **Farm Plot** | Medium | Produces food, reagents, raw materials over time. Requires worker assignment. | Corruption zone proximity affects yield. Verdant Flame standing affects reagent quality. |
| **Workshop** | High | Produces refined components, gear upgrades, consumables. Requires worker + materials. | Ironkin expertise improves output (racial bonus). Vanguard territory = quality stable; Reaver territory = quality variable but no taxation |
| **Information Broker Office** | High | Generates faction intelligence reports over time. | Reaver network required for highest tier. Hollow Crown can provide a legitimate front. |
| **Tavern/Inn** | Medium | Generates passive gold. NPC relationships develop in your establishment. Side quests generated. | Best placed in high-traffic areas regardless of faction control |

### Property Acquisition
- **Purchase:** Standard acquisition from settlement property brokers (available in most Act I+ settlements)
- **Quest Reward:** Some faction quests reward property deeds as payment
- **Seizure:** Player can seize abandoned or hostile-faction-owned property through specific quest chains (morally complex, generates Infamy)
- **Inheritance:** A small number of properties become available through NPC relationship development

### Property in Faction Conflict
When faction conflict escalates in Act II/III, every property has a **faction zone** tag. If the controlling faction of that zone changes:
- **Allied faction takes control:** Property protected, possible bonus (Vanguard adds guard patrol, Verdant Flame purifies adjacent corruption, Reavers add black market access)
- **Hostile faction takes control:** Property at risk. Player must either negotiate (spend Fame), pay protection (spend gold), defend it (combat), or accept seizure (lose the asset)
- **Contested zone:** Income halved, disruption events increase, but some unique trade opportunities emerge (wartime profiteering, information arbitrage)

---

## 6.4 Production Chains

### Overview
Production chains convert raw materials into refined goods that command higher prices, unlock crafting, or supply faction operations in exchange for standing bonuses.

### Raw Materials (Tier 1)
Gathered through exploration, farm plots, or purchase from basic merchants.
- **Agricultural:** Grain, livestock, timber, fiber
- **Mineral:** Iron ore, stone, coal, crystal fragments
- **Organic:** Herbs, animal components, fungal matter
- **Arcane:** Lattice residue (from corruption zones), Wellspring reagents, relic shards

### Refined Goods (Tier 2)
Produced in workshops from Tier 1 materials. Require worker assignment and time.

| Input | Output | Market |
|---|---|---|
| Grain + Livestock | Provisions (high-demand in post-Severance world) | Universal |
| Iron Ore + Coal | Steel components (gear crafting, construction) | Vanguard, Ironkin |
| Herbs + Lattice Residue | Purification compounds | Verdant Flame, general healing market |
| Crystal Fragments + Arcane | Relic stabilizers (repair damaged relics, improve efficiency) | Hollow Crown, mage builds |
| Timber + Stone | Construction materials (settlement building in Act III) | Universal |

### Specialized Goods (Tier 3)
Require both Tier 2 materials and specific faction standing or knowledge unlocks.

| Output | Requirements | Effect |
|---|---|---|
| Vanguard-Grade Arms | Steel components + Tier 3 Vanguard Fame | Highest base damage weapons, sellable to Vanguard at premium or used personally |
| Purified Reagents | Purification compounds + Circle Ally standing | Unlock highest-tier Verdant Flame ability crafting |
| Engineered Relics | Relic stabilizers + Hollow Crown archive knowledge | Relics with enhanced or modified Echo properties |
| Contraband Stockpile | Multiple Tier 2 components + Reaver network access | Highest profit margin, illegal, Vanguard Infamy risk |

### Worker System
Production requires workers assigned to each property. Workers are hired from settlement labor pools.

| Worker Tier | Cost | Productivity | Notes |
|---|---|---|---|
| Unskilled | Low wage | Basic output | Available everywhere |
| Skilled | Medium wage | 40% better output, lower failure rate | Available at larger settlements |
| Specialist | High wage | 80% better output, unique products possible | Rare; often quest-unlocked; race-specific bonuses (Ironkin smiths, Vaelari reagent farmers) |

Workers can be lost during faction conflict events. High Vanguard standing means workers are less likely to flee during conflicts. High Reaver standing means workers are less likely to be extorted. Workers in contested zones require hazard pay (ongoing gold cost) or will leave.

---

## 6.5 Faction Economic Warfare

This is where the economic system becomes viscerally connected to faction politics.

### Act II Economic Friction
As faction tensions escalate:
- **Vanguard** begins enforcing new tariff rates on goods moving through garrison zones (5–15% of cargo value per checkpoint)
- **Reavers** begin extracting protection payments from trade routes that lack explicit Reaver agreements
- **Verdant Flame** imposes embargo on goods moving through or from corruption zones they consider to be actively exploited (limits Tier 1 arcane material trade)
- **Hollow Crown** begins using their political leverage to manipulate commodity prices in settlements they influence (luxury goods price spike, basic goods destabilized)

### Act III Economic Consequences

**Vanguard Takes Hollowford:**
- Tariffs apply to all goods citywide
- Contraband merchants close or go underground
- Stability increases across all Vanguard routes
- Black market prices spike due to supply suppression

**Reavers Liberate the Market (The Liberated Vale):**
- Undercity Layer 2 partially surfaces — formerly restricted goods available through legitimate stalls
- Black market prices drop significantly (reduced scarcity as goods move aboveground)
- Contraband categories shrink (fewer things are restricted, so fewer things carry black market premiums)
- Community-based arbitration replaces faction-controlled trade enforcement — Varek's network facilitates disputes rather than extracting tribute
- Legitimate merchants operate without faction taxation but without faction protection — income is variable, not suppressed
- Trade route maintenance is community-driven (slightly less reliable in bad weather, significantly more accessible to non-faction traders)

**Verdant Flame Controls the Vale Border:**
- Corruption zone routes become passable
- Reagent production increases continent-wide (prices drop)
- Military goods production drops (no faction military infrastructure)
- Agricultural yields improve in purified zones

**Hollow Crown Consolidates Political Power:**
- Luxury goods economy strengthens
- Tariffs manipulated in player's favor if high Fame, against if low
- Archive-driven goods (relic components, historical artifacts) spike in value
- General trade destabilized by political uncertainty

### Price Index
The game tracks a live commodity price index across six categories. Faction actions, world events, and player choices all move these prices:

| Category | Affected By |
|---|---|
| **Food & Provisions** | Farm yields, corruption zone spread, Vanguard stability, Drakeling camp state |
| **Military Goods** | Vanguard demand, faction conflict intensity, player production |
| **Reagents & Components** | Verdant Flame standing, corruption zone density, Wellspring health |
| **Relics & Arcane** | Hollow Crown activity, Reaver trafficking volume, Firstborn ruin access |
| **Contraband** | Reaver dominance, Vanguard suppression, player black market standing |
| **Luxury Goods** | Hollow Crown political stability, trade route safety, noble NPC survival |

---

# SECTION 7: WORLD STATE CHANGES (ACT II/III)

## 7.1 Activation Trigger
World state changes do not activate in Act I. The Vale is in shock — factions are establishing position, not asserting dominance. From the Act II Ashenveil revelation forward, faction-controlled zones begin developing distinct characteristics that are visible, tangible, and mechanically significant.

## 7.2 Faction Zone Characteristics

### Vanguard-Controlled Zones
**Visual:** Guard patrols with torchlight in structured patterns. Checkpoints with Vanguard banners. Suppression glyphs on buildings (magic detection). Repair work on infrastructure. Orderly, cold.
**Mechanical:** Checkpoint friction for players below Tier 2 Fame (papers check, delay, possible search). Magic use in Vanguard zones triggers a warning at first, detention risk on repeat. Trade tariffs active. Worker safety high.
**NPC Behavior:** Citizens are quieter, more guarded. Guards are alert. Merchants are stable but cautious. Beggar NPCs are fewer (Vanguard removes them — where they go is a side quest).

### Reaver-Controlled Zones
**Visual:** No official signage — the zone's identity is communicated through graffiti, specific door markings, and the behavior of NPCs. Improvised construction. Dim lighting favored. Lookouts on rooftops.
**Mechanical:** No checkpoint friction for Reaver Fame Tier 2+. Black market vendors accessible on side streets. Random extortion events for players below Tier 2. Pickpocket risk active. Police presence nonexistent.
**NPC Behavior:** More open, more desperate, more honest. Civilians will say things they won't say in Vanguard zones. The underground economy is visible if you know where to look.

### Verdant Flame Influence Zones
**Visual:** Corruption receding at zone edges (visible green-gold light pushing back the black-vein growth). Planted markers at corruption boundaries. Grove shrines at intersections.
**Mechanical:** Corruption zone passive damage reduced by 50% in adjacent areas. Reagent gathering yields increased. Wild magic events occur here but are more likely to be beneficial than harmful. Vanguard presence minimal.
**NPC Behavior:** Vaelari NPCs move openly. Human NPCs are a mix — relieved about corruption reduction, nervous about the magic. Some report Verdant Flame activity to the Vanguard (side quest hook).

### Hollow Crown Influence Zones
**Visual:** Eltaryn heraldry displayed on buildings (sometimes quietly, sometimes boldly). Hired guards in House livery rather than Vanguard armor. Wealthier, more maintained streets. Subtle intelligence apparatus (watchers, informants — the player can learn to spot them).
**Mechanical:** Noble NPC dialogue options available. Legal disputes can be filed and resolved through House channels. Archive access points appear. Information broker prices lower. Vanguard authority is quietly contested here.
**NPC Behavior:** More formal. More political. Wealth displayed. Information treated as currency. NPCs are more likely to ask who you work for and to offer deals.

---

# SECTION 8: REWARD MODEL SUMMARY

The full reward model across all factions and systems:

### Exclusive Gear & Merchants
- Each faction has 5 gear tiers, unlocked by Fame standing
- Tier 5 faction gear is among the best in the game — competitive with the best dungeon drops
- Faction gear has built-in ideology bonuses (Vanguard armor has crowd-control resistance; Verdant Flame robes have corruption immunity; Reaver equipment has detection resistance; Hollow Crown gear has persuasion skill bonuses)
- Black market (Reaver) and archive dealers (Hollow Crown) carry items unavailable through any other channel

### Unique Quests & Storylines
- All inner-circle questlines (Act II shadow alignment onward) are locked behind Fame thresholds
- Several of the game's most significant narrative moments — Varek's confession, Seraphine's truth, Aelira's reckoning, Hale's breaking point — are only accessible through sustained faction investment
- The Unaligned Gambit (the fifth Act III path) requires deep investment across all four factions simultaneously

### Gameplay Perks & Abilities
- Each faction's Tier 2 and Tier 3 perks unlock ability branches in the Combat Framework (not available through any other progression path)
- Economic perks (reduced prices, patrol contracts, route protections) are faction-standing gated
- Ideology sub-score unlocks the most unusual and powerful options within each faction's perk tree

### Safe Passage, Housing & Stronghold Access
- Faction-controlled zones provide safe houses at Tier 3+ standing (respawn points, merchant access, storage)
- Stronghold access (the closest thing to a player home base) is tied to Act III alignment — the aligned faction provides a permanent headquarters
- Property protection is explicitly tied to faction standing as described in the economic system

---

# SECTION 9: IMPLEMENTATION CHECKLIST

**Reputation System:**
- [ ] Fame/Infamy tracking variables implemented per faction (8 total — 2 per faction)
- [ ] Ideology sub-score tracking implemented per faction (4 hidden variables)
- [ ] Standing state logic implemented (6 states per faction, determined by Fame/Infamy thresholds)
- [ ] Reputation change events mapped to all relevant quests and dialogue choices
- [ ] Faction-to-faction bleed logic implemented (activates Act II)
- [ ] Standing state behavioral changes implemented for all major NPC categories per faction

**Affiliation System:**
- [ ] Act I open field state implemented (no affiliation restrictions)
- [ ] Shadow alignment system implemented (Act II private commitment)
- [ ] Act III forced alignment trigger designed and implemented
- [ ] Unaligned Gambit conditions tracked and quest designed
- [ ] Alignment lock logic implemented (irreversible post-Act III)
- [ ] Companion departure triggers mapped to alignment choices (cross-reference Companion Design Doc)

**World State:**
- [ ] Faction zone tags assigned to all Vale settlements and regions
- [ ] Visual direction per faction zone defined in Art Direction document (cross-reference Doc 9)
- [ ] Mechanical zone effects implemented (checkpoint friction, magic detection, black market spawn, etc.)
- [ ] World state activation tied to Act II trigger
- [ ] Dynamic zone control system implemented (faction territorial changes reflected in real time)

**Minor Factions:**
- [ ] Three-state (Hostile/Neutral/Allied) tracking for all four minor factions
- [ ] Default state logic implemented (major faction standing inheritance)
- [ ] Independent shift quest triggers implemented
- [ ] Minor faction allied unlocks implemented
- [ ] Four minor faction questlines designed, scripted, and tested

**Economic System:**
- [ ] Trade route establishment UI designed and implemented
- [ ] Route disruption event system implemented (5+ event types)
- [ ] Route upgrade system implemented
- [ ] Property purchase, ownership, and management UI implemented
- [ ] Worker hire, assign, and management system implemented
- [ ] Production chain logic implemented (Tier 1 → Tier 2 → Tier 3)
- [ ] Faction economic warfare events implemented (Act II/III)
- [ ] Live commodity price index implemented and tied to faction/world events
- [ ] Property seizure and protection mechanics implemented

**Faction Quests:**
- [ ] All Act I faction quests designed (12 quests — 3 per faction)
- [ ] All Act II faction quests designed (12 quests — 3 per faction)
- [ ] All Act III shadow/inner circle quests designed (8 quests — 2 per faction)
- [ ] All minor faction quests designed (4 quests — 1 per minor faction)
- [ ] Ideology sub-score branching implemented within quest outcomes
- [ ] Cross-faction quest interactions flagged (quests whose outcomes affect multiple factions)
