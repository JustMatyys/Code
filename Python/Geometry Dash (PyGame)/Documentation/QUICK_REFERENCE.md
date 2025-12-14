# JSON Level Format Quick Reference

## Minimal Level Template

```json
{
  "name": "My Level",
  "difficulty": 1,
  "time_limit": 0,
  "background_color": [30, 30, 40],
  "spawn_point": [100, 500],
  "end_point": [1200, 300],
  "platforms": [],
  "obstacles": []
}
```

## Platform Types

### Ground Platform (Static)
```json
{
  "x": 0,
  "y": 600,
  "width": 1280,
  "height": 20,
  "type": "ground",
  "color": [100, 200, 100]
}
```

### Moving Platform (Bounces at screen edges)
```json
{
  "x": 300,
  "y": 500,
  "width": 150,
  "height": 20,
  "type": "moving",
  "color": [150, 100, 200],
  "speed": 200,
  "direction": 1
}
```

### Spring Platform (Bounces player 1.5x higher)
```json
{
  "x": 600,
  "y": 350,
  "width": 150,
  "height": 20,
  "type": "spring",
  "color": [200, 200, 0]
}
```

## Obstacle Types

### Static Box
```json
{
  "x": 450,
  "y": 550,
  "width": 40,
  "height": 50,
  "type": "box",
  "color": [255, 100, 0]
}
```

### Moving Box (Bounces at screen edges)
```json
{
  "x": 450,
  "y": 450,
  "width": 30,
  "height": 50,
  "type": "moving_box",
  "color": [255, 50, 50],
  "speed": 150,
  "direction": 1
}
```

## Common Parameters

| Param | Range | Notes |
|-------|-------|-------|
| difficulty | 1-10 | Visual/informational |
| time_limit | 0+ | 0 = no limit |
| speed | 0-300+ | pixels/second |
| direction | 1 or -1 | 1=right/down, -1=left/up |

## Screen Layout

```
Game Area: 1280×720 pixels
Common spawn: [100, 500]
Common end: [1200, 300]
Platform height: typically 20px
Platform width: 100-300px
Obstacle size: 30-40×50-60px
```

## Color Palette

```
Greens:  [100, 200, 100], [150, 200, 100]
Blues:   [100, 150, 200], [100, 100, 200]
Reds:    [255, 0, 0], [255, 100, 0]
Purples: [150, 100, 200]
Yellows: [200, 200, 0]
Grays:   [100, 100, 100]
Black:   [0, 0, 0]
```

## Creating Levels

1. **Copy template** from section above
2. **Add platforms** - create a path to the goal
3. **Add obstacles** - place challenges in the path
4. **Adjust colors** - make visually distinct
5. **Test** - can you beat your own level?

## Tips

- **Screen width** is 1280, **height** is 720
- **Player radius** is 20 pixels
- **Spawn point** should be on a platform
- **End point** should be reachable
- **Moving objects** bounce at screen edges (both sides)
- **Speed 100** = moderate movement
- **Speed 200** = fast movement
- **Difficulty 1-2** for tutorials
- **Difficulty 8-10** for experts

## File Checklist

Before saving:
- ✅ Valid JSON (no trailing commas)
- ✅ File in `Levels/` directory
- ✅ File ends with `.json`
- ✅ Name is descriptive
- ✅ Spawn point on a platform
- ✅ End point reachable
- ✅ All coordinates are numbers
- ✅ Colors are [R, G, B] 0-255
