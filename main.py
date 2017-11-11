import pygame,sys
from pygame.locals import *

'''def nextlevel(level, score):
    pass

def gameover(level, score):
    pass'''

def loadbricks(level):
    if level==1:
        brickloc=[(14,11),(15,11),(4,10),(5,10),(6,10),(11,9),(12,9),(13,9),(3,8),(4,8),(7,7),(8,7),(13,6),(14,6),(15,6),(3,5),(4,5),(12,4),(13,4),(2,3),(3,3),(4,3),(12,2),(13,2)]

    return brickloc
    

'''def loadLevel(level):
    locatebricks(level)
    locatekeys(level)
    locatedevils(level)'''
    
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
gy=465
dx=740
dy=0
direction='right'
bx=0

loc = [0,12]
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
    brickloc = loadbricks(1)
    for bloc in brickloc:
            DISPLAYSURF.blit(brick,(bloc[0]*40, bloc[1]*40)) 
    base = 0
    while base<1200:
        DISPLAYSURF.blit(brick,(base,540))
        base = base+40
        
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            keyPressed = True
            if event.key == K_LEFT:
                if (loc[0]*40-40)>=0:
                    gx -=40
                    loc[0] -= 1
                
                    print("location: ",loc)
            elif event.key == K_RIGHT:
                if (loc[0]*40+40)<=760:
                    gx +=40
                    loc[0] += 1
                    print("location: ",loc)
            elif event.key == K_UP:
                if (loc[1]*40-40)>=0:
                    gy -=40
                    loc[1] -= 1
                    print("location: ",loc)
            elif event.key == K_DOWN:
                if (loc[1]*40+40)<=480:
                    gy +=40
                    loc[1] += 1
                    print("location: ",loc)
    pygame.display.update()
    fpsClock.tick(FPS) 
    


