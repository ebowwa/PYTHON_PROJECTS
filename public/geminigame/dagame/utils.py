# Enhanced utils.py
import pygame
import sys

def init_screen():
    pygame.init()
    return pygame.display.set_mode((800, 600))

def init_clock():
    return pygame.time.Clock()

def load_image(file_path, alpha=True):
    image = pygame.image.load(file_path)
    if alpha:
        image = image.convert_alpha()
    else:
        image = image.convert()
    return image

def load_sound(file_path):
    sound = pygame.mixer.Sound(file_path)
    return sound

def draw_text(surface, text, font, color, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    return pygame.key.get_pressed(), pygame.mouse.get_pos(), pygame.mouse.get_pressed()

def play_music(file_path, loops=-1, start=0.0, volume=1.0):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(loops, start)
    pygame.mixer.music.set_volume(volume)

def create_button(surface, text, font, color, x, y, width, height, hover_color, click_action=None):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(surface, color, button_rect)

    if button_rect.collidepoint((mouse_x, mouse_y)):
        pygame.draw.rect(surface, hover_color, button_rect)  # Button hover effect
        if click[0] == 1 and click_action:
            click_action()  # Call the function passed as click_action

    text_obj = font.render(text, True, pygame.Color('black'))
    text_rect = text_obj.get_rect(center=button_rect.center)
    surface.blit(text_obj, text_rect)

def update_display():
    pygame.display.flip()

# Example usage of create_button
# def button_clicked():
#    print("Button was clicked!")

# Inside your main game loop, you could use create_button like this:
# create_button(screen, "Click Me!", my_font, (0, 255, 0), 100, 100, 200, 50, (0, 200, 0), button_clicked)
# Don't forget to handle events and update the display within your game loop.
