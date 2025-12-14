# Level JSON Format Cheat Sheet

## Copy-Paste Template (Empty Level)

```json
{
  "name": "My Level",
  "difficulty": 3,
  "time_limit": 0,
  "background_color": [30, 30, 40],
  "spawn_point": [100, 500],
  "end_point": [1200, 300],
  "platforms": [],
  "obstacles": []
}
```

## Complete Minimal Level Example

```json
{
  "name": "First Level",
  "difficulty": 1,
  "time_limit": 0,
  "background_color": [20, 20, 30],
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
      "x": 700,
      "y": 400,
      "width": 200,
      "height": 20,
      "type": "ground",
      "color": [100, 150, 200]
    },
    {
      "x": 1100,
      "y": 300,
      "width": 100,
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

## Platform Snippets

### Ground Platform
```json
{
  "x": 0,
  "y": 600,
  "width": 300,
  "height": 20,
  "type": "ground",
  "color": [100, 200, 100]
}
```

### Moving Platform (Right/Left)
```json
{
  "x": 300,
  "y": 400,
  "width": 150,
  "height": 20,
  "type": "moving",
  "color": [150, 100, 200],
  "speed": 150,
  "direction": 1
}
```

### Spring Platform (High Jump)
```json
{
  "x": 600,
  "y": 300,
  "width": 150,
  "height": 20,
  "type": "spring",
  "color": [200, 200, 0]
}
```

## Obstacle Snippets

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

### Moving Box (Right/Left)
```json
{
  "x": 450,
  "y": 450,
  "width": 30,
  "height": 50,
  "type": "moving_box",
  "color": [255, 50, 50],
  "speed": 120,
  "direction": 1
}
```

## Difficulty Guidelines

### Difficulty 1 (Tutorial)
```json
"difficulty": 1,
"platforms": [
  {"x": 0, "y": 600, "width": 1280, "height": 20, "type": "ground", "color": [100, 200, 100]},
  {"x": 300, "y": 500, "width": 300, "height": 20, "type": "ground", "color": [100, 150, 200]},
  {"x": 700, "y": 400, "width": 300, "height": 20, "type": "ground", "color": [100, 150, 200]}
],
"obstacles": []
```

### Difficulty 5 (Medium)
```json
"difficulty": 5,
"platforms": [
  {"x": 0, "y": 600, "width": 1280, "height": 20, "type": "ground", "color": [100, 200, 100]},
  {"x": 300, "y": 500, "width": 150, "height": 20, "type": "moving", "color": [150, 100, 200], "speed": 150, "direction": 1},
  {"x": 700, "y": 350, "width": 150, "height": 20, "type": "spring", "color": [200, 200, 0]},
  {"x": 1050, "y": 300, "width": 150, "height": 20, "type": "ground", "color": [100, 150, 200]}
],
"obstacles": [
  {"x": 400, "y": 450, "width": 30, "height": 50, "type": "moving_box", "color": [255, 50, 50], "speed": 120, "direction": 1},
  {"x": 850, "y": 300, "width": 30, "height": 50, "type": "box", "color": [255, 100, 0]}
]
```

### Difficulty 9 (Expert)
```json
"difficulty": 9,
"platforms": [
  {"x": 0, "y": 600, "width": 1280, "height": 20, "type": "ground", "color": [100, 200, 100]},
  {"x": 200, "y": 500, "width": 100, "height": 20, "type": "ground", "color": [100, 150, 200]},
  {"x": 400, "y": 420, "width": 100, "height": 20, "type": "moving", "color": [150, 100, 200], "speed": 200, "direction": 1},
  {"x": 650, "y": 350, "width": 100, "height": 20, "type": "spring", "color": [200, 200, 0]},
  {"x": 900, "y": 300, "width": 100, "height": 20, "type": "moving", "color": [150, 100, 200], "speed": 250, "direction": -1}
],
"obstacles": [
  {"x": 350, "y": 550, "width": 25, "height": 50, "type": "box", "color": [255, 100, 0]},
  {"x": 500, "y": 470, "width": 25, "height": 50, "type": "moving_box", "color": [255, 50, 50], "speed": 180, "direction": 1},
  {"x": 800, "y": 400, "width": 25, "height": 50, "type": "moving_box", "color": [255, 50, 50], "speed": 200, "direction": -1}
]
```

## Color Palette Reference

| Purpose | RGB | Usage |
|---------|-----|-------|
| Ground | [100, 200, 100] | Safe platforms |
| Platform | [100, 150, 200] | Secondary platforms |
| Moving | [150, 100, 200] | Moving platforms |
| Spring | [200, 200, 0] | High jump platforms |
| Obstacle | [255, 100, 0] | Static hazards |
| Moving Obstacle | [255, 50, 50] | Moving hazards |
| Background Dark | [20, 20, 30] | Easy backgrounds |
| Background Red | [50, 10, 10] | Hard/dark level |

## Common Mistakes & Fixes

### ❌ No platforms at spawn
```json
// WRONG - player falls immediately
"spawn_point": [100, 300],
"platforms": [{"x": 200, "y": 500, ...}]

// RIGHT - spawn on a platform
"spawn_point": [100, 500],
"platforms": [{"x": 0, "y": 600, "width": 1280, "height": 20, ...}]
```

### ❌ End point unreachable
```json
// WRONG - gap too large
"end_point": [1200, 0],

// RIGHT - reasonable jump distance
"end_point": [1200, 300]
```

### ❌ JSON syntax errors
```json
// WRONG - trailing commas
"obstacles": [
  {"x": 100, "y": 100, ...},  // ← extra comma!
]

// RIGHT - no trailing commas
"obstacles": [
  {"x": 100, "y": 100, ...}
]
```

## Step-by-Step: Create a Level

1. **Copy template** from top of this file
2. **Set name & difficulty**
   ```json
   "name": "My Awesome Level",
   "difficulty": 4
   ```

3. **Pick background color**
   ```json
   "background_color": [30, 30, 40]
   ```

4. **Set spawn & end points**
   ```json
   "spawn_point": [100, 500],
   "end_point": [1200, 300]
   ```

5. **Add bottom platform**
   ```json
   "platforms": [
     {
       "x": 0, "y": 600, "width": 1280,
       "height": 20, "type": "ground",
       "color": [100, 200, 100]
     }
   ]
   ```

6. **Add middle platforms** (staircase to goal)
   ```json
   {
     "x": 300, "y": 500, "width": 200,
     "height": 20, "type": "ground",
     "color": [100, 150, 200]
   },
   {
     "x": 700, "y": 400, "width": 200,
     "height": 20, "type": "ground",
     "color": [100, 150, 200]
   }
   ```

7. **Add obstacles** (optional)
   ```json
   "obstacles": [
     {
       "x": 450, "y": 550, "width": 40,
       "height": 50, "type": "box",
       "color": [255, 100, 0]
     }
   ]
   ```

8. **Save as** `Levels/myLevel.json`

9. **Run game** and test!

---

**Need more help?** See LEVEL_FORMAT.md for complete documentation!
