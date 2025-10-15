#Brayden Hagedorn
#5/24/24
#Computer Science I
#New Albany High School

'''
TO-DO LIST!!!!!!!!!!!!!!

1. Win screen // DONE
2. Menu screen // DONE
3. Tweak the ai to be a little more fair // DONE
4. Randomize ball path at start // done? kinda
5. Give the ball better physics
'''
import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LESS_WHITE = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

#variables
scoreP1 = 0
scoreP2 = 0
start = False
showIns = True
win = 0
screens = 0
x, y = 50, 200
ballX, ballY = 332, 225
com = True #paddle1 is either controlled by a computer or someone else
comSpeed = 0.85
test = False

#fonts
font = pygame.font.SysFont("mscomicsans", 50)
font2 = pygame.font.SysFont("mscomicsans", 75)

#classes
class Ball(pygame.sprite.Sprite):
  def __init__(self, w, h):
    super().__init__()
    self.image = pygame.Surface([w, h])
    self.image.fill(WHITE)
    self.rect = self.image.get_rect()
    self.speedX = 1.5
    self.speedY = 1

class Paddle(pygame.sprite.Sprite):
  def __init__(self, w, h):
    super().__init__()
    self.image = pygame.Surface([w, h])
    self.image.fill(WHITE)
    self.rect = self.image.get_rect()
    self.speedUp = 0
    self.speedDown = 0
    self.walls = None
    
  def update(self):
    self.rect.y += self.speedUp
    self.rect.y += self.speedDown
      
    obj_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
    for i in obj_hit_list:
      if self.speedUp != 0:
        self.rect.top = i.rect.bottom
      if self.speedDown != 0:
        self.rect.bottom = i.rect.top
         
  def reset(self):
    self.rect.y = 200
    y = 200

class Obj(pygame.sprite.Sprite):
  def __init__(self, w, h):
    super().__init__()
    self.image = pygame.Surface([w, h])
    self.image.fill(LESS_WHITE)
    self.rect = self.image.get_rect()
      
#groups
obj_list = pygame.sprite.Group()
barrier_list = pygame.sprite.Group()
paddle_list = pygame.sprite.Group()

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

done = False

clock = pygame.time.Clock()

#lines that seperate both halves of the screen
count = 0
for i in range(7):
  line = Obj(20, 50)
  line.rect.x = 340
  line.rect.y = count
  count += 75
  obj_list.add(line)


#paddle ball!
ball = Ball(35, 35)
ball.rect.x = 332
ball.rect.y = 225
obj_list.add(ball)

#barriers for the ball to bounce off of
topB = Obj(700, 20)
obj_list.add(topB)
barrier_list.add(topB)

bottomB = Obj(700, 20)
bottomB.rect.y = 480
obj_list.add(bottomB)
barrier_list.add(bottomB)

#paddles
paddle1 = Paddle( 15, 100)
obj_list.add(paddle1)
paddle_list.add(paddle1)

paddle2 = Paddle(15, 100)
paddle2.rect.x = 635
paddle2.rect.y = 200 
obj_list.add(paddle2)
paddle_list.add(paddle2)

#main menu buttons
button1 = pygame.Rect([265, 340, 150, 75])
button2 = pygame.Rect([175, 225, 100, 100])
button3 = pygame.Rect([400, 225, 100, 100])

#menu images
vs = pygame.image.load("vs.png")
vs = pygame.transform.scale_by(vs, (0.15, 0.15))

com = pygame.image.load("com.png")
com = pygame.transform.scale_by(com, (0.15, 0.15))

play = pygame.image.load("play.png")
play = pygame.transform.scale_by(play, (0.35, 0.35))

#music
#from CodeManu on OpenGameArt
pygame.mixer.music.load("bgm.ogg")

#sounds
#from phoenix1291 on OpenGameArt
explo = pygame.mixer.Sound("explo.ogg")
blip = pygame.mixer.Sound("blip.ogg")
hit = pygame.mixer.Sound("hit.ogg")

#make the paddles actually stop at the walls
paddle1.walls = barrier_list
paddle2.walls = barrier_list
while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    if win == 0 and screens == 2:
      if event.type == pygame.KEYDOWN:
        if start:
          if event.key == pygame.K_UP:
            paddle2.speedUp -= 2
          if event.key == pygame.K_DOWN:
            paddle2.speedDown += 2
          if not com:
            if event.key == pygame.K_w:
              paddle1.speedUp -= 2
            if event.key == pygame.K_s:
              paddle1.speedDown += 2
      if event.type == pygame.KEYUP:
        if start:
          if event.key == pygame.K_UP:
            paddle2.speedUp = 0
          if event.key == pygame.K_DOWN:
            paddle2.speedDown = 0
          if not com:
            if event.key == pygame.K_w:
              paddle1.speedUp = 0
            if event.key == pygame.K_s:
              paddle1.speedDown = 0
        if event.key == pygame.K_SPACE:
            start = True
            if showIns:
              showIns = False
            if not test:
              pygame.mixer.music.play(-1)
              test = True
            else:
              pygame.mixer.music.unpause()
    if event.type == pygame.MOUSEBUTTONUP: #idk if there's an easier way to do this
        if screens == 0:
          if button1.collidepoint(pos[0], pos[1]):
            screens = 1
            blip.play()
        if screens == 1:
          if button2.collidepoint(pos[0], pos[1]):
            screens = 2
            com = True
            blip.play()
          if button3.collidepoint(pos[0], pos[1]):
            screens = 2
            com = False
            blip.play()
  pos = pygame.mouse.get_pos()

  if com:
    paddle1.rect.topleft = round(x), round(y) #thank you person on stack overflow for telling me rect doesn't support floats
  ball.rect.topleft = round(ballX), round(ballY)
  
  if com:
    if ball.rect.x < 325 and ball.speedX < 0:
      if ball.rect.y < paddle1.rect.top:
        y -= comSpeed
      elif ball.rect.y > paddle1.rect.bottom:
        y += comSpeed
      
    com_hit_list = pygame.sprite.spritecollide(paddle1, barrier_list, False)
    for i in com_hit_list:
      if paddle1.rect.y < 250:
        paddle1.rect.top = i.rect.bottom
      if paddle1.rect.y > 250:
        paddle1.rect.bottom = i.rect.top

  if ball.rect.x < -50 or ball.rect.x > 750:
    paddle1.reset()
    paddle2.reset()
    if ball.rect.x < -50:
      scoreP2 += 1
    elif ball.rect.x > 750:
      scoreP1 += 1
    ballX = 332
    ballY = 225
    paddle1.speedUp = 0
    paddle1.speedDown = 0
    paddle2.speedUp = 0
    paddle2.speedDown = 0
    start = False
    ball.speedX = ball.speedX * -1
    pygame.mixer.music.pause()
    explo.play()

  if not start:
    y = 200
    
  score1 = font.render(str(scoreP1), False, WHITE)
  if win == 1:
    score1 = font.render("P1 wins!", False, WHITE)
  score2 = font.render(str(scoreP2), False, WHITE)
  if win == 2:
    score2 = font.render("P2 wins!", False, WHITE)
  instructions1 = font.render("Press space to start", False, WHITE)
  instructions2 = font.render("Get to 7 points first to win", False, WHITE)
  instructions3 = font.render("Use the arrows keys to move your paddle", False, WHITE)
  instructions4 = font.render("W/S - Paddle 1, UP/DOWN - Paddle 2", False, WHITE)
  
  title = font2.render("pong", False, WHITE)
  text1 = font2.render("Play", False, WHITE)
  text2 = font2.render("com", False, WHITE)
  text3 = font2.render("vs", False, WHITE)
  
  if scoreP1 == 7:
    win = 1
  if scoreP2 == 7:
    win = 2

  ball_hit_list = pygame.sprite.spritecollide(ball, barrier_list, False)
  for i in ball_hit_list:
    if i == topB and ball.speedY < 0:
      ball.speedY = ball.speedY * -1
    if i == bottomB and ball.speedY > 0:
      ball.speedY = ball.speedY * -1
    hit.play()
  ball_hit_list2 = pygame.sprite.spritecollide(ball, paddle_list, False)
  for i in ball_hit_list2:
    if i == paddle2 and ball.speedX > 0:
      ball.speedX = ball.speedX * -1
    if i == paddle1 and ball.speedX < 0:
      ball.speedX = ball.speedX * -1
    hit.play()

  if not com:
    paddle1.update()
  paddle2.update()
  if start:
    ballX += ball.speedX
    ballY += ball.speedY
    
  screen.fill(BLACK)

  if screens == 0:
    pygame.draw.rect(screen, WHITE, button1, 5)
    
    screen.blit(title, [275, 150])

    screen.blit(play, [325, 350])
    
  if screens == 1:
    pygame.draw.rect(screen, WHITE, button2, 5)
    pygame.draw.rect(screen, WHITE, button3, 5)
    
    screen.blit(title, [275, 150])

    screen.blit(vs, [425, 235])
    screen.blit(com, [188.5, 245])

  if screens == 2:
    obj_list.draw(screen)
    if win != 2:
      screen.blit(score1, [100, 100])
    if win != 1 and not win == 2:
      screen.blit(score2, [575, 100])
    if win == 2:
      screen.blit(score2, [400, 100])
    if showIns:
      screen.blit(instructions1, [187.5, 100])
      screen.blit(instructions2, [137.5, 135])
      if com:
        screen.blit(instructions3, [12.5, 170])
      if not com:
        screen.blit(instructions4, [50, 170])

  pygame.display.flip()

  clock.tick(144)

pygame.quit()
