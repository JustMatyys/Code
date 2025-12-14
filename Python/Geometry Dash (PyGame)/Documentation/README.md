# Geometry Dash Level Loader

A fully-featured level loading system for a Geometry Dash clone built with PyGame. Create custom levels using simple JSON files!

## Features

✅ **Level Loading System** - Load levels from JSON files  
✅ **Platform Types** - Static, moving, and spring platforms  
✅ **Obstacle Types** - Static and moving obstacles  
✅ **Level Progression** - Play through multiple levels  
✅ **Difficulty Scaling** - 1-10 difficulty settings  
✅ **Game States** - Menu, playing, game over, level complete  
✅ **Easy Level Creation** - Simple JSON format  

## File Structure

```
Geometry Dash (PyGame)/
├── main.py              # Main game file (run this!)
├── level_manager.py     # Level loading and game logic
├── LEVEL_FORMAT.md      # Documentation on creating levels
├── Levels/              # Level files directory
│   ├── level1.json      # Starter Level
│   ├── level2.json      # Moving Challenges
│   └── level3.json      # Spike Gauntlet
└── Assets/              # Game assets
```

## Installation

1. Install Python 3.8+
2. Install pygame:
   ```bash
   pip install pygame
   ```
3. Run the game:
   ```bash
   python main.py
   ```

## How to Play

- **Select Level**: Press `1-9` to select a level in the menu
- **Start**: Press `ENTER` to start the level
- **Jump**: Press `SPACE`, `W`, or `UP ARROW` to jump
- **Menu**: Press `M` or `ESC` to return to menu
- **Retry**: Press `R` on game over screen (when dead)

## Game Objectives

- **Reach the green circle** at the end of each level
- **Avoid red obstacles** - they kill you on contact
- **Land on platforms** - falling off kills you
- **Progress through levels** - each level gets harder

## Creating Your Own Levels

### Quick Start

1. Create a new file: `Levels/myLevel.json`
2. Copy this template:

```json
{
  "name": "My Level",
  "difficulty": 3,
  "time_limit": 0,
  "background_color": [30, 30, 40],
  "spawn_point": [100, 500],
  "end_point": [1200, 300],
  "platforms": [
    {
      "x": 0,
      "y": 600,
      "width": 1280,
      "height": 20,
      "type": "ground",
      "color": [100, 200, 100]
    }
  ],
  "obstacles": []
}
```

3. Run the game and your level will appear in the menu!

### Level Format Details

See [LEVEL_FORMAT.md](LEVEL_FORMAT.md) for comprehensive documentation on:
- All JSON fields and their meanings
- Platform types (ground, moving, spring)
- Obstacle types (box, moving_box)
- Color palettes
- Design tips
- Examples

### Example Level Concepts

**Easy Level (Difficulty 1-2)**
- Wide platforms
- Simple jumps
- Few obstacles
- Plenty of space to land

**Medium Level (Difficulty 3-5)**
- Moving platforms
- Moderate spacing
- Some moving obstacles
- Spring platforms for variety

**Hard Level (Difficulty 7+)**
- Fast moving obstacles
- Tight platform spacing
- Complex sequences
- Precision jumping required

## Game Architecture

### main.py
- Handles game loop, events, and rendering
- Manages game states (menu, playing, game over, level complete)
- Controls level progression

### level_manager.py

**LevelManager** - Loads and manages levels
- `load_level_from_file()` - Load a level from JSON
- `get_level()` - Retrieve a loaded level
- `list_levels()` - Get all available levels

**GameState** - Manages game state during play
- `update()` - Update physics, collisions, and game state
- `jump()` - Make the player jump
- Collision detection with platforms and obstacles

**Data Classes**
- `LevelData` - Complete level definition
- `Platform` - Platform objects
- `Obstacle` - Obstacle objects

## Physics Constants

- **Gravity**: 700 pixels/second²
- **Jump Power**: 400 pixels/second
- **Player Radius**: 20 pixels
- **Screen Size**: 1280×720 pixels

Modify these in `level_manager.py` GameState class to change gameplay feel.

## Tips for Great Levels

1. **Test your levels** - Make sure they're actually completable!
2. **Gradual difficulty** - Introduce new concepts gradually
3. **Visual feedback** - Use different colors for different platform types
4. **Pacing** - Mix easy and hard sections
5. **Interesting obstacles** - Combine moving and static obstacles
6. **Use springs** - Give players a break with high jumps

## Included Example Levels

### Level 1: Starter Level (Difficulty 1)
Simple introductory level with basic jumps and a few obstacles.

### Level 2: Moving Challenges (Difficulty 3)
Introduces moving platforms and moving obstacles. Features a spring platform near the end.

### Level 3: Spike Gauntlet (Difficulty 5)
Challenge course with many obstacles in sequence. Tests precision jumping.

## Troubleshooting

**Game won't start?**
- Make sure pygame is installed: `pip install pygame`
- Check that you're in the correct directory

**Levels not loading?**
- Check that .json files are in the `Levels/` directory
- Validate JSON syntax (no trailing commas, proper quotes)
- Check console output for error messages

**Level too easy/hard?**
- Adjust difficulty rating in JSON
- Modify platform spacing
- Add/remove obstacles
- Adjust obstacle speed values

**Player controls feel weird?**
- Physics constants can be modified in `level_manager.py`
- Adjust `gravity` and `jump_power` in the `GameState.__init__()` method

## Ideas for Future Improvements

- 🎨 Custom player colors/skins
- 🎵 Background music and sound effects
- 📊 High score tracking
- 🎯 Coins to collect
- ⭐ Star rating system (based on time)
- 🚀 Boost pads
- 👻 Spike patterns
- 🌊 Wave sections
- 📹 Replay system
- 🌍 Level sharing/importing

## License

Feel free to modify and expand this project!

## Questions?

Refer to [LEVEL_FORMAT.md](LEVEL_FORMAT.md) for detailed level creation documentation.