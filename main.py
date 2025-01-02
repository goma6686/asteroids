# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        #check if user clicked quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #move
        for u in updatable:
            u.update(dt)

        for asteroid in asteroids:

            for bullet in shots:
                if bullet.collision(asteroid):
                    bullet.kill()
                    asteroid.split()

            if asteroid.collision(player):
                print("Game over!")
                return
            

        #screen filled with black
        pygame.Surface.fill(screen, (0,0,0))

        #show
        for d in drawable:
            d.draw(screen)
        
        #refresh the screen
        pygame.display.flip()

        #draw a maximum of 60 times per second
        #time passed since tick() was called converted to seconds
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()