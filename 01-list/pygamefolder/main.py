import pygame
import sys


pygame.init()

#Creating a screen
size_x = 800
size_y = 600
screen = pygame.display.set_mode((size_x, size_y))

#Creating Player Image
playerImg = pygame.image.load('C:\Users\Rishabh\Desktop\Coding\Python-Intermediate\pygamefolder\Spaceship.jpeg')

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(playerImg, (100, 100))
    pygame.display.update()

