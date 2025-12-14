# Geometry Dash Level Format Guide

## Overview

Levels are defined in JSON format and placed in the `Levels/` directory. Each level file must have a `.json` extension and follow the structure below.

## Basic Level Structure

```json
{
  "name": "Level Name",
  "difficulty": 1,
  "time_limit": 0,
  "background_color": [30, 30, 40],
  "spawn_point": [100, 500],
  "end_point": [1200, 300],
  "platforms": [],
  "obstacles": []
}
```

## Field Descriptions

### Top-Level Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Display name of the level |
| `difficulty` | number | 1-10 scale indicating difficulty |
| `time_limit` | number | Time limit in seconds (0 = no limit) |
| `background_color` | array | RGB color [R, G, B] where 0-255 |
| `spawn_point` | array | Starting position [x, y] |
| `end_point` | array | Goal position [x, y] |
| `platforms` | array | Array of platform objects |
| `obstacles` | array | Array of obstacle objects |

## Platforms

Platforms are surfaces the player can jump on.

### Platform Properties

```json
{
  "x": 300,
  "y": 500,
  "width": 200,
  "height": 20,
  "type": "ground",
  "color": [100, 150, 200],
  "speed": 0,
  "direction": 1
}
```

| Property | Type | Description |
|----------|------|-------------|
| `x` | number | X coordinate (top-left) |
| `y` | number | Y coordinate (top-left) |
| `width` | number | Width in pixels |
| `height` | number | Height in pixels |
| `type` | string | Type: `"ground"`, `"moving"`, or `"spring"` |
| `color` | array | RGB color [R, G, B] |
| `speed` | number | Movement speed (0 = stationary) |
| `direction` | number | 1 = right/-1, -1 = left/up |

### Platform Types

- **ground**: Static platform (speed should be 0)
- **moving**: Moves back and forth (set speed > 0)
- **spring**: Bounces player higher on landing (multiplies jump by 1.5x)

## Obstacles

Obstacles kill the player on contact.

### Obstacle Properties

```json
{
  "x": 450,
  "y": 550,
  "width": 40,
  "height": 50,
  "type": "box",
  "color": [255, 100, 0],
  "speed": 0,
  "direction": 1
}
```

| Property | Type | Description |
|----------|------|-------------|
| `x` | number | X coordinate (top-left) |
| `y` | number | Y coordinate (top-left) |
| `width` | number | Width in pixels |
| `height` | number | Height in pixels |
| `type` | string | Type: `"box"` or `"moving_box"` |
| `color` | array | RGB color [R, G, B] |
| `speed` | number | Movement speed (0 = stationary) |
| `direction` | number | 1 = right, -1 = left |

### Obstacle Types

- **box**: Static obstacle
- **moving_box**: Moves horizontally (set speed > 0)

## Example Level (Easy)

```json
{
  "name": "Tutorial",
  "difficulty": 1,
  "time_limit": 0,
  "background_color": [20, 20, 30],
  "spawn_point": [100, 500],
  "end_point": [1100, 300],
  "platforms": [
    {
      "x": 0,
      "y": 600,
      "width": 1280,
      "height": 20,
      "type": "ground",
      "color": [100, 200, 100]
    },
    {
      "x": 300,
      "y": 500,
      "width": 200,
      "height": 20,
      "type": "ground",
      "color": [100, 150, 200]
    },
    {
      "x": 600,
      "y": 400,
      "width": 200,
      "height": 20,
      "type": "ground",
      "color": [100, 150, 200]
    },
    {
      "x": 900,
      "y": 300,
      "width": 200,
      "height": 20,
      "type": "ground",
      "color": [100, 150, 200]
    }
  ],
  "obstacles": [
    {
      "x": 450,
      "y": 550,
      "width": 40,
      "height": 50,
      "type": "box",
      "color": [255, 100, 0]
    }
  ]
}
```

## Example Level (Hard)

```json
{
  "name": "Challenge Course",
  "difficulty": 8,
  "time_limit": 0,
  "background_color": [50, 10, 10],
  "spawn_point": [100, 500],
  "end_point": [1200, 100],
  "platforms": [
    {
      "x": 0,
      "y": 600,
      "width": 1280,
      "height": 20,
      "type": "ground",
      "color": [100, 200, 100]
    },
    {
      "x": 300,
      "y": 500,
      "width": 150,
      "height": 20,
      "type": "moving",
      "color": [150, 100, 200],
      "speed": 200,
      "direction": 1
    },
    {
      "x": 700,
      "y": 350,
      "width": 150,
      "height": 20,
      "type": "spring",
      "color": [200, 200, 0]
    }
  ],
  "obstacles": [
    {
      "x": 400,
      "y": 450,
      "width": 30,
      "height": 50,
      "type": "moving_box",
      "color": [255, 50, 50],
      "speed": 150,
      "direction": 1
    },
    {
      "x": 800,
      "y": 300,
      "width": 30,
      "height": 50,
      "type": "moving_box",
      "color": [255, 50, 50],
      "speed": 180,
      "direction": -1
    }
  ]
}
```

## Creating New Levels

1. **Create a new file**: `Levels/levelX.json` (replace X with your level number)
2. **Copy the basic structure** from above
3. **Fill in your level design**:
   - Set spawn and end points
   - Add platforms to create a path
   - Add obstacles to create challenges
   - Adjust colors for visual appeal
4. **Test it**:
   - Run the game
   - Select your level from the menu (press the number key)
   - Try completing it!

## Tips for Level Design

### Difficulty Progression
- **1-2**: Simple, few obstacles, wide platforms
- **3-4**: Add some moving platforms, moderate spacing
- **5-6**: Moving obstacles, tighter jumps
- **7-8**: Complex sequences, fast moving objects
- **9-10**: Extreme challenges, precision required

### Spacing and Timing
- **Screen width**: 1280 pixels
- **Screen height**: 720 pixels
- Player gravity: 700 px/s²
- Jump power: 400 px/s
- Player radius: 20 pixels

### Design Ideas
- Use moving platforms to extend reach
- Spring platforms for high jumps
- Moving obstacles for timing challenges
- Layered platforms for rhythm sections
- Narrow passages for difficulty spikes

## Screen Coordinates Reference

```
(0, 0) -------- (1280, 0)
  |                    |
  |                    |
  |  GAME AREA        |
  |                    |
  |                    |
(0, 720) ---- (1280, 720)
```

## Color Palette Suggestions

```
Greens:     [100, 200, 100], [150, 200, 100]
Blues:      [100, 150, 200], [100, 100, 200]
Purples:    [150, 100, 200], [200, 100, 200]
Yellows:    [200, 200, 0], [255, 255, 100]
Oranges:    [255, 165, 0], [255, 100, 0]
Reds:       [255, 0, 0], [255, 50, 50]
Grays:      [100, 100, 100], [150, 150, 150]
Dark BGs:   [20, 20, 30], [30, 30, 40]
```

## Troubleshooting

**Level doesn't load?**
- Check JSON syntax (use a JSON validator)
- Make sure file is in `Levels/` directory
- Verify file ends with `.json`

**Level is too easy/hard?**
- Adjust platform spacing
- Increase/decrease obstacle speed
- Add/remove obstacles
- Modify time limit

**Player gets stuck?**
- Check collision boxes don't overlap badly
- Ensure spawn point is on a valid platform
- Verify end point is reachable

## Game Controls

| Key | Action |
|-----|--------|
| `1-9` | Select level in menu |
| `ENTER` / `SPACE` | Start level |
| `SPACE` / `W` / `UP` | Jump during gameplay |
| `M` | Return to menu |
| `ESC` | Return to menu |
| `R` | Retry current level (game over screen) |
