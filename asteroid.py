from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        #current is always destroyed. If not smallest, will spawn two of smaller version
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            #generate random angle
            random_angle = random.uniform(20, 50)

            vector_1 = pygame.math.Vector2(self.velocity.x, self.velocity.y).rotate(random_angle)
            vector_2 = pygame.math.Vector2(self.velocity.x, self.velocity.y).rotate(-random_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

            asteroid_1.velocity = vector_1 * 1.2 #multiplying for making it move faster
            asteroid_2.velocity = vector_2 * 1.2