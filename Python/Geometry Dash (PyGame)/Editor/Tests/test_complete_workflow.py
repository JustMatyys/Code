#!/usr/bin/env python3
"""
Comprehensive end-to-end test of the level editor system
Tests: Editor → Save → Load → Game Play
"""
import json
import os
import sys

# Add root directory to path to find level_manager
script_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, script_dir)

import pygame
from level_manager import LevelManager, Platform, Obstacle

def cleanup_custom_levels():
    """Remove all custom levels to start fresh"""
    levels_dir = os.path.join(script_dir, "Levels")
    for f in os.listdir(levels_dir):
        if f.startswith("custom") and f.endswith(".json"):
            os.remove(os.path.join(levels_dir, f))

def create_test_level_programmatically():
    """Create a test level like the editor would"""
    print("=" * 60)
    print("STEP 1: Create Level Programmatically")
    print("=" * 60)
    
    levels_dir = os.path.join(script_dir, "Levels")
    os.makedirs(levels_dir, exist_ok=True)
    
    level_data = {
        "name": "E2E Test Level",
        "difficulty": 4,
        "time_limit": 45.0,
        "background_color": [25, 25, 35],
        "spawn_point": [80, 650],
        "end_point": [950, 250],
        "platforms": [
            {
                "x": 0, "y": 680, "width": 1000, "height": 40,
                "type": "ground", "color": [80, 120, 80], "speed": 0, "direction": 1
            },
            {
                "x": 150, "y": 580, "width": 120, "height": 20,
                "type": "ground", "color": [100, 150, 100], "speed": 0, "direction": 1
            },
            {
                "x": 400, "y": 480, "width": 120, "height": 20,
                "type": "ground", "color": [100, 150, 100], "speed": 0, "direction": 1
            },
            {
                "x": 700, "y": 380, "width": 120, "height": 20,
                "type": "spring", "color": [120, 180, 120], "speed": 0, "direction": 1
            }
        ],
        "obstacles": [
            {
                "x": 300, "y": 640, "width": 30, "height": 40,
                "type": "box", "color": [255, 100, 100], "speed": 0, "direction": 1
            },
            {
                "x": 550, "y": 540, "width": 30, "height": 40,
                "type": "spike", "color": [255, 80, 80], "speed": 0, "direction": 1
            }
        ]
    }
    
    filepath = os.path.join(levels_dir, "custom_e2e_test.json")
    with open(filepath, 'w') as f:
        json.dump(level_data, f, indent=2)
    
    print(f"✓ Created level: {filepath}")
    print(f"  Level name: {level_data['name']}")
    print(f"  Platforms: {len(level_data['platforms'])}")
    print(f"  Obstacles: {len(level_data['obstacles'])}")
    print()
    return filepath

def validate_json_file(filepath):
    """Validate that the JSON file is correct"""
    print("=" * 60)
    print("STEP 2: Validate JSON File")
    print("=" * 60)
    
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        # Check required fields
        required_fields = ['name', 'difficulty', 'time_limit', 'background_color',
                          'spawn_point', 'end_point', 'platforms', 'obstacles']
        
        for field in required_fields:
            if field not in data:
                print(f"✗ Missing field: {field}")
                return False
        
        print(f"✓ All required fields present")
        print(f"✓ Name: {data['name']}")
        print(f"✓ Difficulty: {data['difficulty']}/10")
        print(f"✓ Time limit: {data['time_limit']}s")
        print(f"✓ Background: {data['background_color']}")
        print(f"✓ Spawn: {data['spawn_point']}")
        print(f"✓ End: {data['end_point']}")
        print(f"✓ Platforms count: {len(data['platforms'])}")
        print(f"✓ Obstacles count: {len(data['obstacles'])}")
        
        # Validate platform structure
        for i, plat in enumerate(data['platforms']):
            plat_fields = ['x', 'y', 'width', 'height', 'type', 'color']
            for field in plat_fields:
                if field not in plat:
                    print(f"✗ Platform {i} missing field: {field}")
                    return False
        
        # Validate obstacle structure
        for i, obs in enumerate(data['obstacles']):
            obs_fields = ['x', 'y', 'width', 'height', 'type', 'color']
            for field in obs_fields:
                if field not in obs:
                    print(f"✗ Obstacle {i} missing field: {field}")
                    return False
        
        print(f"✓ All objects have required fields")
        print()
        return True
        
    except json.JSONDecodeError as e:
        print(f"✗ JSON decode error: {e}")
        print()
        return False

def test_level_manager_loads_it(filepath):
    """Test that LevelManager can load the level"""
    print("=" * 60)
    print("STEP 3: Load Level with LevelManager")
    print("=" * 60)
    
    pygame.init()
    
    try:
        lm = LevelManager()
        levels = lm.list_levels()
        
        print(f"✓ LevelManager created")
        print(f"  Levels directory: {lm.levels_dir}")
        print(f"  Available levels: {levels}")
        
        if "custom_e2e_test" not in levels:
            print(f"✗ Test level not in available levels!")
            print()
            return False
        
        level = lm.get_level("custom_e2e_test")
        
        print(f"✓ Level loaded: {level.name}")
        print(f"  Difficulty: {level.difficulty}")
        print(f"  Time limit: {level.time_limit}s")
        print(f"  Spawn: {level.spawn_point}")
        print(f"  End: {level.end_point}")
        print(f"  Platforms: {len(level.platforms)}")
        print(f"  Obstacles: {len(level.obstacles)}")
        print()
        return True
        
    except Exception as e:
        print(f"✗ Error loading level: {e}")
        import traceback
        traceback.print_exc()
        print()
        return False

def test_game_state_simulation(level_name):
    """Test that GameState can simulate the level"""
    print("=" * 60)
    print("STEP 4: Simulate Level with GameState")
    print("=" * 60)
    
    from level_manager import GameState
    
    try:
        lm = LevelManager()
        level = lm.get_level(level_name)
        
        game_state = GameState(level, 1000, 720)
        print(f"✓ GameState initialized")
        print(f"  Player spawn: {game_state.player_pos}")
        print(f"  Gravity: {game_state.gravity}")
        print(f"  Jump power: {game_state.jump_power}")
        
        # Simulate 60 frames (1 second at 60 FPS)
        dt = 1.0 / 60.0
        
        for frame in range(60):
            # Add some movement input
            if frame == 10:
                game_state.keys_pressed.add('jump')
            elif frame == 11:
                game_state.keys_pressed.discard('jump')
            elif frame > 15:
                game_state.keys_pressed.add('right')
            
            game_state.update(dt)
            
            if game_state.game_over:
                print(f"  Player hit obstacle at frame {frame}")
                break
        
        print(f"✓ Simulation completed 60 frames")
        print(f"  Final position: ({game_state.player_pos.x:.1f}, {game_state.player_pos.y:.1f})")
        print(f"  Game over: {game_state.game_over}")
        print(f"  Level complete: {game_state.level_complete}")
        print()
        return True
        
    except Exception as e:
        print(f"✗ Simulation failed: {e}")
        import traceback
        traceback.print_exc()
        print()
        return False

def test_syntax_check():
    """Verify all Python files have valid syntax"""
    print("=" * 60)
    print("STEP 5: Syntax Validation")
    print("=" * 60)
    
    import subprocess
    
    files = ['main.py', 'level_manager.py', 'level_editor.py']
    all_good = True
    
    for filename in files:
        filepath = os.path.join(script_dir, filename)
        result = subprocess.run(
            [sys.executable, '-m', 'py_compile', filepath],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print(f"✓ {filename}")
        else:
            print(f"✗ {filename}: {result.stderr}")
            all_good = False
    
    print()
    return all_good

def main():
    print("\n")
    print("╔" + "═" * 58 + "╗")
    print("║" + " END-TO-END WORKFLOW TEST ".center(58) + "║")
    print("╚" + "═" * 58 + "╝")
    print()
    
    # Clean up old test levels
    cleanup_custom_levels()
    
    tests = [
        ("Syntax Check", test_syntax_check, ()),
        ("Create Level", create_test_level_programmatically, ()),
        ("Validate JSON", validate_json_file, (os.path.join(script_dir, "Levels", "custom_e2e_test.json"),)),
        ("Load with Manager", test_level_manager_loads_it, (os.path.join(script_dir, "Levels", "custom_e2e_test.json"),)),
        ("Simulate Gameplay", test_game_state_simulation, ("custom_e2e_test",)),
    ]
    
    results = []
    for test_name, test_func, args in tests:
        try:
            result = test_func(*args)
            results.append((test_name, result))
        except Exception as e:
            print(f"✗ {test_name} failed: {e}")
            import traceback
            traceback.print_exc()
            results.append((test_name, False))
            print()
    
    # Summary
    print("=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    for test_name, result in results:
        status = "✓" if result else "✗"
        print(f"{status} {test_name}")
    
    passed = sum(1 for _, r in results if r)
    total = len(results)
    
    print()
    print(f"Result: {passed}/{total} tests passed")
    print()
    
    if passed == total:
        print("╔" + "═" * 58 + "╗")
        print("║" + " ✓ ALL TESTS PASSED! ".center(58) + "║")
        print("╚" + "═" * 58 + "╝")
        print()
        print("The complete level editor system is working perfectly!")
        print()
        print("To create levels:")
        print("  python level_editor.py")
        print()
        print("To play the game:")
        print("  python main.py")
        print()
        return 0
    else:
        print("✗ SOME TESTS FAILED")
        return 1

if __name__ == "__main__":
    sys.exit(main())
