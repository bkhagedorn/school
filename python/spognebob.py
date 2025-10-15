import pygame

BLACK = (0, 0, 0) 
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 87, 51)
BLUE = (13, 105, 172)

SKY = (128, 187, 219)
YELLOW = (249, 214, 46)
NOT_YELLOW = (180, 132, 85)
IDK = (176, 142, 68)
ROYAL = (108, 129, 183)
P = (217, 133, 108)
SAND = (249, 233, 153)
ROAD = (27, 42, 53)
A = (255, 176, 0)
MOAI = (0, 32, 96)
DARK_RED = (201, 70, 42)

offset1 = 10
offset2 = 15
offset3 = 3
offset4 = 5
finaloffset = 50

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("spunglebottom")

done = False

clock = pygame.time.Clock()

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

  screen.fill(SKY)

  pygame.draw.ellipse(screen, A, [550, -250, 600, 800])
  pygame.draw.rect(screen, MOAI, [-150, -150, 300, 1000])

  pygame.draw.rect(screen, SAND, [0, 350, 700, 150])
  pygame.draw.rect(screen, ROAD, [0, 450, 700, 150])

  pygame.draw.rect(screen, YELLOW, [237.5 + finaloffset, 365, 10, 50])
  pygame.draw.rect(screen, YELLOW, [342.5 + offset1 + finaloffset, 365, 10, 50])
  pygame.draw.rect(screen, WHITE, [237.5 + finaloffset, 390, 10, 25])
  pygame.draw.rect(screen, WHITE, [342.5 + offset1 + finaloffset, 390, 10, 25])
  pygame.draw.rect(screen, BLUE, [237.5 + finaloffset, 395, 10, 5])
  pygame.draw.rect(screen, BLUE, [342.5 + offset1 + finaloffset, 395, 10, 5])
  pygame.draw.rect(screen, RED, [237.5 + finaloffset, 405, 10, 5])
  pygame.draw.rect(screen, RED, [342.5 + offset1 + finaloffset, 405, 10, 5])

  pygame.draw.rect(screen, BLACK, [215 + finaloffset, 415, 32.5, 10])
  pygame.draw.rect(screen, BLACK, [342.5 + finaloffset + offset1, 415, 32.5, 10])

  pygame.draw.rect(screen, NOT_YELLOW, [225 + finaloffset, 350, 35, 15])
  pygame.draw.rect(screen, NOT_YELLOW, [330 + finaloffset + offset1, 350, 35, 15])

  pygame.draw.rect(screen, YELLOW, [186.5 + finaloffset, 270, 10, 50])
  pygame.draw.rect(screen, YELLOW, [405 + finaloffset, 270, 10, 50])
  pygame.draw.rect(screen, YELLOW, [180 + finaloffset, 320, 20, 20])
  pygame.draw.rect(screen, YELLOW, [400 + finaloffset, 320, 20, 20])

  pygame.draw.ellipse(screen, WHITE, [180 + finaloffset, 250, 20, 15])
  pygame.draw.rect(screen, WHITE, [180 + finaloffset, 255, 20, 25])
  pygame.draw.ellipse(screen, WHITE, [400 + finaloffset, 250, 20, 15])
  pygame.draw.rect(screen, WHITE, [400 + finaloffset, 255, 20, 25])

  pygame.draw.rect(screen, YELLOW, [200 + finaloffset, 100, 200, 250])
  pygame.draw.rect(screen, WHITE, [200 + finaloffset, 275, 200, 25])
  pygame.draw.rect(screen, NOT_YELLOW, [200 + finaloffset, 300, 200, 50])

  pygame.draw.circle(screen, IDK, [240 + finaloffset, 125], 15)
  pygame.draw.circle(screen, IDK, [250 + finaloffset, 250], 13)
  pygame.draw.circle(screen, IDK, [365 + finaloffset, 135], 13)
  pygame.draw.circle(screen, IDK, [350 + finaloffset, 220], 15)
  pygame.draw.circle(screen, IDK, [260 + finaloffset, 155], 8)
  pygame.draw.circle(screen, IDK, [235 + finaloffset, 225], 8)
  pygame.draw.circle(screen, IDK, [375 + finaloffset, 255], 8)

  pygame.draw.rect(screen, BLACK, [210 + finaloffset + offset2, 310, 30, 10])
  pygame.draw.rect(screen, BLACK, [250 + finaloffset + offset2, 310, 30, 10])
  pygame.draw.rect(screen, BLACK, [290 + finaloffset + offset2, 310, 30, 10])
  pygame.draw.rect(screen, BLACK, [330 + finaloffset + offset2, 310, 30, 10]) 

  pygame.draw.line(screen, BLACK, [220  + finaloffset+ offset1, 275], [250 + finaloffset + offset1, 290], 2)
  pygame.draw.line(screen, BLACK, [250 + finaloffset + offset1, 290], [270 + finaloffset + offset1, 275], 2)
  pygame.draw.line(screen, BLACK, [310 + finaloffset + offset1, 275], [330 + finaloffset + offset1, 290], 2)
  pygame.draw.line(screen, BLACK, [330 + finaloffset + offset1, 290], [360 + finaloffset + offset1, 275], 2)
  pygame.draw.polygon(screen, DARK_RED, ([330, 275], [340, 290], [360, 290],[370, 275]))
  pygame.draw.polygon(screen, RED, ([340, 290], [335, 310], [350, 335], [365, 310], [360, 290]))

  pygame.draw.rect(screen, BLACK, [265 + finaloffset - offset3, 125, 5, 25])
  pygame.draw.rect(screen, BLACK, [250 + finaloffset- offset3, 132.5, 5, 25])
  pygame.draw.rect(screen, BLACK, [280 + finaloffset- offset3, 132.5, 5, 25])

  pygame.draw.rect(screen, BLACK, [335 + finaloffset - offset3, 125, 5, 25])
  pygame.draw.rect(screen, BLACK, [320 + finaloffset - offset3, 132.5, 5, 25])
  pygame.draw.rect(screen, BLACK, [350  + finaloffset- offset3, 132.5, 5, 25])

  pygame.draw.circle(screen, WHITE, [265 + finaloffset, 165], 30)
  pygame.draw.circle(screen, WHITE, [335 + finaloffset, 165], 30)
  pygame.draw.circle(screen, ROYAL, [270 + finaloffset, 165], 15)
  pygame.draw.circle(screen, ROYAL, [330 + finaloffset, 165], 15)
  pygame.draw.circle(screen, BLACK, [270 + finaloffset, 165], 9)
  pygame.draw.circle(screen, BLACK, [330 + finaloffset, 165], 9)

  pygame.draw.circle(screen, BLACK, [340 + finaloffset, 203], 10, 5)

  pygame.draw.rect(screen, YELLOW, [290 + finaloffset, 195, 50, 15])

  pygame.draw.line(screen, BLACK, [290 + finaloffset, 195], [340 + finaloffset, 195], 5)
  pygame.draw.line(screen, BLACK, [290 + finaloffset, 210], [340 + finaloffset, 210], 5)

  pygame.draw.rect(screen, WHITE, [285 + finaloffset, 235, 10, 10])
  pygame.draw.rect(screen, WHITE, [300 + finaloffset, 235, 10, 10])

  pygame.draw.line(screen, BLACK, [260 + finaloffset, 225], [275 + finaloffset, 235], 5)
  pygame.draw.line(screen, BLACK, [275 + finaloffset, 235], [325 + finaloffset, 235], 5)

  pygame.draw.line(screen, P, [285 + finaloffset, 255], [310 + finaloffset, 255], 5)

  pygame.draw.rect(screen, BLACK, [285 + finaloffset, 25, 30, 15])
  pygame.draw.rect(screen, WHITE, [280 + finaloffset, 30, 40, 50])
  pygame.draw.rect(screen, BLACK, [280 + finaloffset, 80, 40, 15])
  pygame.draw.rect(screen, BLUE, [275 + finaloffset, 85, 50, 20])

  pygame.draw.line(screen, BLUE, [300 + finaloffset, 50 - offset4], [300 + finaloffset, 75 - offset4], 3)
  pygame.draw.line(screen, BLUE, [290 + finaloffset, 55 - offset4], [310 + finaloffset, 55 - offset4], 3)
  pygame.draw.line(screen, BLUE, [300 + finaloffset, 70 - offset4], [310 + finaloffset, 65 - offset4], 3)
  pygame.draw.line(screen, BLUE, [300 + finaloffset, 70 - offset4], [290 + finaloffset, 65 - offset4], 3)
  pygame.draw.circle(screen, BLUE, [300 + finaloffset, 46 - offset4], 5, 3)

  pygame.display.flip()

  clock.tick(60)

pygame.quit()
