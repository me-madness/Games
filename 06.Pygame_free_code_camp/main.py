import pygame
import random

# Initialize the pygame
pygame.init()

# Create the screen     
screen = pygame.display.set_mode((800, 660))

# Background
background = pygame.image.load('planet_background.png')

# Title and Icon
pygame.display.set_caption("Dark Space Ship")
icon = pygame.image.load('favicon.png')

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 40

def player(x, y):
    screen.blit(playerImg, (x, y))
    
def enemy(x, y):
    screen.blit(enemyImg, (x, y))    
    
    
# Game Loop
running = True
while running:
    # RGB - Red, Green, Blue        
    screen.fill((0, 0, 0)) 
       
    # Background Image
    screen.blit(background, (0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # If keystrokes pressed check whether its right or left
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -0.3
        if event.key == pygame.K_RIGHT:
            playerX_change = 0.3    
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0    

            
    # Checking for boundaries of spaceship so it doesn't go out of bounds        
    playerX += playerX_change
    
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
        
    # Enemy Movement
    enemyX += enemyX_change
    
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change
        
   
                       
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()        