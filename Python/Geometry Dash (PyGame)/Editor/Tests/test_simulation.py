#!/usr/bin/env python3
"""
Quick test that verifies a level can be loaded and simulated
"""
import sys
import os

# Add root directory to path to find level_manager
script_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, script_dir)

import pygame
from level_manager import LevelManager, GameState

def test_level_simulation():
    """Simulate playing a level to ensure all mechanics work"""
    print("=" * 60)
    print("TEST: Level Simulation (30 frames)")
    print("=" * 60)
    
    pygame.init()
    
    lm = LevelManager()
    level = lm.get_level("test_editor_level")
    
    print(f"✓ Loading level: {level.name}")
    print(f"  Spawn: {level.spawn_point}")
    print(f"  End: {level.end_point}")
    print(f"  Platforms: {len(level.platforms)}")
    print(f"  Obstacles: {len(level.obstacles)}")
    print()
    
    # Create game state
    game_state = GameState(level, 1000, 720)
    print(f"✓ GameState created")
    print(f"  Initial player pos: {game_state.player_pos}")
    print()
    
    # Simulate 30 frames
    dt = 1.0 / 60.0  # 60 FPS
    
    for frame in range(30):
        game_state.update(dt)
        
        # Simulate some input on frame 5
        if frame == 5:
            game_state.keys_pressed.add('jump')
            print(f"Frame {frame}: Player jumped")
        elif frame == 6:
            game_state.keys_pressed.discard('jump')
        
        # Move right
        if frame > 5:
            game_state.keys_pressed.add('right')
        
        if frame % 10 == 0:
            print(f"Frame {frame}: Player at ({game_state.player_pos.x:.1f}, {game_state.player_pos.y:.1f}), Velocity: ({game_state.player_velocity_x:.1f}, {game_state.player_velocity_y:.1f})")
    
    print()
    print(f"✓ Simulation completed successfully")
    print(f"  Final position: ({game_state.player_pos.x:.1f}, {game_state.player_pos.y:.1f})")
    print(f"  Game over: {game_state.game_over}")
    print()
    
    pygame.quit()
    return True

def main():
    print("\n")
    print("╔" + "═" * 58 + "╗")
    print("║" + " LEVEL SIMULATION TEST ".center(58) + "║")
    print("╚" + "═" * 58 + "╝")
    print()
    
    try:
        result = test_level_simulation()
        if result:
            print("=" * 60)
            print("✓ SIMULATION TEST PASSED!")
            print("=" * 60)
            return 0
    except Exception as e:
        print(f"✗ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
