# to install use : pip install pygame

from Game_Loec.map_tools import *
from Game_Loec.pygame_tools import init_pygame, get_pressed_key, leave_game
from Game_Loec.settings import block_size, fps


# get map
map = get_map()

# initialise pygame (screen and clock references)
screen, clock = init_pygame(map)

# game loop
move_finished = True
while True:
    # redraw map
    redraw(screen, map)

    # check keyboard
    events = get_pressed_key()

    # leave infinity loop
    if leave_game(events):
        break

    # if arrow keys are pressed change map
    change_map(map, events, move_finished)

    # some delay 1/fps in seconds
    clock.tick(fps)

# Quit Pygame
pygame.quit()
