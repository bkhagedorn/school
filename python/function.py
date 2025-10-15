import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

DARK_GREEN = (39, 70, 45)
ALMOST_BLACK = (22, 29, 50)
TRANSPARENT = (236, 236, 236)

def drawWT(x, y):
  pygame.draw.polygon(screen, ALMOST_BLACK, [(x - 10, y), (x, y + 50), (x + 25, y + 50), (x + 25, y)])

  pygame.draw.rect(screen, ALMOST_BLACK, [x, y, 100, 175])
  pygame.draw.rect(screen, TRANSPARENT, [x + 10, y + 10, 80, 100])
  pygame.draw.rect(screen, DARK_GREEN, [x + 20, y + 20, 60, 80])

  pygame.draw.line(screen, BLACK, [x + 20, y + 125], [x + 80, y + 125], 5)
  pygame.draw.line(screen, BLACK, [x + 20, y + 135], [x + 80, y + 135], 5)
  pygame.draw.line(screen, BLACK, [x + 20, y + 145], [x + 80, y + 145], 5)

  pygame.draw.line(screen, ALMOST_BLACK, [x + 25, y - 50], [x + 25, y], 10)
  pygame.draw.rect(screen, ALMOST_BLACK, [x + 50, y - 10, 35, 10])

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

  drawWT(100, 50)
  drawWT(500, 50)
  drawWT(300, 175)
  drawWT(300, 425)
  
  pygame.display.flip()

  clock.tick(144)

pygame.quit()
