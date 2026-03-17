# Assets — Claude Code Instructions
## Target Engine: Unreal Engine 5.7 | 3D Tool: Blender

---

## Folder Structure

```
/Assets/
├── /3D/
│   ├── /Source/        ← .blend files (working files — stay here)
│   │   ├── /Characters/
│   │   ├── /Environment/
│   │   ├── /Props/
│   │   └── /Creatures/
│   └── /Exports/       ← Engine-ready FBX/GLB files (UE5.7 import)
│       ├── /Characters/
│       ├── /Environment/
│       ├── /Props/
│       └── /Creatures/
├── /Textures/          ← PNG / EXR, organized by asset name
└── /Reference/         ← Concept art, mood boards, style references (READ ONLY)
```

---

## Naming Convention
`[category]_[descriptor]_[variant]`

| Category Prefix | Use For |
|---|---|
| `human_` | Human race assets (characters, armor, props) |
| `vaelari_` | Vaelari race assets |
| `aetherborn_` | Aetherborn race assets |
| `npc_` | Generic NPC assets not race-specific |
| `env_` | Environment assets (structures, terrain pieces) |
| `prop_` | Standalone props (furniture, objects, containers) |
| `creature_` | Corrupted creatures, wildlife, constructs |
| `firstborn_` | Firstborn ruins, constructs, technology assets |
| `vanguard_` | Ironbound Vanguard faction assets |
| `flame_` | Circle of Verdant Flame faction assets |
| `reaver_` | Ashmar Reaver faction assets |
| `crown_` | House of the Hollow Crown faction assets |

**Examples:**
- `human_armor_vanguard_heavy_v1`
- `vaelari_npc_rootbound_elder`
- `firstborn_ruin_arch_standard`
- `env_hollowford_gatehouse`
- `creature_wolf_corrupted_v2`

---

## Blender Export Settings for UE5.7

### FBX Export (Standard — use for all static meshes and characters)
- **Scale:** 1.0 (UE5.7 imports at correct scale with default FBX settings)
- **Forward:** -Z Forward
- **Up:** Y Up
- **Apply Unit:** Yes
- **Apply Transform:** Yes
- **Mesh:** Smoothing = Face, Triangulate Faces = Yes
- **Armature:** Add Leaf Bones = No, Primary Bone Axis = Y, Secondary = X
- **Root Bone:** Must be at world origin (0,0,0)

### Character Skeleton Rules (UE5 compatibility)
- Root bone at origin, Y-forward
- Use UE5 skeleton hierarchy if targeting MetaHuman retargeting
- Mesh must be bound to armature before export
- Apply all modifiers before export (except Armature)

### Texture Export
- **Diffuse/Albedo:** PNG, 8-bit, sRGB
- **Normal Maps:** PNG, 8-bit, Linear (NOT sRGB)
- **Roughness/Metallic/AO:** PNG, 8-bit, Linear, packed as R/G/B channels
- **Emissive (Firstborn assets, Aetherborn):** EXR, 16-bit, HDR values allowed
- Resolution: 2048×2048 for primary assets, 1024×1024 for secondary

---

## Visual Register Rules (from SD_09)
Always identify register before modeling. Each has distinct rules.

### Register 1 — Ordinary World
Human settlements, daily life, pre-industrial materiality.
- Worn stone, thatch, timber, iron, mud
- No visual excitement — this is the baseline
- Damage should look specific: "a family was eating dinner when the sky tore open"
- NOT generic ruin aesthetics

### Register 2 — Broken World
Register 1 encountering the Severance. Visual wrongness — almost right, but not.
- Same photorealistic foundation as Register 1
- Corruption: geometric crack patterns in stone, metal rusted in hours, opaque water
- Corrupted creatures look like the base creature, except wrong — subtle, not monstrous
- Planar thinning: shadows with mass, temperature anomalies, things that are almost there

### Register 3 — Firstborn World
Ancient, precise, completely alien to everything else.
- Non-human design logic — NOT human architecture made grander
- Different geometric and engineering principles entirely
- Decay is different: a precision instrument's failure ≠ a wooden building's rot
- Stepping into a Firstborn ruin should feel like a different kind of world
- NO organic curves, NO fantasy-trope grandeur, NO human proportions

---

## UE5.7 Import Checklist (after Blender export)
- [ ] FBX exported to correct `/Assets/3D/Exports/[subfolder]/`
- [ ] Textures exported to `/Assets/Textures/[asset-name]/`
- [ ] In UE5.7: Import FBX with "Generate Lightmap UVs" = Yes (static meshes)
- [ ] Enable Nanite on all static environment meshes above 10k tris
- [ ] Assign material slots — do not leave default grey materials
- [ ] For characters: verify skeleton compatibility before import
- [ ] Git commit after successful import: `"assets: imported [asset-name] to UE5.7"`

---

## Style Reference
Always consult before starting any asset:
- `SD_09_Art_Direction_Style_Guide.md` — Primary art direction authority
- `/Assets/Reference/` — Mood boards and concept art
- SD_01 Section 6 — Geographic and environmental descriptions by region

The game looks like **a real place that had a catastrophe four weeks ago.**
Not stylized gloom. Not fantasy aesthetics. A specific place dealing with specific consequences.
