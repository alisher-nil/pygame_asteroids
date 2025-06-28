import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_ACCEL_RATE, ASTEROID_MIN_RADIUS

ASTEROID_WIDTH = 2


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        child_vector1 = self.velocity.rotate(angle)
        child_vector2 = self.velocity.rotate(-angle)

        child_radius = self.radius - ASTEROID_MIN_RADIUS

        child1 = Asteroid(self.position.x, self.position.y, child_radius)
        child2 = Asteroid(self.position.x, self.position.y, child_radius)

        child1.velocity = child_vector1 * ASTEROID_ACCEL_RATE
        child2.velocity = child_vector2 * ASTEROID_ACCEL_RATE
