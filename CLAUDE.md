# Shattered Dominion — Claude Code Instructions

## First: Read the Context File
Before any task touching game design, lore, naming, characters, factions,
or story content, read:
  /Design_Bible/SHATTERED_DOMINION_CONTEXT.md

This file contains all canonical facts, open decisions, terminology rules,
and behavioral instructions for this project. It is the authoritative
reference. Do not proceed on design tasks without reading it.

---

## Engine & Pipeline
- **Engine:** Unreal Engine 5.7
- **3D Tool:** Blender (connected via MCP)
- **Export format:** FBX (Blender source → FBX export → UE5.7 import)
- **Key UE5.7 systems in use:** Lumen (global illumination), Nanite (environment
  geometry), MetaHuman-compatible pipeline for characters

### UE5.7-Specific Rules
- All Blueprint work goes in `/Game_Code/Blueprints/`
- All C++ source goes in `/Game_Code/Source/`
- UE5.7 project file (.uproject) lives at project root — do not move it
- Use Lumen for all dynamic lighting. No baked lighting unless explicitly instructed.
- Nanite should be enabled on all static environment meshes above 10k tris
- Character skeletons must be UE5 compatible (root bone at origin, Y-forward)

---

## Folder Permissions

| Folder | Permission | Notes |
|---|---|---|
| `/Design_Bible/` | READ only | Never edit without explicit instruction. Use `/doc-edit` command when editing. |
| `/Assets/3D/Source/` | READ/WRITE | Blender .blend working files live here |
| `/Assets/3D/Exports/` | WRITE (exports only) | FBX and GLB files for UE5.7 import. Never modify .blend files here. |
| `/Assets/Textures/` | READ/WRITE | PNG and EXR texture files |
| `/Assets/Reference/` | READ only | Concept art and style references — never modify |
| `/Tools_and_Scripts/` | READ/WRITE | Python tools and pipeline scripts |
| `/Game_Code/` | READ/WRITE | UE5.7 Blueprints, C++ source, project files |
| `/Archive/` | READ only | Superseded files — never modify, never delete |

---

## Blender + MCP Rules
- Before any modeling task, state which visual register the asset belongs to:
  **Ordinary World**, **Broken World**, or **Firstborn World** (defined in SD_09)
- Firstborn assets must NOT use human architectural proportions, organic curves,
  or fantasy-trope design logic. Geometric precision and non-human logic only.
  Read SD_09 Section on Register 3 before modeling any Firstborn asset.
- After modeling, always export FBX to `/Assets/3D/Exports/` in the correct
  subfolder (Characters / Environment / Props / Creatures)
- Asset naming convention: `[race/category]_[descriptor]_[variant]`
  Examples: `human_armor_vanguard_v1`, `vaelari_npc_rootbound_elder`,
  `firstborn_ruin_arch_standard`

---

## Slash Commands
Use these for recurring tasks. They encode the correct workflow:
- `/consistency-check` — Audit all SD files against canonical facts
- `/new-asset` — Pre-model checklist (visual register, style rules)
- `/doc-edit` — Document editing protocol (version bump, change log, canonical check)

---

## Git Rules
- This project uses git for version control
- After any significant file change, commit with a clear message:
  `git commit -m "[area]: [what changed and why]"`
  Examples: `"design: SD_03 updated endings count to three"`
           `"assets: exported vanguard armor FBX to /Exports/Characters/"`
           `"code: added lattice corruption damage blueprint"`
- Never force-push. Never rebase shared history.
- `.blend1` and `.blend2` autosave files are in `.gitignore` — do not add them

---

## Critical Rules (Never Violate)
1. Never resolve open design decisions — flag them and ask Kyle
2. Never use "Sylvarai" — the race is called "Vaelari"
3. Never describe Ironkin or Drakelings as playable — expansion-only
4. Never reference four acts or four endings — three acts, three endings
5. Never edit `/Archive/` or `/Assets/Reference/`
6. Never import .blend files into UE5.7 — FBX exports only
7. Never commit UE5.7 derived data (DerivedDataCache, Intermediate, Saved folders)
   — these are in .gitignore

---

## If You're Unsure
- Design question → read SHATTERED_DOMINION_CONTEXT.md first
- Open decision encountered → stop, flag it, ask Kyle
- New inconsistency found → flag it at the start of your response
- UE5.7 / engine question → proceed with best practice and note assumptions made
