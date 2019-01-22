import pygame, sys
from pygame.locals import *

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
text = pygame.font.Font("..\..\\resource\QinYuanJ.TTF",25)
text_fmt = text.render("进程已结束,退出代码",1,BLACK)

text_matrics = text.metrics("你")
text_matrics1 = text.metrics("吗")
print(text.size("你"))
print(text_fmt.get_width())
print(text_fmt.get_size())

# draw on the surface object
DISPLAYSURF.fill(BLUE)
DISPLAYSURF.blit(text_fmt,(100,100))
pygame.display.set_caption('Hello Pygame World!')

'''

'''
def getTextByPositon(text, font, beginPos):

    wordWidths = []
    for word in text:
        wordWidths.append(font.size(word)[0])

    wordHeight = font.size(word)[1]
    mouseX, mouseY = pygame.mouse.get_pos()
    if beginPos[1] < mouseY and beginPos[1] + wordHeight > mouseY:
        totalLength = 0
        for i in range(len(wordWidths)):
            totalLength += wordWidths[i]
            if totalLength + beginPos[0] > mouseX:
                return text[i]
    return ""


def getTextListByArea(text, font, textPos, beginPos, endPos):

    wordWidths = []
    for word in text:
        wordWidths.append(font.size(word)[0])
    wordHeight = font.size(word)[1]

    beginIndex = -1
    endIndex = -1
    beginSelPos = 0
    endSelPos = 0
    if (textPos[1] < beginPos[1] and textPos[1] + wordHeight > beginPos[1]) \
        and (textPos[1] < endPos[1] and textPos[1] + wordHeight > endPos[1]):
       totalLength = 0
       for i in range(len(wordWidths)):
           totalLength += wordWidths[i]
           if totalLength + textPos[0] > beginPos[0] and beginIndex == -1:
               beginIndex = i
               beginSelPos = totalLength - wordWidths[i]
           if totalLength + textPos[0] > endPos[0] and endIndex == -1:
               endIndex = i + 1
               endSelPos = totalLength + textPos[0]

    if endIndex >= len(text):
        endIndex = len(text)

    if beginIndex > -1 and endIndex > -1:
        return text[beginIndex:endIndex], beginSelPos, endSelPos
    return '',0,0


def getSelectTextPos(text, font, beginPos):
    pass


beginPos = ()
endPos = ()
while True: # main game loop

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                text_new = text.render("程已结束,退",1,RED)
                DISPLAYSURF.blit(text_new,(125,100))
            if event.key == K_RIGHT:
                text_new = text.render("程已结束,退",1,BLACK)
                DISPLAYSURF.blit(text_new,(125,100))
        elif event.type == MOUSEBUTTONDOWN:
            beginPos = pygame.mouse.get_pos()
        elif event.type == MOUSEBUTTONUP:
            endPos = pygame.mouse.get_pos()
            #selectText = getTextByPositon("进程已结束,退出代码",text,(100,100))
            #print(selectText)
        if len(beginPos) > 0 and len(endPos) > 0:
            selText, beginPos, endPos = getTextListByArea("进程已结束,退出代码",
                                                          text,(100,100),beginPos,endPos)
            if len(selText) > 0:
                print(selText)
                text_new = text.render(selText, 1, RED)
                DISPLAYSURF.blit(text_new, (beginPos + 100, 100))
            beginPos = ()
            endPos = ()




    # 获得鼠标位置
    x, y = pygame.mouse.get_pos()



    pygame.display.update()