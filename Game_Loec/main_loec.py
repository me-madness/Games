import pygame



def get_map():
    # Create a map as a list
    # 0 - nothing
    # 1 - blue wall
    # 2 - moving red block
    # 3 - 
    
    map = [
        
        
        
        
        
        
    ]
    
    
    def init_pygame(height, width):
        # Initialize pygame
        
        
        def redraw(screen, map):
            background_color = (255, 255, 255) # example, white
            wall_color = (0, 0, 255) # for example black
            block_color = (0, 255, 0) # for example green
            personage_color = (0, 255, 0) # for example green
            # Clear the screen
            screen.fill(background_color)
            
            for ix in range(len(Nx)):
                # ix is the index of column
                for iy in range(len(Ny)):
                # iy is the index of row
                    x = ix * block_size
                    y = iy * block_size
                    code = map[iy][ix]
                    
                    if code == 1: # wall
                        pygame.draw.rect(screen, wall_color, (x, y, block_size, block_size))
                    elif code == 2: # moving block
                        pygame.draw.rect(screen, block_color, (x, y, block_size, block_size)) 
                    elif code == 3: # personagek
                        pygame.draw.rect(screen, personage_color, (x + block_color, y + , block_size, block_size))
                        
                        
                        
                        
                        
                        
block_size = 0                        
pygame.init()
                            