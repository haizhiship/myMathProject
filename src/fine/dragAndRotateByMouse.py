import pygame, sys
from pygame.locals import *

class mySprite(pygame.sprite.Sprite):
    def __init__(self,color,initPosition,initRect):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(initRect)
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.topleft=initPosition

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BLANK = 'None'
CENTER = 'center'
RIGHTSIDE = 'right'
LEFTSIDE = 'left'
CHANGEMOUSESPACE = 8 #判断鼠标在边缘的位置，是否是拉长还是移动
# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

'''
根据鼠标位置判断所落图形的方位
'''
def judgeMousePosInRect(imagePos, imageRect):
    x, y = pygame.mouse.get_pos()
    #如果鼠标落在图形中间
    if imagePos[0] + CHANGEMOUSESPACE < x <= imagePos[0]+ imageRect[0] - CHANGEMOUSESPACE \
            and imagePos[1] < y < imagePos[1] + imageRect[1]:
        return CENTER
    #如果鼠标落在左侧边缘
    elif imagePos[0] + CHANGEMOUSESPACE >= x > imagePos[0] - CHANGEMOUSESPACE \
            and imagePos[1] < y < imagePos[1] + imageRect[1]:
        return LEFTSIDE
    #如果鼠标落在右侧边缘
    elif imagePos[0] + imageRect[0] - CHANGEMOUSESPACE < x < imagePos[0] + imageRect[0] + CHANGEMOUSESPACE \
            and imagePos[1] < y < imagePos[1] + imageRect[1]:
        return RIGHTSIDE
    return BLANK

def main():

    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

    # draw on the surface object
    DISPLAYSURF.fill(WHITE)
    pygame.display.set_caption('Hello Pygame World!')

    imageSurfPos = [150, 100]
    imageSurfRect = [50, 50]

    changeSurf = mySprite(RED, imageSurfPos, imageSurfRect)
    # changeImage = pygame.image.load(mouse_image_filename).convert_alpha()
    changeImage = changeSurf.image

    canMove = False
    while True: # main game loop
        DISPLAYSURF.fill(WHITE)

        x, y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # 鼠标点击后，保存鼠标位置和图形边缘的距离，用以移动图形后获取图形应该的坐标
            elif event.type == MOUSEBUTTONDOWN:
                canMove = True
                distX = x - imageSurfPos[0]
                distY = y - imageSurfPos[1]
                pos = judgeMousePosInRect(imageSurfPos, imageSurfRect)
                print(pos)

            elif event.type == MOUSEBUTTONUP:
                canMove = False
                pygame.mouse.set_cursor(*pygame.cursors.arrow)

            elif event.type == MOUSEMOTION:

                if canMove == True:
                    if pos == 'center':
                        imageSurfPos = [x-distX, y-distY]
                    if pos == 'right':
                        pygame.mouse.set_cursor(*pygame.cursors.tri_right)
                        beginPos = pygame.mouse.get_pos()
                        imageSurfRect[0] = abs(beginPos[0] - imageSurfPos[0])
                        if imageSurfRect[0] == 0:
                            imageSurfRect[0] = 5
                        changeImage = pygame.transform.scale(changeImage,
                                                             (imageSurfRect[0], imageSurfRect[1]))
                    if pos == 'left':
                        pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                        beginPos = pygame.mouse.get_pos()
                        imageSurfRect[0] = abs(imageSurfRect[0] + imageSurfPos[0] - beginPos[0])
                        if imageSurfRect[0] <= 5:
                            break
                        changeImage = pygame.transform.scale(changeImage,
                                                             (imageSurfRect[0], imageSurfRect[1]))
                        imageSurfPos = [beginPos[0], imageSurfPos[1]]

        DISPLAYSURF.blit(changeImage, imageSurfPos)
        pygame.display.update()

if __name__ == '__main__':
    main()