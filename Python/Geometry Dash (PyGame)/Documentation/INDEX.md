# 📖 Documentation Index

## Getting Started (Start Here!)

1. **[README.md](README.md)** - Overview and installation
   - How to install and run
   - How to play
   - Quick level creation guide

2. **[SYSTEM_OVERVIEW.md](SYSTEM_OVERVIEW.md)** - Complete system architecture
   - What's been created
   - How everything works together
   - Quick tips and tricks

## Creating Levels

### For Quick Level Creation
- **[CHEAT_SHEET.md](CHEAT_SHEET.md)** ⭐ START HERE for copy-paste templates
  - Ready-to-use JSON snippets
  - Complete examples at different difficulties
  - Common mistakes and fixes

### For Detailed Reference
- **[LEVEL_FORMAT.md](LEVEL_FORMAT.md)** - Complete level format documentation
  - All fields explained
  - Platform types
  - Obstacle types
  - Color palettes
  - Level design tips

### Quick Tips
- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - One-page reference
  - Parameters and ranges
  - Screen coordinates
  - Color palette

## Example Levels

See these in action in the game:
- **Levels/level1.json** - Starter Level (Easy)
- **Levels/level2.json** - Moving Challenges (Medium)
- **Levels/level3.json** - Spike Gauntlet (Hard)

## Code Files

- **main.py** - Main game file (run this!)
- **level_manager.py** - Level loading and physics engine

## How to Navigate

### "I want to create a level RIGHT NOW"
→ Go to [CHEAT_SHEET.md](CHEAT_SHEET.md) and copy a template!

### "I want to understand the whole system"
→ Read [SYSTEM_OVERVIEW.md](SYSTEM_OVERVIEW.md)

### "I want detailed reference on JSON format"
→ Check [LEVEL_FORMAT.md](LEVEL_FORMAT.md)

### "I'm stuck or need quick tips"
→ Look in [QUICK_REFERENCE.md](QUICK_REFERENCE.md)

### "I need step-by-step help"
→ See the "Step-by-Step: Create a Level" section in [CHEAT_SHEET.md](CHEAT_SHEET.md)

## Quick Links by Topic

### Game Controls
→ [README.md](README.md#how-to-play)

### Platform Types
→ [CHEAT_SHEET.md](CHEAT_SHEET.md#platform-snippets) or [LEVEL_FORMAT.md](LEVEL_FORMAT.md#platform-types)

### Obstacle Types
→ [CHEAT_SHEET.md](CHEAT_SHEET.md#obstacle-snippets) or [LEVEL_FORMAT.md](LEVEL_FORMAT.md#obstacle-types)

### Difficulty Guidelines
→ [CHEAT_SHEET.md](CHEAT_SHEET.md#difficulty-guidelines) or [LEVEL_FORMAT.md](LEVEL_FORMAT.md#difficulty-progression)

### Level Design Tips
→ [LEVEL_FORMAT.md](LEVEL_FORMAT.md#tips-for-level-design)

### Physics Constants
→ [SYSTEM_OVERVIEW.md](SYSTEM_OVERVIEW.md#-physics-constants)

### Architecture
→ [SYSTEM_OVERVIEW.md](SYSTEM_OVERVIEW.md#-architecture)

### Troubleshooting
→ [README.md](README.md#troubleshooting)

## File Organization

```
README.md               ← Start here
SYSTEM_OVERVIEW.md     ← Understand the system
CHEAT_SHEET.md         ← Copy templates
LEVEL_FORMAT.md        ← Detailed reference
QUICK_REFERENCE.md     ← One-page reference
main.py                ← Run this
level_manager.py       ← Game engine
Levels/
  ├── level1.json      ← Example easy level
  ├── level2.json      ← Example medium level
  └── level3.json      ← Example hard level
```

## Common Tasks

### Create Your First Level
1. Open [CHEAT_SHEET.md](CHEAT_SHEET.md)
2. Copy the "Copy-Paste Template" section
3. Paste into new file: `Levels/myLevel.json`
4. Modify the name, platforms, and obstacles
5. Save and run the game!

### Make a Moving Platform Level
1. Check "Moving Platform" snippet in [CHEAT_SHEET.md](CHEAT_SHEET.md)
2. Copy and modify speed/direction
3. Add multiple moving platforms for challenge

### Create a Specific Difficulty Level
1. Find the difficulty level in [CHEAT_SHEET.md](CHEAT_SHEET.md) "Difficulty Guidelines"
2. Copy the entire example
3. Customize platforms and obstacles

### Understand How Platforms Work
1. Read [LEVEL_FORMAT.md](LEVEL_FORMAT.md#platforms)
2. Check examples in [CHEAT_SHEET.md](CHEAT_SHEET.md#platform-snippets)
3. Look at actual JSON files in Levels/

### Learn Game Architecture
1. Read [SYSTEM_OVERVIEW.md](SYSTEM_OVERVIEW.md#-architecture)
2. Study the classes in level_manager.py
3. Trace through main.py game loop

## Tips for Success

✅ **Always validate JSON** before testing
- Use an online JSON validator
- Check for trailing commas
- Ensure quotes are correct

✅ **Start simple**
- Create easy levels first
- Add complexity gradually
- Test frequently

✅ **Use examples**
- Study the included level files
- Copy and modify them
- Experiment with different values

✅ **Keep the format consistent**
- Follow the JSON structure exactly
- Use the same field names
- Match data types (numbers vs strings)

## Document Legend

| Document | Best For | Read Time |
|----------|----------|-----------|
| README.md | Getting started | 5 min |
| SYSTEM_OVERVIEW.md | Understanding everything | 10 min |
| CHEAT_SHEET.md | Copy-paste templates | 2 min |
| LEVEL_FORMAT.md | Detailed reference | 15 min |
| QUICK_REFERENCE.md | Quick lookup | 1 min |

---

**Ready to create levels? Start with [CHEAT_SHEET.md](CHEAT_SHEET.md)! 🎮**
