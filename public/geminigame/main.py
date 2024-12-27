# main.py
import pygame
from dagame.setup import initialize_game_objects, initialize_controls
from dagame.utils import init_screen, init_clock

def run_game():
    screen, clock = init_screen(), init_clock()
    player, ground, objects = initialize_game_objects(screen)
    controls = initialize_controls(player)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        dt = clock.tick(60) / 1000.0
        for obj in objects:
            obj.update_position(dt)
        controls.update_pressed_keys()
        controls.handle_controls()
        for obj in objects:
            obj.draw(screen)
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    run_game()
