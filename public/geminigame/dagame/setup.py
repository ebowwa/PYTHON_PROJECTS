# setup.py
from .game import Game
from .player import Player
from .ground import Ground
from .controls import Controls
import pygame

def initialize_game_objects(screen):
    player = Player(100, 300, 50, 50, 1)
    ground = Ground(0, 550, 800, 50, 0)
    objects = [player, ground]
    game = Game(screen, objects)
    return player, ground, objects

def initialize_controls(player):
    control_keys = {
        pygame.K_UP: player.move_up,
        pygame.K_DOWN: player.move_down,
        pygame.K_LEFT: player.move_left,
        pygame.K_RIGHT: player.move_right
    }
    return Controls(control_keys)
