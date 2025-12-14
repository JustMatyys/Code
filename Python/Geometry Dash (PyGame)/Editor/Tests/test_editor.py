#!/usr/bin/env python3
"""
Test script to verify the level editor and game integration
"""
import os
import json
import sys

# Add root directory to path to find level_manager
script_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, script_dir)

from level_manager import LevelManager, Platform, Obstacle

def test_level_manager():
    """Test that LevelManager finds levels correctly"""
    print("=" * 60)
    print("TEST 1: Level Manager Path Resolution")
    print("=" * 60)
    
    lm = LevelManager()
    print(f"✓ LevelManager initialized")
    print(f"  Levels directory: {lm.levels_dir}")
    print(f"  Directory exists: {os.path.exists(lm.levels_dir)}")
    print(f"  Available levels: {lm.list_levels()}")
    print()
    return True

def test_create_test_level():
    """Create a test level manually"""
    print("=" * 60)
    print("TEST 2: Create Test Level")
    print("=" * 60)
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    levels_dir = os.path.join(script_dir, "Levels")
    os.makedirs(levels_dir, exist_ok=True)
    
    test_level = {
        "name": "Test Level",
        "difficulty": 3,
        "time_limit": 30.0,
        "background_color": [30, 30, 50],
        "spawn_point": [100, 600],
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
            },
            {
                "x": 200,
                "y": 550,
                "width": 150,
                "height": 20,
                "type": "ground",
                "color": [100, 150, 100],
                "speed": 0,
                "direction": 1
            },
            {
                "x": 500,
                "y": 450,
                "width": 150,
                "height": 20,
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
    
    test_file = os.path.join(levels_dir, "test_editor_level.json")
    with open(test_file, 'w') as f:
        json.dump(test_level, f, indent=2)
    
    print(f"✓ Test level created: {test_file}")
    print()
    return True

def test_load_test_level():
    """Load and verify the test level"""
    print("=" * 60)
    print("TEST 3: Load Test Level")
    print("=" * 60)
    
    lm = LevelManager()
    levels = lm.list_levels()
    
    if "test_editor_level" not in levels:
        print("✗ Test level not found!")
        return False
    
    level = lm.get_level("test_editor_level")
    print(f"✓ Level loaded: {level.name}")
    print(f"  Difficulty: {level.difficulty}")
    print(f"  Time limit: {level.time_limit}s")
    print(f"  Platforms: {len(level.platforms)}")
    print(f"  Obstacles: {len(level.obstacles)}")
    print(f"  Spawn: {level.spawn_point}")
    print(f"  End: {level.end_point}")
    print()
    return True

def test_editor_import():
    """Test that the editor imports correctly"""
    print("=" * 60)
    print("TEST 4: Level Editor Import")
    print("=" * 60)
    
    try:
        # Add Editor directory to path to find level_editor
        editor_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        sys.path.insert(0, editor_dir)
        from level_editor import LevelEditor
        print("✓ Level editor imported successfully")
        print()
        return True
    except Exception as e:
        print(f"✗ Error importing level editor: {e}")
        import traceback
        traceback.print_exc()
        print()
        return False

def test_json_serialization():
    """Test JSON serialization of level objects"""
    print("=" * 60)
    print("TEST 5: JSON Serialization")
    print("=" * 60)
    
    platform = Platform(100, 200, 150, 20, "ground", (100, 150, 100), 0, 1)
    obstacle = Obstacle(300, 400, 40, 50, "box", (255, 100, 100), 0, 1)
    
    platform_dict = {
        "x": platform.x,
        "y": platform.y,
        "width": platform.width,
        "height": platform.height,
        "type": platform.platform_type,
        "color": list(platform.color),
        "speed": platform.speed,
        "direction": platform.direction
    }
    
    obstacle_dict = {
        "x": obstacle.x,
        "y": obstacle.y,
        "width": obstacle.width,
        "height": obstacle.height,
        "type": obstacle.obstacle_type,
        "color": list(obstacle.color),
        "speed": obstacle.speed,
        "direction": obstacle.direction
    }
    
    # Test serialization
    json_str = json.dumps({"platform": platform_dict, "obstacle": obstacle_dict})
    restored = json.loads(json_str)
    
    print(f"✓ Platform serialization: {restored['platform']}")
    print(f"✓ Obstacle serialization: {restored['obstacle']}")
    print()
    return True

def main():
    print("\n")
    print("╔" + "═" * 58 + "╗")
    print("║" + " GEOMETRY DASH LEVEL EDITOR - TEST SUITE ".center(58) + "║")
    print("╚" + "═" * 58 + "╝")
    print()
    
    tests = [
        ("Level Manager Path Resolution", test_level_manager),
        ("Create Test Level", test_create_test_level),
        ("Load Test Level", test_load_test_level),
        ("Level Editor Import", test_editor_import),
        ("JSON Serialization", test_json_serialization),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"✗ Exception in {test_name}: {e}")
            import traceback
            traceback.print_exc()
            results.append((test_name, False))
            print()
    
    print("=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    passed = sum(1 for _, result in results if result)
    total = len(results)
    for test_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status}: {test_name}")
    
    print()
    print(f"Total: {passed}/{total} tests passed")
    print()
    
    if passed == total:
        print("✓ ALL TESTS PASSED!")
        return 0
    else:
        print("✗ SOME TESTS FAILED")
        return 1

if __name__ == "__main__":
    sys.exit(main())
