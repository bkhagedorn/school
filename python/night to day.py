import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

sky = [0, 0, 50] #128, 187, 219
ground = [0, 50, 0] #40, 127, 71
MOON = (200, 200, 200)
SUN = (245, 205, 48)

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

done = False

clock = pygame.time.Clock()

# x N y values
moonX = 500
moonY = 100

sunX = 300
sunY = 600
sunR = 10 # radius :3333

# change values
change1 = 1
change2 = 2
change3 = 1/7


while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

  moonX += change1
  moonY += change2

  sunX -= change1
  sunY -= change2
  sunR += change3

  if sky[0] <= 128:
    sky[0] += 0.65
  if sky[1] <= 187:
    sky[1] += 0.65
  if sky[2] <= 219:
    sky[2] += 0.65

  if ground[0] <= 75:
    ground[0] += 0.35
  if ground[1] <= 175:
    ground[1] += 0.5
  if ground[2] <= 100:
    ground[2] += 0.4

  if sunX <= 15:
    change1 = 0
  if sunY <= 25:
    change2 = 0

  #D;
  if sunR >= 50:
    change3 = 0

  screen.fill(sky)

  # drawing stuff
  pygame.draw.circle(screen, MOON, [moonX, moonY], 15)
  pygame.draw.circle(screen, SUN, [sunX, sunY], round(sunR)) #wtf
  pygame.draw.rect(screen, ground, [0, 450, 700, 500])

  pygame.display.flip()

  clock.tick(60)

pygame.quit()
