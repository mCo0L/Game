import pygame,sys
from pygame.locals import *

'''def nextlevel(level, score):
    pass

def gameover(level, score):
    pass'''

def loaditems(level):
    if level==1:
        brickloc=[[14,11],[15,11],[4,10],[5,10],[6,10],[11,9],[12,9],[13,9],[3,8],[4,8],[7,7],[8,7],[13,6],[14,6],[15,6],[3,5],[4,5],[12,4],[13,4],[2,3],[3,3],[4,3],[12,2],[13,2],[0,11],[1,11],[9,11],[10,11],[11,11],[19,11],[19,9],[18,9],[17,9],[16,9],[19,7],[18,7],[13,8],[0,7],[1,7],[8,5],[5,11],[5,12],[5,13],[19,4],[18,4],[17,4],[15,4],[15,5],[16,4],[8,0],[8,1],[8,2],[8,3],[8,4],[8,5],[8,6]]
        keysloc=[[19,8],[7,2],[6,4]]
    return brickloc,keysloc
    

'''def loadLevel(level):
    locatebricks(level)
    locatekeys(level)
    locatedevils(level)'''

def getLocation(currLoc, action):
    newLoc = currLoc[:]
    if action == K_LEFT:
        newLoc[0] -= 1
    if action == K_RIGHT:
        newLoc[0] += 1
    if action == K_UP:
        newLoc[1] -= 1
    if action == K_DOWN:
        newLoc[1] += 1
        
    if newLoc in brickloc:
        print("Nope lol")
        return currLoc
    if newLoc in keysloc:
        global keysloc
        keysloc.pop(keysloc.index(newLoc))
        print(keysloc)
        return newLoc
    
    elif (newLoc[0] <= 19 and newLoc[0] >= 0 ) and (newLoc[1] <= 13 and newLoc[1] >= 0):
        return newLoc
    else:
        return currLoc


pygame.init()

FPS=30
BLACK=(0,0,0)
GREEN=(0,255,50)
fpsClock= pygame.time.Clock()

DISPLAYSURF=pygame.display.set_mode((800,600))
pygame.display.set_caption("GoMaria")
#back= pygame.image.load('background.jpg')
maria = pygame.image.load('pinkgirl.png')
maria = pygame.transform.scale(maria,(40, 60))
doorClosed = pygame.image.load("doorclosed.png")
doorClosed = pygame.transform.scale(doorClosed,(60, 100))
brick = pygame.image.load('brick.png')
brick = pygame.transform.scale(brick,(40, 40))
key = pygame.image.load('key.png')
key = pygame.transform.scale(key,(40, 40))

girlLoc =[0, 13]
doorLoc = [18,0]
level = 1
brickloc,keysloc = loaditems(level)

while True:
    DISPLAYSURF.fill(GREEN)
    #DISPLAYSURF.blit(back,(0,0))
    DISPLAYSURF.blit(maria,(girlLoc[0]*40,girlLoc[1]*40))
    DISPLAYSURF.blit(doorClosed,(doorLoc[0]*40,doorLoc[1]*40))
    #brickloc,keysloc = loaditems(level)
    
    for bloc in brickloc:
            DISPLAYSURF.blit(brick,(bloc[0]*40, bloc[1]*40)) 
            
    for keys in keysloc:
            DISPLAYSURF.blit(key,(keys[0]*40, keys[1]*40)) 
    base = 0
    while base<800:
        DISPLAYSURF.blit(brick,(base,560))
        base = base+40
        
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            keyPressed = True
            action = event.key
            girlLoc = getLocation(girlLoc, action)
            print("Location: ",girlLoc)


    pygame.display.update()
    fpsClock.tick(FPS) 
    


