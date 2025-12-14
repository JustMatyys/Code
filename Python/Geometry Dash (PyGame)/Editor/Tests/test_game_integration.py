#!/usr/bin/env python3
"""
Test that the game can load and play custom levels
"""
import subprocess
import time
import os
import sys

# Add root directory to path to find level_manager
script_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, script_dir)

from level_manager import LevelManager

def test_game_can_load_custom():
    """Test that the game can load the custom level"""
    print("=" * 60)
    print("TEST: Game Can Load Custom Levels")
    print("=" * 60)
    
    lm = LevelManager()
    levels = lm.list_levels()
    
    print(f"Available levels in game: {levels}")
    
    if "test_editor_level" in levels:
        print("✓ Test level can be loaded by game")
        
        # Load and verify
        level = lm.get_level("test_editor_level")
        print(f"  Name: {level.name}")
        print(f"  Platforms: {len(level.platforms)}")
        print(f"  Obstacles: {len(level.obstacles)}")
        print()
        return True
    else:
        print("✗ Test level NOT found in game")
        print()
        return False

def test_syntax():
    """Check syntax of all Python files"""
    print("=" * 60)
    print("TEST: Python Syntax Check")
    print("=" * 60)
    
    files = [
        "main.py",
        "level_manager.py",
        "level_editor.py"
    ]
    
    all_good = True
    for filename in files:
        filepath = os.path.join(script_dir, filename)
        result = subprocess.run(
            [sys.executable, "-m", "py_compile", filepath],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print(f"✓ {filename}: OK")
        else:
            print(f"✗ {filename}: SYNTAX ERROR")
            print(f"  {result.stderr}")
            all_good = False
    
    print()
    return all_good

def main():
    print("\n")
    print("╔" + "═" * 58 + "╗")
    print("║" + " GAME INTEGRATION TEST ".center(58) + "║")
    print("╚" + "═" * 58 + "╝")
    print()
    
    test1 = test_syntax()
    test2 = test_game_can_load_custom()
    
    print("=" * 60)
    print("FINAL RESULT")
    print("=" * 60)
    
    if test1 and test2:
        print("✓ ALL INTEGRATION TESTS PASSED!")
        print()
        print("The level editor is ready to use!")
        print()
        print("To use the editor:")
        print("  python level_editor.py")
        print()
        print("Features:")
        print("  - Add platforms and obstacles by clicking buttons")
        print("  - Drag objects to move them")
        print("  - Set spawn and end points")
        print("  - Save levels to Levels/customXYZ.json")
        print("  - Load and edit existing levels")
        print()
        return 0
    else:
        print("✗ SOME TESTS FAILED")
        return 1

if __name__ == "__main__":
    sys.exit(main())
