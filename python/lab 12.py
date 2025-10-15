import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

class Rectangle():
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def draw_red_rect(self):
    pygame.draw.rect(screen, RED, [self.x, self.y, 100, 50])

  def draw_blue_square(self):
    pygame.draw.rect(screen, BLUE, [self.x, self.y, 30, 30])

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

done = False

clock = pygame.time.Clock()

obj_1 = Rectangle(100, 100)
obj_2 = Rectangle(300, 400)

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

  screen.fill(WHITE)
  
  obj_1.draw_red_rect()
  obj_1.draw_blue_square()
  obj_2.draw_red_rect()
  obj_2.draw_blue_square()
  
  pygame.display.flip()

  clock.tick(144)

pygame.quit()
