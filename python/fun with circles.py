import pygame
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

NOUGAT = (204, 142, 105)
TR_YELLOW = (255, 255, 0)
BURPLE = (205, 98, 152)
BREEN = (44, 101, 29)
GLUE = (16, 42, 220)
BAVENDER = (140, 91, 159)

pygame.init()
 
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
done = False
 
clock = pygame.time.Clock()
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, [100, 100], 50, 1)
    pygame.draw.circle(screen, NOUGAT, [300, 100], 50, 10)
    pygame.draw.circle(screen, TR_YELLOW, [500, 100], 50)
    pygame.draw.circle(screen, BURPLE, [200, 300], 100)
    pygame.draw.circle(screen, BREEN, [100, 400], 100)
    pygame.draw.circle(screen, BAVENDER, [700, 500], 100)
    pygame.draw.circle(screen, GLUE, [600, 400], 50)
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
