import pygame
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

SCOTBLUE = (0, 94, 184)
TBROWN = (160, 95, 53)
TBODY = (75, 151, 75)

x = 100
y = 100

xT = 100
yT = 100

xSpeed = 0
ySpeed = 0

xTSpeed = 0
yTSpeed = 0

flipped = False

pygame.init()

def scotland(x, y):
  pygame.draw.rect(screen, SCOTBLUE, [x, y, 225, 150])
  pygame.draw.line(screen, WHITE, [x, y], [x+225, y+150], 35)
  pygame.draw.line(screen, WHITE, [x+225, y], [x, y+150], 35)
  
def turtleRight(xT, Yt):
  pygame.draw.ellipse(screen, TBODY, [xT-100, yT-15, 50, 30])
  pygame.draw.ellipse(screen, TBODY, [xT-50, yT+50, 30, 50])
  pygame.draw.ellipse(screen, TBODY, [xT+20, yT+50, 30, 50])
  pygame.draw.ellipse(screen, TBODY, [xT-50, yT-100, 30, 50])
  pygame.draw.ellipse(screen, TBODY, [xT+20, yT-100, 30, 50])
  pygame.draw.ellipse(screen, TBODY, [xT+35, yT-40, 100, 60])
  pygame.draw.circle(screen, TBROWN, [xT, yT], 75)
  
def turtleLeft(xT, yT):
  pygame.draw.ellipse(screen, TBODY, [xT+50, yT-15, 50, 30])
  pygame.draw.ellipse(screen, TBODY, [xT-50, yT+50, 30, 50])
  pygame.draw.ellipse(screen, TBODY, [xT+20, yT+50, 30, 50])
  pygame.draw.ellipse(screen, TBODY, [xT-50, yT-100, 30, 50])
  pygame.draw.ellipse(screen, TBODY, [xT+20, yT-100, 30, 50])
  pygame.draw.ellipse(screen, TBODY, [xT-130, yT-40, 100, 60])
  pygame.draw.circle(screen, TBROWN, [xT, yT], 75)

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
        xTSpeed = -3
        flipped = True
      if event.key == pygame.K_RIGHT:
        xTSpeed = 3
        flipped = False
      if event.key == pygame.K_UP:
        yTSpeed = -3
      if event.key == pygame.K_DOWN:
        yTSpeed = 3
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT:
        xTSpeed = 0
      if event.key == pygame.K_RIGHT:
        xTSpeed = 0
      if event.key == pygame.K_UP:
        yTSpeed = -0
      if event.key == pygame.K_DOWN:
        yTSpeed = 0
  pos = pygame.mouse.get_pos()
  x = pos[0] - 110
  y = pos[1] - 65
        
  xT += xTSpeed
  yT += yTSpeed

  screen.fill(WHITE)

  scotland(x, y)
  if not flipped:
    turtleRight(xT, yT)
  else:
    turtleLeft(xT, yT)
  
  pygame.display.flip()

  clock.tick(144)

pygame.quit()
