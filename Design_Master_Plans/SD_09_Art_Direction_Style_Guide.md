# THE SHATTERED DOMINION — ART DIRECTION & STYLE GUIDE
## Document 9 of 10 | Version 1.0 | Depends on: World Bible & Lore Foundation, Race & Origin System, Faction Playbook, Severant Vale Region Guide

**Purpose:** This document is the visual constitution of The Shattered Dominion. It defines the game's overall aesthetic identity, environmental design language, faction visual profiles, character and creature design rules, UI/HUD philosophy, item visual hierarchy, camera system, lighting, and the specific visual rules that keep every asset feeling like it belongs to the same world. Every artist, technical artist, UI designer, and animator working on this project defers to this document. If a visual decision contradicts what is written here, this document wins.

**Design Foundation:**
- Visual style: Grounded realism — photorealistic textures, realistic lighting, gritty and weathered
- References: The Witcher 3 (lived-in world, weather and decay), Dragon Age: Origins (faction identity, political world), Skyrim (environmental scale, exploration reward, lived-in northern atmosphere)
- HUD: Minimal — nearly invisible during exploration, contextual fade-in
- Factions: Emergent — they look like what they are practically
- Races: Grounded fantastical — nothing looks like a fantasy illustration
- Firstborn ruins: Ancient alien — non-human design logic, unsettling precision
- Item quality: Color-coded rarity with material quality difference on equipped gear
- Emotional register: Contrasting — dark world with specific genuinely beautiful moments; contrast does the emotional work
- Camera: Flexible third-person — default pulled-back, zooms in for dialogue and key moments

---

# SECTION 1: VISUAL IDENTITY STATEMENT

## 1.1 The Core Principle

**The Shattered Dominion looks like a real place that had a catastrophe four weeks ago.**

Not a fantasy world in permanent crisis-aesthetic. Not stylized gloom. A specific place — the Severant Vale, temperate farmland country, late autumn — that was functioning normally until recently and is now dealing with the consequences of something that broke in a single night. The world's beauty is not decorative. The world's damage is not atmospheric. Both are the result of specific events with specific causes, and the visual design must communicate that at every scale.

Every asset in this game should be able to answer the question: *What was this before the Severance, and what is it now?* A farmhouse that looks simply ruined has failed. A farmhouse that looks like a family was eating dinner when the sky tore open has succeeded.

## 1.2 The Three Visual Registers

The game operates in three distinct visual registers that coexist without contradiction. **The contrast between them is the primary emotional tool of the art direction.**

**Register 1 — The Ordinary World:**
Human settlements, daily life, the materiality of a pre-industrial civilization. Worn stone, thatch and timber, iron tools, muddy roads, candlelight through shuttered windows. This is The Witcher 3's register — grounded, practical, human-scale. Nothing in this register is visually exciting. It is the baseline against which everything else is measured. When Register 1 looks exactly like what it is — a farming town, a soldier's barracks, a widow's kitchen — it is doing its job.

**Register 2 — The Broken World:**
What happens when Register 1 encounters the Severance. Lattice fractures splitting the earth. Corruption zones consuming farmland. The aurora flicker of residual energy in the sky. Ruins that shouldn't be active, active. This register uses the same photorealistic foundation as Register 1 but introduces deliberate visual wrongness — things that are almost right but aren't, which is more unsettling than things that are obviously supernatural. A cow that has been corrupted shouldn't look like a fantasy creature. It should look like a cow, except wrong in ways you can't immediately name.

**Register 3 — The Firstborn World:**
Ancient, precise, and completely alien to everything else in the game. The Firstborn did not build like humans. Their architecture is not inspired by human architecture made grander — it operates on different geometric and engineering logic entirely. Entering a Firstborn ruin should feel like stepping into a different kind of world that was here long before anything the player has encountered and will be here long after. Register 3 does not decay the way Register 1 and 2 do. Its decay is different — a precision instrument's failure is different from a wooden building's rot.

The emotional power of the game comes from the movement between registers. A player who walks out of a corrupted farmhouse (Register 2) into a pristine Firstborn chamber (Register 3) has experienced something the visual design produced deliberately.

## 1.3 What This Game Does Not Look Like

Defining exclusions is as important as defining inclusions:

- **Not high fantasy.** No saturated colors, no glowing magical particles as ambient decoration, no armor that couldn't be worn by a human body, no swords that glow for no reason.
- **Not grimdark.** The world is not uniformly desaturated. Beautiful moments exist and are meant to be beautiful. The Witcher 3 is not grimdark — it is a world where beauty and horror coexist, and that is the register.
- **Not post-apocalyptic aesthetic.** The world does not look like it has been abandoned for decades. It looks like it has been in crisis for weeks. The difference is visible in everything — the state of roads, the condition of buildings, the presence of people.
- **Not convenient fantasy medieval.** No anachronistic cleanliness. No suspiciously well-maintained equipment on everyone. No towns that look like they were built as game levels rather than places where people actually live and work.

---

# SECTION 2: ENVIRONMENTAL DESIGN

## 2.1 The Vale — Visual Foundation

The Severant Vale at game start is late autumn. This is not arbitrary — it was chosen because autumn provides:
- Natural desaturation (golden light, muted greens, dead amber) that reads as beauty without requiring post-processing tricks
- Visual contrast between the Vale's former agricultural abundance (implied by the scale of the fields, the size of the barns, the width of the trade roads) and its current failing state
- A season associated with endings, which is appropriate

**Base palette — Vale:**

| Element | Pre-Severance Color | Post-Severance Shift |
|---|---|---|
| Sky | Clear blue, seasonal clouds | Gray-overcast dominant; aurora flicker at dawn/dusk |
| Farmland | Amber harvest fields | Amber fields with patches of wrong-color (too dark, too bright, or dead gray) |
| Forest (healthy) | Mixed amber/deep green | Slightly dimmer; some color saturation loss |
| Forest (corrupted) | N/A | Black veins on bark, purple-gray ground cover, dead gray-brown understory |
| Road surfaces | Brown earth, worn stone | Same, but with lattice fracture lines (pale blue-white cracks that pulse faintly) |
| River Serpentis | Clear blue-gray | Still clear; appears normal; the wrongness is subtle — occasional reversed ripples near the Old Ford |
| Buildings (occupied) | Natural stone, warm wood | Same, but with visible repairs using wrong materials; hasty patching |
| Buildings (abandoned) | N/A | Damage is recent, not aged; shutters torn off, not rotted; doors forced, not decayed |

**Lighting — Vale:**

The Vale's default lighting is overcast. This is a deliberate choice: post-Severance, the sky is wrong. Weather is unpredictable. An overcast sky is not depressing — it is correct. It is what the world looks like now.

Exceptions exist and are meaningful:
- **Golden hour** (30 minutes before sunset): The Vale's most beautiful lighting condition. Warm amber light through the overcast's break catches the landscape at the end of the day. This lighting should appear daily and should be the game's primary "beautiful moment" lighting for the outdoor world. Players who are outside at golden hour see the Vale as it might have been.
- **After rain:** The world is briefly brighter. Washed stone, clean air, the specific quality of light through post-storm clearing. Scheduled rain events produce this as a reward for waiting through the wet.
- **Clear night:** Stars visible through the aurora flicker. The sky at night is the most visually unusual element of the Vale — the aurora is not the Northern Lights color (green, red) but rather a pale blue-white that matches lattice energy colors. Beautiful and wrong.

## 2.2 Hollowford — Visual Rules

Hollowford is built from limestone and timber. It is not a fantasy city. It is a real medieval-scale market town that has been significantly overcrowded for four weeks.

**Visual rules specific to Hollowford:**

*Density communicates crisis:* The refugee camp outside the South Gate should be visibly improvised compared to the city proper — the difference between stone-and-mortar construction and canvas-and-salvage is the visual story of the Severance's impact. The city didn't get worse overnight. The camp appeared overnight.

*Wear is recent, not ancient:* Damage to the city walls shows impact from the Severance night (scorch marks, crack patterns consistent with a ground surge) rather than centuries of neglect. This matters — old decay reads as atmosphere, recent damage reads as event.

*Faction presence through objects, not signage:* The Vanguard garrison is identifiable because there are weapons racks visible through open doors, soldiers in armor moving on patrol patterns, and supply crates stacked with military efficiency. There is no glowing Vanguard logo on the wall. The Hollow Crown's presence in the Noble Quarter is identifiable because the windows have curtains, there are horses tied with expensive tack, and there are people at the door who are watching without appearing to watch. Visual storytelling through behavior and object, not through faction branding.

*Vertical complexity:* Hollowford has three readable layers — street level (commerce, foot traffic, visible poverty), mid-level (windows with lives behind them, laundry lines, second-floor workshops), and rooftop/wall level (guard patrols, a child watching from a window, a figure on a roof that shouldn't be there). All three layers should be populated and readable at any given time.

**District visual identities:**

| District | Primary Materials | Dominant Color | Character |
|---|---|---|---|
| Market Quarter | Limestone, timber, canvas stalls | Warm ochre, brown, rust | Chaotic, layered, human |
| Noble Quarter | Dressed limestone, wrought iron, glass | Cool gray, faded gilt, deep green (overgrown gardens) | Decaying grandeur |
| Garrison | Rough stone, iron, utilitarian timber | Dark gray, iron black, Vanguard blue-steel | Military efficiency |
| Forge District | Soot-darkened stone, fire-brick, exposed metal | Black, orange-red, industrial brown | Industrial heat |
| Undercity | Raw stone, Firstborn-adjacent carved elements, salvage | Near-black, amber torch-glow, occasional pale blue Firstborn light | Criminal permanence |

## 2.3 Frontier Settlements

Each of the four frontier settlements has a distinct visual profile that communicates its function before the player reads any text.

**Ironwood (NW):** Dense conifer forest creates perpetual shade. Buildings are timber-primary — these are loggers who have access to the best material in the region. The settlement smells like sawdust and pine pitch in the audio design equivalent — visually, fresh-cut timber stacks are everywhere, the road is surfaced with split logs, and the buildings are newer and better-constructed than Hollowford's oldest structures. The settlement looks competent and self-sufficient.

**Grainfell (NE):** Open sky — this is farming country and the lack of tree cover is itself visual information. Buildings are stone-based but smaller than Hollowford, spread out across the landscape rather than clustered. The visual signature is the fields — and the visual story is told by the contrast between the healthy western fields (gold and green, correct colors) and the eastern fields adjacent to the corruption zone (wrong colors, uneven growth, the specific visual failure of agricultural land that something has touched).

**Ashford (NW, high ground):** The approach from the south shows the elevation — the settlement sits above the Vale on a rocky outcrop, and the view back down into the Vale is one of the game's significant vistas. The settlement itself is utilitarian to the point of severity: stone-cut buildings, minimal decoration, everything oriented toward the mine entrance. The mine is the first thing visible from the approach road and the last thing visible leaving.

**Southwatch (SE):** Flat, open, exposed. The Crimson Flats begin just south — the ground changes from Vale green-brown to an increasingly dry, reddish terrain. At night, the faint glow of the still-burning Flats is visible on the southern horizon. The settlement exists to watch the border and process refugees; its buildings are functional checkpoints and transit structures. The Drakeling camp adjacent to it has improvised heat-generation structures (small fires in specific arrangements, heat-resistant materials) that look unlike anything else in the Vale.

## 2.4 Biome Visual Rules (Summary — Detailed in Region Guide)

**Farmland:** Hedgerow-divided fields, rutted roads, working agricultural infrastructure in various states of failure. Autumn palette dominant.

**Mixed forest:** The Vale's trees are northern European in character — oak, birch, pine, with heavy undergrowth. Dappled light through canopy in healthy zones. Specific visual rule: logging scars (stumps, cleared areas, abandoned equipment) communicate human presence and human scale in a way that makes the forest feel real rather than backdrop.

**Rocky hills:** High contrast — bright stone, deep shadows. The palette shifts to gray and umber. Wind is visible in the vegetation movement. The eastern ridge provides the Vale's most dramatic terrain and its best views into Verdantheart.

**Corruption zones:** Defined fully in Section 2.5.

## 2.5 Corruption Zone Visual Language

Corruption zones are the game's most distinctive visual element. They must read as wrong without being visually noisy. The visual identity of corruption is precision and wrongness — not chaos.

**Color system:**
- Base: Black — not dark brown, not dark gray. A specific desaturated black that reads as the absence of natural color rather than darkness.
- Secondary: Deep violet-purple — specifically the purple associated with lattice energy gone wrong. Not a bright, saturated purple. A deep, almost bruised purple that appears where corruption is most concentrated.
- Accent: Pale blue-white — the color of lattice energy in its raw state. Appears at fracture lines, at the edges of crystalline growths, at node locations. This color is also the color of Firstborn relic energy, creating a visual connection between corruption and origin.

**Visual progression (corruption intensity levels):**

*Level 1 — Edge corruption (approaching a zone):*
Black veins appear in the bark of trees at the zone's boundary. Ground cover begins losing color — grass goes from green-amber to gray-brown. The light quality changes very slightly — a slight filtering toward gray. Animals are absent. The silence is visible in the lack of birds, the stillness.

*Level 2 — Active zone:*
Black veins dominate. Crystalline growths (angular, geometric — Firstborn shapes) emerge from the ground and tree bark. The purple-violet glow appears in shadows and pools. Some trees have partially merged with crystalline structures. Corrupted creatures are present. The player's relic pulses faintly in this zone.

*Level 3 — Deep zone (corruption zone cores):*
The organic world is largely absent — what remains is a hybrid of dead organic matter and crystalline/lattice growth. The violet glow is ambient, not just in shadows. The Firstborn pale blue-white appears at the zone's heart, where the underlying lattice damage is deepest. The visual rule at Level 3: it is almost beautiful in a specific way — the crystalline structures catch the pale light and refract it, and the geometry is precise and strange. This is deliberate. The corruption is not simple destruction. It is transformation, and transformation has its own visual logic.

**What corruption does NOT look like:**
- Bright glowing slime or ooze
- Cartoon darkness or shadow-substance
- Purple fog or haze (fog implies weather; this is structural)
- Generic rot or decay (rot is organic; this is geometric)

---

# SECTION 3: FIRSTBORN VISUAL IDENTITY

## 3.1 The Core Principle — Ancient Alien

The Firstborn built differently because they thought differently. Their architecture is not human architecture made more impressive. It operates on different geometric and engineering logic — and this difference should be visible, consistent, and slightly unsettling in its precision.

**The design rules that define Firstborn work:**

*Perfect geometry:* Firstborn surfaces are machined-flat or precisely curved to mathematical tolerances that pre-industrial human construction cannot achieve. Walls that are exactly, verifiably flat. Angles that are exactly correct. This should be visible in how light falls on Firstborn surfaces — shadows fall clean and hard because the geometry is exact.

*Functional beauty:* Every element of a Firstborn structure serves a function, and the Firstborn understood that beautiful things function better when they are well-made. Firstborn architecture is decorated, but the decoration is always structural — carved conduit channels double as bas-relief patterns, support arches use curves that are both load-bearing-optimal and visually elegant. Nothing is purely decorative.

*Scale that implies a different species:* Firstborn corridors are slightly too tall, slightly too wide, for human proportion. Not dramatically — the Firstborn were 2.0–2.4m tall, and their spaces reflect this. But the cumulative effect of spaces built for beings slightly larger and physically different is a persistent, low-grade wrongness that a human player feels without necessarily articulating.

*Rune-script as infrastructure:* Firstborn writing is not decorative inscription. It is functional data — maintenance records, operational parameters, warnings, calibration marks. It should look like industrial labeling on a machine, not like a fantasy language spelled out in artistic script. The forms are precise, angular, and consistent across all Firstborn surfaces — they were engineered, not developed culturally.

*Stone that does not decay the same way:* Firstborn stone is not limestone or granite — it is an engineered material the Firstborn created specifically for lattice infrastructure. It weathers differently. Over millennia, it has developed a specific patina — a slight iridescence in certain lighting conditions, a surface texture that is smooth where weathered rather than rough. It does not grow moss in the same way organic stone does. Where moss grows on Firstborn stone, it grows in straight lines following the surface channels, because the channels drain water predictably.

## 3.2 Interior vs. Exterior Visual Split

The contrast-driven principle applies at the structure level: **Firstborn exteriors are the world reclaiming them; Firstborn interiors are the world preserved against all odds.**

**Exteriors:**
Buried, cracked, overgrown — but the overgrowth follows the geometry. Vines follow conduit channels. Moss grows in the carved rune-script tracks. The Firstborn surface beneath is intact; the world has simply grown over it. When the player first sees a Firstborn exterior, they should see something ancient and half-buried. When they get close, they should see that what is beneath the burial is in perfect condition.

**Interiors:**
When the player enters through a seal or a crack opened by the Severance, the interior condition depends on whether the facility is powered. Powered facilities (active nodes, functioning constructs) look almost operational — the engineered stone is clean, the rune-script glows faintly at nodes, the air is dry and still. Depowered facilities are dark and dust-still but structurally intact — the Firstborn material does not crumble or decay like human construction.

**The moment of entry:**
The visual transition from exterior (organic, decayed, familiar) to interior (precise, preserved, alien) is one of the game's most important recurring visual beats. This transition should never be gradual. It should be a threshold — one step in the exterior, one step in the interior, and the player is in a different world.

## 3.3 Firstborn Color Palette

| Element | Color | Notes |
|---|---|---|
| Primary stone | Blue-gray with iridescent undertone | Visible in raking light; not obvious in flat light |
| Rune-script (inactive) | Dark charcoal, slightly raised | Reads as carved relief in shadow |
| Rune-script (active) | Pale blue-white glow | The same color as corruption accents — intentional connection |
| Structural light (powered) | Cold white-blue | Comes from within the stone at conduit intersections |
| Construct materials | Same stone + iron-like metal alloy | Metal has a slight bronze undertone; not gold, not silver |
| Void/damaged sections | The absence of the above | Corruption color bleeds in where the lattice has failed |

---

# SECTION 4: FACTION VISUAL PROFILES

## 4.1 Design Philosophy — Emergent Identity

Faction members look like what they are practically. No faction has a uniform color scheme that exists for visual clarity — they have practical reasons for every visual choice. The player reads faction identity the same way a person reads it in a real world: through clothing and equipment that reflects the life being lived, not through team colors.

**The test:** If you covered up all identifying heraldry and markings, could you still tell which faction a character belongs to? If yes, the design is working. If no, the faction's visual identity is too dependent on branding.

## 4.2 Ironbound Vanguard

**What they are:** A military organization that was the Dominion's armed force and is now functioning as an emergency government without a mandate. They have supply chains, armories, and institutional culture. They have the best equipment in the Vale, and it shows.

**Visual identity:**

*Armor:* Military grade — functional, maintained, standardized. Steel plate on officers, chainmail on foot soldiers, padded gambeson on support personnel. The standardization is the tell: Vanguard equipment shows the same design language across individuals. Buckle placement, strap configuration, the specific shape of pauldrons — these are consistent because this equipment was issued, not assembled piecemeal.

*Color:* Steel-blue and iron-gray. Not bright — the same muted blue-gray as well-maintained steel, with leather straps and backing in dark brown. In bad light, a Vanguard patrol reads as a moving wall of gray.

*Condition:* Good. Maintained. This is not post-apocalyptic soldier aesthetic — these are people who still have access to their armory, still sharpen their weapons, still repair their equipment. The contrast with refugee characters is stark: the Vanguard looks like the before of a crisis, not the during.

*Heraldry:* An iron gauntlet on blue-gray field. Applied practically — stamped onto metal equipment, painted on shields, sewn into fabric. Present but not prominent.

*Officers vs. enlisted:* Officers have additional plate coverage, better-quality leather, and visible rank insignia (etched into pauldrons, not attached badges). Kael's visual distinguishes him from other officers through accumulated personal equipment — his gear is well-maintained Vanguard standard plus specific personal items that have been with him for years.

## 4.3 Circle of Verdant Flame

**What they are:** A nature-philosophy organization that predates the current crisis and has been warning about it for decades. Their members are researchers, practitioners, and advocates — not soldiers. They live and work in natural environments.

**Visual identity:**

*Clothing:* Practical for field work in forest environments. Layered — multiple garments because temperature regulation matters in outdoor conditions. Natural materials: undyed wool, hemp, treated leather, plant-fiber cord. Greens, browns, and grays that exist because these are the colors of the materials they use, not because they color-coordinate with nature.

*Distinguishing elements:* Verdant Flame members often carry or wear specific natural items that have cultural significance: dried herbs in pouches at the belt, carved wooden tokens, Wellspring water in sealed containers. These items accumulate over time — a veteran Circle member's equipment is layered with personal additions. Younger or newer members have less of this accumulated personal material.

*Corruption damage:* Verdant Flame members who work in corruption zones show the physical cost. Slight discoloration of exposed skin near the hands and face (long-term corruption proximity), equipment that has been treated and re-treated against corruption damage, the specific weariness of people doing physically exhausting work in hazardous conditions.

*Aelira specifically:* Her visual design reflects her position as both gifted and guilt-ridden. Her equipment is high-quality Verdant Flame field gear in good condition — she maintains it because ritual and maintenance are her anchors — but she wears it plainly, without the personal accumulation that marks veteran Circle members. She stripped herself of those things after the Severance.

## 4.4 Ashmar Reavers

**What they are:** A decentralized criminal network operating on pragmatic survival principles. They have no uniform because a uniform would be a liability. Their visual identity is improvised by definition.

**Visual identity:**

*Clothing:* Assembled from whatever is available, whatever works, whatever can be quickly replaced or discarded. A Reaver field operative looks like a particularly competent scavenger — functional mix of purchased, stolen, and jury-rigged equipment that does its job without broadcasting organizational affiliation.

*The visual tell:* Reavers don't have a color or a heraldry. They have a shared aesthetic of functionality-above-appearance and specific small indicators of professional pride: a good knife that has been maintained when everything else is rough, a piece of armor that is wrong for the rest of the outfit but clearly works, the specific confident posture of people who are used to moving through spaces that are nominally hostile to them.

*Varek specifically:* Varek looks better than his organization should permit. His equipment is functional but selected — he has chosen each piece deliberately. He wears nothing that could be traced to any faction or origin. The one personal item he wears consistently is a specific ring that has no heraldic significance and no obvious function. What it means is a question the player can investigate.

*Maren specifically:* Her visual design is defined by layering and concealment. Multiple functional garments, the outermost of which could belong to any character in the Vale. The blades she carries are not obviously displayed but also not hidden — positioned for access, not for display.

## 4.5 House of the Hollow Crown

**What they are:** The remnants of a feudal aristocracy that lost its institutional basis in a single night but retained its material wealth and its archive knowledge. They look wealthy because they are wealthy — and they know that appearance is political capital.

**Visual identity:**

*Clothing:* Pre-Severance noble fashion, maintained. Fine wool, silk lining, quality leather accessories. The materials are genuine — Hollow Crown members are not performing wealth, they have it. The condition of their clothing communicates that they have not been materially affected by the crisis in the way everyone else has.

*The political statement:* Every Hollow Crown operative who appears in public is making a deliberate statement about continuity — the Dominion is not dead, because we are still dressed as though it exists. This is conscious and calculated. The clothing is a political argument.

*Seraphine specifically:* Her visual design is controlled to the point of deliberateness. Every element of her appearance is chosen. She wears Eltaryn colors (deep burgundy and silver-gray) in fabric that communicates quality without ostentation — she is too intelligent to appear extravagant in a city where people are starving. Her single most important visual element is the House Eltaryn signet ring, which she uses as a tool (she is always aware of when it is visible) as much as a symbol.

*The Archivist:* Deliberately visually ambiguous. Clothing is scholarly — dark, practical, good-quality but not showy. Nothing that places them in any faction or social class. They could be a Verdant Flame researcher, a Vanguard administrator, or a merchant's accountant. The ambiguity is the design.

---

# SECTION 5: CHARACTER DESIGN — RACES

## 5.1 The Grounded Fantastical Principle

Non-human races should pass the **photographic test**: if an image of a Vaelari, Aetherborn, or Ironkin character were placed alongside a realistic photograph, it should not look like a fantasy illustration that has been made realistic. It should look like a photograph of something that actually exists but that you have never seen before.

This means: no anachronistic beauty conventions, no convenient silhouettes, no features that exist for visual appeal rather than narrative function. Everything about a non-human character's appearance should have a reason that comes from what they are, not from what looks striking in a concept image.

## 5.2 Humans

**Design rules:**

The human population of the Severant Vale is diverse in the way a real medieval-adjacent frontier community would be — shaped by generations of mixed settlement, trade, and migration. No single ethnic template. Skin shows weathering, scarring, sun damage, and age appropriate to origin and lifestyle. Clean skin is rare — this is a post-catastrophe world where personal hygiene is not the priority.

**What humans do NOT look like:** Fantasy game humans — suspiciously symmetrical, conventionally attractive, with impractical hair for their apparent profession. A frontier settler should look like a frontier settler. A Vanguard soldier should look like someone who has been living in armor for weeks.

**Relic mark visual:** Where the failsafe relic bonded — chest, forearm, or neck — a glowing runic pattern pulses faintly. The glow uses the same pale blue-white of Firstborn lattice energy. It is subtle enough to be invisible under clothing and visible in dim light. It should look like something under the skin that is slightly wrong, not like decorative body art.

## 5.3 Vaelari

**Design rules:**

The Vaelari are not elves. The comparison will be made — it should be made as difficult as possible by ensuring every visual choice is grounded in what Vaelari actually are rather than in what elves conventionally look like.

**Body:** Taller than humans (1.85–2.1m average), with longer limb proportions. Not thin — slender, but with the physical capability their biology suggests. The elongation is subtle enough that a Vaelari could be mistaken for a very tall human at distance; up close, the proportions are clearly different.

**Face:** Angular, high-cheeked, narrow-jawed. Expression tends toward stillness — Vaelari communicate through eyes and voice more than through broad facial movement. This should be designed into their face models: less range of prominent facial expression muscle definition, more emphasis on eye expressiveness.

**Hair:** Natural Vaelari tones — silver-white, ash blonde, deep auburn, blue-black, or faded green-gray. Post-Severance, many Vaelari's hair has dulled or silvered prematurely. Hair grows, moves, and behaves physically like human hair. No supernatural movement, no luminescence, no fantasy styling.

**Skin:** Slight luminous quality in certain lighting conditions — not a glow, but a surface reflectance slightly different from human skin. Most visible in low light or at dusk. During Wellspring distress (post-Severance), the luminosity is reduced — Vaelari who were healthy before look slightly flatter now.

**Relic mark:** More organic pattern than human marks — flowing lines rather than sharp geometry, same pale blue-white with a slight green-gold undertone at the edges.

**What Vaelari do NOT look like:** Tolkien elves. No long pointed ears extending above the head, no ethereal otherworldly beauty, no obviously inhuman facial structure. The ears are slightly longer and come to a modest point — more noticeable than human ear variation, less prominent than any fantasy elf design.

## 5.4 Aetherborn

**Design rules:**

Aetherborn are three weeks old at game start. They manifested during the Severance from ambient lattice energy — they did not grow, they appeared. Their visual design should reflect this origin in every detail.

**Body:** Human proportions — Aetherborn formed from ambient energy interacting with biological patterns in the environment, so they are recognizably humanoid. However, their bodies have not had time to develop the physical markers of lived experience: no weathering, no scars, no sun damage. The skin is the specific visual problem — it has a quality of newness that reads as wrong next to anyone who has actually lived in a body for years.

**The glow:** Aetherborn emit a visible faint light from their skin, particularly at joints, fingertips, and along the collarbone — the locations where lattice energy concentrates most densely in a biological vessel. This is not a dramatic fantasy glow — it is the kind of light that is visible in dim conditions and not visible in bright daylight. In the dark, an Aetherborn is faintly luminous. In sunlight, they look like a person with unusually bright eyes and a slightly iridescent skin quality.

**Eyes:** The most obviously inhuman element. Aetherborn eyes are the same pale blue-white of lattice energy — no visible iris division, just the luminous color. They do not glow brightly; they simply are that color, which is arresting up close.

**Clothing and equipment:** Aetherborn begin with almost nothing because they began with nothing. Their early game visual should communicate this — improvised coverings, minimal equipment. As the game progresses, their visual identity develops through what they acquire. Unlike other races, Aetherborn gear acquisition tells the story of their existence directly.

## 5.5 Ironkin

**Design rules:**

Ironkin are not metal beings. They are organic beings whose biological process incorporates iron compounds during development — their skin has a metallic quality, their bone density is significantly higher than human, and their musculature is built around carrying more weight than human frames support.

**Body:** Broader and shorter than humans on average (1.6–1.8m, heavily built). The silhouette is stocky — not fat, genuinely muscular and dense. Ironkin move with deliberate economy; they don't waste motion.

**Skin:** Gray-brown with metallic undertone — visible most in raking light, where the slight metallic quality produces a different light response than organic skin. Not obviously metallic at a glance; clearly not-human on close inspection.

**Face:** Heavy-featured, with a jaw structure that reflects higher bone density. Ironkin faces have a quality of being carved rather than grown — high-relief features, strong brow, prominent cheekbones. Expression is minimal by human standards but the emotions are present in posture and hands as much as face.

**Forge-temple markings:** Ironkin in Covenant standing have ritual markings worked into their skin during Tempering rites — these are not tattoos but actual metal-compound pigment processes, and they read as slightly raised lines of darker gray-silver against the base skin tone.

---

# SECTION 6: CREATURE DESIGN

## 6.1 The Creature Design Principle

Every creature in The Shattered Dominion is something that could exist in the world as described. No creature exists purely as a combat obstacle with interesting visual design. Each creature's appearance communicates what it is, where it came from, and what happened to it.

**The corruption creature rule:** Corrupted creatures must read as what they were before being corrupted. A corrupted wolf should look like a wolf that something terrible happened to, not like a new creature that happens to look wolf-adjacent. The corruption transformation should be legible as transformation — the original animal's anatomy should still be visible underneath what the corruption has done to it.

**The Undead rule:** Undead should look like the dead things they are. Risen soldiers look like soldiers who have been dead for varying periods. The lattice energy animating them is visible (blue-white at joints, in eye sockets) but the dominant visual is always the corpse, not the energy.

**The Construct rule:** Firstborn Constructs are machines. They should look like machines — well-engineered, precise, built for function. They are not organic, not ominous-dark-metal, not styled for intimidation. Their visual threat comes from their obvious physical capability and their obvious lack of any biological limits, not from a designed-to-be-scary aesthetic.

**The Arcane Anomaly rule:** Anomalies have no physical form — they are lattice energy given reactive behavior. Their visual design should be purely energetic: the pale blue-white of raw lattice, geometric rather than organic in form (because lattice energy follows the engineered conduit geometry), with no faces, no limbs, no biological references.

---

# SECTION 7: ITEM AND LOOT VISUAL SYSTEM

## 7.1 The Dual-Layer System

Item quality is communicated through two simultaneous layers:

**Layer 1 — Color tinting (ground drops and inventory):**
Following the D2 model, items have a visual quality indicator applied as a subtle ambient tint in the world and as a color coding in the inventory UI. The tinting in the world is subtle — not a beacon glow, a faint color cast that rewards players who are paying attention to loot without forcing visual noise on everyone.

| Quality Tier | Name | World Tint | Inventory Color |
|---|---|---|---|
| 1 | Common | None | White/Gray text |
| 2 | Touched | Very faint blue shimmer | Blue text |
| 3 | Forged | Soft yellow-gold cast | Yellow text |
| 4 | Bound | Soft green cast | Green text |
| 5 | Remnant | Amber-orange glow | Orange text |

**Layer 2 — Material quality on equipped gear:**
A Remnant sword should look visually superior to a Common sword in ways that have nothing to do with the color glow system. The material quality difference should be visible in:
- Surface finish (Common: rough and worn; Touched: functional; Forged: clearly worked; Remnant: exceptional craftsmanship)
- Condition (Common: damaged and repaired; Remnant: pristine or deliberately distressed in a way that communicates age rather than neglect)
- Detail density (Common: minimal surface detail; Remnant: fine detail work, inlay, inscriptions)
- Proportional quality (Common: slightly imprecise; Remnant: geometrically correct and intentional)

**Relic Shards (visual):**
Socketed Relic Shards are visible on equipped items as small geometric fragments embedded in the surface — each Shard type has a specific color (Anchor Shard: deep iron-gray; Flow Shard: pale silver-blue; Void Shard: near-black with a slight purple edge). When a Shard Combination activates, the socketed Shards briefly illuminate in sequence before settling to a persistent dim glow — the combination's named effect visually announced through the gear itself.

---

# SECTION 8: UI AND HUD DESIGN

## 8.1 Core Philosophy — Minimal and Contextual

The HUD is nearly invisible during exploration. It fades in only when relevant. The player's experience of the Vale, Hollowford, and its inhabitants should not be mediated by a constant layer of abstracted information. The world should feel like the world, not like a game overlay on a world.

**The three HUD states:**

*Exploration state (default):* No persistent UI elements. The screen shows only the game world. No health bar, no stamina bar, no minimap, no waypoint markers. Navigation is done through the environment (readable landmarks, the river, roads, sun position). Players who want to see their map open it manually.

*Combat state (automatic trigger — enemies in combat range):* UI elements fade in. Health and stamina bars appear at bottom-center, styled as minimal bars rather than decorated frames. Active ability hotbar appears at bottom. Enemy health bar appears above their head when locked-on. All elements fade out within 5 seconds of combat ending.

*Interaction state (dialogue, inspection, crafting):* Context-specific UI appears for the interaction and disappears on exit. Dialogue presents as clean floating text with speaker name — no dialogue wheel design that suggests choices as explicit menus; choices appear as natural text continuations.

## 8.2 UI Visual Language

**Typography:**
Clean, slightly weighted serif for important text (item names, NPC names, key information). Light sans-serif for secondary information (descriptions, lore text). Both fonts are grounded in period-adjacent design without being historically literal — they should read as naturally belonging to this world without using actual historical typography.

**Color system (UI-specific):**
- Primary UI: Off-white (#E8DFD0 approximate) — not pure white, which reads as modern; a slightly warm off-white that fits the game's palette
- Secondary UI: Muted gray-brown
- Alert/important: Same pale blue-white of Firstborn lattice energy — used sparingly and specifically for new information and significant events
- Item quality colors: As defined in Section 7.1

**Relic mark integration:**
The player's relic mark (chest, forearm, or neck) acts as the diegetic UI anchor. Relic charge level is communicated through the physical glow of the relic mark — brighter and more steady at full charge, dimmer and slightly flickering when depleted. A player who has learned to read their character's relic mark does not need a separate UI element for relic charge. The bar exists for those who want it; the diegetic version exists for those who don't.

**Map:**
The in-game map is a hand-drawn cartographic representation — not a satellite view, not a clean vector graphic, but a map that looks like it was drawn by someone who walked the terrain. Hub fast travel points are marked as established icons (settlement gate symbols, dungeon entrance symbols). Non-hub locations the player has visited are noted in handwritten annotation style. The map updates as the player explores — new sections drawn in, old annotations sometimes crossed out and corrected.

**Dialogue system:**
Dialogue does not use a wheel. Choices appear as clean text options below the dialogue text, numbered 1–4. The current speaker and their emotional state (tense, calm, hostile, distressed) is communicated through their portrait's visual rather than through text description. Portraits are rendered in the game's visual style — not illustrated, not stylized, but lit and framed like character photography.

## 8.3 Notifications and Alerts

**Quest journal:** Journal entries are written in the player character's voice — first-person observations rather than objective quest descriptions. The journal updates automatically when significant events occur; the player can read new entries by opening the journal or ignore them. Journal entries for micro-discoveries are not added — this is intentional. Micro-discoveries are not logged. If the player wants to remember them, they remember them.

**Loot notifications:** When an item is looted, a small text line appears bottom-left (item name + quality color) for three seconds, then fades. No dramatic loot reveal animation. Items looted from the world simply disappear from the ground and appear in the inventory. Exceptional items (Remnants, Set pieces) receive a slightly longer notification with the item name in its quality color — a small additional visual weight, not a fanfare.

**Level up:** A subtle lattice-energy pulse effect centered on the player's relic mark, lasting approximately one second. The sound design equivalent is a single clean resonance tone. No screen-filling animation, no "LEVEL UP" text. Players who don't notice level-ups are not being penalized — they will interact with the level-up point allocation screen at their next pause.

---

# SECTION 9: CAMERA SYSTEM

## 9.1 Default Camera — Pulled Back

The default gameplay camera is pulled back — enough distance to see the player character fully and to read the environment they are moving through. This camera distance supports the combat system (dodge-and-read requires spatial awareness) and the exploration design (environmental storytelling is designed to be visible from the default camera position).

**Default camera distance:** Approximately 3.5–4m behind and 1.5m above the player character's shoulder level. Slight downward angle. This is the Elden Ring / Dark Souls territory, not the God of War territory.

**Combat camera:** Identical to default during active combat. Lock-on adjusts horizontal angle to keep the locked target in frame while maintaining the pulled-back distance. The camera does not push in during combat — maintaining spatial awareness is more important than cinematic feel during active play.

## 9.2 Dialogue Camera — Pulled In

During dialogue sequences, the camera moves to a medium-close framing — approximately 1.5–2m from the speaker's face, at eye level or slightly below. This is the camera distance at which human facial expression becomes readable and emotionally legible.

Dialogue camera transitions are slow and organic — no snap cuts, no dramatic repositioning. The camera moves to the new position during the opening moments of a conversation and moves back to default during the closing moments. The transition should not interrupt the dialogue's emotional content.

**Dialogue camera options:**
The player can enable a fixed dialogue camera that stays at pulled-back distance — some players prefer to remain in the world rather than moving to close-up during dialogue. This is a settings option, not the default.

## 9.3 Exploration Camera — Special Cases

**Vista moments:** At locations specifically designed as vista points (Sunspear Ridge, the Ashenveil Archive exterior, the Corruption Front's full extent visible from the eastern ridge), the camera very slightly widens its field of view and tilts incrementally — a subtle cue that the player is in a view-worthy location. This is not a locked cinematic shot; the player remains in control. The camera adjustment is purely additive.

**Dungeon entry:** On entering a Firstborn ruin for the first time (threshold crossing), the camera holds still for approximately 1.5 seconds — the player character stops, the camera settles, and the interior is allowed to read before movement resumes. This beat is identical in design to the "entering a cathedral" beat in architectural experience — a moment of pause that communicates scale and significance before the player asserts agency again.

**Player adjustment:** The player can zoom the camera in and out within a defined range (2m closer to 2m further than default) and can raise or lower the vertical angle within a limited arc. Full camera control is not available — the default framing is intentional and the player range is a refinement rather than a full override.

---

# SECTION 10: LIGHTING AND TIME OF DAY

## 10.1 The Lighting Principle

Lighting in The Shattered Dominion communicates world state before any other visual element. A player who is shown a screenshot of any location at any time of day should be able to read three things from the lighting alone: where they are (environment type), when it is (time of day/season), and what is happening (crisis state, corruption presence, faction control).

## 10.2 The Day Cycle

**Dawn (5–7am):** Cool blue-gray light. The aurora flicker is most visible at dawn — the residual lattice energy is at its most apparent when the sky transitions. This is the spookiest time of day, not because of darkness but because of the specific quality of the wrong-color aurora against a brightening sky.

**Morning (7am–noon):** Overcast ambient light. The Vale's default. Flat, melancholic, gray-warm. Not depressing — simply the light of a world under overcast sky. Detail-visible, shadow-minimal, honest.

**Golden hour (5–7pm):** The day's best light. Amber-warm shafts through cloud breaks. The Vale at golden hour looks like what it was. This is the visual equivalent of the world showing you what it used to be, briefly, before the light goes.

**Dusk (7–9pm):** Rapid light loss. The aurora becomes visible. The corruption zones begin their nocturnal luminescence — the purple-violet glow is most visible at dusk as the sky darkens and the zone's own light becomes relative.

**Night (9pm–5am):** Dark blue-black sky with aurora and stars. In healthy areas, near-darkness — player light sources are functional and visible. Near corruption zones, the zone's ambient glow provides light that is not natural. In Firstborn ruins (powered), the cold blue-white interior light. In Hollowford, torch and window light creates pools of warm orange against cool stone.

## 10.3 Dynamic Weather

Post-Severance weather is unpredictable. The weather system generates:

**Standard conditions:** Overcast (default), intermittent rain, occasional clear sky.

**Severance weather events:** Arcane storms (lightning that is the wrong color — pale blue-white rather than yellow-white, striking along lattice fracture lines), sudden frosts that are too early or too late in the season, heat events that have no meteorological explanation. These are scheduled narrative weather events, not random — they occur at specific story beats and should feel authored rather than random.

**Rain visual:** Heavy rain uses a volumetric particle system with appropriate surface splash and run-off. Post-rain condition (wet stone, clear air, different light quality) persists for 20–30 in-game minutes. Rain is one of the game's deliberate emotional resets — after rain, the world is briefly more beautiful than its crisis state.

---

# SECTION 11: AUDIO-VISUAL INTEGRATION NOTES

This section provides direction for audio design alignment with visual language. Full audio design is a separate document; this section defines the visual-audio relationship at key moments.

**Corruption zone audio-visual rule:** The visual silence (no birds, no wind sound in level 1 zones) must precede the visual corruption indicators by approximately 10 seconds of player travel. The player should feel the silence before they see the black veins. Sound absence as warning.

**Firstborn ruin audio-visual rule:** The interior audio should match the interior visual — the clean, preserved quality of a powered Firstborn interior should have an ambient tone that is precise and low-frequency, not creaking or dripping or otherwise organic. When Constructs activate, their audio should sound manufactured — not growling, not screaming, but mechanical.

**Level up audio-visual sync:** The single resonance tone at level-up should be tuned to the specific frequency of the Firstborn relic energy sound established in the Echo Interface audio. The connection between the player's progression and the Firstborn system they are interfacing with should be subconsciously reinforced.

**Weather transition:** Weather changes should be presaged by audio (wind change, pressure change in the music mix) before they are visually visible — the player should be able to hear a storm coming. This is consistent with the grounded realism approach and rewards players who pay attention to non-visual cues.

---

# SECTION 12: IMPLEMENTATION CHECKLIST

**Global Style:**
- [ ] Grounded realism visual standard confirmed and distributed to all art leads
- [ ] Three visual registers (Ordinary, Broken, Firstborn) documented with examples for each asset category
- [ ] "What was this before the Severance, and what is it now?" design test applied to all environment assets

**Environment:**
- [ ] Vale base palette documented with seasonal and corruption variants
- [ ] Hollowford district visual identity guides completed (materials, colors, character per district)
- [ ] Frontier settlement visual profiles completed (4 documents, one per settlement)
- [ ] Corruption zone visual language formalized (3 intensity levels with specific color values)
- [ ] Lighting plan completed (day cycle, weather system, aurora specification)

**Firstborn:**
- [ ] Firstborn stone material created (iridescent blue-gray, specific weathering behavior)
- [ ] Rune-script system designed (functional industrial labeling aesthetic)
- [ ] Interior vs. exterior contrast rule implemented (threshold visual beat scripted)
- [ ] Firstborn color palette formalized with specific values

**Faction Visuals:**
- [ ] Vanguard visual guide completed (armor specs, color values, condition rules)
- [ ] Verdant Flame visual guide completed (material palette, accumulation rules)
- [ ] Reaver visual guide completed (improvised assembly aesthetic, Varek and Maren specific notes)
- [ ] Hollow Crown visual guide completed (quality materials, political statement framing)

**Character and Creature:**
- [ ] Human character design brief (diversity standards, wear and weathering rules)
- [ ] Vaelari design brief (specific feature rules, what NOT to do list)
- [ ] Aetherborn design brief (glow specification, newness quality, progression)
- [ ] Ironkin design brief (metallic skin specification, proportions, marking rules)
- [ ] Corruption creature design rule documented and applied to all corruption enemies
- [ ] Construct design rule documented and applied to all Firstborn constructs
- [ ] Anomaly design rule documented and applied to all Arcane Anomaly enemies

**Item Visual System:**
- [ ] Color tinting system implemented per quality tier (specific color values per tier)
- [ ] Material quality difference guidelines documented (surface finish, condition, detail density per tier)
- [ ] Relic Shard visual (geometric fragment, color per type, combination glow sequence)

**UI/HUD:**
- [ ] Three HUD states implemented (exploration, combat, interaction)
- [ ] Typography selected and applied (serif primary, sans-serif secondary)
- [ ] Map design completed (hand-drawn cartographic style, hub icons, annotation style)
- [ ] Dialogue system implemented (text-based choices, portrait system, no dialogue wheel)
- [ ] Relic mark as diegetic UI element implemented
- [ ] Level-up visual and audio moment specified and implemented
- [ ] Notification system implemented (bottom-left loot notification, 3-second fade)

**Camera:**
- [ ] Default camera distance and angle locked
- [ ] Dialogue camera transition implemented (organic movement, eye-level close)
- [ ] Player camera adjustment range defined and implemented
- [ ] Vista camera adjustment (subtle FOV widening at designated vista points)
- [ ] Dungeon entry camera beat implemented (1.5-second hold at threshold)

---

*End of Document 9: Art Direction & Style Guide*
*Next Document: MVP Development Roadmap*
