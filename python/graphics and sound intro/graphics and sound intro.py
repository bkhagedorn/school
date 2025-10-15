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

back = pygame.image.load("NAHS.jpg").convert()
back = pygame.transform.scale(back, [700,500])

dog = pygame.image.load("bulldog.png").convert()
dog = pygame.transform.scale(dog, [200, 150])
dog.set_colorkey(BLACK)

moly = pygame.image.load("holy moly.jpg").convert()
moly = pygame.transform.scale(moly, [200, 200])

sound = pygame.mixer.Sound("magic.ogg")

font = pygame.font.SysFont('comicsansms', 25, False, False)
text = font.render('dog', False, BLACK)

pygame.mouse.set_visible(False)
while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    if event.type == pygame.MOUSEBUTTONDOWN:
      sound.play()

  pos = pygame.mouse.get_pos()
  x = pos[0] - 100
  y = pos[1] - 100

  #screen.fill(WHITE)
  screen.blit(back, [0, 0])
  screen.blit(moly, [300, 100])
  screen.blit(dog, [x, y])
  screen.blit(text, [x, y])
  
  pygame.display.flip()

  clock.tick(144)

pygame.quit()
