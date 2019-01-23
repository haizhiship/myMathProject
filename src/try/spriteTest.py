import pygame, sys
from pygame.locals import *

mouse_image_filename = '..\..\\resource\\fugu.png'

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

changeSurf=mySprite([255,0,0],[50,100])
#changeImage = pygame.image.load(mouse_image_filename).convert_alpha()
changeImage = changeSurf.image

imagePos = []
imageRect = []

def judgeMousePosInRect(imagePos, imageRect):
    x, y = pygame.mouse.get_pos()
    #如果鼠标落在图形中间
    if x > imagePos[0] + 5 and x <= imagePos[0]+ imageRect[0] - 5  \
        and y > imagePos[1] and y < imagePos[1] + imageRect[1]:
        return 'center'
    #如果鼠标落在左侧边缘
    elif  x <= imagePos[0] + 5  and x > imagePos[0] - 5 \
            and y > imagePos[1] and y < imagePos[1] + imageRect[1]:
        return 'left'
    #如果鼠标落在右侧边缘
    elif x > imagePos[0] + imageRect[0] - 5 and x < imagePos[0] + imageRect[0] + 5 \
        and y > imagePos[1] and y < imagePos[1] + imageRect[1]:
        return 'right'
    return 'None'

rectX = 150
rectY = 100
height = 50
width = 50
canMove = False
while True: # main game loop
    DISPLAYSURF.fill(WHITE)

    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # 鼠标点击后，方块的大小会改变为(150,150)
        elif event.type == MOUSEBUTTONDOWN:
            canMove = True
            distX = x - rectX
            distY = y - rectY
            pos = judgeMousePosInRect([rectX, rectY], [width, height])
            print(pos)
        elif event.type == MOUSEBUTTONUP:
            canMove = False
        elif event.type == MOUSEMOTION:

            if canMove == True:

                if pos == 'center':
                    (rectX, rectY) = (x-distX, y-distY)
                if pos == 'right':
                    beginPos = pygame.mouse.get_pos()
                    width = abs(beginPos[0]-rectX)
                    changeImage = pygame.transform.scale(changeImage,
                                                         (width, 50))
                if pos == 'left':
                    beginPos = pygame.mouse.get_pos()
                    width = width + rectX - beginPos[0]
                    changeImage = pygame.transform.scale(changeImage,
                                                         (width, height))
                    (rectX, rectY) = (beginPos[0], rectY)

    DISPLAYSURF.blit(changeImage, (rectX, rectY))
    pygame.display.update()