import pygame,sys
from pygame.locals import *

'''def nextlevel(level, score):
    pass

def gameover(level, score):
    pass'''

def loadbricks(level):
    if level==1:
        brickloc=[(14,11),(15,11),(4,10),(5,10),(6,10),(11,9),(12,9),(13,9),(3,8),(4,8),(7,7),(8,7),(13,6),(14,6),(15,6),(3,5),(4,5),(12,4),(13,4),(2,3),(3,3),(4,3),(12,2),(13,2),(0,11),(1,11),(9,11),(10,11),(11,11),(19,11),(19,9),(18,9),(17,9),(16,9),(19,7),(18,7),(13,8),(0,7),(1,7),(8,5),(5,11),(5,12),(5,13),(19,4),(18,4),(17,4),(15,4),(15,5),(16,4),(8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,6)]
    return brickloc
    

'''def loadLevel(level):
    locatebricks(level)
    locatekeys(level)
    locatedevils(level)'''

def getLocation(currLoc, action):
    if currLoc in loadbricks(level):
        return currLoc
    else:
        newLoc = currLoc.copy()
        if event.key == K_LEFT:
            newLoc[0] -= 40
        if event.key == K_RIGHT:
            newLoc[0] += 40
        if event.key == K_UP:
            newLoc[1] -= 40
        if event.key == K_DOWN:
            newLoc[1] -= 40

        if (0 <= newLoc[0] <= 760) and (0 <= newLoc[1] <= 480):
            return newLoc
        else:
            return currLoc


pygame.init()

FPS=30
BLACK=(0,0,0)
WHITE=(255,255,255)
fpsClock= pygame.time.Clock()

DISPLAYSURF=pygame.display.set_mode((800,600))
pygame.display.set_caption("GoMaria")

maria = pygame.image.load('pinkgirl.png')
doorClosed = pygame.image.load("doorclosed.png")
doorClosed = pygame.transform.scale(doorClosed,(60, 100))
brick = pygame.image.load('brick.png')
brick = pygame.transform.scale(brick,(40, 40))

girlLoc =[0, 460]
doorLoc = [740,0]
level = 1


while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(maria,(girlLoc[0],girlLoc[1]))
    DISPLAYSURF.blit(doorClosed,(doorLoc[0],doorLoc[1]))
    brickloc = loadbricks(1)
    for bloc in brickloc:
            DISPLAYSURF.blit(brick,(bloc[0]*40, bloc[1]*40)) 
    base = 0
    while base<800:
        DISPLAYSURF.blit(brick,(base,540))
        base = base+40
        
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            keyPressed = True
            girlLoc = getLocation(girlLoc, event.key, level)


    pygame.display.update()
    fpsClock.tick(FPS) 
    

