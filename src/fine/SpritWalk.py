import pygame, sys
from pygame.locals import *

# Create the constants (go ahead and experiment with different values)
BOARDWIDTH = 4  # number of columns in the board
BOARDHEIGHT = 4  # number of rows in the board
TILESIZE = 80
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
FPS = 30
BLANK = None
ADREAMERBODYSPEED = 20
ADREAMEWALKSPEED = -2
ADREAMECENTER = (350,200)
STOPPOSITIONX = 220

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 25, 255)


def loadImage(file, subWidth, subHeight, xNumber, yNumber):
    subSurfaceList = []
    try:
        surface = pygame.image.load(file).convert_alpha()
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s' % (file, pygame.get_error()))

    for i in range(xNumber):
        for j in range(yNumber):
            subSurfaceList.append(surface.subsurface(Rect((j * subWidth, i * subHeight)
                                                          , (subWidth, subHeight))))
    return subSurfaceList


class ADreamer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rate = 100 # 一帧画面要保持多少毫秒
        self.order = 4
        self.subSufaceList = loadImage('..\..\\resource\\AWalk.png', 25, 38, 4, 4)
        self.image = self.subSufaceList[self.order]
        self.passedTime = 0 # 记录着游戏经过了多少毫秒
        self.rect = self.image.get_rect(center=ADREAMECENTER)
        self.stop = False
        self.selected = False



    def update(self, passedTime):
        if self.stop == False:
            self.passedTime += passedTime #控制摆臂的频率
            if self.passedTime > self.rate:
                self.passedTime = 0
            self.order += int(self.passedTime / self.rate) % 4
            if self.order == 8:
                self.order = 4
            self.image = self.subSufaceList[self.order]
            self.rect.move_ip(ADREAMEWALKSPEED, 0)
            if self.rect.right < 0:
                self.kill()
        if self.stop == True:
            if self.selected == False:
                self.image = self.subSufaceList[6]
            else:
                self.image = self.subSufaceList[1]

def turnSelectedFace(ADreams):
    x, y = pygame.mouse.get_pos()
    for body in ADreams:
        if body.rect.collidepoint(x,y):
            body.selected = True
        else:
            body.selected = False

def main():
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

    # draw on the surface object
    DISPLAYSURF.fill(WHITE)
    pygame.display.set_caption('Hello Pygame World!')
    ADreame = ADreamer()
    ADreame2 = ADreamer()
    ADreame3 = ADreamer()
    ADreame4 = ADreamer()

    ADreamers = []
    ADreamers.append(ADreame)
    ADreamers.append(ADreame2)
    ADreamers.append(ADreame3)
    ADreamers.append(ADreame4)

    ADreamQueueIndex = 0
    allStop = False

    while True:  # main game loop
        DISPLAYSURF.fill(WHITE)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                if allStop == True:
                    turnSelectedFace(ADreamers)


        # 一个个排队出来显示
        if ADreamQueueIndex == 0:
            if ADreamers[ADreamQueueIndex].rect.x == STOPPOSITIONX:
                ADreamers[ADreamQueueIndex].stop = True
        elif ADreamQueueIndex < len(ADreamers) and allStop == False:
            if pygame.sprite.collide_rect(ADreamers[ADreamQueueIndex],
                                               ADreamers[ADreamQueueIndex - 1]):
                ADreamers[ADreamQueueIndex].stop = True

        #如果全部显示，保持下标不越界
        if ADreamers[ADreamQueueIndex].stop == True:
            ADreamQueueIndex += 1
            if ADreamQueueIndex >= len(ADreamers):
                ADreamQueueIndex = len(ADreamers) - 1
                allStop = True

        # 全部显示出来后还是要全量刷新显示
        for i in range(0,ADreamQueueIndex + 1):
            ADreamers[i].update(ADREAMERBODYSPEED)
            DISPLAYSURF.blit(ADreamers[i].image,ADreamers[i].rect)

        pygame.display.flip()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()
