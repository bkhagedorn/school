import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
screen2 = pygame.display.set_mode(size)

homeScreen = True
soundPlayed = False

pygame.display.set_caption("My Game")

done = False

clock = pygame.time.Clock()

bg = pygame.image.load("bg.jpg").convert()
bg = pygame.transform.scale(bg, [700, 500])

bg2 = pygame.image.load("download.jfif").convert()
bg2 = pygame.transform.scale(bg2, [700, 500])

jonesy = pygame.image.load("jonesy.png").convert()
jonesy.set_colorkey(BLACK)

spitfire = pygame.image.load("idk.png").convert()
spitfire.set_colorkey(BLACK)

logo = pygame.image.load("logo.png").convert()
logo = pygame.transform.scale(logo, [600, 400])
logo.set_colorkey(WHITE)

score = 0

font = pygame.font.SysFont("comicsansms", 25, False, False)
font2 = pygame.font.SysFont("comicsansms", 35, False, False)
text1 = font.render("Score: " + str(score), False, WHITE)
text2 = font.render("Lives: 3", False, WHITE)
text3 = font2.render("Click to start", False, BLACK)
text4 = font.render("Press E to play a sound", False, BLACK)

goofy = pygame.mixer.Sound("goofy.ogg")

x = 100
y = 300
x2 = 350
y2 = 300

xS = 0
yS = 0
x2S = 0
y2S = 0

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        xS = -3
      if event.key == pygame.K_RIGHT:
        xS = 3
      if event.key == pygame.K_UP:
        yS = -3
      if event.key == pygame.K_DOWN:
        yS = 3
      if event.key == pygame.K_a:
        x2S = -3
      if event.key == pygame.K_d:
        x2S = 3
      if event.key == pygame.K_w:
        y2S = -3
      if event.key == pygame.K_s:
        y2S = 3
      if event.key == pygame.K_e:
        if not homeScreen and not soundPlayed:
          goofy.play()
          soundPlayed = True
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT:
        xS = 0
      if event.key == pygame.K_RIGHT:
        xS = 0
      if event.key == pygame.K_UP:
        yS = 0
      if event.key == pygame.K_DOWN:
        yS = 0
      if event.key == pygame.K_a:
        x2S = 0
      if event.key == pygame.K_d:
        x2S = 0
      if event.key == pygame.K_w:
        y2S = 0
      if event.key == pygame.K_s:
        y2S = 0
    if event.type == pygame.MOUSEBUTTONDOWN:
      homeScreen = False
        
  x += x2S
  y += y2S
  x2 += xS
  y2 += yS

  if homeScreen:
    screen.fill(WHITE)

    screen.blit(bg, [0, 0])
    screen.blit(logo, [50, -100])

    screen.blit(text3, [235, 200])

  else:
    screen2.fill(BLACK)

    screen2.blit(bg2, [0, 0])

    screen2.blit(jonesy, [x, y])
    screen2.blit(spitfire, [x2, y2])

    screen2.blit(text1, [5, 435])
    screen2.blit(text2, [5, 465])

    if not soundPlayed:
      screen2.blit(text4, [0, 0])
  
  pygame.display.flip()

  clock.tick(144)

pygame.quit()
