import pygame
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
NAVY_BLUE = (28, 48, 92)
PURPLE = (142, 66, 133)
YELLOW = (249, 214, 46)
PINK = (255, 152, 220)
ORANGE = (255, 176, 0)
LIGHT_BLUE = (175, 221, 255)
BROWN = (143, 76, 42)
 
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
 
    screen.fill(NAVY_BLUE)

    pygame.draw.line(screen, PURPLE, [0, 0], [700, 1000], 15)
    pygame.draw.line(screen, YELLOW, [0, 0], [700,800], 15)
    pygame.draw.line(screen, PINK, [0, 0], [700, 600], 15)
    pygame.draw.line(screen, ORANGE, [0, 0], [700, 400], 15)
    pygame.draw.line(screen, LIGHT_BLUE, [0, 0], [700, 200], 15)
    pygame.draw.line(screen, BROWN, [0, 0], [700, 1200], 15)
    
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
