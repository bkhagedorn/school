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

class Ball:
  def __init__(self):
    #Ball position
    self.x = 0
    self.y = 0

    #Ball's vector
    self.change_x = 0
    self.change_y = 0

    #Ball size
    self.size = 10

    #Ball color
    self.color = [255, 255, 255]

  def move(self):
    self.x += self.change_x
    self.y += self.change_y

  def draw(self):
    pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)

volleyball = Ball()
volleyball.change_x = 2
volleyball.change_y = 1

beach = Ball()
beach.color = [13, 105, 172]
beach.size = 20
beach.change_x = 1
beach.change_y = 2

sun = Ball()
sun.color = [245, 205, 48]
sun.size = 200

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

  screen.fill(BLACK)

  volleyball.draw()
  volleyball.move()
  beach.draw()
  beach.move()
  sun.draw()
  
  pygame.display.flip()

  clock.tick(144)

pygame.quit()
