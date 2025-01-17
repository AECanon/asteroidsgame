import pygame
import random
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        white = (255, 255, 255)
        pygame.draw.circle(screen, white, self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt   

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        
        velocity1 = self.velocity.rotate(random_angle) * 1.2  # Scale up by 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2  # Scale up by 1.2

        # Compute the new radius for the smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two new asteroids at the current position with the new radius
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velocity2

        for container in Asteroid.containers:
            container.add(asteroid1, asteroid2)
