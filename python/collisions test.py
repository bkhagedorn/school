import pygame

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
x = 150
y = 200
xS = 0
yS = 0

clock = pygame.time.Clock()

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        xS = -3
      if event.key == pygame.K_RIGHT:
        xS = 3
      if event.key == pygame.K_DOWN:
        yS = 3
      if event.key == pygame.K_UP:
        yS = -3
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT:
        xS = 0
      if event.key == pygame.K_RIGHT:
        xS = 0
      if event.key == pygame.K_DOWN:
        yS = 0
      if event.key == pygame.K_UP:
        yS = 0

  x += xS
  y += yS
  test = pygame.Rect(x, y, 50, 50)
  test2 = pygame.Rect(500, 200, 50, 50)

  if pygame.Rect.colliderect(test, test2) == True:
    if xS > 0:
      test.right = test2.left
      xS = 0
    if xS < 0:
      test.left = test2.right
      xS = 0
    if yS < 0:
      test.top = test2.bottom
      yS = 0
    if yS > 0:
      test.bottom = test2.top
      yS = 0

  screen.fill(WHITE)

  pygame.draw.rect(screen, BLACK, test)
  pygame.draw.rect(screen, BLACK, test2)
    
  pygame.display.flip()

  clock.tick(144)

pygame.quit()
