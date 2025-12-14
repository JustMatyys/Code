# Folder Structure Guide

## 📁 Project Organization

```
Geometry Dash (PyGame)/
│
├── main.py                          ⭐ START HERE - Run the game
├── level_manager.py                 Core game engine & level loading
│
├── Editor/
│   ├── level_editor.py              Level editor GUI
│   └── Tests/
│       ├── test_editor.py           Editor functionality tests
│       ├── test_game_integration.py  Game integration tests
│       ├── test_simulation.py        Physics simulation tests
│       └── test_complete_workflow.py End-to-end tests
│
├── Levels/                          Game level files
│   ├── level1.json
│   ├── level2.json
│   ├── level3.json
│   └── custom*.json                 Your custom levels
│
├── Documentation/                   Guides & references
│   ├── EDITOR_QUICKSTART.md         Quick 5-min tutorial
│   ├── LEVEL_EDITOR_GUIDE.md        Complete feature guide
│   ├── EDITOR_IMPLEMENTATION_SUMMARY.md
│   ├── README_EDITOR.md
│   └── (other docs)
│
└── __pycache__/                     Python cache (ignore)
```

## 🎮 Quick Commands

### Run the Game
```bash
python main.py
```

### Run the Level Editor
```bash
python Editor/level_editor.py
```

### Run Tests
```bash
python Editor/Tests/test_editor.py
python Editor/Tests/test_game_integration.py
python Editor/Tests/test_simulation.py
python Editor/Tests/test_complete_workflow.py
```

## 📂 What's Where

| What | Where |
|------|-------|
| Game Executable | `main.py` (root) |
| Level Editor | `Editor/level_editor.py` |
| Test Suites | `Editor/Tests/` |
| Level Files | `Levels/` |
| Documentation | `Documentation/` |
| Core Engine | `level_manager.py` (root) |

## ✨ File Purposes

### Root Level
- **main.py** - The game executable. Run this to play!
- **level_manager.py** - Handles level loading, game state, physics

### Editor/
- **level_editor.py** - GUI editor for creating custom levels
- **Tests/** - All test scripts for validation

### Levels/
- **level*.json** - Original built-in levels
- **custom*.json** - Custom levels you create with the editor

### Documentation/
- Step-by-step guides
- Feature documentation
- Implementation details
- Quick reference

## 🚀 Getting Started

1. **Play the game**: `python main.py`
2. **Create levels**: `python Editor/level_editor.py`
3. **Save custom levels**: They go to `Levels/custom*.json`
4. **Read guides**: Check `Documentation/` for help

## 🧪 Testing

All test files are in `Editor/Tests/` and automatically find:
- The root directory for `level_manager.py`
- The `Editor/` directory for `level_editor.py`
- The `Levels/` directory for level files

Just run any test from the project root:
```bash
python Editor/Tests/test_editor.py
```

## 💡 Import Paths

Both the editor and tests use smart path resolution:
- They automatically find parent directories
- They work from any working directory
- No hardcoded paths needed

This means you can run:
```bash
# From project root
python Editor/level_editor.py

# From anywhere
cd /path/to/project && python Editor/level_editor.py
```

Both work! ✓

## 📝 Notes

- `__pycache__` can be safely ignored (Python cache)
- Custom levels automatically appear in the game menu
- Test files can be run independently
- All imports use relative path resolution

---

**Everything is organized and easy to find!** 🎉
