import pygame
import random

# Grass values
heights = [15, 25]
grassx = -10
grassHeight = 0
awesomeGrassValue = 75

# Cloud values
cloudx = 0
cloudy = 0
cloudWidth = 0
awesomeCloudValue = 10

# Flower values
flowerx = 0
flowery = 0
awesomeFlowerValue = 5

# draw grass
def grass(grassx,grassHeight):
    if grassHeight>30:
      grassHeight=30
    elif grassHeight<10:
      grassHeight=10
    pygame.draw.polygon(screen, GREEN, ([grassx,500], [grassx+5, 500-grassHeight], [grassx+10,500]))

# draw cloud
def cloud(cloudx, cloudy, cloudWidth):
    if cloudy>200:
      cloudy=200
    if cloudWidth>400:
      cloudWidth=400
    pygame.draw.ellipse(screen, WHITE, [cloudx, cloudy, cloudWidth, 70])  

# draw flower
def flower(flowerx, flowery):
  if flowery<300:
        flowery=300
  elif flowery>450:
        flowery=450
  pygame.draw.line(screen, GREEN, [flowerx, 500], [flowerx, flowery], 5) 
  pygame.draw.circle(screen, ORANGE, [flowerx, flowery], 20)
  pygame.draw.circle(screen, YELLOW, [flowerx, flowery], 5)
  pygame.draw.line(screen, GREEN, [flowerx, flowery+40], [flowerx+10, flowery+30],5)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (75, 214, 140)
BLUE = (137, 215, 232)
YELLOW = (237, 229, 109)
ORANGE=(240, 157, 70)

pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
done = False
clock = pygame.time.Clock()

grassXL = []
grassHL = []
for i in range(awesomeGrassValue):
  grassx += 10
  grassHeight = random.choice(heights)
  grassXL.append(grassx)
  grassHL.append(grassHeight)

cloudXL = []
cloudYL = []
cloudHL = []
for i in range(awesomeCloudValue):
  cloudx = random.randrange(0, 700)
  cloudy = random.randrange(0, 200)
  cloudHeight = random.randrange(100, 300)
  cloudXL.append(cloudx)
  cloudYL.append(cloudy)
  cloudHL.append(cloudHeight)

flowerXL = []
flowerYL = []
for i in range(awesomeFlowerValue):
  flowerx += 120
  flowery = random.randrange(300, 375)
  flowerXL.append(flowerx)
  flowerYL.append(flowery)

#indent the lines in the main game loop AFTER you have pasted it into python.
while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
  screen.fill(BLUE)

  for i in range(awesomeGrassValue):
    grass(grassXL[i], grassHL[i])

  for i in range(awesomeCloudValue):
    cloud(cloudXL[i], cloudYL[i], cloudHL[i])

  for i in range(awesomeFlowerValue):
    flower(flowerXL[i], flowerYL[i])

  pygame.display.flip()
  clock.tick(60)
pygame.quit()
