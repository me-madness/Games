import random
import math
import pygame

# Initialize the pygame
pygame.init()

# Create the screen     
screen = pygame.display.set_mode((800, 660))

# Background
background = pygame.image.load('planet_background.png')

# Title and Icon
pygame.display.set_caption("Dark Space Battle")
icon = pygame.image.load('favicon.png')

# Player
playerImg = pygame.image.load('player1.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('enemy2.png')
enemyX = random.randint(0, 735)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 40

# Bullet

# Ready = You can't see the bullet on the screen

# Fire - the bullet is currently moving

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

score = 0

def player(x, y):
    screen.blit(playerImg, (x, y))
    
def enemy(x, y):
    screen.blit(enemyImg, (x, y))    
    
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False     
        
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
            playerX_change = -0.5
        if event.key == pygame.K_RIGHT:
            playerX_change = 0.5   
        if event.key == pygame.K_SPACE:
            if bullet_state is "ready":
                # Get the current coordinate of the spaceship
                bulletX = playerX
                fire_bullet(bulletX, bulletY)
            
             
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
        enemyX_change = 0.2
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.2
        enemyY += enemyY_change
    
    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
        
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change    
   
    # Collision
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)
    
                       
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    # fire_bullet(bulletX, bulletY)
    pygame.display.update()        