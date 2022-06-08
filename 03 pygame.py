import random
import pygame
import sys

#initializing pygame
pygame.init()

#Create the screen
screen = pygame.display.set_mode((800, 600))

# player variables
playerX = 370
playerY = 480
playerX_change = 0

#Enemey
GhostX = random.randint(0, 800)
GhostY = random.randint(20, 100)
GhostX_change = 1
GhostY_change = 0

#Bullet variables
bulletX = 200
bulletY = 200    
bulletX_change = 0
bulletY_change = 4
bullet_state = "ready"

# importing player image
Playerimg = pygame.image.load('Player.png')
Ghostimg = pygame.image.load('ghost.png')
bulletImg = pygame.image.load('bullet.png')

# importing backdrop image
Backgroundimg = pygame.image.load('B.jpeg')

def fire_bullet(x, y):
    screen.blit(bulletImg, (x, y))

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key == pygame.K_LEFT:
                playerX_change = -4
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                playerX_change = 4
            if event.key == pygame.K_a:
                playerX_change = -4
        if event.type == pygame.KEYUP:
            playerX_change = 0

    # boundary detection
    if playerX > 736:
        playerX = 736
    elif playerX < 0:
        playerX = 0

    #Enemy Boundary bounce off
    if GhostX > 736 or GhostX < 0:
        GhostX_change = - GhostX_change 
        GhostY += 10

    playerX = playerX + playerX_change
    GhostX = GhostX + GhostX_change

    fire_bullet(200, 200)


    screen.blit(Backgroundimg, (0, 0))   
    screen.blit(Playerimg, (playerX, playerY))
    screen.blit(Ghostimg, (GhostX, GhostY))
    fire_bullet(200, 200)   
    pygame.display.update()     