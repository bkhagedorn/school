# brayden hagedorn 1-16-24
# snowman function - together

import pygame
import random

def drawSnowman(defX):
  pygame.draw.circle(screen, WHITE, [defX, 450], 75)
  pygame.draw.circle(screen, WHITE, [defX, 350], 50)
  pygame.draw.circle(screen, WHITE, [defX, 285], 35)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (128, 187, 219)

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

  screen.fill(BLUE)

  drawSnowman(350)
  drawSnowman(100)
  drawSnowman(600)

  pygame.display.flip()

  clock.tick(144)

pygame.quit()
