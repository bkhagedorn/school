import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (245, 205, 48)

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

sounded = False
countNum = 0

font = pygame.font.SysFont("comicsansms", 40, False, False)
font2 = pygame.font.SysFont("comicsansms", 25, False, False)
font3 = pygame.font.SysFont("comicsansms", 65, False, False)
title = font.render("CLICK OR DIE!!!!!!!!!", False, WHITE)
text = font2.render("Press E to play a sound", False, WHITE)
count = font2.render("Count: " + str(countNum), False, WHITE)
win = font3.render("YOU WIN", False, YELLOW)

bg = pygame.image.load("download.jfif").convert()
bg = pygame.transform.scale(bg, [700, 500])

sound = pygame.mixer.Sound("goofy.ogg")

done = False

clock = pygame.time.Clock()

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_e:
        if not sounded:
          sound.play()
          sounded = True
    if event.type == pygame.MOUSEBUTTONDOWN:
      if countNum < 10:
        countNum += 1
        count = font2.render("Count: " + str(countNum), False, WHITE)

  screen.fill(WHITE)

  screen.blit(bg, [0, 0])
  if countNum < 10:
    screen.blit(title, [175, 100])
  else:
    screen.blit(win, [205, 100])
  if not sounded:
    screen.blit(text, [0, 35])
  screen.blit(count, [0, 0])
  
  pygame.display.flip()

  clock.tick(144)

pygame.quit()
