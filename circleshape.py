import pygame

# Base class for game obj
class CircleShape(pygame.sprite.Sprite):

    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    # sub-classes must override
    def draw(self, screen):
        pass

    # sub-classes must override
    def update(self, dt):
        pass

    def collision(self, circle_shape):
        distance = pygame.math.Vector2.distance_to(self.position, circle_shape.position)

        return self.radius + circle_shape.radius > distance