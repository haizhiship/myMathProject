import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
RED = (0, 255, 0)
BLACK = (0, 0, 0)

size = (640, 480)
screen = pygame.display.set_mode(size)
screen_rect = screen.get_rect()

pygame.display.set_caption("JCads Develop")

done = False
clock = pygame.time.Clock()


def make_text(message, size, color):
    font = pygame.font.SysFont('Arial', size)
    text = font.render(message, True, color)
    rect = text.get_rect(center=(screen_rect.centerx, screen_rect.centery))
    return text, rect


pygame_text = []
possible_outcome = ['JamieVanCadsand', 'VinnieOrgers', 'LiesbethVDJagt']
for outcome in possible_outcome:
    pygame_text.append(make_text(outcome, 15, (255, 0, 0)))
text, rect = pygame_text[0]  # set a default

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                text, rect = pygame_text[0]
            elif event.key == pygame.K_g:
                text, rect = pygame_text[1]
            elif event.key == pygame.K_b:
                text, rect = pygame_text[2]
            elif event.key == pygame.K_ESCAPE:
                done = True

    screen.fill(WHITE)
    # pygame.draw.line(screen, RED, [0, 0], [100, 100], 5)

    # font = pygame.font.SysFont('Calibri', 25, True, False)
    # text = font.render(string, True, BLACK)
    screen.blit(text, [250, 250])
    pygame.display.flip()

    clock.tick(60)
pygame.quit()
sys.exit()