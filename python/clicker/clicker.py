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

clock = pygame.time.Clock()

#Variables
countNum = 0
mult = 0
helper = False
price = 10
priceMult = 1
upMult = 1
upPrice = 100
upPriceMult = 1
critPrice = 1000
critPriceMult = 1
scale = 100
x = 325
y = 175
chance = 100
roll = None
critted = False
cAlpha = 255
helperS = 1000
helperSPrice = 1500
helperSMult = 1


#Text
font = pygame.font.SysFont("comicsansms", 25, False, False)
count = font.render("Count: " + str(countNum), False, BLACK)
help = font.render("Z: Helper (" + str(round(price ** priceMult)) + ") " + str(mult), False, BLACK)
upgrade = font.render("X: Click Upgrade (" + str(round(upPrice ** upPriceMult)) + ") " + str(upMult), False, BLACK)
crit = font.render("CRIT!", False, RED)
luck = font.render("C: Luck (" + str(round((critPrice ** critPriceMult))) + ") " + str(int((1/chance) * 100)) + "%", False, BLACK)
speed = font.render("V: Helper Speed (" + str(round((helperSPrice ** helperSMult))) + ") " + str(helperS), False, BLACK)

#Sound/Music
pygame.mixer.music.load("SO_rout1nes.ogg")
pygame.mixer.music.set_volume(0.5)
sound = pygame.mixer.Sound("crit.ogg")

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    #Click
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1:
        countNum += 1 * upMult
        scale = 75 #scales down square
        x = 337.5
        y = 187.5
        pygame.time.set_timer(pygame.USEREVENT + 1, 100)
        roll = random.randrange(chance)
        print("Rolled " + str(roll))
        if roll == 0:
          countNum += (1 * upMult) * 100
          print("CRIT!")
          critted = True
          sound.play()
    #Helper stuff
    if event.type == pygame.USEREVENT:
      countNum += 1 * mult
    if event.type == pygame.USEREVENT + 1:
      scale = 100 #scale up square
      x = 325
      y = 175
    if event.type == pygame.KEYDOWN:
      #Helper
      if event.key == pygame.K_z:
        if countNum >= price ** priceMult:
          if helper:
            mult += 1
          else:
            pygame.time.set_timer(pygame.USEREVENT, helperS)
            helper = True
            mult = 1
          countNum -= price ** priceMult
          priceMult += 0.125
          print("User bought helper!")
        else:
          print("User doesn't have enough money")
      #Upgrade
      if event.key == pygame.K_x:
        if countNum >= upPrice ** upPriceMult:
          upMult += 1
          countNum -= upPrice ** upPriceMult
          upPriceMult += 0.15
          print("User bought upgrade!")
        else:
          print("User doesn't have enough money")
      #Crit chance
      if event.key == pygame.K_c:
        if countNum >= critPrice ** critPriceMult:
          if chance > 10:
            countNum -= critPrice ** critPriceMult
            chance -= 5
            critPriceMult += 0.05
            print("User increased luck!")
        else:
          print("User doesn't have enough money")
      #Helper speed
      if event.key == pygame.K_v:
        if countNum >= helperSPrice ** helperSMult:
          if helperS > 100:
            countNum -= helperSPrice ** helperSMult
            helperS -= 100
            helperSMult += 0.1
            pygame.time.set_timer(pygame.USEREVENT, helperS)
        
        
          
  #Updating text
  count = font.render("Count: " + str(round(countNum)), False, BLACK)
  help = font.render("Z: Helper (" + str(round(price ** priceMult)) + ") " + str(mult), False, BLACK)
  upgrade = font.render("X: Click Upgrade (" + str(round(upPrice ** upPriceMult)) + ") " + str(upMult), False, BLACK)
  luck = font.render("C: Luck (" + str(round((critPrice ** critPriceMult))) + ") 1/" + str(chance), False, BLACK)
  speed = font.render("V: Helper Speed (" + str(round((helperSPrice ** helperSMult))) + ") " + str(helperS), False, BLACK)
    
  screen.fill(WHITE)
  
  pygame.draw.rect(screen, BLACK, [x, y, scale, scale])
  
  screen.blit(count, [0, 0])
  screen.blit(help, [0, 380])
  screen.blit(upgrade, [0, 410])
  screen.blit(luck, [0, 440])
  screen.blit(speed, [0, 470])
  if critted:
    screen.blit(crit, [625, 0])
    cAlpha -= 2
    crit.set_alpha(cAlpha)
    if cAlpha <= 0:
      critted = False
      cAlpha = 255
  
  pygame.display.flip()

  clock.tick(144)

pygame.quit()
