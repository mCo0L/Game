import pygame,sys
from pygame.locals import *

pygame.init()
BLACK=(0,0,0)
windowWidth, windowHeight = 854, 480 #854, 480 #640, 360 #750, 500 #1280, 720
window = pygame.display.set_mode((windowWidth,windowHeight)) # put ",pygame.FULLSCREEN" after "windowHeight)" for fulscreen
pygame.display.set_caption('First Game')
pygame.display.set_caption("new game")
pixObj = pygame.PixelArray(window)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()