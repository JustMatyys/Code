"""
Level Editor for Geometry Dash
Allows creation and editing of levels with a GUI
"""
import pygame
import json
import os
import sys

# Add parent directory to path to find level_manager
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from level_manager import Platform, Obstacle, LevelData
from enum import Enum


class EditorMode(Enum):
    SELECT = 0
    ADD_PLATFORM = 1
    ADD_OBSTACLE = 2
    EDIT_PROPERTIES = 3
    SET_SPAWN = 4
    SET_END = 5


class Button:
    """Simple button class"""
    def __init__(self, x, y, width, height, text, color, text_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.text_color = text_color
        self.hovered = False
    
    def draw(self, screen, font):
        color = tuple(min(c + 30, 255) for c in self.color) if self.hovered else self.color
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
        text_surf = font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)
    
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
    
    def update_hover(self, pos):
        self.hovered = self.rect.collidepoint(pos)


class LevelEditor:
    def __init__(self):
        pygame.init()
        self.screen_width = 1400
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Geometry Dash Level Editor")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 24)
        self.small_font = pygame.font.Font(None, 18)
        self.large_font = pygame.font.Font(None, 36)
        
        # Canvas area (left side)
        self.canvas_rect = pygame.Rect(0, 0, 1000, self.screen_height)
        self.canvas_color = (30, 30, 40)
        
        # UI panel (right side)
        self.panel_rect = pygame.Rect(1000, 0, 400, self.screen_height)
        self.panel_color = (50, 50, 60)
        
        # Level data
        self.platforms = []
        self.obstacles = []
        self.spawn_point = (100, 100)
        self.end_point = (900, 300)
        self.level_name = "custom"
        self.difficulty = 5
        self.time_limit = 0.0
        self.background_color = (20, 20, 30)
        
        # Editor state
        self.mode = EditorMode.SELECT
        self.selected_object = None
        self.dragging = False
        self.drag_offset = (0, 0)
        
        # UI Elements
        self.setup_buttons()
        
        # Text input
        self.input_active = None
        self.input_value = ""
        
        # Drawing parameters for new objects
        self.new_platform_type = "ground"
        self.new_obstacle_type = "box"
        self.temp_start = None
    
    def setup_buttons(self):
        """Setup UI buttons"""
        self.buttons = {
            'add_platform': Button(1020, 20, 160, 40, "Add Platform", (100, 150, 100), (0, 0, 0)),
            'add_obstacle': Button(1020, 70, 160, 40, "Add Obstacle", (150, 100, 100), (0, 0, 0)),
            'save': Button(1020, 120, 160, 40, "Save Level", (100, 100, 200), (0, 0, 0)),
            'load': Button(1020, 170, 160, 40, "Load Level", (100, 100, 200), (0, 0, 0)),
            'clear': Button(1020, 220, 160, 40, "Clear All", (200, 100, 100), (0, 0, 0)),
            'properties': Button(1020, 270, 160, 40, "Properties", (150, 150, 100), (0, 0, 0)),
            'set_spawn': Button(1020, 320, 160, 40, "Set Spawn", (100, 150, 150), (0, 0, 0)),
            'set_end': Button(1020, 370, 160, 40, "Set End", (150, 100, 150), (0, 0, 0)),
            'delete_selected': Button(1020, 420, 160, 40, "Delete Sel.", (200, 100, 100), (0, 0, 0)),
            'exit': Button(1020, 720 - 50, 160, 40, "Exit", (100, 100, 100), (255, 255, 255)),
        }
    
    def handle_events(self):
        """Handle events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            mouse_pos = pygame.mouse.get_pos()
            
            # Update button hover
            for button in self.buttons.values():
                button.update_hover(mouse_pos)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    if self.panel_rect.collidepoint(mouse_pos):
                        self.handle_panel_click(mouse_pos)
                    elif self.canvas_rect.collidepoint(mouse_pos):
                        self.handle_canvas_click(mouse_pos)
            
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.dragging = False
            
            elif event.type == pygame.MOUSEMOTION:
                if self.dragging and self.selected_object and self.canvas_rect.collidepoint(mouse_pos):
                    self.drag_object(mouse_pos)
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DELETE and self.selected_object:
                    self.delete_selected()
                elif event.key == pygame.K_ESCAPE:
                    self.mode = EditorMode.SELECT
                    self.selected_object = None
                elif event.key == pygame.K_RETURN and self.input_active:
                    self.handle_input_submit()
        
        return True
    
    def handle_panel_click(self, pos):
        """Handle clicks on panel"""
        if self.buttons['add_platform'].is_clicked(pos):
            self.mode = EditorMode.ADD_PLATFORM
            self.selected_object = None
        
        elif self.buttons['add_obstacle'].is_clicked(pos):
            self.mode = EditorMode.ADD_OBSTACLE
            self.selected_object = None
        
        elif self.buttons['save'].is_clicked(pos):
            self.save_level()
        
        elif self.buttons['load'].is_clicked(pos):
            self.load_level()
        
        elif self.buttons['clear'].is_clicked(pos):
            self.clear_all()
        
        elif self.buttons['properties'].is_clicked(pos):
            self.show_properties_dialog()
        
        elif self.buttons['set_spawn'].is_clicked(pos):
            self.mode = EditorMode.SET_SPAWN
            self.selected_object = None
        
        elif self.buttons['set_end'].is_clicked(pos):
            self.mode = EditorMode.SET_END
            self.selected_object = None
        
        elif self.buttons['delete_selected'].is_clicked(pos):
            self.delete_selected()
        
        elif self.buttons['exit'].is_clicked(pos):
            pygame.quit()
            exit()
    
    def handle_canvas_click(self, pos):
        """Handle clicks on canvas"""
        canvas_pos = (pos[0], pos[1])
        
        if self.mode == EditorMode.ADD_PLATFORM:
            if not self.temp_start:
                self.temp_start = canvas_pos
            else:
                self.add_platform(self.temp_start, canvas_pos)
                self.temp_start = None
                self.mode = EditorMode.SELECT
        
        elif self.mode == EditorMode.ADD_OBSTACLE:
            if not self.temp_start:
                self.temp_start = canvas_pos
            else:
                self.add_obstacle(self.temp_start, canvas_pos)
                self.temp_start = None
                self.mode = EditorMode.SELECT
        
        elif self.mode == EditorMode.SET_SPAWN:
            self.spawn_point = canvas_pos
            self.mode = EditorMode.SELECT
        
        elif self.mode == EditorMode.SET_END:
            self.end_point = canvas_pos
            self.mode = EditorMode.SELECT
        
        else:
            # Select object
            self.selected_object = None
            
            # Check platforms
            for platform in self.platforms:
                rect = pygame.Rect(platform.x, platform.y, platform.width, platform.height)
                if rect.collidepoint(canvas_pos):
                    self.selected_object = ('platform', self.platforms.index(platform))
                    self.dragging = True
                    self.drag_offset = (canvas_pos[0] - platform.x, canvas_pos[1] - platform.y)
                    break
            
            # Check obstacles
            if not self.selected_object:
                for obstacle in self.obstacles:
                    rect = pygame.Rect(obstacle.x, obstacle.y, obstacle.width, obstacle.height)
                    if rect.collidepoint(canvas_pos):
                        self.selected_object = ('obstacle', self.obstacles.index(obstacle))
                        self.dragging = True
                        self.drag_offset = (canvas_pos[0] - obstacle.x, canvas_pos[1] - obstacle.y)
                        break
    
    def drag_object(self, pos):
        """Drag selected object"""
        canvas_pos = (pos[0], pos[1])
        new_x = max(0, min(canvas_pos[0] - self.drag_offset[0], self.canvas_rect.width - 1))
        new_y = max(0, min(canvas_pos[1] - self.drag_offset[1], self.canvas_rect.height - 1))
        
        if self.selected_object:
            obj_type, obj_idx = self.selected_object
            if obj_type == 'platform':
                self.platforms[obj_idx].x = new_x
                self.platforms[obj_idx].y = new_y
            elif obj_type == 'obstacle':
                self.obstacles[obj_idx].x = new_x
                self.obstacles[obj_idx].y = new_y
    
    def add_platform(self, start, end):
        """Add a platform"""
        x, y = min(start[0], end[0]), min(start[1], end[1])
        width = abs(end[0] - start[0])
        height = abs(end[1] - start[1])
        
        if width < 20:
            width = 60
        if height < 10:
            height = 20
        
        platform = Platform(x, y, width, height, self.new_platform_type, (100, 150, 100), 0, 1)
        self.platforms.append(platform)
    
    def add_obstacle(self, start, end):
        """Add an obstacle"""
        x, y = min(start[0], end[0]), min(start[1], end[1])
        width = abs(end[0] - start[0])
        height = abs(end[1] - start[1])
        
        if width < 20:
            width = 40
        if height < 10:
            height = 30
        
        obstacle = Obstacle(x, y, width, height, self.new_obstacle_type, (255, 100, 100), 0, 1)
        self.obstacles.append(obstacle)
    
    def delete_selected(self):
        """Delete selected object"""
        if self.selected_object:
            obj_type, obj_idx = self.selected_object
            if obj_type == 'platform' and 0 <= obj_idx < len(self.platforms):
                self.platforms.pop(obj_idx)
            elif obj_type == 'obstacle' and 0 <= obj_idx < len(self.obstacles):
                self.obstacles.pop(obj_idx)
            self.selected_object = None
    
    def clear_all(self):
        """Clear all objects"""
        if pygame.time.get_ticks() % 2 == 0:  # Simple confirmation
            self.platforms = []
            self.obstacles = []
            self.selected_object = None
    
    def show_properties_dialog(self):
        """Show properties dialog"""
        print("=== LEVEL PROPERTIES ===")
        print(f"Name: {self.level_name}")
        print(f"Difficulty: {self.difficulty}")
        print(f"Time Limit: {self.time_limit} (0 = no limit)")
        print(f"Background Color: {self.background_color}")
        print("Edit in console or modify level_editor.py")
    
    def save_level(self):
        """Save level to JSON"""
        # Find next custom level number - save to parent Levels/ directory
        script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        levels_dir = os.path.join(script_dir, "Levels")
        os.makedirs(levels_dir, exist_ok=True)
        
        custom_num = 1
        while os.path.exists(os.path.join(levels_dir, f"custom{custom_num}.json")):
            custom_num += 1
        
        level_data = {
            "name": f"Custom Level {custom_num}",
            "difficulty": self.difficulty,
            "time_limit": self.time_limit,
            "background_color": list(self.background_color),
            "spawn_point": list(self.spawn_point),
            "end_point": list(self.end_point),
            "platforms": [
                {
                    "x": p.x,
                    "y": p.y,
                    "width": p.width,
                    "height": p.height,
                    "type": p.platform_type,
                    "color": list(p.color),
                    "speed": p.speed,
                    "direction": p.direction
                }
                for p in self.platforms
            ],
            "obstacles": [
                {
                    "x": o.x,
                    "y": o.y,
                    "width": o.width,
                    "height": o.height,
                    "type": o.obstacle_type,
                    "color": list(o.color),
                    "speed": o.speed,
                    "direction": o.direction
                }
                for o in self.obstacles
            ]
        }
        
        filename = os.path.join(levels_dir, f"custom{custom_num}.json")
        with open(filename, 'w') as f:
            json.dump(level_data, f, indent=2)
        
        print(f"✓ Level saved to {filename}")
    
    def load_level(self):
        """Load level from JSON"""
        # Load from parent Levels/ directory
        script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        levels_dir = os.path.join(script_dir, "Levels")
        os.makedirs(levels_dir, exist_ok=True)
        
        files = [f for f in os.listdir(levels_dir) if f.endswith('.json')]
        if not files:
            print("No levels to load")
            return
        
        print("Available levels:")
        for i, f in enumerate(files):
            print(f"{i}: {f}")
        
        try:
            choice = int(input("Enter level number: "))
            if 0 <= choice < len(files):
                self.load_from_file(os.path.join(levels_dir, files[choice]))
        except ValueError:
            print("Invalid input")
    
    def load_from_file(self, filepath):
        """Load level from file"""
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            self.level_name = data.get('name', 'custom')
            self.difficulty = data.get('difficulty', 5)
            self.time_limit = data.get('time_limit', 0)
            self.background_color = tuple(data.get('background_color', [20, 20, 30]))
            self.spawn_point = tuple(data.get('spawn_point', [100, 100]))
            self.end_point = tuple(data.get('end_point', [900, 300]))
            
            self.platforms = [
                Platform(
                    p['x'], p['y'], p['width'], p['height'],
                    p.get('type', 'ground'),
                    tuple(p.get('color', [100, 150, 100])),
                    p.get('speed', 0),
                    p.get('direction', 1)
                )
                for p in data.get('platforms', [])
            ]
            
            self.obstacles = [
                Obstacle(
                    o['x'], o['y'], o['width'], o['height'],
                    o.get('type', 'box'),
                    tuple(o.get('color', [255, 100, 100])),
                    o.get('speed', 0),
                    o.get('direction', 1)
                )
                for o in data.get('obstacles', [])
            ]
            
            print(f"✓ Level loaded from {filepath}")
        except Exception as e:
            print(f"✗ Error loading level: {e}")
    
    def handle_input_submit(self):
        """Handle text input submission"""
        self.input_active = None
        self.input_value = ""
    
    def draw(self):
        """Draw everything"""
        self.screen.fill((0, 0, 0))
        
        # Draw canvas
        self.screen.fill(self.background_color, self.canvas_rect)
        
        # Draw grid
        for x in range(0, self.canvas_rect.width, 50):
            pygame.draw.line(self.screen, (60, 60, 70), (x, 0), (x, self.canvas_rect.height), 1)
        for y in range(0, self.canvas_rect.height, 50):
            pygame.draw.line(self.screen, (60, 60, 70), (0, y), (self.canvas_rect.width, y), 1)
        
        # Draw platforms
        for i, platform in enumerate(self.platforms):
            color = (150, 200, 150) if self.selected_object == ('platform', i) else platform.color
            pygame.draw.rect(self.screen, color, (platform.x, platform.y, platform.width, platform.height))
            pygame.draw.rect(self.screen, (255, 255, 255), (platform.x, platform.y, platform.width, platform.height), 2)
            
            # Draw platform type label
            type_text = self.small_font.render(platform.platform_type[:3], True, (255, 255, 255))
            self.screen.blit(type_text, (platform.x + 5, platform.y + 5))
        
        # Draw obstacles
        for i, obstacle in enumerate(self.obstacles):
            color = (255, 150, 150) if self.selected_object == ('obstacle', i) else obstacle.color
            pygame.draw.rect(self.screen, color, (obstacle.x, obstacle.y, obstacle.width, obstacle.height))
            pygame.draw.rect(self.screen, (255, 200, 100), (obstacle.x, obstacle.y, obstacle.width, obstacle.height), 2)
            
            # Draw obstacle type label
            type_text = self.small_font.render(obstacle.obstacle_type[:3], True, (255, 255, 255))
            self.screen.blit(type_text, (obstacle.x + 5, obstacle.y + 5))
        
        # Draw spawn point
        pygame.draw.circle(self.screen, (100, 200, 100), self.spawn_point, 15)
        pygame.draw.circle(self.screen, (255, 255, 255), self.spawn_point, 15, 2)
        spawn_text = self.small_font.render("S", True, (255, 255, 255))
        spawn_rect = spawn_text.get_rect(center=self.spawn_point)
        self.screen.blit(spawn_text, spawn_rect)
        
        # Draw end point
        pygame.draw.circle(self.screen, (100, 100, 200), self.end_point, 15)
        pygame.draw.circle(self.screen, (255, 255, 0), self.end_point, 15, 2)
        end_text = self.small_font.render("E", True, (255, 255, 255))
        end_rect = end_text.get_rect(center=self.end_point)
        self.screen.blit(end_text, end_rect)
        
        # Draw temp line if drawing
        if self.temp_start:
            mouse_pos = pygame.mouse.get_pos()
            if self.canvas_rect.collidepoint(mouse_pos):
                pygame.draw.line(self.screen, (200, 200, 200), self.temp_start, mouse_pos, 2)
        
        # Draw mode indicator
        mode_text = self.font.render(f"Mode: {self.mode.name}", True, (200, 200, 200))
        self.screen.blit(mode_text, (10, 10))
        
        # Draw panel
        self.screen.fill(self.panel_color, self.panel_rect)
        pygame.draw.line(self.screen, (200, 200, 200), (1000, 0), (1000, self.screen_height), 3)
        
        # Draw buttons
        for button in self.buttons.values():
            button.draw(self.screen, self.font)
        
        # Draw info
        info_y = 480
        info_texts = [
            "--- LEVEL INFO ---",
            f"Platforms: {len(self.platforms)}",
            f"Obstacles: {len(self.obstacles)}",
            f"Difficulty: {self.difficulty}",
            f"Time Limit: {self.time_limit}s",
            "",
            "--- CONTROLS ---",
            "Click Add Platform/Obstacle",
            "Click twice to place",
            "Drag to move objects",
            "Delete key to remove",
            "ESC to cancel mode",
        ]
        
        for i, text in enumerate(info_texts):
            color = (150, 150, 150) if text.startswith("-") else (200, 200, 200)
            info_text = self.small_font.render(text, True, color)
            self.screen.blit(info_text, (1020, info_y + i * 20))
        
        pygame.display.flip()
    
    def run(self):
        """Main editor loop"""
        running = True
        while running:
            running = self.handle_events()
            self.draw()
            self.clock.tick(60)
        
        pygame.quit()


if __name__ == "__main__":
    editor = LevelEditor()
    editor.run()
