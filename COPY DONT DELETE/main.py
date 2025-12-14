"""
Geometry Dash Clone with Level Loading System
"""
import pygame
import os
from level_manager import LevelManager, GameState


# pygame setup
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("what do i call this? GD from wish.com?")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 72)

# Initialize level manager
level_manager = LevelManager()
available_levels = level_manager.list_levels()

if not available_levels:
    print("ERROR: No levels found! Make sure Levels/ directory has .json files")
    pygame.quit()
    exit()

print(f"Available levels: {available_levels}")

# Game states
STATE_MENU = 0
STATE_PLAYING = 1
STATE_GAME_OVER = 2
STATE_LEVEL_COMPLETE = 3

# Initialize game
current_state = STATE_MENU
current_level_index = 0
game_state = None


def draw_menu():
    """Draw level selection menu"""
    screen.fill((20, 20, 30))
    
    title = large_font.render("what do i call this? GD from wish.com?", True, (255, 255, 255))
    screen.blit(title, (screen_width // 2 - title.get_width() // 2, 50))
    
    subtitle = font.render("Select a Level (1-9 or mouse click)", True, (200, 200, 200))
    screen.blit(subtitle, (screen_width // 2 - subtitle.get_width() // 2, 150))
    
    y_offset = 250
    for i, level_name in enumerate(available_levels):
        color = (100, 255, 100) if i == current_level_index else (150, 150, 150)
        text = font.render(f"{i + 1}. {level_name}", True, color)
        screen.blit(text, (200, y_offset + i * 50))
    
    instruction = font.render("Press ENTER to start or ESC to quit", True, (100, 200, 255))
    screen.blit(instruction, (screen_width // 2 - instruction.get_width() // 2, screen_height - 100))


def draw_game():
    """Draw the game"""
    screen.fill(game_state.level.background_color)
    
    # Draw platforms
    for platform in game_state.level.platforms:
        pygame.draw.rect(screen, platform.color, 
                        (platform.x, platform.y, platform.width, platform.height))
        # Draw platform outline
        pygame.draw.rect(screen, (255, 255, 255), 
                        (platform.x, platform.y, platform.width, platform.height), 2)
    
    # Draw obstacles
    for obstacle in game_state.level.obstacles:
        pygame.draw.rect(screen, obstacle.color, 
                        (obstacle.x, obstacle.y, obstacle.width, obstacle.height))
        # Draw obstacle outline
        pygame.draw.rect(screen, (255, 200, 100), 
                        (obstacle.x, obstacle.y, obstacle.width, obstacle.height), 2)
    
    # Draw end point (goal)
    end_x, end_y = game_state.level.end_point
    pygame.draw.circle(screen, (0, 255, 0), (int(end_x), int(end_y)), 30)
    pygame.draw.circle(screen, (255, 255, 0), (int(end_x), int(end_y)), 30, 3)
    
    # Draw player
    pygame.draw.circle(screen, (255, 50, 50), 
                      (int(game_state.player_pos.x), int(game_state.player_pos.y)), 
                      game_state.player_radius)
    pygame.draw.circle(screen, (255, 200, 100), 
                      (int(game_state.player_pos.x), int(game_state.player_pos.y)), 
                      game_state.player_radius, 3)
    
    # Draw UI
    level_text = font.render(f"Level: {game_state.level.name}", True, (255, 255, 255))
    screen.blit(level_text, (10, 10))
    
    if game_state.level.time_limit > 0:
        time_text = font.render(f"Time: {game_state.elapsed_time:.1f}s / {game_state.level.time_limit}s", 
                               True, (255, 255, 100))
    else:
        time_text = font.render(f"Time: {game_state.elapsed_time:.1f}s", 
                               True, (255, 255, 100))
    screen.blit(time_text, (10, 50))
    
    difficulty_text = font.render(f"Difficulty: {game_state.level.difficulty}/10", 
                                 True, (255, 100, 100))
    screen.blit(difficulty_text, (10, 90))


def draw_game_over():
    """Draw game over screen"""
    screen.fill((50, 10, 10))
    
    game_over_text = large_font.render("GAME OVER!", True, (255, 0, 0))
    screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, 200))
    
    time_text = font.render(f"Time survived: {game_state.elapsed_time:.1f}s", True, (255, 255, 255))
    screen.blit(time_text, (screen_width // 2 - time_text.get_width() // 2, 350))
    
    instruction = font.render("Press R to retry or M for menu", True, (100, 200, 255))
    screen.blit(instruction, (screen_width // 2 - instruction.get_width() // 2, 450))


def draw_level_complete():
    """Draw level complete screen"""
    screen.fill((10, 50, 10))
    
    complete_text = large_font.render("LEVEL COMPLETE!", True, (0, 255, 0))
    screen.blit(complete_text, (screen_width // 2 - complete_text.get_width() // 2, 200))
    
    time_text = font.render(f"Time: {game_state.elapsed_time:.1f}s", True, (255, 255, 255))
    screen.blit(time_text, (screen_width // 2 - time_text.get_width() // 2, 350))
    
    if current_level_index < len(available_levels) - 1:
        instruction = font.render("Press SPACE for next level or M for menu", True, (100, 200, 255))
    else:
        instruction = font.render("Press M for menu (All levels completed!)", True, (100, 200, 255))
    screen.blit(instruction, (screen_width // 2 - instruction.get_width() // 2, 450))


# Main game loop
running = True
while running:
    dt = clock.tick(60) / 1000
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if current_state == STATE_MENU:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    # Start level
                    level_name = available_levels[current_level_index]
                    level = level_manager.get_level(level_name)
                    game_state = GameState(level, screen_width, screen_height)
                    current_state = STATE_PLAYING
                    print(f"Starting level: {level_name}")
                
                elif event.key == pygame.K_ESCAPE:
                    running = False
                
                # Number keys to select level
                elif pygame.K_1 <= event.key <= pygame.K_9:
                    level_num = event.key - pygame.K_1
                    if level_num < len(available_levels):
                        current_level_index = level_num
            
            elif current_state == STATE_PLAYING:
                if event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_UP:
                    game_state.jump()
                
                elif event.key == pygame.K_m:
                    current_state = STATE_MENU
                
                elif event.key == pygame.K_ESCAPE:
                    current_state = STATE_MENU
                
                # Handle movement keys
                game_state.handle_key_down(event.key)
            
            elif current_state == STATE_GAME_OVER:
                if event.key == pygame.K_r:
                    # Retry current level
                    level = level_manager.get_level(available_levels[current_level_index])
                    game_state = GameState(level, screen_width, screen_height)
                    current_state = STATE_PLAYING
                
                elif event.key == pygame.K_m:
                    current_state = STATE_MENU
            
            elif current_state == STATE_LEVEL_COMPLETE:
                if event.key == pygame.K_SPACE:
                    if current_level_index < len(available_levels) - 1:
                        current_level_index += 1
                        level = level_manager.get_level(available_levels[current_level_index])
                        game_state = GameState(level, screen_width, screen_height)
                        current_state = STATE_PLAYING
                    else:
                        current_state = STATE_MENU
                
                elif event.key == pygame.K_m:
                    current_state = STATE_MENU
        
        elif event.type == pygame.KEYUP:
            if current_state == STATE_PLAYING:
                game_state.handle_key_up(event.key)
    
    # Update game state
    if current_state == STATE_PLAYING:
        game_state.update(dt)
        
        if game_state.game_over:
            current_state = STATE_GAME_OVER
        elif game_state.level_complete:
            current_state = STATE_LEVEL_COMPLETE
    
    # Draw
    if current_state == STATE_MENU:
        draw_menu()
    elif current_state == STATE_PLAYING:
        draw_game()
    elif current_state == STATE_GAME_OVER:
        draw_game_over()
    elif current_state == STATE_LEVEL_COMPLETE:
        draw_level_complete()
    
    pygame.display.flip()

pygame.quit()
print("Thanks for playing!")