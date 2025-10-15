'''
animated snowfall
1-5-24
'''

import pygame
import random
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
pygame.init()
 
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
done = False
 
clock = pygame.time.Clock()

snow_list = []
for i in range(50):
        x = random.randrange(700)
        y = random.randrange(500)
        snow_list.append([x, y])
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    screen.fill(BLACK)

    for item in snow_list:
        pygame.draw.circle(screen, WHITE, item, 2)
        item[1] += 1

        if item[1] > 500:
            item[1] = random.randrange(-20, -5)
            item[0] = random.randrange(700)
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
