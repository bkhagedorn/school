# brayden hagedorn 1-16-24
# snowman function - together

import pygame
import random

x = 350
y = 350

xSpeed = 0
ySpeed = 0

def drawSnowman(x, y):
  pygame.draw.circle(screen, WHITE, [x, y + 100], 75)
  pygame.draw.circle(screen, WHITE, [x, y], 50)
  pygame.draw.circle(screen, WHITE, [x, y - 65], 35)

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
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        xSpeed = -3
      if event.key == pygame.K_RIGHT:
        xSpeed = 3
      if event.key == pygame.K_UP:
        ySpeed = -3
      if event.key == pygame.K_DOWN:
        ySpeed = 3
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT:
        xSpeed = 0
      if event.key == pygame.K_RIGHT:
        xSpeed = 0
      if event.key == pygame.K_UP:
        ySpeed = 0
      if event.key == pygame.K_DOWN:
        ySpeed = 0

  x += xSpeed
  y += ySpeed

  screen.fill(BLUE)

  drawSnowman(x, y)

  pygame.display.flip()

  clock.tick(144)

pygame.quit()
