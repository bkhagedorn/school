import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

done = False

clock = pygame.time.Clock()

y = 450

yS = 0

font = pygame.font.SysFont("comicsansms", 10, False, False)

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        yS = 1

  y -= yS
  if y <= 700:
    yS = 0
  if yS > 0:
    yS -= 0.01

  text = font.render("SPEED: " + str(yS), False, BLACK)
  
  screen.fill(WHITE)

  screen.blit(text, [0, 487.5])

  pygame.draw.rect(screen, BLACK, [300, y, 50, 50])
  
  pygame.display.flip()

  clock.tick(144)

pygame.quit()
