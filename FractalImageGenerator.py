"""
Fractal Image Generator
Designed by: Prahlad
"""

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fractal Image Generator")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw_fractal(x, y, width, height, depth):
    """
    Recursively draw a fractal pattern.

    Parameters:
    - x, y: Coordinates of the top-left corner of the fractal rectangle.
    - width, height: Dimensions of the fractal rectangle.
    - depth: Recursion depth, controls the level of detail.
    """
    if depth == 0:
        pygame.draw.rect(screen, WHITE, (x, y, width, height))
    else:
        # Divide the rectangle into four smaller rectangles
        new_width = width // 2
        new_height = height // 2

        # Recursively draw each smaller rectangle
        draw_fractal(x, y, new_width, new_height, depth - 1)
        draw_fractal(x + new_width, y, new_width, new_height, depth - 1)
        draw_fractal(x, y + new_height, new_width, new_height, depth - 1)
        draw_fractal(x + new_width, y + new_height, new_width, new_height, depth - 1)

def main():
    # Set up the clock
    clock = pygame.time.Clock()

    # Run the game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Draw the fractal with parameters
        draw_fractal(50, 50, 700, 500, 5)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(30)

if __name__ == "__main__":
    main()
