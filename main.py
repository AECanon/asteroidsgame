# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroidfield import *
from shot import *


def main():
    # Initialize pygame
    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill the screen with black
        screen.fill((0, 0, 0))  # RGB for black

        #player.update(dt)
        for p in updatable:
            p.update(dt)

        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                pygame.quit()
                return  # Exit the game
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    #asteroid.kill()
                    asteroid.split()

        #player.draw(screen)
        for p in drawable:
            p.draw(screen)
       
        # Refresh the screen
        pygame.display.flip()

        # Pause the loop until 1/60th of a second has passed
        dt = clock.tick(60) / 1000

    # Quit pygame at the end of the program
    # pygame.quit()

if __name__ == "__main__":
    main()
