import pygame
import random

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

all_sprite_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()
car_list = pygame.sprite.Group()
dead_list = pygame.sprite.Group()

class Frog(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("frog.png")
    self.image = pygame.transform.scale_by(self.image, (0.25, 0.25))
    self.image = pygame.transform.rotate(self.image, -180)
    self.rect = self.image.get_rect()
    self.direction = "down"

  def reset(self):
    if self.direction == "left":
      self.image = pygame.transform.rotate(self.image, -180)
    if self.direction == "down":
      self.image = pygame.transform.rotate(self.image, 90)
    if self.direction == "up":
      self.image = pygame.transform.rotate(self.image, -90)

  def lookLeft(self):
    self.reset()
    self.image = pygame.transform.rotate(self.image, 180)
    self.direction = "left"

  def lookRight(self):
    self.reset()
    self.direction = "right"

  def lookUp(self):
    self.reset()
    self.image = pygame.transform.rotate(self.image, 90)
    self.direction = "up"

  def lookDown(self):
    self.reset()
    self.image = pygame.transform.rotate(self.image, -90)
    self.direction = "down"

class Car(pygame.sprite.Sprite):
  def __init__(self, x):
    super().__init__()
    self.image = pygame.image.load("car.png")
    self.image = pygame.transform.scale_by(self.image, (0.25, 0.25))
    self.image = pygame.transform.flip(self.image, True, False)
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = random.randrange(135, 450)

  def update(self):
    self.rect.x -= 2
    
  def blowup(self):
    self.kill()

player = Frog()
all_sprite_list.add(player)
player_list.add(player)
player.rect.x = 300
player.rect.y = 75

count = 800
for i in range(10): 
  car = Car(count)
  all_sprite_list.add(car)
  car_list.add(car)
  count += 150

bg = pygame.image.load("background.png")
bg = pygame.transform.scale(bg, (700, 900))

clock = pygame.time.Clock()

font = pygame.font.SysFont("comicsansms", 50, False)
font2 = pygame.font.SysFont("comicsansms", 100, False)

move = 25
alive = True
win = False
while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    if event.type == pygame.KEYDOWN:
      if alive and not win:
        if event.key == pygame.K_LEFT:
          if player.rect.x > 0:
            player.rect.x -= move
          player.lookLeft()
        if event.key == pygame.K_RIGHT:
          if player.rect.x < 650:
            player.rect.x += move
          player.lookRight()
        if event.key == pygame.K_UP:
          if player.rect.y > 75:
            player.rect.y -= move
          player.lookUp()
        if event.key == pygame.K_DOWN:
          player.rect.y += move
          player.lookDown()
  if alive and not win:
    car_list.update()

  if player in dead_list:
    alive = False

  if player.rect.y > 450:
    win = True

  if not win:
    for i in car_list:
      if i.rect.x < -100:
        car_list.remove(i)
    for i in range(10 - len(car_list.sprites())):
      car = Car(car_list.sprites()[-1].rect.x + 150)
      all_sprite_list.add(car)
      car_list.add(car)

  text2 = font2.render("Game Over", False, False)
  text3 = font2.render("You win!", False, False)

  dead_list = pygame.sprite.groupcollide(player_list, car_list, False, False)

  if not alive:
    all_sprite_list.empty()
  if win:
    all_sprite_list.empty()
    all_sprite_list.add(player)

  screen.fill(WHITE)

  screen.blit(bg, [0, -350])
  all_sprite_list.draw(screen)
  if not alive:
    screen.blit(text2, [85, 175])
  if win:
    screen.blit(text3, [150, 175])
  
  pygame.display.flip()

  clock.tick(144)

pygame.quit()