# Example file showing a circle moving on screen
import pygame
import os

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# Load background image (replace with your path)
try:
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, 'Assets', 'Pictures', 'background1.png')
    print(f"Looking for image at: {image_path}")
    
    if os.path.exists(image_path):
        background = pygame.image.load(image_path)
        background = pygame.transform.scale(background, (1280, 720))  # Scale to screen size
        print("Image loaded successfully!")
    else:
        background = None
        print(f"Image not found at: {image_path}")
except Exception as e:
    background = None
    print(f"Error loading image: {e}")

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_velocity_y = 0
gravity = 700 # pixels per second 2301
jump_power = 400  # pixels per second
ground_level = screen.get_height() - 200
ball_radius = 40
is_jumping = False

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")  # Always clear with black first
    
    if background:
        screen.blit(background, (0, 0))  # Draw background image to cover everything

    # draw ground
    pygame.draw.line(screen, "white", (0, ground_level), (screen.get_width(), ground_level), 5)

    # Draw ball with solid color and outline
    pygame.draw.circle(screen, "red", player_pos, ball_radius)  # Solid ball
    pygame.draw.circle(screen, "yellow", player_pos, ball_radius, 3)  # Outline

    keys = pygame.key.get_pressed()
    # Jump input (space, W, or up arrow)
    if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:
        if not is_jumping:  # Only jump if on ground
            player_velocity_y = -jump_power
            is_jumping = True
    
    # Apply gravity
    player_velocity_y += gravity * dt
    player_pos.y += player_velocity_y * dt
    
    # Ground collision
    if player_pos.y + ball_radius >= ground_level:
        player_pos.y = ground_level - ball_radius
        player_velocity_y = 0
        is_jumping = False

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
print("super cool geometry dash clone")