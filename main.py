import pygame,sys
from pygame.locals import *

def nextlevel(level, score):
    pass

def gameover(level, score):
    pass

def loadbricks(level):
    pass
    

def loadLevel(level):
    locatebricks(level)
    locatekeys(level)
    locatedevils(level)
    
pygame.init()
BLACK=(0,0,0)
FPS=30
fpsClock= pygame.time.Clock()
DISPLAYSURF=pygame.display.set_mode((800,600))

pygame.display.set_caption("new game")
dimg1=pygame.image.load("doorclosed.png")
WHITE=(255,255,255)
gimg=pygame.image.load('pinkgirl.png')
dimg1 = pygame.transform.scale(dimg1,(60, 100))
brick=pygame.image.load('brick.png')
brick = pygame.transform.scale(brick,(40, 40))
gx=0
gy=480
dx=500
dy=0
direction='right'
bx=0
def checkbound(x,y):
    if (x<0):
        return 0
    if (y<0):
        return 0
while True:
    DISPLAYSURF.fill(WHITE)
    
    """if direction =='right':
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
            direction='right'"""

    DISPLAYSURF.blit(gimg,(gx,gy))
    DISPLAYSURF.blit(dimg1,(dx,dy))
    base = 0
    while base<1200:
        DISPLAYSURF.blit(brick,(0,base+40))
        base = base+40
    #gx=checkbound(gx,gy)
    #gy=checkbound(gx,gy)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            keyPressed = True
            if event.key == K_LEFT:
                gx -=40
            elif event.key == K_RIGHT:
                gx +=40
            elif event.key == K_UP:
                gy -=40
            elif event.key == K_DOWN:
                gy +=40
    pygame.display.update()
    fpsClock.tick(FPS) 
    


