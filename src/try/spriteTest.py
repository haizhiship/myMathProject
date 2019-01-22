import pygame, sys
from pygame.locals import *

class mySprite(pygame.sprite.Sprite):
    def __init__(self,color,initial_position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50,50])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.topleft=initial_position


# Create the constants (go ahead and experiment with different values)
BOARDWIDTH = 4  # number of columns in the board
BOARDHEIGHT = 4 # number of rows in the board
TILESIZE = 80
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
FPS = 30
BLANK = None

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,  25, 255)

pygame.init()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),0,32)

# draw on the surface object
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption('Hello Pygame World!')

b=mySprite([255,0,0],[50,100])
DISPLAYSURF.blit(b.image,b.rect)



while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            beginPos = pygame.mouse.get_pos()


    pygame.display.update()