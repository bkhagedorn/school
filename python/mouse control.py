import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

SKY = [0, 0, 89]
ALIEN = (177, 229, 166)
UFO_GREY = (109, 110, 108)
UFO_BLUE = (123, 182, 232)
UFO_RED = (255, 87, 51)
GROUND = (0, 100, 0)

x = 235

changeC = 0.5

pygame.init()

def alien(x, y):
  pygame.draw.ellipse(screen, ALIEN, [x, y, 35, 50], 0)
  pygame.draw.line(screen, ALIEN, [x - 15, y - 15], [x + 10, y + 5], 5)
  pygame.draw.line(screen, ALIEN, [x + 50, y - 15], [x + 20, y + 5], 5)
  pygame.draw.line(screen, ALIEN, [x + 16, y + 10], [x + 16, y + 100], 5)
  pygame.draw.line(screen, ALIEN, [x - 15, y + 35], [x + 15, y + 50], 5)
  pygame.draw.line(screen, ALIEN, [x + 50, y + 35], [x + 19, y + 50], 5)
  pygame.draw.line(screen, ALIEN, [x - 15, y + 135], [x + 15, y + 100], 5)
  pygame.draw.line(screen, ALIEN, [x + 50, y + 135], [x + 18, y + 100], 5)
  pygame.display.flip()


size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

done = False

clock = pygame.time.Clock()
pygame.mouse.set_visible(0)

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

  pos = pygame.mouse.get_pos()
  x = pos[0]
  y = pos[1]

  # sky color change
  SKY[2] += changeC
  if SKY[2] >= 145 or SKY[2] <= 89:
    changeC = changeC * -1

  screen.fill(SKY)

  alien(x - 15, y)
  
  clock.tick(144)

pygame.quit()
