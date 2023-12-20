import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Solar System Simulation")

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Celestial bodies' properties
sun_radius = 50
sun_pos = (width // 2, height // 2)
planet_radius = 20
planet_distance = 200
planet_pos = (sun_pos[0] + planet_distance, sun_pos[1])

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(BLACK)

    # Draw the sun
    pygame.draw.circle(screen, YELLOW, sun_pos, sun_radius)

    # Draw the planet
    pygame.draw.circle(screen, BLUE, planet_pos, planet_radius)

    # Update the display
    pygame.display.flip()
