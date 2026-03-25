# THE SHATTERED DOMINION — ECONOMY SYSTEM
## Document 11 | Version 1.0 | Depends on: SD_01 World Bible, SD_05 Faction Playbook, SD_08 Severant Vale Region Guide

**Purpose:** This document is the authoritative specification for the economy system in The Shattered Dominion. It supersedes and replaces SD_05 Section 6 (The Economic System), which should be treated as a deprecated sketch. All implementation, design iteration, and future documentation referencing the economy defers to this document.

**Scope:** Currency architecture, survival economy, merchant relationships, trade routes (including named caravan masters, route specializations, disruption events, and upgrades), property and business ownership, production chains, the management interface, wealth as social power, compound business design, and the living price index. Faction economic warfare remains in SD_05 Section 6.5 and is referenced here but not duplicated.

**Design Reference:** The economy should feel like something you built, not something you administered. Every significant decision has a human face attached. Wealth is social power — it buys options unavailable through any other means.

---

# SECTION 1: DESIGN PHILOSOPHY

## 1.1 Core Principles

**The economy is the Severance made mechanical.** Prices that tripled overnight. Currency that might be worthless by next season. A black market better-stocked than legitimate merchants. These are not balance decisions — they are storytelling. Every time the player winces at the cost of a healing potion or finds a pre-Severance chest and feels the windfall, the world is doing narrative work.

**Money must be hard to get and meaningful to spend.** Scarcity is the point. Players swimming in gold by Act II means the Severance stops feeling catastrophic and economic choices become trivial. The goal is not to make the player feel poor — it is to make every financial step feel genuinely earned.

**Multiple paths to wealth mirror multiple paths through the game.** A combat-focused player earns through salvage, bounties, and monster components. A politically savvy player earns through information brokering and faction commissions. A builder earns through trade routes and production chains. A criminal earns through the Reavers. No single path is mechanically dominant — they feel different.

**Wealth is social power, not just purchasing power.** The most compelling economic moments are not "I can now afford better armor." They are "I just bribed a Vanguard checkpoint with money I earned through six cycles of careful route management," or "I funded Kael's supply request before he had to beg House Eltaryn for it," or "I bought the building my contact was about to be evicted from." Design toward those moments.

**The economy is not mandatory, but disengagement has a cost.** Completing the main story without engaging the economy is possible. However, the economy gates 3–5 significant narrative moments — access paths, dialogue options, and quest resolutions — for players who do engage. This is a deliberate design decision. Alternate access paths for these moments are not provided. Players who disengage accept missing them.

## 1.2 Three-Phase Economic Arc

The economy operates in three distinct phases across the playthrough. Each phase has its own logic, tone, and mechanical identity.

| Phase | Acts | Player State | Core Loop |
|---|---|---|---|
| **Survival Economy** | Act I (early–mid) | No coin, no contacts | Scavenge, odd jobs, information brokering, monster salvage |
| **Establishment Economy** | Act I (late) – Act II | First property, first route | Trade routes, production chains, merchant relationships |
| **Power Economy** | Act II–III | Multiple income streams | Compound businesses, political investment, wealth as leverage |

The transition between phases is not gated by a quest or a menu unlock. It emerges from accumulated capital, relationships, and player initiative. The player who reaches the Established tier at hour 12 and the player who reaches it at hour 25 have had different games, and both are valid.

---

# SECTION 2: CURRENCY ARCHITECTURE

## 2.1 The Four Currency Types

The post-Severance world does not have a stable currency. This is not flavor — it is a mechanical fact the player navigates throughout the game.

### Crown Marks (Primary Currency)
**Form:** Copper / Silver / Gold at 100:1 ratios.
**Issued by:** House Eltaryn and the Crown Mint, which no longer has meaningful authority.
**Accepted:** Everywhere. Still the default because nothing better exists.
**Value trend:** Slowly devaluing. The Hollow Crown is the primary defender of Crown Mark value because their political legitimacy depends on it. If Hollow Crown political power collapses in Act III, Crown Mark purchasing power drops 10–15% across all markets.
**Use:** All standard transactions. Primary currency for property purchase, caravan wages, worker wages, merchant purchases, and bribes.

**Base price reference (post-Severance):**
- Bread: 3 copper (up from 1 copper pre-Severance)
- Basic meal: 8 copper
- Healing potion (basic): 40 silver
- Iron sword (standard): 2 gold (Highwinter iron scarce; up from 50 silver pre-Severance)
- Caravan hire (first route): 8–20 silver per cycle depending on master and distance

### Lattice Chips (Premium Currency)
**Form:** Small fragments of stabilized lattice crystal. Cannot be manufactured. Naturally occurring near Wellspring nodes and Firstborn ruins.
**Supply:** Finite and decreasing as corruption spreads. Not convertible to Crown Marks.
**Accepted by:** Hollow Crown merchants (preferred), Verdant Flame vendors (preferred), high-tier Undercity vendors, Firstborn-adjacent services.
**Value trend:** Rising as supply contracts.
**Use:** Rare goods, relic components, Firstborn-adjacent services, high-tier Hollow Crown transactions. The player accumulates approximately 30–50 across a full playthrough. Spending one is a decision, not a habit.
**Design note:** Lattice Chips are never a second gold bar. They are a key that opens specific doors. Finding one should feel like finding something genuinely valuable.

### Favor Markers (Reaver Credit)
**Form:** Not physical. A tracked reputation-debt system within the Reaver network, logged in Varek Seven-Knives' ledger.
**Earned by:** Completing Reaver jobs, providing services, delivering intelligence, clearing problems Varek wants cleared.
**Spent on:** Black market access, Undercity vendor discounts, Reaver disruption resolution, Reaver Protection route upgrades, Reaver network intelligence.
**Properties:** Non-transferable. Cannot be stolen. Not reset by player death. Not reset by zone hostility. Reavers respect debts from the grave.
**Design note:** Enables a fully criminal economic path. A player who never accumulates significant gold can still be economically powerful through Reaver relationships alone. Favor Markers provide Reaver Cut immunity at the equivalent of Crew-Adjacent Fame, making them a viable alternative to the Fame track for economically-minded players.

### Barter (Informal Early Economy)
**Form:** Not a tracked currency — a transaction flag on specific vendors and NPCs.
**Who uses it:** Frontier merchants in low-currency zones, refugee camp vendors, some Verdant Flame field contacts, Drakeling community traders at Emberhaven.
**What they want:** Monster components, salvaged materials, pre-Severance artifacts, food, tools.
**Design note:** Barter is not a separate mechanic — it is a vendor attribute. It teaches the player that resources have intrinsic value beyond their sell price and that knowing the right buyer matters more than knowing the standard price.

---

# SECTION 3: THE SURVIVAL ECONOMY (PHASE 1)

## 3.1 Design Intent

The survival economy covers the period from the player's arrival in Hollowford through the late stages of Act I. The player has no trade routes, no properties, and minimal merchant relationships. This phase must feel desperate and interesting — full of genuine choice — rather than like a waiting room before the real systems open. Every income source in this phase is also a world-building delivery mechanism.

## 3.2 Six Income Sources

All six coexist. The player is expected to use them opportunistically based on risk tolerance and build.

### Salvage
The post-Severance world is littered with abandoned property. Pre-Severance homes evacuated too quickly, merchant carts overturned on disrupted roads, Vanguard supply caches scattered, corruption zone edges where people fled.

Salvage drops are not random loot tables — they are curated by location and carry environmental storytelling. A farmhouse at a corruption zone edge contains preserved food, farming tools, and a lockbox with a family's savings. An overturned merchant cart on the Hollowford road has trade goods in broken crates and a manifest identifying what was supposed to arrive where — which is itself information worth selling.

Salvage from corruption zones yields the rarest materials at the highest risk. Some Act I materials are only obtainable this way, establishing early that risk calibration is central to the economy.

**Design constraint:** Salvage should never feel like looting for its own sake. The best salvage moments carry the story of why something was left behind. That context makes the act of taking it feel meaningful rather than mechanical.

### Monster Salvage
Combat drops standard loot (gear, weapons) and monster components (organs, hides, bones, venom sacs). Standard loot is useful personally or saleable at basic merchants. Monster components are more valuable than they initially appear — but only to the right buyers.

**Specialized buyer premium:** This is a core teaching mechanic. Harren Voss buys a Drake scale for 4 silver. The Verdant Flame alchemist buys the same scale for 22 silver. A Reaver fence buys it for 14 silver. Learning who pays what for which materials is a skill the player develops, and it transforms combat from "kill and vendor" into "kill and consider."

Monster component demand fluctuates with world state. When corruption zones expand, purification compound demand spikes and Verdant Flame alchemists pay more for organic materials. When the Vanguard launches a campaign, military-grade material demand increases. These signals are visible through merchant dialogue before any price indicator changes.

### Odd Jobs and Courier Work
Hollowford's quest board and the Market Quarter social landscape provide steady low-pay, low-risk work. Carry this message. Locate this person. Bring this package to the Garrison. Find out if the merchant at Southwatch is still operating.

Pay range: 5–30 silver per job.

**Critical design constraint:** Odd jobs are not filler. Each one introduces a named NPC, a location, a faction relationship, or a piece of information. The player who completes three courier missions for Harren Voss has a different relationship with him when the trade route system opens — Voss trusts them, offers better rates, and mentions which routes are currently lucrative. Small economic work pays forward into larger economic systems.

### Information Brokering
The post-Severance world is information-starved. People want to know if their family's settlement is standing. Whether a road is clear. What faction controls a checkpoint. What the Vanguard is planning.

The player learns things through play — exploration, faction quests, companion conversations — and some of that information has economic value. Selling it means finding the right buyer. The Hollow Crown pays for Vanguard troop movements. A merchant pays for confirmation a route is passable. A worried parent pays for news of their child's camp.

Pay range: 20–80 silver per piece of genuine intelligence.

**Primary value:** Relationship-building. Every transaction establishes the player as someone worth talking to, with cascading effects on quest access and dialogue options throughout the game. Information brokering is the income source that most directly rewards the player who talks to everyone and explores thoroughly.

### Pre-Severance Artifact Finding
Firstborn ruins and abandoned settlements contain items whose value most NPCs do not recognize. A sealed Firstborn vessel. A pre-Severance trade ledger. A set of Hollow Crown archive stamps.

To basic merchants: curiosities worth a few copper.
To the right buyer: an archive scholar, an antique dealer, a Reaver fence who moves specialty goods — substantial amounts, sometimes Lattice Chips.

**The puzzle:** Figuring out who values what. The player who wanders into the Noble Quarter and mentions the sealed Firstborn vessel they found gets a fundamentally different offer than the player who sold it to Voss. This teaches players to ask around before selling and to build a mental map of which buyers exist for which categories. It is the clearest introduction to the "right buyer" mechanic that carries through the entire economy.

### Gambling and Contests
The Broken Chalice hosts dice games, arm wrestling, a shooting range in the yard, and occasional informal combat tournaments. These are not reliable income — they are the economy's pressure valve.

**Critical design constraint:** The house does not always win. Skill-based contests (arm wrestling, shooting range, combat tournaments) give the player a genuine advantage based on build stats. Dice games have fair odds with no house advantage. Gambling should feel like a real option, not a trap.

---

# SECTION 4: MERCHANT RELATIONSHIPS

## 4.1 Relationship Tiers

Merchant reputation is a separate track from faction Fame, operating at the individual level. Every named merchant tracks the player's history: transaction frequency, job delivery, and honesty. This is not a UI-visible meter — it manifests through NPC dialogue and unlocked behaviors.

| Tier | Threshold | What Changes |
|---|---|---|
| **Stranger** | Default | Base prices. Standard service. No special information. |
| **Regular** | 5+ successful transactions | Merchant mentions what's selling well, what's in short supply, upcoming opportunities. Prices unchanged. |
| **Trusted** | 20+ transactions, at least one significant favor | 10–15% better buy/sell rates. Merchant holds reserved goods. Flags incoming price changes. |
| **Partner** | Quest-locked, specific to each merchant | Merchant becomes an active economic collaborator. Rumors flagged proactively. Access to unlisted goods. Standing orders available. |

## 4.2 Haggling

Available at any transaction. Governed by the player's Willpower stat and current relationship tier. At Stranger tier: 5–8% discount on success. At Trusted tier: the starting price is already closer to fair value, making haggling more effective from a better floor.

Haggling has a per-merchant per-in-game-day cooldown. Attempting two haggles in succession triggers refusal — the merchant knows what their goods are worth. Repeated over-haggling costs relationship standing.

**Design constraint:** Haggling should never feel mandatory. It is a satisfying option for players who engage with the relationship system, not a tax on those who do not.

## 4.3 Standing Orders (Partner Tier Only)

At Partner tier, the player can establish standing orders for output disposition: auto-sell at market price, auto-route goods to a specific destination, or auto-store in a designated warehouse. Standing orders are not available to strangers. Earning them reflects the trust relationship that makes delegation possible.

---

# SECTION 5: TRADE ROUTES

## 5.1 Establishing a Route — Three Preconditions

Routes are not purchased from a menu. They emerge from play when three organic preconditions are satisfied.

**Precondition 1 — Route knowledge:** The player must have physically traveled the route at least once. Every physical overland journey between two locations logs that leg as a known path. Fast travel does not satisfy this precondition. In practice, most Hollowford-to-settlement routes will be walked organically during Act I through quest and exploration activity before the trade route system opens.

For inter-settlement routes (Ironwood to Grainfell, for example) that the player may not have walked organically, a route survey option is available: a hireable scout NPC unlocks the route for a one-time fee of 15–25 silver. This is the only case where physical travel can be substituted. The scout NPC explains what they found on the path — terrain, hazards, checkpoint locations — making the route knowledge feel earned even when delegated.

**Precondition 2 — Endpoint relationships:** A route needs a named contact at both origin and destination. These relationships are built through normal play. The player who completed three odd jobs for Harren Voss can use Voss Trading Company as a Hollowford terminus. The player who helped stabilize Grainfell's farms has a relationship with the grain cooperative as an origin point.

**Precondition 3 — Caravan capital:** The player must have the gold to hire a caravan master for the first cycle. Costs range from 8 silver (basic, short route) to 40 silver (experienced master, long or dangerous route) per cycle.

When all three conditions are met, the player opens the route through a conversation with their endpoint contact — not a menu.

## 5.2 Named Caravan Masters

**This is the most important design decision in the trade route system.**

Caravans are not anonymous logistics units. Each has a named caravan master who is a character in the world. There are twelve named caravan masters in the Vale. The player cannot hire anonymous caravans — they hire specific people. Named masters can be permanently lost.

### The Twelve Named Masters

**Darro Aldbridge** — Human, 50s. Former royal roads inspector before the Severance ended the Crown's authority. Runs the safest, most professional caravans on legitimate routes. Expensive. Refuses contraband. Will not operate in contested zones without prior route assessment. Has a daughter in the Vanguard. Carries a grudge against the Reavers who robbed him twice in the first month post-Severance. Best master for Vanguard-territory routes.

**Yeva Saltborn** — Human-Drakeling mixed heritage, 30s. The only caravan master with genuine Crimson Flats experience. Southwatch routes are her specialization. Moderate cost. Has access to the Drakeling camp's informal network — better information on Flats-adjacent route conditions than anyone else provides. Runs a side operation moving items for the Drakeling community, which the Vanguard considers suspicious. Best master for Southwatch and southeastern routes.

**Cobb "Three-Load" Munn** — Human, 40s. Former fence, now "legitimate." Runs the highest-capacity caravans in the Vale — three wagons standard where others run one. Moderate cost, moderate reliability, no questions about cargo. Reaver-network adjacent. Routes through Reaver-controlled territory carry significantly reduced disruption risk when he operates them. The Vanguard has brought him in for questioning twice. He smiled both times. Best master for contraband routes and high-volume agricultural runs.

**Sera of the Understep** — Vaelari Driftless, 20s. The only caravan master who routinely operates through Verdantheart-adjacent routes without losses. Expensive for her specialization, average cost for everything else. Delivers reagents at 15% better quality than any other master on arcane routes, because she understands what she is carrying. Carries purification compounds back from Verdant Flame contacts even when not paid to — she thinks it is the right thing to do. Best master for arcane and reagent routes.

*Eight additional named masters to be developed during production. Each should have: a faction alignment or notable neutrality, a route specialization, a personal history that intersects with at least one active world event, and a moral constraint that affects what cargo they will carry.*

### Permanent Loss Mechanic — Player Communication

Permanent loss only works as a design mechanic if players understand the stakes before experiencing them. The following structure ensures informed consent:

**At first hire:** The NPC who brokers the first caravan hire (typically Harren Voss or a settlement contact) includes a line that contextualizes risk: *"Darro's good. Lost two men last spring to a Reaver ambush. He doesn't forget that."* This establishes that masters have histories with danger — and by extension, that the danger is real.

**First disruption event:** The first time a route is disrupted and the player does nothing, the outcome is **cargo loss and route suspension only** — not a master death. This is the "close call" that teaches the stakes before enforcing them permanently.

**Escalating consequences:** Subsequent unresponded disruptions on the same route escalate: the second is a near-miss with master injury (reduced productivity for 3 days); the third unresponded disruption on the same route puts the master in genuine life-threatening danger. Players who understand the pattern will recognize the third notification as the real stakes moment. Players who have been ignoring all disruptions will have had two prior warnings.

**When a master dies:** The notification is personal — not a system message. The NPC who brokered the original hire has a brief dialogue acknowledging the loss. The master's name is removed from the hire roster permanently. A replacement can eventually be found, but they are a different person, with different skills, and the player starts from Stranger relationship with them.

## 5.3 Route Specializations

Every route has a specialization chosen at establishment. This determines what goods travel, which buyers matter, which risks are elevated, and which upgrades apply. Specialization cannot be changed without dissolving and re-establishing the route.

### Agricultural Routes
**Origins:** Grainfell (grain, herbs, Vaelari medicinals), Ironwood (preserved game, forest herbs)
**Destinations:** Hollowford Market Quarter, frontier settlement general stores, Verdant Flame outposts
**Margin:** Low to moderate (3–8 silver profit per trip per wagon)
**Risk profile:** Low base risk, elevated when corruption zones expand near Grainfell's eastern fields.
**Disruption types:** Crop failure events (goods unavailable at origin; route idles one cycle), corruption contamination (goods devalued 30% on arrival), Vanguard food security seizure (Vanguard conscripts food shipments during military crises — unavoidable at Hostile standing).
**Unique mechanic — Seasonal pricing:** Grain shipped immediately before winter is worth 40% more than grain shipped in summer. Timing route output around the in-game season cycle rewards attentive players.

### Mineral and Material Routes
**Origins:** Ashford (iron ore, stone, coal; lattice crystal gated behind "The Lower Level" quest completion), Ironwood (timber, structural lumber)
**Destinations:** Hollowford Forge District, Vanguard Garrison arms production, Hollow Crown archive construction
**Margin:** Moderate to high (8–18 silver per trip for standard ore; 2–5 gold per lattice crystal shipment)
**Risk profile:** Moderate base risk elevated by Ashford road elevation, Highlands border incidents, and Hollow Crown/Vanguard conflict over mine control in Act II.
**Disruption types:** Road collapse (physical blockage requiring repair quest or reroute), Vanguard nationalization attempt (cargo seized; player must negotiate or fight to recover), mining disaster (supply disruption at origin; route idles until resolved).
**Unique mechanic — Lattice crystal handling:** Lattice crystal requires a specialized sealed container purchased from Hollow Crown merchants. Using a standard wagon degrades cargo by 50% and generates a Vanguard flag event. This is not communicated by a tooltip — it is discovered through play or by asking Hollow Crown contacts.

### Arcane and Reagent Routes
**Origins:** Verdant Flame outpost supply points (herbs, purification compounds, reagents), corruption zone edge salvage operations (lattice residue — requires player to establish a salvage operation first, gated by zone proximity quest)
**Destinations:** Hollowford healer's market, mage-build player personal stockpile, Hollow Crown research purchases
**Margin:** High (15–40 silver per trip, or paid in Lattice Chips for Hollow Crown purchases)
**Risk profile:** High. Verdant Flame supply requires maintained standing — standing drops cut supply. Corruption zone salvage routes have the highest disruption frequency of any route type. Reagents are temperature-sensitive.
**Disruption types:** Standing revocation (Verdant Flame suspends supply if Infamy rises or player acts against the Circle), wild magic events (cargo damaged by unstable lattice energy in transit — weather-hardened wagons partially mitigate), Vanguard confiscation (reagents classified as potentially dangerous materials at Hostile standing).
**Unique mechanic — Master quality:** Sera of the Understep delivers reagents at 15% better condition than any other master. This is the only route type where individual master skill materially affects cargo quality.

### Contraband Routes
**Origins:** Reaver Undercity supply (requires Crew-Adjacent standing), black market acquisition points in contested zones
**Destinations:** Broken Grid fence network, frontier settlement black market contacts, private noble buyers of restricted goods
**Margin:** Very high (30–80 silver per trip, or equivalent Favor Markers) with significant variance — a seized shipment costs cargo value plus a Vanguard Infamy tick.
**Risk profile:** Very high. Vanguard checkpoint encounter is near-certain without active mitigation. Requires either Reaver tunnels (bypasses checkpoints entirely, requires Crew-Adjacent standing) or corrupted guards (bribery, requires renewal every 7 days).
**Disruption types:** Vanguard seizure (cargo confiscated, master detained — player must negotiate release or lose them), informant tip-off (rival faction reports the route; Vanguard response intensity doubles for one in-game week), Reaver shake-down (Varek wants a larger cut than agreed — negotiation or conflict).
**Two-tier structure:** Soft contraband (Vanguard-restricted but not criminalized — certain reagents, Firstborn artifacts, Vaelari cultural items) carries moderate Infamy risk. Hard contraband (weapons, controlled alchemy, stolen archive materials) carries severe Infamy risk and commensurate reward.
**Note:** Contraband routes and Vanguard Patrol Contract upgrades are mutually exclusive on the same route.

### Military Supply Routes
**Origins:** Hollowford Forge District production, Ashford ore, player-owned workshop output
**Destinations:** Vanguard Garrison, frontier settlement defenses, faction military operations
**Margin:** Moderate to high (12–25 silver per trip plus Vanguard Fame gains per shipment delivered)
**Risk profile:** Low — the Vanguard actively protects its own supply chains. Becomes a liability in Act II if the player is aligned with the Vanguard, as the Reavers may begin targeting it specifically.
**Unique mechanic — Fame income:** Military supply routes generate Vanguard Fame alongside gold. At sufficient supply volume, Kael Thornwright acknowledges the player's contribution in dialogue, and specific mission unlocks become available that are not accessible to players who did not invest in Vanguard logistics.

## 5.4 Route Income — Reference Figures

These are design targets, not hard-coded values. Tune during development.

| Configuration | Daily net (single wagon) |
|---|---|
| New route, no upgrades, basic master | 6–12 silver |
| Armed escort added | 4–10 silver (escort cost offset) |
| Insider contact unlocked at destination | 8–15 silver |
| Fully upgraded, experienced master, single wagon | 25–45 silver |
| Fully upgraded, three wagons, high-margin route | 1.5–3 gold |
| Inter-settlement route, Act II+ | 2–4 gold |

**Floor income guarantee:** A player who establishes a route and ignores all disruptions (choosing the "do nothing" option every time) should still net positive after average disruption losses, once caravan wages are subtracted. The floor is not zero — it is low but functional. Players who engage with disruptions should see approximately 40–60% better income than the ignore-everything baseline on the same route.

**Establishment overhead:** The total player time to establish a first route — satisfying preconditions, having the hire conversation, and running the first cycle — should not exceed 20 minutes. If playtesting shows it regularly exceeds this, the precondition requirements need trimming. The first cycle income should feel like a genuine win.

## 5.5 Route Disruption Events — Full Decision Trees

### Bandit Ambush (Most Common)

**Trigger:** Ambush notification names the caravan master and location. States what cargo was taken. Response window: 3 in-game days.

| Response | Requirements | Outcome |
|---|---|---|
| Respond directly | None | Travel to ambush site. Combat engagement. Partial cargo recovered. Small bounty earned. Route resumes next cycle. |
| Reaver network | Crew-Adjacent+ Reaver standing | Costs Favor Markers. 2-day suspension. Route resumes. Cargo outcome uncertain (partial recovery likely). Player never learns exactly what happened to the attackers. |
| Pay extortion | Gold (30–50% of cargo value) | Immediate resumption. 7-day "protection" active. Recurring cost if renewed. Bandits may escalate demands on next occurrence. |
| Reroute | None | Route takes 40% longer. Profit drops one cycle. No engagement required. Does not address underlying threat. |
| Do nothing | — | Route suspended 3 days. Full cargo lost. Master trust decreases. **First occurrence only:** no other consequence. **Second unresponded occurrence:** master injury, 3-day productivity reduction. **Third unresponded occurrence:** master death risk. |

### Vanguard Checkpoint

**Trigger:** New checkpoint established on route. Caravan delayed and assessed a tariff. Ongoing cost if unaddressed.

| Response | Requirements | Outcome |
|---|---|---|
| Pay ongoing tariff | Gold (5–15% of cargo value per cycle) | Route continues. Infamy neutral. Predictable cost. |
| Vanguard merchant exemption | Auxiliary+ Vanguard standing | One conversation with Garrison officer. Tariff reduced to 4% permanently on this route. |
| Reaver tunnel bypass | Crew-Adjacent+ Reaver standing | Checkpoints bypassed entirely. Costs Favor Markers per use or standing arrangement. Generates Vanguard Infamy if discovered. |
| Bribe checkpoint captain | Gold (40–80 silver) | 7 days of checkpoint blindness on this route. Must be renewed. Slow Vanguard Infamy accumulation. |
| Political leverage | Applicable faction standing | A player with standing in a faction that has influence over the Vanguard checkpoint's command chain can apply pressure to waive the checkpoint on their route. Costs standing (spending a favor). Rewards players who built broad faction relationships. |

### Corruption Zone Expansion

**Trigger:** Route passes through a zone that has expanded. Cargo takes passive damage — percentage lost scales with zone density.

| Response | Requirements | Outcome |
|---|---|---|
| Clear the lattice node | Combat | Removes the zone expansion source. Route passable permanently (until next expansion event). |
| Weather-hardened wagon upgrade | Gold (one-time, 60 silver per wagon) | Halves corruption cargo damage. Route continues at reduced loss. Does not address zone growth. |
| Reroute | None | Avoids the zone. 30% longer route. Lower profit. No further corruption risk on this route specifically. |
| Abandon and re-establish | None | Dissolves the route. Player re-establishes on a cleaner path. Loses established relationship and upgrade investment on old route. |

### Faction Seizure (Act III Only)

**Trigger:** A faction the player is at war with controls territory the route passes through. Goods in transit seized.

| Response | Requirements | Outcome |
|---|---|---|
| Retake militarily | Combat capability in the zone | Combat quest to clear the faction presence. Route restored. Significant Infamy cost with seizing faction. |
| Negotiate | Gold or Favor Markers | Pay "transit fee" to seizing faction. Route restored with ongoing cost. Effectively legitimizes their control. |
| Political leverage | Standing with faction that has influence over seizing faction | Apply pressure through faction relationships to release goods without combat or gold. Costs standing. Rewards broad political investment. |
| Abandon | — | Route dissolved. Goods lost. No further losses but income stream ends. |

## 5.6 Route Upgrades

| Upgrade | Cost Type | Cost | Effect | Notes |
|---|---|---|---|---|
| Armed Escort | Ongoing | 8 silver/cycle | Bandit ambush success rate reduced 70% | Does not help with checkpoints or corruption events |
| Vanguard Patrol Contract | Ongoing | 14 silver/cycle | Near-immunity to bandit disruption; checkpoint friction waived on this route | Requires Auxiliary+ standing. Incompatible with contraband routes. Vanguard inspects cargo — restricted goods flagged. |
| Reaver Protection Agreement | Ongoing | 10 Favor Markers/week | Reaver disruptions eliminated; bandit disruption reduced 50% (many bandits operate under loose Reaver affiliation) | If discovered by Vanguard: automatic Infamy gain. Incompatible with Vanguard Patrol Contract. |
| Weather-Hardened Wagons | One-time | 60 silver/wagon | Corruption zone cargo damage halved; cold-weather route efficiency maintained | Near-mandatory for arcane routes crossing corruption zones |
| Insider Contact at Destination | One-time | 20–80 silver per settlement | 15–20% revenue improvement on sell price; no theft events at destination | Requires Trusted relationship with destination merchant before purchase is offered |
| Second Wagon | One-time | 40 silver | Cargo volume ×2, income ×2 | Also doubles cargo lost in a successful disruption. Three-wagon caravans face catastrophic disruption losses if unresponded. |
| Third Wagon | One-time | 40 silver | Cargo volume ×3, income ×3 | See above. Three-wagon caravans should only be run on routes with strong disruption mitigation. |

---

# SECTION 6: PROPERTY AND BUSINESS OWNERSHIP

## 6.1 Property Types

| Type | Base Cost | Primary Function | Faction Interaction |
|---|---|---|---|
| **Storefront** | Low | Sells player-produced goods automatically. Generates passive income from walk-in trade. | District faction control affects clientele volume, price ceiling, and theft risk. |
| **Warehouse** | Medium | Stores goods, components, and trade inventory. Trade route terminus point. Enables speculation on price movements. | Can be seized by hostile faction. Can be fortified (one-time investment reduces seizure risk). |
| **Farm Plot** | Medium | Produces Tier 1 agricultural and organic materials over time. Requires worker assignment. | Corruption zone proximity reduces yield. Verdant Flame standing improves reagent quality from adjacent land. |
| **Workshop** | High | Converts Tier 1 materials to Tier 2 and Tier 3 goods. Requires worker + material inputs. | Ironkin specialist workers increase output quality 80%. Vanguard territory: quality stable, no contraband. Reaver territory: variable quality, no taxation. |
| **Information Broker Office** | High | Generates faction intelligence reports over time. Unlocks intelligence-for-sale dialogue options with multiple factions. | Reaver network required for highest-tier intelligence. Hollow Crown can provide a legitimate front that reduces Vanguard suspicion. |
| **Tavern/Inn** | Medium | Passive gold generation. NPC relationships develop in the player's establishment. Generates low-level side quests organically. | Best placed in high-traffic areas regardless of faction control. Contested zone placement generates unique events. |

## 6.2 Property Acquisition Methods

- **Purchase:** Standard acquisition from settlement property brokers. Available at most Act I+ settlements. No faction requirement for basic properties.
- **Quest reward:** Some faction quests pay out property deeds instead of or in addition to gold. These properties often have pre-established worker relationships.
- **Seizure:** Player can seize abandoned or hostile-faction-owned property through specific quest chains. Morally complex. Generates Infamy with the faction that previously controlled it. The prior owner may reappear.
- **Inheritance:** A small number of properties become available through deep NPC relationship development. Not advertised — discovered through play.

## 6.3 Named Property Histories

Every purchasable property has a prior history the player can discover before acquiring it. This history affects starting conditions and the complications that come with ownership.

**The Westwall Warehouse** (Hollowford, Market Quarter)
Previously owned by a merchant guild that dissolved after its leadership died in the first week post-Severance. The Vanguard has been using it informally as overflow storage. Legal purchase is possible, but the Garrison has not cleared their materials — the player must negotiate this, creating a Vanguard interaction and a small Fame gain if handled diplomatically. Starting condition: 20% capacity occupied by Vanguard materials until resolved.

**The Broken Mill** (Grainfell)
A working grain mill with structural damage from a Severance tremor. Sold at half the price of a functional mill — requires a one-time repair investment (40 silver in materials, three days worker time). Once repaired, it functions as a combined farm plot and processing operation. The prior owner — a widowed farmer who could not afford the repair alone — is still in Grainfell. She cares what happens to the mill. She will occasionally comment on what the player does with it.

**The Underside Stall** (Hollowford, Undercity)
Not legally purchasable. Access is earned through Reaver standing (Crew-Adjacent) and a conversation with Varek Seven-Knives. The player does not own it outright — they hold a rented position in the Undercity Market under Varek's licensing, payable in ongoing Favor Markers. The only retail point for player goods with zero Vanguard oversight and direct access to Undercity clientele who pay premium for certain categories.

*Additional named properties should follow this pattern: a brief history, a prior owner the player may encounter, a starting complication, and one ongoing NPC relationship attached to the property's story.*

## 6.4 Worker System

### Hiring

Workers are found through the world, not a menu. The labor pool at each settlement reflects that settlement's population and circumstances. Grainfell's pool includes farming families, some Driftless Vaelari with botanical expertise, and a handful of Drakeling refugees with geological and heat-metallurgy knowledge. Hollowford's pool is larger and more diverse but skilled workers require either Trusted merchant tier or a gold premium.

Named specialist workers have a brief introduction conversation when hired. They have opinions. They comment on what is being produced. They will tell the player when supply chains are causing production problems. They are characters, not sliders.

### Worker Tiers

| Tier | Wage | Productivity | Availability |
|---|---|---|---|
| Unskilled | Low | Base output rate | Available everywhere |
| Skilled | Medium | +40% output; lower failure rate | Available at larger settlements |
| Specialist | High | +80% output; unique products possible | Rare; often quest-unlocked; race-specific bonuses |

**Race-specific specialist bonuses:**
- Ironkin smiths: +80% on metalworking chains; can produce Vanguard-grade arms quality without the standing gate (but still requires the knowledge unlock)
- Vaelari reagent farmers: +80% on organic and arcane material yields; purification compounds produced at Specialist quality reach Verdant Flame premium price tier automatically

### Worker Loyalty States

Workers operate in one of three loyalty states: **Content**, **Strained**, or **Leaving**.

**Content:** Full productivity at rated efficiency.

**Strained:** 70% productivity. Escalating attrition risk. Caused by: unpaid or late wages, faction conflict in the worker's zone, hazardous working conditions, or being assigned work they find morally objectionable. Workers who are strained for more than 5 in-game days without resolution begin showing Leaving behavior.

**Leaving:** Worker gives one cycle's warning in dialogue, then departs. Cannot be retained through wages alone at this stage — the underlying cause must be addressed or the departure is inevitable.

**Maintaining loyalty:** Wages are the baseline. Periodic property investment (workers get better tools, better conditions) provides a loyalty buffer. The player's faction reputation in the worker's zone affects loyalty independently — Reaver extortion operating against workers in a zone damages loyalty faster than anything else.

### Worker Moral Constraints

Named specialist workers have moral limits that affect what they will produce. These are character traits, not bugs.

**Maret** (example Ironkin smith specialist): Will not produce contraband weapons. This constraint is not a hard block — it is a conversation. When the player attempts to assign her to contraband production, she refuses and explains why. The player then has three options:

1. **Respect the refusal:** Maret stays and is assigned to legitimate metalworking. The contraband chain is staffed with an unskilled worker at reduced quality and output.
2. **Attempt persuasion:** Dialogue check. Fails unless the player has a deep relationship with Maret (20+ cycles of work together, at least one personal quest interaction). If it succeeds, she agrees reluctantly at a loyalty cost — she will continue working but her loyalty state moves to Strained and recovers slowly. Using persuasion more than once exhausts her goodwill entirely.
3. **Replace her:** Maret departs immediately. Her specialist bonus is lost. The player starts from Stranger with any replacement worker. This is a story moment — the player chose profit over a person they built a relationship with. The game does not editorialize, but it does remember.

*Every specialist worker should have at least one moral constraint defined during production. The constraint should fit their character and create a moment of genuine player choice when the player's business evolution encounters it.*

## 6.5 Property Incident Events

Beyond route disruptions, properties generate their own incident events approximately once per 10–15 in-game days. These are not crises — they are the texture of running a business in a broken world.

**Supply shortage:** A raw material the production chain needs has spiked in price or become unavailable. Player options: pay the new market price (income drops temporarily), find an alternate source (quest hook), or pause production (no cost, no income, no lasting consequence).

**Worker dispute:** Two workers have a conflict reducing productivity. The player can hear both sides and adjudicate, or ignore it (one worker leaves). Disputes typically have a valid position on both sides — they are micro-versions of the broader moral complexity the game is built around.

**Local reputation event:** The storefront did something that affected neighborhood reputation. Examples: sold goods to refugees at fair prices during a crisis (small local Fame gain), sold restricted goods that caused a public incident (Vanguard Infamy tick, storefront reputation damage). These are notifications — they do not require player action — but they reinforce that the business exists in a social world.

**Structural damage:** Combat events near a property, corruption zone expansion, or severe post-Severance weather damage the building. Player can invest in repair (gold and worker time) or operate at reduced capacity indefinitely.

## 6.6 Property in Faction Conflict

Every property carries a faction zone tag. When the controlling faction of that zone changes in Acts II/III:

- **Allied faction takes control:** Property protected. Possible bonus: Vanguard adds guard patrol (reduces theft events); Verdant Flame purifies adjacent corruption (farm yield increases); Reavers add black market access (storefront gains Undercity clientele at premium prices).
- **Hostile faction takes control:** Property at risk. Player must negotiate (spend Fame), pay protection (ongoing gold), defend it through combat, or accept seizure and lose the asset.
- **Contested zone:** Income halved, disruption event frequency doubles. However, specific trade opportunities unique to contested zones open: wartime profiteering on military goods, information arbitrage between factions who both want intelligence on each other's movements.

---

# SECTION 7: PRODUCTION CHAINS

## 7.1 The Four-Phase Loop

Production chains are not passive timers. They have four distinct player-facing phases.

### Phase 1 — Input Procurement
The player ensures raw materials are arriving at the workshop via trade route delivery (automatic, route overhead applies), direct merchant purchase (more expensive, no overhead), or personal gathering (free, time-intensive). The key economic decision: is a dedicated supply route worth establishing, or is spot-purchasing cheaper given route setup cost and ongoing caravan wages? For early workshops, spot-purchasing is usually correct. For workshops producing at consistent high volume, a dedicated supply route becomes profitable around the 15th production cycle.

### Phase 2 — Production
The workshop converts input to output over a defined cycle time. The player is not required to be present. However, checking in generates worker commentary that often contains market intelligence not available from any other source. Workers notice things: demand spikes, faction movements affecting supply, upcoming events that will shift prices. This information is only available through the relationship of being present.

### Phase 3 — Output Disposition
When goods are ready, the player chooses: auto-sell through a storefront (current market price), warehouse storage (speculating on price increases), route to a trade destination (via a delivery route), or personal use (crafting, combat consumables). This decision is never invisible. The player makes it actively each cycle, or delegates it via standing orders — which require Partner tier with the receiving merchant.

### Phase 4 — Reinvestment Decision
After 5–7 cycles, the player has enough data to ask: does this chain warrant adding a second worker? Upgrading to Tier 2 workshop capacity? Switching to a higher-value output? A player who notices Verdant Flame reagent demand spiking and has the materials to pivot to purification compounds has a meaningful window to capture that margin — if they reconfigure their workshop in time. This is where the production chain becomes active economic strategy rather than passive income.

## 7.2 Production Chain Reference

### Tier 1 Raw Materials
Gathered through exploration, farm plots, or merchant purchase.

| Category | Materials |
|---|---|
| Agricultural | Grain, livestock, timber, fiber |
| Mineral | Iron ore, stone, coal, crystal fragments |
| Organic | Herbs, animal components, fungal matter |
| Arcane | Lattice residue (corruption zones), Wellspring reagents, relic shards |

### Tier 2 Refined Goods

| Input | Output | Cycle Time | Primary Market | Base Margin |
|---|---|---|---|---|
| Grain + livestock | Provisions | 1 day | Universal | Low–Med |
| Iron ore + coal | Steel components | 2 days | Vanguard, Ironkin | Medium |
| Herbs + lattice residue | Purification compounds | 3 days | Verdant Flame, general healing | Med–High |
| Crystal fragments + arcane | Relic stabilizers | 3 days | Hollow Crown, mage builds | High |
| Timber + stone | Construction materials | 2 days | Universal (Act III peak demand) | Medium |

### Tier 3 Specialized Goods

| Output | Requirements | Cycle Time | Market | Margin |
|---|---|---|---|---|
| Vanguard-grade arms | Steel components + Tier 3 Vanguard Fame | 5 days | Vanguard direct contract | Very High |
| Purified reagents | Purification compounds + Circle Ally standing | 4 days | Verdant Flame premium | High |
| Engineered relics | Relic stabilizers + Hollow Crown archive knowledge | 7 days | Hollow Crown, specialist buyers | Very High |
| Contraband stockpile | Multi Tier 2 + Reaver network access | 7 days | Undercity only | Highest / high risk |

## 7.3 The Compound Business

The most powerful economic configuration is not a single maximized route or a single optimized workshop. It is a compound business — a player-owned network that chains input sourcing, processing, and distribution.

**Example A — Vanguard-aligned, Act II:**
Ashford farm plot → iron ore produced → Hollowford workshop (Maret assigned) → steel components → Forge District storefront → Vanguard Garrison direct contract

Involves: two properties, one supply route, one production cycle, one faction contract. Net income at full operation: approximately 2.5 gold per in-game day. Extending to Vanguard-grade arms production with Maret operating at specialist capacity pushes daily output toward 4 gold plus ongoing Vanguard Fame.

Narrative consequence: Kael Thornwright knows the player's name. The Reavers view this operation as a legitimate target in Act II. The Verdant Flame has an opinion about the player arming the faction that opposes them. The compound business creates story stakes, not just income.

**Example B — Reaver-aligned, Act II:**
Corruption zone edge salvage operation (lattice residue) → Hollowford workshop → purification compounds → Undercity stall → sold at black market premium, bypassing Vanguard price controls

Requires four separate unlocks: the salvage operation (quest-gated), the workshop (property purchase), the production knowledge (Verdant Flame or independent research unlock), and the Undercity stall (Reaver standing). Margin is significantly higher than the legitimate chain because the Undercity pays 40% above market for purification compounds in restricted supply.

**Moral complexity — mechanically realized:** This chain harvests from zones the corruption is actively destroying, processes the material into healing compounds, and routes them through criminal distribution rather than to the communities that need them most. The Verdant Flame will eventually notice their compounds are being undercut in the Undercity supply. Senna Brightwell, a named Verdant Flame field healer operating near Grainfell, is consistently short on compounds and mentions it in ambient dialogue — she is the human face of the supply problem the player's contraband chain created. The player who walks past her after cornering the Undercity supply will hear about it without any quest marker pointing at the connection.

---

# SECTION 8: WEALTH AS SOCIAL POWER

## 8.1 Gold Buys Options, Not Just Gear

The economy's most important design principle in practice: wealth should unlock narrative options unavailable through any other system.

**Bribery:** Vanguard checkpoints, individual guards, and some faction operatives can be bribed. Cost scales with what the player is trying to accomplish — moving contraband costs more than skipping a papers check. Individual guards remember. Bribing the same guard twice in a short window triggers suspicion. At high Vanguard Fame, discovered bribes are treated as a misunderstanding; at Hostile standing, they are treated as evidence.

**Funding quests:** Several Act II and Act III quests have gold-based resolution options. A village facing a food shortage can be resolved by funding grain shipments directly — the quest completes faster, settlement disposition improves significantly, and the player earns a "Benefactor" flag affecting later dialogue and pricing. Kael's supply request to House Eltaryn can be interrupted by the player funding it personally — this shifts the political dynamic (Eltaryn's leverage is removed) and earns significant Vanguard Fame.

**Intelligence purchasing:** The Hollow Crown sells information. So does Varek Seven-Knives, in a different register. Purchased intelligence gives the player an information advantage that changes how they approach subsequent quests — they know what is waiting before they arrive, or who the relevant NPCs actually are, or what the real objective of a mission is versus what they were told.

**Settlement investment:** At Wealthy tier, the player can invest in frontier settlement development beyond what base quests unlock. Additional investment in Grainfell's farms changes the settlement visually. Workers who were desperate survivors in Act I are running small businesses in Act III. The investment is visible in the world state in ways that feel real.

## 8.2 Wealth Tier Thresholds

| Tier | Approximate Gold | Core Unlock | Social Signal |
|---|---|---|---|
| Destitute | 0–50 silver | Survival. Basic food and repair. | NPCs treat the player with indifference or pity. |
| Surviving | 50 silver–5 gold | Gear upgrades affordable. First crafting possible. | Merchants recognize the player as a regular customer. |
| Established | 5–50 gold | Trade route activation. First property purchase eligible. | Harren Voss invites the player to his office to discuss business. |
| Wealthy | 50–300 gold | Production chains active. Quest funding viable. Bribery reliable. | Faction representatives approach the player for economic partnership. |
| Magnate | 300 gold+ | Settlement-level investment. Political spending. Endgame leverage. | NPC dialogue references the player's reputation as an economic force in the Vale. |

**Design note:** These are thresholds the player feels through NPC behavior before any UI indicator confirms them. Tier transitions should be experienced through the world, not a notification.

---

# SECTION 9: THE LIVING PRICE INDEX

## 9.1 Design Intent

The price index is the economy's environmental storytelling mechanism. Price movements should signal world state to the player before any NPC explains it explicitly. Players who pay attention to prices and act on what they reveal are experiencing the world as a system.

Six commodity categories are tracked. All are affected by faction actions, world events, player choices, and the time elapsed since the Severance. Prices are visible on all merchant screens and in the Ledger.

| Category | Primary Drivers |
|---|---|
| **Food & Provisions** | Farm yields, corruption zone spread, Vanguard stability, Drakeling camp state |
| **Military Goods** | Vanguard demand, faction conflict intensity, player production volume |
| **Reagents & Components** | Verdant Flame standing, corruption zone density, Wellspring health |
| **Relics & Arcane** | Hollow Crown activity, Reaver trafficking volume, Firstborn ruin access |
| **Contraband** | Reaver dominance, Vanguard suppression intensity, player black market standing |
| **Luxury Goods** | Hollow Crown political stability, trade route safety, noble NPC survival |

## 9.2 Key Price Signal Events

**The Bread Canary:** When bread price moves from 3 copper to 6+ copper, the farms are in crisis. The player notices before being told. Investigating the cause reveals a quest hook. This is the clearest example of the price index as environmental storytelling — the economy signals a problem, the player investigates, the cause becomes a mission.

**The Reagent Spike:** When Verdant Flame supply routes are disrupted — by player action or world events — healing and alchemical reagent prices jump. A player invested in alchemy notices immediately and has strong motivation to address the disruption, regardless of their faction alignment. The economy creates non-faction-driven quest motivation.

**The Luxury Collapse:** When Hollow Crown political influence wanes in Act II, luxury goods markets destabilize. Wine becomes cheap (hoarding nobles dumping stock). Art becomes nearly worthless. Items that were expensive in Act I are suddenly available at discounts — and simultaneously, players who invested in luxury trade routes see income drop. The economy reflects political reality faster than any NPC reports it.

**The Black Market Surge:** When Vanguard tightens enforcement in Hollowford (triggered by specific main quest events), restricted goods prices spike at legitimate merchants. The Undercity simultaneously gets better-stocked, because suppression drives demand underground. Players with Reaver standing benefit; players without it face genuine supply problems for certain crafting materials.

---

# SECTION 10: THE MANAGEMENT INTERFACE

## 10.1 Design Principles

All economic complexity must be accessible without feeling like accounting homework. The management interface operates on one principle: **the player sees what matters, when it matters, and can act on it immediately.**

## 10.2 The Ledger

Accessible from any property or from the Echo's management menu. Single-screen overview showing:

- All active routes with status (operating, disrupted, suspended), current caravan master, next expected cycle
- All owned properties with current worker count, loyalty state summary, and last cycle income
- Pending decisions (disruption events with their response options and remaining time window)
- Income summary: last 7 in-game days actual, projected 7 in-game days
- Price index snapshot: current values and directional trends for all six categories

The Ledger is designed to be fully read in 30 seconds. No decision requires more than two button presses to act on from this screen. It is never the player's only interface to their economy — it is the at-a-glance layer.

## 10.3 In-Person Property Management

Visiting a property physically opens its full management screen. Workers greet the player. The workshop shows the current production queue. The storefront shows current inventory and recent sales. The farm shows crop status and yield projection.

Management done in person is richer than management done through the Ledger. The player receives worker commentary about market conditions, supply problems, and local events. This is information they will not get remotely. Players who visit their properties regularly have a genuine information advantage.

## 10.4 The Echo as Economic Advisor

At high Echo Interface investment (see SD_07 Combat & Build Framework for Echo Interface levels), the Echo provides ambient economic observations. It does not automate decisions. It provides information:

- Flagging when a price index movement represents a selling opportunity the player has not acted on
- Noting when a route has been suspiciously quiet and may have a disruption the player has not been notified about yet
- Observing when a worker's loyalty state is declining before the formal incident event triggers

This is not available at low Echo Interface levels. It is a late-game information reward for players who developed the Echo relationship — and it reinforces that the Echo is genuinely invested in the player's success in the world.

---

# SECTION 11: CROSS-DOCUMENT DEPENDENCIES AND GAPS

## 11.1 SD_05 Relationship

This document supersedes SD_05 Section 6 (The Economic System). SD_05 Section 6.5 (Faction Economic Warfare) remains canonical and is not duplicated here — it describes how faction actions shift the price index and affect zone control, which are the inputs that drive the systems described in this document. Both documents are required for full economic system understanding.

**Required SD_05 update:** SD_05 Section 6.2 (Trade Routes, Establishing a Route, bullet 1) currently reads "Player must have physically traveled the route at least once." This should be updated to: "Player must have physically traveled the route at least once, OR completed a route survey through a hireable scout NPC. Fast travel does not satisfy this requirement." This document is the canonical source for that clarification.

## 11.2 Resolved Gap — Faction Seizure Political Leverage Option

SD_05 Section 6.2 (Route Disruption Events — Faction Seizure) listed three player responses: retake militarily, negotiate, or abandon. This document adds a fourth: political leverage. A player with standing in a faction that has influence over the seizing faction can apply that influence to release goods without combat or gold expenditure. This costs standing (spending a favor) and rewards players who built broad faction relationships rather than deep single-faction alignment. This fourth option should be added to SD_05 Section 6.2 during the next consistency pass.

## 11.3 Resolved Gap — Reaver Favor Markers and the Cut System

SD_05 Section 6 implies that Reaver cuts apply to all Hollowford trade below Tier 3 Reaver Fame. Favor Markers (defined in this document, Section 2.1) provide the same immunity as Tier 2 Reaver Fame with respect to Reaver cuts on trade routes. This makes the Favor Marker economic path a genuine alternative to the Fame track for economically-minded players operating within the Reaver network. SD_05 should be updated to reflect this equivalency.

## 11.4 Open Dependency — SD_07 Echo Interface Levels

Section 10.4 of this document references Echo Interface investment levels for the economic advisor function. The specific investment threshold that unlocks economic observations should be defined during the SD_07 consistency pass. Recommend: mid-tier Echo Interface investment (not the highest tier — this should be accessible to players who engaged meaningfully with the Echo, not only to those who maximized it).

---

*End of Document 11: Economy System v1.0*
*This document supersedes SD_05 Section 6 (The Economic System sketch).*
*Next required action: SD_05 consistency pass to update Section 6.2 (route survey clarification, political leverage option, Favor Marker equivalency).*
