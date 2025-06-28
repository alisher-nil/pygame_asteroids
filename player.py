import pygame
from pygame import Vector2

from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED


class Player(CircleShape):
    line_width = 2

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation: float = 0

    def triangle(self) -> list[Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), self.line_width)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:  # turning left
            self.rotate(-dt)
        if keys[pygame.K_d]:  # turning right
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

    def move(self, dt):
        forward_vector = Vector2(0, 1).rotate(self.rotation)
        self.position += forward_vector * PLAYER_SPEED * dt
