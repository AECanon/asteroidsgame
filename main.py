# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *


def main():
    # Initialize pygame
    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill the screen with black
        screen.fill((0, 0, 0))  # RGB for black

        # Refresh the screen
        pygame.display.flip()

    # Quit pygame at the end of the program
    # pygame.quit()

if __name__ == "__main__":
    main()
