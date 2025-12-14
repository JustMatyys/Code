# Level Editor Quick Start

## Installation

Make sure pygame is installed:
```bash
/home/oem/Code/.venv/bin/pip install pygame
```

## Quick Start in 5 Minutes

### 1. Open the Level Editor
```bash
cd /home/oem/Code/Python/Geometry\ Dash\ \(PyGame\)
python level_editor.py
```

### 2. Build Your Level (Example)

**Create a platform path:**
- Click "Add Platform"
- Click at position (50, 650) - click once
- Click at position (950, 650) - click again
- Bottom platform created!

**Add obstacle:**
- Click "Add Obstacle"  
- Click at (400, 620)
- Click at (430, 650)
- Small obstacle appears

**Set spawn point:**
- Click "Set Spawn"
- Click at (100, 600)
- Blue "S" appears

**Set goal:**
- Click "Set End"
- Click at (900, 300)
- Blue "E" appears

**Save the level:**
- Click "Save Level"
- Saved to `Levels/custom1.json`

### 3. Play in the Game
```bash
python main.py
```
Your custom level appears in the level menu!

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| DELETE | Remove selected object |
| ESC | Cancel current mode |
| Mouse Drag | Move selected objects |

## Tips

✓ Click objects to select them (they highlight)  
✓ Drag to move - works while selected  
✓ Right panel shows object count  
✓ Grid helps with alignment  

## File Locations

- **Editor**: `level_editor.py`
- **Game**: `main.py`
- **Saved Levels**: `Levels/custom1.json`, `Levels/custom2.json`, etc.
- **Documentation**: `LEVEL_EDITOR_GUIDE.md`

## Troubleshooting

**"ModuleNotFoundError: No module named 'pygame'"**
```bash
/home/oem/Code/.venv/bin/pip install pygame
```

**Level doesn't appear in game**
- Make sure you saved it (check `Levels/` folder)
- Restart the game to refresh level list

**Objects won't appear**
- Make sure you clicked twice for platforms/obstacles
- First click sets start, second click sets end

---

That's it! You're ready to create levels. Happy designing! 🎮
