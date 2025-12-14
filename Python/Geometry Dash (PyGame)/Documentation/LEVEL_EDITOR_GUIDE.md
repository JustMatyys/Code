# Level Editor Documentation

## Overview

The **Geometry Dash Level Editor** (`level_editor.py`) is a GUI tool that allows you to create and edit custom levels for the Geometry Dash game. All custom levels are automatically saved to `Levels/customXYZ.json` and can be played directly in the main game.

## Features

✓ **Full Object Support**
  - Platforms (ground, spring, moving)
  - Obstacles (box, spike, moving_box)
  - Spawn and End points
  - Level properties (difficulty, time limit, background color)

✓ **Easy to Use Interface**
  - Visual canvas with grid (1000x720 pixels)
  - Button-based controls
  - Real-time object placement
  - Drag and drop to move objects

✓ **File Management**
  - Save levels to `Levels/customXYZ.json`
  - Load and edit existing levels
  - Auto-numbered custom levels
  - Proper path handling (works from any directory)

## Running the Editor

```bash
python level_editor.py
```

The editor will open with:
- **Left panel (1000x720)**: Canvas for building levels
- **Right panel (400 width)**: Controls and level info

## How to Use

### 1. Add Platforms

1. Click **"Add Platform"** button
2. Mode changes to "ADD_PLATFORM"
3. Click once on the canvas to set the start point
4. Click again to set the end point (creates a rectangle)
5. Platform is placed - now in SELECT mode

**Platform Types** (edit in code if needed):
- `ground` - Normal platform
- `spring` - Bounces player higher
- `moving` - Moves back and forth

### 2. Add Obstacles

1. Click **"Add Obstacle"** button
2. Mode changes to "ADD_OBSTACLE"
3. Click once to set start point
4. Click again to set end point
5. Obstacle is placed

**Obstacle Types**:
- `box` - Standard obstacle
- `spike` - Sharp object
- `moving_box` - Moves back and forth

### 3. Set Spawn Point (Where player starts)

1. Click **"Set Spawn"** button
2. Click anywhere on canvas
3. Blue circle with "S" marks the spawn point

### 4. Set End Point (Level goal)

1. Click **"Set End"** button
2. Click anywhere on canvas
3. Blue circle with "E" marks the goal location

### 5. Configure Level Properties

Click **"Properties"** button to view/edit:
- Level name
- Difficulty (1-10)
- Time limit (0 = no limit)
- Background color

*(Currently shown in console - edit directly in `level_editor.py` if needed)*

### 6. Save Level

Click **"Save Level"** button to:
- Auto-generate filename (custom1.json, custom2.json, etc.)
- Save to `Levels/` directory
- Print confirmation with file path

### 7. Load Level

Click **"Load Level"** button to:
- See list of available levels
- Choose which level to edit
- Load into editor

### 8. Delete Objects

1. Click on an object to select it (highlighted)
2. Press **Delete key** OR click **"Delete Sel."** button
3. Object is removed

### 9. Clear All

Click **"Clear All"** button to remove all objects at once.

## Controls

| Action | Control |
|--------|---------|
| Select Mode | ESC key |
| Delete Selected | Delete key |
| Drag Objects | Click + hold + drag |
| Pan View | N/A (full canvas visible) |
| Mode Indicator | Top-left of canvas |

## Visual Guide

```
┌─────────────────────────────────┬──────────────┐
│                                 │              │
│    CANVAS (1000x720)            │  CONTROLS    │
│                                 │              │
│  [Grid]                         │  [Buttons]   │
│  Platform: Green rect           │              │
│  Obstacle: Red rect             │  [Info]      │
│  Spawn "S": Blue circle         │              │
│  End "E": Blue circle           │              │
│                                 │              │
└─────────────────────────────────┴──────────────┘
```

## File Format

Saved levels are JSON files with this structure:

```json
{
  "name": "Custom Level 1",
  "difficulty": 5,
  "time_limit": 30.0,
  "background_color": [20, 20, 30],
  "spawn_point": [100, 100],
  "end_point": [900, 300],
  "platforms": [
    {
      "x": 50,
      "y": 650,
      "width": 900,
      "height": 30,
      "type": "ground",
      "color": [100, 150, 100],
      "speed": 0,
      "direction": 1
    }
  ],
  "obstacles": [
    {
      "x": 350,
      "y": 600,
      "width": 40,
      "height": 50,
      "type": "box",
      "color": [255, 100, 100],
      "speed": 0,
      "direction": 1
    }
  ]
}
```

## Playing Custom Levels

Once saved, custom levels appear automatically in the main game:

```bash
python main.py
```

Select custom levels from the menu just like built-in levels!

## Path Resolution

The editor uses smart path resolution:
- Finds the `Levels/` directory relative to the editor script
- Works regardless of where you run the command from
- Matches with game's path resolution system

## Troubleshooting

### "No levels to load" error
- Check that `Levels/` directory exists
- Verify levels are saved with `.json` extension

### Level doesn't appear in game
- Make sure you saved the level (check for `customX.json` in `Levels/`)
- Restart the game to refresh level list
- Check file permissions

### Objects disappear when dragging
- Ensure you're clicking within the canvas area
- Objects are constrained to canvas boundaries

### Game crashes when loading level
- Check JSON syntax (save console output)
- Verify spawn point is within canvas
- Ensure all required fields are present

## Advanced Customization

Edit `level_editor.py` to customize:

```python
# Line 13-14: Change canvas size
self.canvas_rect = pygame.Rect(0, 0, 1000, self.screen_height)

# Line 22-25: Change default level properties
self.difficulty = 5
self.time_limit = 0.0
self.background_color = (20, 20, 30)

# Line 128: Change default platform type when adding
self.new_platform_type = "ground"

# Line 129: Change default obstacle type when adding
self.new_obstacle_type = "box"
```

## Performance

- Handles up to 50+ objects without lag
- Grid redraw optimized at 60 FPS
- Smooth dragging and interaction

## Tips for Level Design

1. **Start with spawn point** - Set it where player enters
2. **Add platforms progressively** - Build safe paths first
3. **Add obstacles** - Place challenges strategically
4. **Set end point** - Place goal at difficulty level
5. **Test in game** - Play to verify difficulty
6. **Adjust difficulty rating** - Scale with actual challenge

## Known Limitations

- Moving platform speeds must be edited in JSON manually
- Platform/obstacle colors limited to predefined RGB tuples
- No undo/redo system (save frequently!)
- No preview of moving obstacles in editor

## Future Enhancements

Potential improvements:
- [ ] Property editor GUI dialog
- [ ] Undo/redo system
- [ ] Moving platform speed adjustment in GUI
- [ ] Color picker for custom colors
- [ ] Level preview/playtest mode
- [ ] Multi-level project management
