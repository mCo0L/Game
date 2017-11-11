import pygame,sys
from pygame.locals import *

pygame.init()
BLACK=(0,0,0)
FPS=30
fpsClock= pygame.time.Clock()
DISPLAYSURF=pygame.display.set_mode((600,600),0,32)

pygame.display.set_caption("new game")

WHITE=(255,255,255)
gimg=pygame.image.load('pinkgirl.png')
gx=10
gy=10
direction='right'

while True:
    DISPLAYSURF.fill(WHITE)
    
    if direction =='right':
        gx +=5
        if gx==280:
            direction="down"
    elif direction =='down':
        gy +=5
        if gy ==220:
            direction ='left'
    elif direction == 'left':
        gx -=5
        if gx ==10:
            direction ='up'
    elif direction =='up':
        gy -=5
        if gy ==10:
            direction='right'
    DISPLAYSURF.blit(gimg,(gx,gy))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)  