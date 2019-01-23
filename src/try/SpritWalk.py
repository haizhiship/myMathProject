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

def loadImage(file, width=None, height=None, number=None):
    file = os.path.join(MAIN_DIR, 'data/image', file)
    try:
        surface = pygame.image.load(file).convert_alpha()
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s' % (file, pygame.get_error()))
    if width == None:
        return surface
    height = surface.get_height()

    return [surface.subsurface(
        Rect((i * width, 0), (width, height))
    ) for i in xrange(number)]

class ADreamer(pygame.sprite.Sprite):
    def __init__(self,topleft):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))  # 这个就是每个精灵的图片Surface
        self.image.fill(color)
        self.rect = self.image.get_rect()  # 每个精灵Surface显示的Rectangle
        self.rect.topleft = topleft  # 设定矩阵左上角的位置

    def update(self):
        speed = random.randint(0, 10)
        self.rect.left += speed
        if self.rect.left > 630:
            self.rect.left = -10




def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),0,32)

    # draw on the surface object
    DISPLAYSURF.fill(WHITE)
    pygame.display.set_caption('Hello Pygame World!')



    while True: # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


        pygame.display.update()

if __name__ == '__main__':
    main()