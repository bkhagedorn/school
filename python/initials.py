import pygame
 
DARK_GREEN = (42, 140, 68)

LIGHT_PURPLE = (191, 101, 247)
YELLOW = (222, 242, 41)
ORANGE = (255, 177, 43)

offset = 75
 
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
 
    screen.fill(DARK_GREEN)

    pygame.draw.line(screen, LIGHT_PURPLE, (50 + offset, 100), (50 + offset, 400), 5)
    pygame.draw.line(screen, LIGHT_PURPLE, (50 + offset, 100), (150 + offset, 200), 5)
    pygame.draw.line(screen, LIGHT_PURPLE, (50 + offset, 250), (150 + offset, 200), 5)
    pygame.draw.line(screen, LIGHT_PURPLE, (50 + offset, 250), (150 + offset, 300), 5)
    pygame.draw.line(screen, LIGHT_PURPLE, (50 + offset, 400), (150 + offset, 300), 5)

    pygame.draw.line(screen, YELLOW, (200 + offset, 100), (200 + offset, 400), 5)
    pygame.draw.line(screen, YELLOW, (200 + offset, 250), (300 + offset, 100), 5)
    pygame.draw.line(screen, YELLOW, (200 + offset, 250), (300 + offset, 400), 5)

    pygame.draw.line(screen, ORANGE, (350 + offset, 100), (350 + offset, 400), 5)
    pygame.draw.line(screen, ORANGE, (450 + offset, 100), (450 + offset, 400), 5)
    pygame.draw.line(screen, ORANGE, (350 + offset, 250), (450 + offset, 250), 5)
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
