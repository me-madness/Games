import pygame

from Game_Loec.settings import block_size, background_color, wall_color, block_color, personage_color


def get_map():
    # create a map as a list
    # 0 - nothing
    # 1 - blue wall
    # 2 - moving red block
    # 3 - personage (green circle)
    map = [
        [3, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 2, 0, 1, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        [0, 2, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
    ]
    # or load from file
    return map


def redraw(screen, map):
    """
    Determine position of the value 'param'
    :param map: game map
    :param param: searching value
    :return: x and y index
    
    """
    Nx = len(map[0])
    Ny = len(map)

    # Clear the screen
    screen.fill(background_color)

    for ix in range(Nx):
        # ix is the index of column
        for iy in range(Ny):
            # iy is the index of row
            x = ix * block_size
            y = iy * block_size
            code = map[iy][ix]

            if code == 1:  # wall
                pygame.draw.rect(screen, wall_color, (x, y, block_size, block_size))
            elif code == 2:  # moving block
                pygame.draw.rect(screen, block_color, (x, y, block_size, block_size))
            elif code == 3:  # personage
                pygame.draw.circle(screen, personage_color, (x + block_size/2, y + block_size/2), block_size/2)

    # Update the display
    pygame.display.flip()


def personage_position(map, param):
    Nx = len(map[0])
    Ny = len(map)

    for ix in range(Nx):
        # ix is the index of column
        for iy in range(Ny):
            # iy is the index of row
            code = map[iy][ix]
            if code == param:
                return ix, iy


def move_block(iy1, ix1, iy2, ix2, map):
    """
    Move the block from the starting position (iy1, ix1) to final position (iy2, ix2)
    in the game map
    
    :param iy1: y-axis start position
    :param ix1: x-axis start position
    :param iy2: y-axis final position
    :param ix2: x-axis final position
    :param map: game map
    
    """
    Nx = len(map[0])
    Ny = len(map)

    if iy1 == iy2:
        if ix1 < ix2:  # move to right
            if ix2 < Nx:  # we are not at the board, we can move
                print(f'we can move to right')
                # we can move
                if map[iy2][ix2] == 0:
                    map[iy2][ix2] = 2  # new block position
                    map[iy1][ix1] = 0  # block previous position
                    return True
        if ix1 > ix2:  # move to left
            if ix2 >= 0:  # we are not at the board, we can move
                # we can move
                if map[iy2][ix2] == 0:
                    print(f'we can move to left')
                    map[iy2][ix2] = 2  # new block position
                    map[iy1][ix1] = 0  # block previous position
                    return True
    if ix1 == ix2:
        if iy1 < iy2:  # move to down
            if iy2 < Ny:  # we are not at the board, we can move
                # we can move
                if map[iy2][ix2] == 0:
                    print(f'we can move to down')
                    map[iy2][ix2] = 2  # new block position
                    map[iy1][ix1] = 0  # block previous position
                    return True
        if iy1 > iy2:  # move to up
            if iy2 >= 0:  # we are not at the board, we can move
                # we can move
                if map[iy2][ix2] == 0:
                    print(f'we can move to up')
                    map[iy2][ix2] = 2  # new block position
                    map[iy1][ix1] = 0  # block previous position
                    return True
    return False


def change_map(map, events, move_finished):
    """
    Change game map according the game 
    
    
    
    
    """
    Nx = len(map[0])
    Ny = len(map)

    if move_finished:
        move_finished = False
        ix, iy = personage_position(map, 3)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if ix > 0:  # we are not at the board
                        if map[iy][ix - 1] == 0:  # this is ground
                            # we can move
                            if map[iy][ix - 1] == 0:
                                map[iy][ix - 1] = 3
                                map[iy][ix] = 0
                        # move block
                        elif map[iy][ix - 1] == 2:  # this moving block
                            if move_block(iy, ix - 1, iy, ix - 2, map):
                                map[iy][ix - 1] = 3
                                map[iy][ix] = 0
                if event.key == pygame.K_RIGHT:
                    if ix < Nx-1:  # we are not at the board
                        if map[iy][ix + 1] == 0:  # this is ground
                            # we can move
                            if map[iy][ix + 1] == 0:
                                map[iy][ix + 1] = 3
                                map[iy][ix] = 0
                        # move block
                        elif map[iy][ix + 1] == 2:
                            if move_block(iy, ix + 1, iy, ix + 2, map):
                                map[iy][ix + 1] = 3
                                map[iy][ix] = 0
                if event.key == pygame.K_UP:
                    if iy > 0:  # we are not at the board
                        if map[iy - 1][ix] == 0:  # this is ground
                            # we can move
                            if map[iy - 1][ix] == 0:
                                map[iy - 1][ix] = 3
                                map[iy][ix] = 0
                        # move block
                        elif map[iy - 1][ix] == 2:
                            if move_block(iy - 1, ix, iy - 2, ix, map):
                                map[iy - 1][ix] = 3
                                map[iy][ix] = 0
                if event.key == pygame.K_DOWN:
                    if iy < Ny - 1:  # we are not at the board
                        if map[iy + 1][ix] == 0:  # this is ground
                            # we can move
                            if map[iy + 1][ix] == 0:
                                map[iy + 1][ix] = 3
                                map[iy][ix] = 0
                        # move block
                        if map[iy + 1][ix] == 2:
                            if move_block(iy + 1, ix, iy + 2, ix, map):
                                map[iy + 1][ix] = 3
                                map[iy][ix] = 0
        move_finished = False
