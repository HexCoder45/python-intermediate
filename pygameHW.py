from operator import truediv
import pygame
import sys

#initializing pygame
pygame.init()

#Create the screen
screen = pygame.display.set_mode((800, 600))

# player variables
playerX = 370
playerY = 480
playerX_Change = 0


# importing player image
Playerimg = pygame.image.load('/Users/deveshsarkar9/Documents/Devesh/Python/python-intermediate/02-PyGame/Player.png')

# importing backdrop image
Backgroundimg = pygame.image.load('/Users/deveshsarkar9/Documents/Devesh/Python/python-intermediate/02-PyGame/B.jpeg')


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_Change = 4
            if event.key == pygame.K_LEFT:
                playerX_Change = -4
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                playerX_Change = 4
            if event.key == pygame.K_a:
                playerX_Change = -4
        if event.type == pygame.KEYUP:
            playerX_Change = 0

    # boundary detection
    if playerX > 736:
        playerX = 736
    elif playerX < 0:
        playerX = 0

    
    playerX = playerX + playerX_Change

    screen.blit(Backgroundimg, (0, 0))   
    screen.blit(Playerimg, (playerX, playerY))   
    pygame.display.update()             