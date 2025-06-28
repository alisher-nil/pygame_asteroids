# this allows us to use code from
# the open-source pygame library
# throughout this file
import inspect
import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import FPS_RATE, SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    dt = 0.0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides(player):
                print("Game over!")
                sys.exit()
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt_ms = clock.tick(FPS_RATE)
        dt = dt_ms / 1000


if __name__ == "__main__":
    main()
