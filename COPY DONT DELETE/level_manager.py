import json
import pygame
from dataclasses import dataclass
from typing import List, Dict
import os


@dataclass
class Obstacle:
    """Represents an obstacle (spike, box, etc.)"""
    x: float
    y: float
    width: float
    height: float
    obstacle_type: str  # "spike", "box", "moving_box", etc.
    color: tuple = (255, 0, 0)  # RGB
    speed: float = 0  # For moving obstacles
    direction: int = 1  # 1 for right, -1 for left


@dataclass
class Platform:
    """Represents a platform"""
    x: float
    y: float
    width: float
    height: float
    platform_type: str  # "ground", "spring", "moving", etc.
    color: tuple = (100, 100, 100)  # RGB
    speed: float = 0  # For moving platforms
    direction: int = 1


@dataclass
class LevelData:
    """Complete level data"""
    name: str
    difficulty: int  # 1-10
    time_limit: float  # seconds, 0 for no limit
    obstacles: List[Obstacle]
    platforms: List[Platform]
    background_color: tuple
    spawn_point: tuple  # (x, y)
    end_point: tuple  # (x, y) - level goal


class LevelManager:
    """Manages level loading and game objects"""
    
    def __init__(self, levels_dir: str = "Levels"):
        self.levels_dir = levels_dir
        self.current_level = None
        self.levels = {}
        self._ensure_levels_dir()
        self.load_all_levels()
    
    def _ensure_levels_dir(self):
        """Create levels directory if it doesn't exist"""
        if not os.path.exists(self.levels_dir):
            os.makedirs(self.levels_dir)
    
    def load_all_levels(self):
        """Load all available levels"""
        if not os.path.exists(self.levels_dir):
            return
        
        for filename in sorted(os.listdir(self.levels_dir)):
            if filename.endswith('.json'):
                level_name = filename.replace('.json', '')
                try:
                    self.load_level_from_file(level_name)
                except Exception as e:
                    print(f"Error loading level {level_name}: {e}")
    
    def load_level_from_file(self, level_name: str) -> LevelData:
        """Load a level from JSON file"""
        filepath = os.path.join(self.levels_dir, f"{level_name}.json")
        
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        # Parse obstacles
        obstacles = []
        for obs_data in data.get('obstacles', []):
            obstacles.append(Obstacle(
                x=obs_data['x'],
                y=obs_data['y'],
                width=obs_data['width'],
                height=obs_data['height'],
                obstacle_type=obs_data.get('type', 'box'),
                color=tuple(obs_data.get('color', [255, 0, 0])),
                speed=obs_data.get('speed', 0),
                direction=obs_data.get('direction', 1)
            ))
        
        # Parse platforms
        platforms = []
        for plat_data in data.get('platforms', []):
            platforms.append(Platform(
                x=plat_data['x'],
                y=plat_data['y'],
                width=plat_data['width'],
                height=plat_data['height'],
                platform_type=plat_data.get('type', 'ground'),
                color=tuple(plat_data.get('color', [100, 100, 100])),
                speed=plat_data.get('speed', 0),
                direction=plat_data.get('direction', 1)
            ))
        
        level = LevelData(
            name=data['name'],
            difficulty=data.get('difficulty', 1),
            time_limit=data.get('time_limit', 0),
            obstacles=obstacles,
            platforms=platforms,
            background_color=tuple(data.get('background_color', [0, 0, 0])),
            spawn_point=tuple(data.get('spawn_point', [100, 100])),
            end_point=tuple(data.get('end_point', [1200, 300]))
        )
        
        self.levels[level_name] = level
        return level
    
    def get_level(self, level_name: str) -> LevelData:
        """Get a loaded level"""
        if level_name not in self.levels:
            self.load_level_from_file(level_name)
        return self.levels[level_name]
    
    def list_levels(self) -> List[str]:
        """List all available levels"""
        return sorted(self.levels.keys())


class GameState:
    """Manages game state and collision detection"""
    
    def __init__(self, level: LevelData, screen_width: int, screen_height: int):
        self.level = level
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Player state
        self.player_pos = pygame.Vector2(*level.spawn_point)
        self.player_velocity_x = 0
        self.player_velocity_y = 0
        self.is_jumping = False
        self.player_radius = 20
        
        # Game state
        self.game_over = False
        self.level_complete = False
        self.start_time = pygame.time.get_ticks()
        self.elapsed_time = 0
        
        # Physics
        self.gravity = 700
        self.jump_power = 400
        self.move_speed = 300  # Horizontal movement speed
        self.keys_pressed = set()  # Track which keys are currently pressed
    
    def update(self, dt: float):
        """Update game state"""
        if self.game_over or self.level_complete:
            return
        
        self.elapsed_time = (pygame.time.get_ticks() - self.start_time) / 1000
        
        # Check time limit
        if self.level.time_limit > 0 and self.elapsed_time > self.level.time_limit:
            self.game_over = True
            return
        
        # Handle horizontal movement based on keys pressed
        self.player_velocity_x = 0
        if 'left' in self.keys_pressed:
            self.player_velocity_x = -self.move_speed
        if 'right' in self.keys_pressed:
            self.player_velocity_x = self.move_speed
        
        # Apply gravity
        self.player_velocity_y += self.gravity * dt
        
        # Update player position
        self.player_pos.x += self.player_velocity_x * dt
        self.player_pos.y += self.player_velocity_y * dt
        
        # Keep player in bounds horizontally
        self.player_pos.x = max(self.player_radius, min(self.player_pos.x, self.screen_width - self.player_radius))
        
        # Update moving platforms
        for platform in self.level.platforms:
            if platform.platform_type == "moving":
                platform.x += platform.speed * platform.direction * dt
                # Bounce at screen edges
                if platform.x < 0 or platform.x + platform.width > self.screen_width:
                    platform.direction *= -1
        
        # Update moving obstacles
        for obstacle in self.level.obstacles:
            if obstacle.obstacle_type == "moving_box":
                obstacle.x += obstacle.speed * obstacle.direction * dt
                if obstacle.x < 0 or obstacle.x + obstacle.width > self.screen_width:
                    obstacle.direction *= -1
        
        # Collision detection with platforms
        self._check_platform_collisions()
        
        # Collision detection with obstacles
        self._check_obstacle_collisions()
        
        # Check if level complete
        self._check_level_complete()
        
        # Out of bounds
        if self.player_pos.y > self.screen_height + 100:
            self.game_over = True
    
    def jump(self):
        """Perform a jump"""
        if not self.is_jumping:
            self.player_velocity_y = -self.jump_power
            self.is_jumping = True
    
    def handle_key_down(self, key):
        """Handle key press"""
        if key == pygame.K_w or key == pygame.K_UP:
            self.keys_pressed.add('jump')
        elif key == pygame.K_a or key == pygame.K_LEFT:
            self.keys_pressed.add('left')
        elif key == pygame.K_d or key == pygame.K_RIGHT:
            self.keys_pressed.add('right')
    
    def handle_key_up(self, key):
        """Handle key release"""
        if key == pygame.K_a or key == pygame.K_LEFT:
            self.keys_pressed.discard('left')
        elif key == pygame.K_d or key == pygame.K_RIGHT:
            self.keys_pressed.discard('right')
    
    def _check_platform_collisions(self):
        """Check collision with platforms"""
        player_rect = pygame.Rect(
            self.player_pos.x - self.player_radius,
            self.player_pos.y - self.player_radius,
            self.player_radius * 2,
            self.player_radius * 2
        )
        
        for platform in self.level.platforms:
            platform_rect = pygame.Rect(platform.x, platform.y, platform.width, platform.height)
            
            if player_rect.colliderect(platform_rect):
                # Landing on platform
                if self.player_velocity_y > 0 and player_rect.centery < platform_rect.centery:
                    self.player_pos.y = platform.y - self.player_radius
                    self.player_velocity_y = 0
                    self.is_jumping = False
                    
                    # Spring platforms bounce higher
                    if platform.platform_type == "spring":
                        self.player_velocity_y = -self.jump_power * 1.5
                        self.is_jumping = True
    
    def _check_obstacle_collisions(self):
        """Check collision with obstacles"""
        player_rect = pygame.Rect(
            self.player_pos.x - self.player_radius,
            self.player_pos.y - self.player_radius,
            self.player_radius * 2,
            self.player_radius * 2
        )
        
        for obstacle in self.level.obstacles:
            obstacle_rect = pygame.Rect(obstacle.x, obstacle.y, obstacle.width, obstacle.height)
            
            if player_rect.colliderect(obstacle_rect):
                self.game_over = True
    
    def _check_level_complete(self):
        """Check if player reached the end point"""
        end_x, end_y = self.level.end_point
        distance = ((self.player_pos.x - end_x) ** 2 + (self.player_pos.y - end_y) ** 2) ** 0.5
        
        if distance < self.player_radius + 30:
            self.level_complete = True
