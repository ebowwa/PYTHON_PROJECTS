# game.py
import pygame
from .player import Player
from .ground import Ground

class Game:
    def __init__(self, screen, objects):
        self.screen = screen
        self.objects = objects
        self.running = True

    def update(self, dt):
        for obj in self.objects:
            obj.update_position(dt)
            obj.apply_force([0, -9.8 * obj.mass])  # Apply gravity effect on each object
            for other in self.objects:
                if obj != other:
                    obj.collide(other)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def render(self):
        self.screen.fill((0, 0, 0))  # Fill the screen with black before drawing objects
        for obj in self.objects:
            pygame.draw.rect(self.screen, (255, 255, 255), (obj.x, obj.y, obj.width, obj.height))
        pygame.display.flip()  # Update the full display Surface to the screen

    def main_loop(self, clock):
        while self.running:
            dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds
            self.handle_events()
            self.update(dt)
            self.render()
