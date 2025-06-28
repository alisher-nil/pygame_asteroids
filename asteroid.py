import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_ACCEL_RATE, ASTEROID_MIN_RADIUS

ASTEROID_WIDTH = 2


class Asteroid(CircleShape):
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        child_radius = self.radius - ASTEROID_MIN_RADIUS
        self.spawn_child(child_radius, angle)
        self.spawn_child(child_radius, -angle)

    def spawn_child(self, radius: float, escape_angle: float) -> None:
        child = Asteroid(self.position.x, self.position.y, radius)
        child_vector = self.velocity.rotate(escape_angle)
        child.velocity = child_vector * ASTEROID_ACCEL_RATE
