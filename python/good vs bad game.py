import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (180, 210, 228)
BRIGHT_VIOLET = (107, 50, 124)

class Obj(pygame.sprite.Sprite):
  def __init__(self, color, w, h):
    super().__init__()
    self.image = pygame.Surface([w,h])
    self.image.fill(color)
    self.rect = self.image.get_rect()

  def move(self, direction):
    if direction == "+":
      self.rect.x += 2
    if direction == "-":
      self.rect.x -= 1
      
pygame.init()

all_sprites_list = pygame.sprite.Group()
bullets = pygame.sprite.Group()
baddies = pygame.sprite.Group()
player = pygame.sprite.GroupSingle()

good = Obj(LIGHT_BLUE, 50, 50)
good.rect.x = 100
good.rect.y = 200
all_sprites_list.add(good)
player.add(good)
for i in range(20):
  bad = Obj(BRIGHT_VIOLET, 35, 35)
  bad.rect.y = random.randrange(0, 450)
  bad.rect.x = (i * 250) + 750
  all_sprites_list.add(bad)
  baddies.add(bad)
  
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

done = False

clock = pygame.time.Clock()

score = 0
y_up = 0
y_down = 0

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        bullet = Obj(LIGHT_BLUE, 10, 10)
        bullet.rect.x = 150
        bullet.rect.y = good.rect.y + 22.5
        all_sprites_list.add(bullet)
        bullets.add(bullet)
      if event.key == pygame.K_UP:
        y_up -= 2
      if event.key == pygame.K_DOWN:
        y_down += 2
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_UP:
        y_up = 0
      if event.key == pygame.K_DOWN:
        y_down = 0
  if good.rect.y > 0:
    good.rect.y += y_up
  if good.rect.y < 450:
    good.rect.y += y_down

  for i in bullets:
    i.move("+")  
    if i.rect.x > 800:
      bullets.remove(i)

  for i in baddies:
    i.move("-")
    for i in range(20 - len(baddies)):
      bad = Obj(BRIGHT_VIOLET, 35, 35)
      bad.rect.y = random.randrange(0, 450)
      bad.rect.x = baddies[-1].rect.x + 150
      all_sprites_list.add(bad)
      baddies.add(bad)

  collisions = pygame.sprite.groupcollide(baddies, player, False, True)
  collisions = pygame.sprite.groupcollide(bullets, baddies, True, True)
    
  screen.fill(WHITE)

  all_sprites_list.draw(screen)
    
  pygame.display.flip()

  clock.tick(144)

pygame.quit()
