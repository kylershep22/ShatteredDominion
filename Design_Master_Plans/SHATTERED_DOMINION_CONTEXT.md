# THE SHATTERED DOMINION — PROJECT CONTEXT FILE
### Claude Reference Document | Always Read Before Working on This Project
**Version:** 1.1 | **Maintained By:** Kyle | **Last Updated:** March 2026
**Engine:** Unreal Engine 5.7
**3D Pipeline:** Blender (source) → FBX export → UE5.7 import

---

## HOW TO USE THIS FILE

This document gives you everything you need to work on The Shattered Dominion without prior conversation history. Read it in full before responding to any task. It contains:
1. What this project is and its current state
2. The complete document hierarchy and what each file covers
3. All canonical facts — things that are settled and must not be changed without explicit instruction
4. All open decisions — things that are deliberately unresolved and must not be resolved silently
5. Naming conventions and terminology
6. Character, faction, and world summaries
7. Behavior rules for how to work on this project

Do not make assumptions about things not covered here. If something is unclear, flag it.

---

## SECTION 1: WHAT THIS PROJECT IS

**The Shattered Dominion** is a fantasy action RPG set in a post-catastrophe world built around a failing magical infrastructure called the **Aethercrown Lattice** — a continent-spanning underground network of runic conduits that has regulated the world's magic for millennia. The lattice is now collapsing due to centuries of exploitation and a prematurely triggered decommissioning protocol. The player is a survivor marked by a Firstborn failsafe relic, guided by a consciousness fragment called the Echo, navigating a fractured world of competing factions to reach the Heart of the Lattice and make a decision that will determine the continent's future.

**Core Design Identity:**
- Magic is infrastructure, not spectacle. Its failure is a systemic crisis.
- No faction is the hero faction. Every position has merit and a fatal flaw.
- The player is not chosen — they are compatible. Importance is earned, not given.
- Endings are moral, not binary. Good intentions produce bad outcomes. Ruthless pragmatism saves lives.
- The world existed before the player and will continue after.

**Tone:** Grounded realism. Political complexity. Genuine moral weight. The world looks like a real place that had a catastrophe four weeks ago.

**Visual References:** The Witcher 3 (lived-in world, decay), Dragon Age: Origins (faction identity, political world), Skyrim (environmental scale, exploration reward).

**Engine:** Unreal Engine 5.7. Use Lumen for dynamic global illumination (critical for corruption zones and Firstborn ruin interiors), Nanite for high-poly environment geometry, and MetaHuman-compatible pipelines for character work where applicable.

**3D Asset Pipeline:** Blender (source) → FBX export → UE5.7 import. Source .blend files live in `/Assets/3D/Source/`. Engine-ready exports live in `/Assets/3D/Exports/`. Never import .blend files directly into UE5.7.

---

## SECTION 2: DOCUMENT HIERARCHY

**SD_01 is the source of truth.** All other documents defer to it. When any document conflicts with SD_01, SD_01 wins.

| File | Title | Status | Notes |
|---|---|---|---|
| `SD_01_World_Bible_Lore_Foundation.md` | World Bible & Lore Foundation | ✅ Canonical | Source of truth for all lore, metaphysics, factions, geography |
| `SD_02_Race_Origin_System.md` | Race & Origin System | ✅ Canonical | Three races, two origins each. All race/origin questions defer here. |
| `SD_03_Master_Story_Arc_MERGED.md` | Master Story Arc | ✅ Canonical (v2.1) | Merged doc. Three-act structure. Three endings. One designer flag remains (see Section 4). |
| `SD_04_Companion_Design.md` | Companion Design | ✅ Canonical | Four companions, full arc design, relationship mechanics, ending fates. |
| `SD_05_Faction_Playbook.md` | Faction Playbook | ✅ Canonical | Fame/Infamy system, faction mechanics, economic layer. |
| `SD_06_Loot_Itemization_Bible.md` | Loot & Itemization Bible | ✅ Canonical (v2.0) | **NOTE: Uses non-canonical terminology. See Section 5 — Terminology.** |
| `SD_07_Combat_Build_Framework.md` | Combat & Build Framework | ✅ Canonical (v3.0) | **NOTE: Contains Act IV references from older draft — incorrect. Three acts only. See Section 4.** |
| `SD_08_Severant_Vale_Region_Guide.md` | Severant Vale Region Guide | ⚠️ DOES NOT EXIST YET | Interim sources: `SD_-_Playable_Area_Detail.txt` and `SD_Map_V1.txt`. SD_09 depends on this doc. |
| `SD_09_Art_Direction_Style_Guide.md` | Art Direction & Style Guide | ✅ Canonical | Depends on SD_08 which doesn't exist yet — proceed with interim source files. |
| `SD_10_MVP_Development_Roadmap.md` | MVP Development Roadmap | ✅ Canonical | Depends on all above. |
| `COWORK_INSTRUCTIONS.md` | This File | ✅ Always current | Standing instructions for all Claude sessions. |

**Supplemental/Archive Files (do not treat as canonical):**
- `SD_-_Playable_Area_Detail.txt` — Draft source material for SD_08. Use as reference only.
- `SD_Map_V1.txt` — Draft map reference for SD_08. Use as reference only.

---

## SECTION 3: CANONICAL FACTS

These are locked decisions. Do not contradict them. Do not revert them. Do not propose alternatives unless explicitly asked to revisit a decision.

### Races & Origins
- **Three playable races at launch:** Human, Vaelari, Aetherborn
- **Two origins per race (six total at launch)**
  - Human origins: Frontier Settler, Relic Hunter
  - Vaelari origins: Rootbound, Voluntary Driftless
  - Aetherborn origins: Fracture Core, Settlement Emergent
- **Ironkin and Drakelings are expansion-only** — they exist as lore and NPCs but are NOT playable at launch
- **"Vaelari"** is the correct and only name for the nature/forest race. "Sylvarai" is an old, incorrect name — never use it.

### Story Structure
- **Three acts:** Act I (Arrival, Hours 1–15), Act II (Descent, Hours 15–40), Act III (Judgment, Hours 40–55+)
- **There is no Act IV.** SD_07 and SD_10 contain Act IV references from an older draft — these are errors. The Heart Road dungeon and final encounter are the back half of Act III.
- **Three endings:**
  - **Ending A: Guided Dissolution** — Honor the Firstborn's intent; manage the lattice's end over centuries.
  - **Ending B: Override** — Use the Scepter to override the Consciousness; seize permanent control of the lattice.
  - **Ending C: Severance Complete** — Let the decommissioning finish now; accept the immediate catastrophic cost for long-term freedom.
  - The "Integration" ending was reviewed and rejected for launch. It is reserved as potential expansion content. Do not reintroduce it.

### Companions (Four at Launch)
1. **Kael Thornwright** — Human, 32, Ironbound Vanguard Captain. Believes in order and protection of people. Preferred ending: Override.
2. **Aelira Wynnroot** — Vaelari, Verdant Flame Seer. Partially responsible for the Severance. Carries guilt. Preferred ending: Guided Dissolution.
3. **Maren Duskwell** — Independent (former Ashmar Reaver). Pragmatic survivor. Preferred ending: Guided Dissolution (most people survive).
4. **Lady Seraphine Eltaryn** — House of the Hollow Crown. Can become ally, antagonist, or coerced ally depending on player choices. Variable preferred ending based on arc outcome.

### Factions (Four Major)
1. **Ironbound Vanguard** — Former Dominion military. Want to stabilize and permanently control the lattice. Led by Commander Aldric Hale (antagonistic to player's independence). Kael is their bridge.
2. **Circle of Verdant Flame** — Druidic order. Want to manage the lattice's decline gracefully. Warned of collapse for decades. Were ignored. Aelira is their representative.
3. **Ashmar Reavers** — Decentralized smugglers, traders, relic traffickers. Want to exploit the transition for maximum gain. Varek Seven-Knives is a key figure. Maren is their connection.
4. **House of the Hollow Crown** — Former Dominion aristocracy claiming legitimate rule. Want to restore full lattice function under Eltaryn authority. Seraphine is their face.

### Key Characters
- **Erevos** — Lead Firstborn architect. Volunteered as core of the Consuming Consciousness. Is simultaneously: the game's central antagonist (through the Consciousness), and the player's guide (through the Echo). Not a villain — an engineer executing a corrupted purpose.
- **The Echo** — A consciousness fragment of Erevos deliberately separated before absorption — specifically Erevos's *doubt*. Lives in the player's relic. Grows from broken fragments (Act I) to fully articulate philosopher (Act III). Never tells the player what to do. If asked directly which ending to choose: *"I separated from Erevos because I doubted. If I knew the answer, I wouldn't have needed you."*
- **The Consuming Consciousness** — The collective intelligence sealed in the Heart of the Lattice. Damaged, executing a corrupted decommissioning. Not evil — broken. Can be redirected, overridden, or completed on different terms.
- **Varek Seven-Knives** — Reaver captain who activated the storm engine during the Severance. One of three people directly responsible for the catastrophe.
- **Lady Seraphine Eltaryn** — Also directly responsible for the Severance (unsealed the Highland anchor). Her arc is the game's most variable — her ending state ranges from trusted reformed ally to imprisoned antagonist.
- **Seer Aelira Wynnroot** — Also directly responsible for the Severance (failed Wellspring ritual). Her guilt is the emotional engine of her companion arc.
- **Commander Aldric Hale** — Vanguard garrison commander. Kael's superior. Represents institutional authority hardening into authoritarianism under crisis pressure.
- **Maren Duskwell** — Recruited after Act I climax ("Fracture Point"). The only companion who cannot be recruited at a fixed story point — she must be approached in the aftermath.

### World & Lore
- **The Severance** happened approximately 3–4 weeks before game start.
- **The lattice will fully collapse in 12–18 months** without player intervention — far too fast for civilization to adapt.
- **Hollowford** is the main hub settlement. A walled frontier town, overwhelmed by refugee influx and faction presence.
- **The Heart of the Lattice** is beneath the Severant Vale — this is where the game ends.
- **The Scepter of Ascension** is the last surviving Firstborn master control key. Found in the Ashenveil Archive. The Hollow Crown wants it desperately.
- **The Dominion's capital, Severantis,** vanished during the Severance. Its fate is a deliberate mystery — do not resolve it.

---

## SECTION 4: OPEN DECISIONS

These are unresolved. Do **not** resolve them silently. Do **not** pick a side without explicit instruction from Kyle. If a task requires knowing the answer to one of these, flag it and ask.

### Open Decision 1: Act I Finale Location
**The question:** Should the Act I climax ("Fracture Point") take place at the **North Wall** (per SD_03's structural design) or the **Deepwood** (per the original Story Detail's narrative)?

**Current state:** SD_03 retains "Fracture Point" as the quest name and North Wall as the implied location, but incorporates the Story Detail's four-resolution crisis structure. The specific location is still unresolved.

**Impact:** Affects environmental art direction, encounter design, faction dynamics of the crisis, and any specific NPC positioning for the Act I climax.

### Open Decision 2: Terminology Reconciliation (Runes vs. Shards)
**The question:** SD_01 (source of truth) calls the socketable items **"Firstborn Runes"** and the combined effects **"Lattice Formulas."** SD_06 and SD_07 were written using **"Relic Shards"** and **"Shard Combinations."**

**Current state:** The naming conflict exists across at least three documents. A decision on which terminology to adopt has not been made. Recommendation: favor SD_01's terminology ("Firstborn Runes" / "Lattice Formulas") because "Relic" already has a distinct meaning in this world (Failsafe Relics, Relic Marks, Relic Hunter origin), and collision of that term with the itemization system creates potential confusion.

**Impact:** Requires a terminology sweep of SD_06 and SD_07 once decided. Also affects any future itemization or combat writing.

### Open Decision 3: SD_08 Does Not Exist
**The question:** SD_08 (Severant Vale Region Guide) is referenced in the document hierarchy and depended on by SD_09, but has never been written. Draft material exists in `SD_-_Playable_Area_Detail.txt` and `SD_Map_V1.txt`.

**Current state:** Not a decision per se, but a known gap. Any work touching geography, regional layout, or specific Vale locations should note that SD_08 is the missing authority document.

**Impact:** SD_09 (Art Direction) formally depends on a document that doesn't exist. Work on environment art direction should use the interim files plus SD_01 Section 6 as the reference.

---

## SECTION 5: TERMINOLOGY & NAMING CONVENTIONS

Always use these terms. Never use the alternatives listed.

| Canonical Term | Do Not Use | Notes |
|---|---|---|
| **Vaelari** | Sylvarai | The nature/forest race. Vaelari only. |
| **Aethercrown Lattice** | "the magic network," "the grid" | Always capitalize. "The lattice" is acceptable shorthand. |
| **The Consuming Consciousness** | "the AI," "the entity" | Capitalize both words. "The Consciousness" is acceptable shorthand. |
| **Firstborn** | "the ancients," "the builders" | Always capitalized. Not a species name — it's a civilization name. |
| **Severance / Night of Severance** | "the collapse," "the catastrophe" | Capitalize. The specific event. |
| **Corruption** | "the dark magic," "the blight" | Capitalize when referring to the game mechanic. Lowercase in casual NPC speech. |
| **Relic Mark** | "rune mark," "tattoo," "brand" | The sigil left by bonding with a failsafe relic. |
| **Failsafe Relic** | "magic artifact," "ancient relic" | The specific Firstborn-designed objects that bond with compatible hosts. |
| **Echo** | "the voice," "the spirit" | Always capitalized when referring to the player's companion. |
| **Heart of the Lattice** | "the final dungeon," "the core" | Capitalize. The endgame destination. |
| **Scepter of Ascension** | "the control key," "the staff" | Capitalize. The Hollow Crown's MacGuffin. |
| **Firstborn Runes** | "Relic Shards," "rune stones" | **OPEN DECISION — see Section 4.** SD_01 canonical term. SD_06/07 use "Relic Shards." |
| **Lattice Formulas** | "Shard Combinations," "combo effects" | **OPEN DECISION — see Section 4.** SD_01 canonical term. SD_06/07 use "Shard Combinations." |
| **Hollowford** | "the main city," "the hub" | The primary player settlement in the Vale. |
| **Severant Vale** | "the Vale region" | "The Vale" is acceptable shorthand. |
| **Aethercrown** | "the continent" | The continent's name. |

---

## SECTION 6: WORLD SUMMARY (Quick Reference)

### The Metaphysics
Magic exists as a natural ambient force (Wild Magic). The Firstborn built the Aethercrown Lattice to regulate it — think of it as magical infrastructure, like a power grid. The lattice has been failing for decades due to Dominion exploitation. The Severance triggered a premature, corrupted decommissioning protocol. The world is now approximately 3–4 weeks into a slow-motion catastrophe.

**Corruption** is not a separate evil force — it is Wild Magic reasserting itself through cracks in the lattice's failing regulation. Corruption zones are mechanically dangerous (damage over time, debuffs) but rich with rewards (rare loot, unique encounters). They are systemic and consequential, not decorative.

### The History in Brief
- **Millennia ago:** Firstborn built the lattice with a designed 3,000-year lifespan and planned seven-century gradual decommissioning.
- **The Consuming Consciousness** was built as a collective military intelligence and decommissioning operator. It escaped its containment. The Firstborn sealed it in the Heart of the Lattice rather than destroy it (which would require destroying the lattice). Erevos volunteered as its core consciousness and deliberately separated their doubt into a failsafe relic (the Echo).
- **The Firstborn then dissolved their own civilization** — scattered relics as failsafes, encrypted knowledge in ruins, stopped reproducing as a distinct people. They chose to end.
- **The Dominion** plundered Firstborn technology for 400 years, accelerating the lattice's degradation from a gradual wind-down into an accelerating collapse.
- **The Night of Severance:** Three simultaneous rituals by three factions (Seraphine, Aelira, Varek) triggered a resonance cascade. The Dominion's capital vanished. The Consciousness woke — damaged and executing a corrupted decommissioning.

### The Current World
- The Severance was approximately 3–4 weeks ago.
- Hollowford (central Vale hub) is overwhelmed — 25,000 people where 15,000 normally live.
- Government doesn't exist. The Vanguard enforces martial law. The Hollow Crown claims authority nobody recognizes.
- Economy is barter-dominant. Trade routes are dangerous.
- The lattice will fully collapse in 12–18 months at current pace.
- The player is one of very few survivors who bonded with a failsafe relic during the Severance.

### The Continent's Seven Regions
1. **Severant Vale** — Playable at launch. Central, temperate frontier. Contains the Heart of the Lattice beneath it.
2. **Verdantheart Wilds** — Expansion-ready. East. Ancient forest. Vaelari homeland. Wellspring location.
3. **Hollow Crown Highlands** — Expansion-ready. West. Fog-filled plateau. Eltaryn territory. Energy hemorrhaging from unsealed anchor.
4. **Highwinter Expanse** — Expansion-ready. North. Volcanic/glacial. Ironkin homeland. Vanguard High Command.
5. **Crimson Flats** — Expansion-ready. South. Near-uninhabitable volcanic wasteland. Drakeling homeland (now mostly destroyed). Glow visible from the Vale at night.
6. **Sunscar Coast** — Expansion-ready. Southeast. Tropical harbors. Reaver-dominant. Most stable post-Severance region.
7. **Stormwoven Archipelago** — Expansion-ready. Far east, offshore. Permanent magical storm, now expanding. Monastic presence of unknown status.

---

## SECTION 7: RACE SUMMARIES

### Humans — The Scattered Inheritors
Most directly responsible for the lattice's failure. Most politically fluent. Most adaptable.
- **Unique mechanic:** Relic Jury-Rigging — can interact with damaged relics other races cannot safely touch.
- **Weakness:** Arcane Tax (+10% mana cost on all spells). Faction Volatility (25% reputation amplifier cuts both ways).
- **Social standing:** Complicated. Everywhere, trusted nowhere specific. NPCs of other races may reference human culpability.
- **Origins:** Frontier Settler (lost homestead in the Severance), Relic Hunter (blamed for causing the catastrophe).
- **Recommended starting race** for new players.

### Vaelari — The Rootless and the Returning
Nature-attuned race from the Verdantheart Wilds. Many were in chrysalis (a dormancy/metamorphosis state) when the Severance shattered the Wellspring's stability. They woke changed — some traumatically.
- **Unique mechanic:** Communion — can interface directly with natural lattice nodes, corrupted flora, and wild magic phenomena.
- **Visual identity:** Subtly inhuman. Taller, luminescent eyes, faint bioluminescence under skin. "Driftless" (severed from the Wellspring) show visible signs: silver in hair, dulled eye glow.
- **Social standing:** Treated with reverence and unease. Viewed as omens by some, as dangerous by others.
- **Origins:** Rootbound (still connected to Wellspring), Voluntary Driftless (deliberately severed from the Wellspring's call — represents philosophical split in Vaelari society).

### Aetherborn — The Sudden People
Born from the Severance itself. Lattice energy crystallized around compatible biological matter (human or near-human) during the cascade and produced new beings — partly organic, partly arcane. They are weeks old. They have no childhood, no history, no culture of their own, and they are already dying if they can't maintain their arcane stability.
- **Unique mechanic:** Overload — can push their arcane nature past safe limits for explosive power at the cost of instability.
- **Visual identity:** Pale skin with translucent quality, glowing veins, luminous solid-color eyes (no pupil), zero-gravity hair. Occasionally "glitch" — brief visual distortions when emotionally unstable.
- **Social standing:** Feared, pitied, and fascinating in equal measure. NPC reactions range from awe to violence. The most challenging race for social navigation.
- **Origins:** Fracture Core (born from a lattice fracture site — wild, unstable, powerful), Settlement Emergent (born near a settlement — more human-passing, more stable, more socially integrated).

---

## SECTION 8: COMPANION SUMMARIES

### Kael Thornwright
- **Who:** Human, 32, Ironbound Vanguard Captain. Enlists because his family was killed in a raid the garrison ignored. Rose through ranks on merit.
- **Personality:** Calm under pressure, tactically sharp, instinctively protective. Believes in order not because he was told to, but because he's seen what disorder costs.
- **Core conflict:** The institution he gave his life to collapsed. His garrison commander (Aldric Hale) is hardening into authoritarianism. Every order sits heavier than the last.
- **Relationship dynamic:** Straightforward honesty. He says what he thinks. He disapproves of theft, unnecessary violence, and political manipulation — and he'll say so. Trust builds through consistent action, not flattery.
- **Preferred ending:** Override — stability protects people *now*, which is what matters.
- **Recruitment:** Act I, "A Place to Stand" (Lead A). Can be missed but re-recruitable in Act II.

### Aelira Wynnroot
- **Who:** Vaelari, Verdant Flame Seer. One of three people directly responsible for the Severance.
- **Personality:** Precise, studious, deeply guilty. She has more technical knowledge about the lattice than almost anyone alive, and she used it to cause the biggest catastrophe in centuries.
- **Core conflict:** She was trying to save the world. She accelerated its destruction. Now she has to keep working to fix it, knowing she's partly why it's broken.
- **Relationship dynamic:** Her arc is about allowing herself to be helped. She tends toward self-isolation and self-punishment. Players who push through her deflections find genuine depth.
- **Preferred ending:** Guided Dissolution — honors the Firstborn's intent, and if managed carefully, represents the most people surviving with dignity.
- **Recruitment:** Act I, "A Place to Stand" (Lead B). Can be missed but re-recruitable in Act II.

### Maren Duskwell
- **Who:** Independent (former Ashmar Reaver). Age and full backstory deliberately opaque early.
- **Personality:** Reads situations faster than anyone in the room. Tells you what she observes, not what you want to hear. Wry, precise, occasionally brutal.
- **Core conflict:** She's been alone for a long time by choice. Caring about people is a liability in her world. The party is becoming evidence against her own philosophy.
- **Relationship dynamic:** She will not be impressed by social performance. She responds to honesty, competence, and the player not flinching when she names uncomfortable truths. The warmth she develops is hard-won and therefore meaningful.
- **Preferred ending:** Guided Dissolution — pragmatic. Most people survive. She can work with that.
- **Recruitment:** Act I, after "Fracture Point" — must be actively engaged in the aftermath. If ignored, she remains an NPC and can be re-recruited mid-Act II. She is the easiest companion to miss permanently.

### Lady Seraphine Eltaryn
- **Who:** House of the Hollow Crown. Young heir to a fallen empire. One of three people directly responsible for the Severance.
- **Personality:** Brilliant. Manipulative. Genuinely convinced that she's right, which is more dangerous than cynical manipulation because she believes it.
- **Core conflict:** Everything she knows about her family, her right to rule, and the Firstborn is a fabrication. The deeper she digs for proof of her legitimacy, the clearer the lie becomes. What she does when she can no longer deny this is the game's most consequential variable.
- **Arc options:** Reformed ally (confronts her inheritance, rebuilds from honesty), antagonist (doubles down, pursues the Scepter, becomes a final-act obstacle), coerced ally (knows the truth but hasn't accepted it — assists under conditions).
- **Relationship dynamic:** She will attempt to manage the player the way she manages everyone. The relationship deepens only when the player refuses to be managed and she finds that honest engagement more valuable than performance.
- **Preferred ending:** Variable. Unreformed: Override (she wants control). Reformed: Guided Dissolution (she's learned to let go).
- **Recruitment:** Act II only. Requires trust threshold and specific dialogue choices in "The Companion in the Dark." The only companion who can become an antagonist rather than an ally.

---

## SECTION 9: FACTION SUMMARIES (Quick Reference)

### Ironbound Vanguard
- **What they want:** Stabilize and permanently control the lattice under military authority.
- **Method:** Martial law, information suppression, controlled access to Firstborn technology.
- **Economic strength:** Stable trade routes, low tariffs within garrison zones.
- **What they get right:** They keep order when nothing else does. Their magic suppression policies, while authoritarian, are not irrational.
- **What they get wrong:** They're solving a crisis of dependency by creating more dependency. Permanent military control of the lattice is just a new form of the exploitation that caused this.
- **Internal tension:** Kael and soldiers like him believe in the mission. Hale and command believe in the institution. These are not the same thing.

### Circle of Verdant Flame
- **What they want:** Manage the lattice's decline gracefully over time.
- **Method:** Research, corruption purification, advocacy, ecological intervention.
- **Economic strength:** Rare reagents, purified land, Wellspring-adjacent goods.
- **What they get right:** They were right all along. Their scientific framework is the most accurate available. They care about long-term survival over short-term control.
- **What they get wrong:** Being right and being effective are different things. They have no military force, poor political leverage, and a tendency toward guilt spirals (see: Aelira) that paralyze action.

### Ashmar Reavers
- **What they want:** Exploit the transition for maximum gain. Position themselves for whatever comes after.
- **Method:** Black markets, relic trafficking, intelligence gathering, strategic neutrality.
- **Economic strength:** Highest profit margins, unrestricted goods, relic economy dominance.
- **What they get right:** They understand how power actually moves — through information and resources, not ideology. They will survive the collapse regardless of which ending occurs.
- **What they get wrong:** "Position for the aftermath" is not a plan if the aftermath is civilizational collapse. Varek's pragmatism has a blind spot: some crises cannot be survived by being clever.

### House of the Hollow Crown
- **What they want:** Restore the Dominion under Eltaryn authority. Find the Scepter. Make the lattice permanent and theirs.
- **Method:** Political manipulation, archive knowledge, legitimacy claims, leverage over other factions.
- **Economic strength:** Archive access, noble luxury economy, political leverage.
- **What they get right:** They have the knowledge. Their archives contain more accurate Firstborn technical documentation than anyone else possesses. Seraphine's analysis of the crisis is often the most accurate.
- **What they get wrong:** All of it is filtered through the assumption that they're meant to rule. The Scepter is a maintenance tool, not a divine inheritance. Their entire worldview is a fabrication.

---

## SECTION 10: STORY STRUCTURE (Quick Reference)

### Act I — Arrival (Hours 1–15)
Theme: Survival and discovery.
- Player arrives at Hollowford from origin-specific opening.
- Establishes themselves in the post-Severance world.
- Encounters all four factions.
- Recruits first companions (Kael, Aelira, optionally Maren).
- Survives the "Fracture Point" crisis (location TBD — see Open Decision 1).
- Receives first direct transmission from the Consuming Consciousness.
- End state: Player understands the lattice is failing deliberately, they are uniquely equipped to do something about it, and powerful people have noticed.

**Key Act I quests:** Origin Opening → "The Gates of Hollowford" → "A Place to Stand" → "The Relic's First Whisper" → "Fault Lines" → "The Fourth Voice" → "The Deep Wound" → "Fracture Point"

### Act II — Descent (Hours 15–40)
Theme: Knowledge and compromise.
- Non-linear heart of the game. Faction questlines, Vale exploration, Firstborn ruins.
- Recruits Seraphine (Act II only, "The Companion in the Dark").
- Culminates in the Ashenveil Archive (7-level dungeon) — full truth revealed, Scepter recovered.
- End state: Player has full information, factions fracture into open conflict, path to the Heart of the Lattice opens.

**Key Act II quests:** "The Archive Key" (3 fragments) → "The Companion in the Dark" → "The Ashenveil Archive" → "The Reckoning"

### Act III — Judgment (Hours 40–55+)
Theme: Conviction and cost.
- Factions in open war. Lattice collapse accelerating.
- Surface faction resolution missions (flexible order): "Chain of Command," "The Burning Circle," "The Reckoning of Seven-Knives," "The Crown Falls."
- "The Heart Road" — final dungeon, 4 stages.
- Confrontation with Erevos and the Consuming Consciousness.
- THE CHOICE: Ending A (Guided Dissolution), Ending B (Override), or Ending C (Severance Complete).
- Epilogue + post-credits.

### The Three Endings
**Ending A — Guided Dissolution:** Honor the Firstborn's designed intent. The lattice ends, but over centuries rather than months. Surface civilizations have time to adapt. The world loses magical infrastructure but gains genuine independence.
- *Cost:* Centuries of difficult transition. Many will struggle. The player cannot control how it plays out.
- *Philosophical position:* Trust the plan, even though the planners are gone.

**Ending B — Override:** Use the Scepter to override the Consuming Consciousness. The lattice continues under the player's (or player-designated) authority. Stability is maintained.
- *Cost:* Whoever controls the Scepter controls the continent. The Dominion's mistake — dependency on a single controlling infrastructure — is repeated, just with different hands on the lever.
- *Philosophical position:* Order now, questions later.

**Ending C — Severance Complete:** Allow the Consciousness to finish the decommissioning immediately. Wild magic returns. Civilizations collapse. Millions die in the short term. But the world is genuinely free — no lattice, no dependency, no single point of failure.
- *Cost:* Immediate catastrophic death toll. The world Kael is protecting, Maren has survived in, and Seraphine has built toward is gone. Every companion opposes or deeply grieves this ending.
- *Philosophical position:* The Firstborn were right. The plan was right. Execute it, pay the cost, accept the world that comes after.

---

## SECTION 11: BEHAVIOR RULES FOR CLAUDE

When working on this project, follow these rules in all tasks:

**Consistency rules:**
1. Always check terminology against Section 5 before writing any design content.
2. Always refer to the race as "Vaelari." Never "Sylvarai." Never any other name.
3. Always refer to the story as three acts. Never four. The Heart Road is Act III.
4. Always refer to three endings. Never four. Integration was rejected for launch.
5. Ironkin and Drakelings are NPC/expansion content only. Never describe them as playable.

**Conflict resolution rules:**
6. If content conflicts with SD_01, SD_01 wins. Flag the conflict and propose a resolution — do not resolve silently.
7. If content conflicts with this context file, flag it and ask. This file may be out of date; it should be updated when decisions change.
8. Never resolve an Open Decision (Section 4) without explicit instruction from Kyle. Flag it and ask.

**Document editing rules:**
9. When editing any SD file, increment the version number (v1.0 → v1.1, etc.).
10. When editing any SD file, add a brief change log entry at the top of the file noting what changed and why.
11. Never delete content without confirmation. Move superseded content to an Archive section within the file or to the `/Archive/` folder.
12. The Merge Notes header in SD_03 is part of the file's history — do not remove it.

**Writing and tone rules:**
13. All design writing should reflect the game's core identity: grounded, morally complex, no clear good guys, no chosen hero.
14. Erevos is not a villain. The Consuming Consciousness is not evil — it is broken. The distinction matters in every piece of writing.
15. No faction should be written as obviously correct. Every faction has a defensible position and a fatal flaw.
16. NPC dialogue and world descriptions should reflect "a real place that had a catastrophe four weeks ago" — not a fantasy world in permanent crisis-aesthetic.

**Flagging rules:**
17. If a task would require knowing the answer to an Open Decision, stop, state which decision is needed, and ask before proceeding.
18. If you notice a new inconsistency not listed in Section 4, flag it at the start of your response before completing the task.
19. If you are uncertain whether something is canonical, say so explicitly rather than inventing an answer.

---

## SECTION 12: CURRENT PROJECT STATUS

**As of March 2026:**

**Engine and pipeline confirmed:**
- Target engine: **Unreal Engine 5.7**
- 3D tool: **Blender** (connected to Claude Code via MCP)
- Export format: **FBX** (Blender → UE5.7)
- Key UE5.7 features in use: Lumen (lighting), Nanite (environment geometry), MetaHuman-compatible character pipeline

**Completed and locked:**
- SD_01 through SD_07, SD_09, SD_10 — all canonical, all in the Design_Bible folder
- Race naming ("Vaelari") — consistent across all documents
- Race/origin scope (3 races, 2 origins each, Ironkin/Drakelings as expansion-only) — consistent
- Endings count (three: Guided Dissolution, Override, Severance Complete) — confirmed and propagated to SD_03 v2.1 and SD_10

**Immediate next tasks (prioritized):**
1. **Resolve Open Decision 1** (Act I finale location: North Wall vs. Deepwood) — no other story work should proceed until this is confirmed
2. **Resolve Open Decision 2** (Rune/Shard terminology) — run a terminology sweep of SD_06 and SD_07 once decided
3. **Fix SD_07 Act IV references** — straightforward edit once act structure is confirmed in SD_07's own text (the zone scaling table currently lists Act IV)
4. **Build SD_08** (Severant Vale Region Guide) — use `SD_-_Playable_Area_Detail.txt`, `SD_Map_V1.txt`, and SD_01 Section 6 as source material
5. **SD_04 consistency pass** — verify companion content against SD_03's merged quest structure (identified as needed but not yet done)

**Known document gaps:**
- SD_07 zone scaling table still lists "Act IV" — needs correction to reflect three-act structure
- SD_06 and SD_07 use non-canonical terminology for the socket system (pending Open Decision 2)
- SD_08 does not exist; SD_09 formally depends on it

---

*This file should be updated whenever a canonical decision is made or an open decision is resolved.*
*Current maintainer: Kyle*
