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
y = 105

Cx = x
Cy = y

changeC = 0.5

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

  # sky color change
  SKY[2] += changeC
  if SKY[2] >= 145 or SKY[2] <= 89:
    changeC = changeC * -1

  # move alien
  y += 2
  if y > 550:
    y = Cy

  screen.fill(SKY)

  #ground + moon
  pygame.draw.rect(screen, GROUND, [0, 450, 700, 50])
  pygame.draw.circle(screen, WHITE, [550, 100], 25)
  pygame.draw.circle(screen, SKY, [545, 95], 20)

  #ufo :3
  pygame.draw.circle(screen, UFO_RED, [150, 120], 10)
  pygame.draw.circle(screen, UFO_RED, [350, 120], 10)
  
  #alien
  pygame.draw.ellipse(screen, ALIEN, [x, y, 35, 50], 0)
  pygame.draw.line(screen, ALIEN, [x - 15, y - 15], [x + 10, y + 5], 5)
  pygame.draw.line(screen, ALIEN, [x + 50, y - 15], [x + 20, y + 5], 5)
  pygame.draw.line(screen, ALIEN, [x + 16, y + 10], [x + 16, y + 100], 5)
  pygame.draw.line(screen, ALIEN, [x - 15, y + 35], [x + 15, y + 50], 5)
  pygame.draw.line(screen, ALIEN, [x + 50, y + 35], [x + 19, y + 50], 5)
  pygame.draw.line(screen, ALIEN, [x - 15, y + 135], [x + 15, y + 100], 5)
  pygame.draw.line(screen, ALIEN, [x + 50, y + 135], [x + 18, y + 100], 5)

  #ufo
  pygame.draw.ellipse(screen, UFO_GREY, [100, 100, 300, 150], 0)
  pygame.draw.ellipse(screen, UFO_BLUE, [175, 75, 150, 100], 0)

  pygame.draw.circle(screen, UFO_RED, [100, 175], 10)
  pygame.draw.circle(screen, UFO_RED, [400, 175], 10)
  pygame.draw.circle(screen, UFO_RED, [150, 230], 10)
  pygame.draw.circle(screen, UFO_RED, [350, 230], 10)
  pygame.draw.circle(screen, UFO_RED, [250, 250], 10)
  
  pygame.display.flip()

  clock.tick(144)

pygame.quit()
