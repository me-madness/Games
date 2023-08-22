import pygame

from Game_Loec.settings import EXIT_KEY, block_size


def init_pygame(map):
    Nx = len(map[0])
    Ny = len(map)
    width = block_size * Nx
    height = block_size * Ny

    # Initialize Pygame
    pygame.init()
    # create a window
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Your first maze game")

    # init pygame clock
    clock = pygame.time.Clock()

    return screen, clock


def get_pressed_key():
    # Get pressed keys
    events = pygame.event.get()
    return events


def leave_game(events):
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == EXIT_KEY:
                print('Exit key was pressed')
                return True
    return False


