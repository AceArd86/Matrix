import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1920, 1080
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
FONT_SIZE = 20  # Slightly larger font size for better readability
FPS = 30
TRAIL_ALPHA = 50  # Transparency for the trail effect

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matrix Rain")

# Set up the font
font = pygame.font.SysFont("monospace", FONT_SIZE)

# Create a list of drop positions for each layer
layers = 5  # Increased number of layers for more depth
drops = [[random.randint(0, HEIGHT // FONT_SIZE) for _ in range(WIDTH // FONT_SIZE)] for _ in range(layers)]
speeds = [0.5, 1, 1.5, 2, 2.5]  # Slower speeds for each layer

# Create a surface for the trail effect
trail_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    # Draw the trail surface with transparency
    trail_surface.fill((0, 0, 0, TRAIL_ALPHA))
    screen.blit(trail_surface, (0, 0))

    for layer in range(layers):
        for i in range(len(drops[layer])):
            char = random.choice("01")
            char_surface = font.render(char, True, GREEN)
            screen.blit(char_surface, (i * FONT_SIZE, drops[layer][i] * FONT_SIZE))

            # Update drop position
            drops[layer][i] += speeds[layer] / 2  # Further slowed down the speed

            # Reset drop position if it goes off screen
            if drops[layer][i] * FONT_SIZE > HEIGHT:
                drops[layer][i] = 0

    pygame.display.flip()
    clock.tick(FPS)  # Cap the frame rate

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Quit on ESC key press
                running = False

pygame.quit()
