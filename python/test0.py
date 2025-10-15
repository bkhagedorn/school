import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

def drawItem(x, y):
  pygame.draw.rect(screen, BLACK, [x, y, 100, 50])
  pygame.draw.rect(screen, BLACK, [x+50, y+50, 100, 50])
  pygame.draw.rect(screen, BLACK, [x-50, y-50, 100, 50])

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

  drawItem(100, 75)
  drawItem(200, 50)
  drawItem(472, 276)
  
  pygame.display.flip()

  clock.tick(144)

pygame.quit()
