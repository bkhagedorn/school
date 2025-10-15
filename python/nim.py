import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

size = (500, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

done = False

clock = pygame.time.Clock()

nimrods = [[230, 20, 20, 50]]

for i in range(2):
  for x in range(i * 2):
    nimrods.append([230 - (30 * x), 20 + (50 * x), 20, 50])

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

  screen.fill(WHITE)

  for i in nimrods:
    pygame.draw.rect(screen, BLACK, i)
  
  pygame.display.flip()

  clock.tick(60)
  
pygame.quit()
