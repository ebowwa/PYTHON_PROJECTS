# ground.py
from .object import Object
import pygame  # Make sure to import pygame

class Ground(Object):
    def __init__(self, x, y, width, height, mass):
        super().__init__(x, y, width, height, mass)

    def draw(self, screen):
        # Draw the ground as a rectangle
        pygame.draw.rect(screen, (139, 69, 19), (self.x, self.y, self.width, self.height))  # Brown color for ground
    def collide(self, other):
      # Implementing ground-specific collision responses if needed in the future
      # For now, it might simply serve to provide a solid platform for other objects
      # but can be expanded for more interactive ground behavior (e.g., moving platforms)
      pass