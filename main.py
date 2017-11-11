import pygame,sys
from pygame.locals import *

pygame.init()
BLACK=(0,0,0)
DISPLAYSURF=pygame.display.set_mode((600,600),0,32)
DISPLAYSURF.fill((255,255,255))
pygame.display.set_caption("new game")
pixObj = pygame.PixelArray(DISPLAYSURF)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()