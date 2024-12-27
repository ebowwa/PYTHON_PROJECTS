# player.py
from .object import Object
from vec_ops.vector import engVector  # Correct import statement
import pygame

class Player(Object):
    def __init__(self, x, y, width, height, mass):
        super().__init__(x, y, width, height, mass)
        self.is_jumping = False
        # Initialize velocity as an engVector instance
        self.velocity = engVector.create_vector(0, 0)  # Use the static method for initialization

    def collide(self, other):
        # Simple collision detection
        if self.x < other.x + other.width and self.x + self.width > other.x and self.y < other.y + other.height and self.y + self.height > other.y:
            self.is_jumping = False
            self.y = other.y - self.height  # Place the player on top of the ground
            # Reset vertical velocity using engVector
            self.velocity = engVector.create_vector(self.velocity[0], 0)

    def move_up(self):
        # Move the player up
        if not self.is_jumping:
            self.is_jumping = True
            # Adjust the vertical velocity for jumping
            self.velocity = engVector.create_vector(self.velocity[0], -10)

    def move_down(self):
        # Move the player down
        self.velocity = engVector.create_vector(self.velocity[0], 10)  # Adjust the vertical velocity for going down

    def move_left(self):
        # Move the player left
        self.velocity = engVector.create_vector(-10, self.velocity[1])  # Adjust the horizontal velocity

    def move_right(self):
        # Move the player right
        self.velocity = engVector.create_vector(10, self.velocity[1])  # Adjust the horizontal velocity

    def draw(self, screen):
        # Draw the player as a rectangle for simplicity
        pygame.draw.rect(screen, (0, 128, 255), (self.x, self.y, self.width, self.height))
