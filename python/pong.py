import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

rect_X = 325
rect_Y = 225

ping = 162.5
pong = 162.5
middle1 = 225
s1up = 0
s1down = 0
s2up = 0
s2down = 0

test1 = 150
test2 = 300

change_X = 2
change_Y = 1

counter = 3
p1 = counter
p2 = counter

start = False
win = False
 
pygame.init()

class Button():
    def __init__(self, n, x, y, w, h):
        self.name = n
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def create(self):
        self.name = pygame.Rect([self.x, self.y, self.width, self.height])
        
 
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

font = pygame.font.SysFont("comicsansms", 35, False, False)
font2 = pygame.font.SysFont("comicsansmns", 65, False, False)
speed = font.render("SPEED UP", False, WHITE)
speed.set_alpha(0)
win1 = font.render("P1 wins!", False, WHITE)
win2 = font.render("P2 wins!", False, WHITE)

screens = 0

pos = pygame.mouse.get_pos()

diffSelect = False
diff = 1

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            if not start and not win:
              start = True
              if diff == 0:
                pygame.time.set_timer(pygame.USEREVENT, 10000)
              if diff == 1:
                pygame.time.set_timer(pygame.USEREVENT, 7500)
              if diff == 2:
                pygame.time.set_timer(pygame.USEREVENT, 5000)
              if random.randrange(2) == 0:
                change_X = 2
              else:
                change_X = -2
              if random.randrange(2) == 0:
                change_Y = 1
              else:
                change_Y = -1
          if event.key == pygame.K_w:
            s1up -= 2
          if event.key == pygame.K_s:
            s1down += 2
          if event.key == pygame.K_UP:
            s2up -= 2
          if event.key == pygame.K_DOWN:
            s2down += 2
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_w:
            s1up = 0
          if event.key == pygame.K_s:
            s1down = 0
          if event.key == pygame.K_UP:
            s2up = 0
          if event.key == pygame.K_DOWN:
            s2down = 0
        if event.type == pygame.USEREVENT:
          change_X = change_X * 1.15
          change_Y = change_Y * 1.15
          pygame.time.set_timer(pygame.USEREVENT + 1, 2500)
          speed.set_alpha(255)
        if event.type == pygame.USEREVENT + 1:
          speed.set_alpha(0)
        if event.type == pygame.MOUSEBUTTONUP:
          if diffSelect:
            if click1.collidepoint(pos[0], pos[1]):
              screens = 1
              diff = 0
              rect_X = 312.5
              rect_Y = 212.5
            if click2.collidepoint(pos[0], pos[1]):
              screens = 1
              diff = 1
            if click3.collidepoint(pos[0], pos[1]):
              screens = 1
              diff = 2
            if click5.collidepoint(pos[0], pos[1]):
                if counter > 1:
                    counter -= 1
                    p1 = counter
                    p2 = counter
            if click6.collidepoint(pos[0], pos[1]):
                if counter < 5:
                    counter += 1
                    p1 = counter
                    p2 = counter
          if not diffSelect:
            if clicky.collidepoint(pos[0], pos[1]):
              diffSelect = True
              
 
    # --- Game logic should go here
    pos = pygame.mouse.get_pos()
    
    life1 = font.render(str(p1), False, WHITE)
    life2 = font.render(str(p2), False, WHITE)
    play = font.render("Play", False, WHITE)
    easy = font.render("Easy", False, WHITE)
    normal = font.render("Normal", False, WHITE)
    hard = font.render("Hard", False, WHITE)
    lives = font.render("Lives: " + str(counter), False, WHITE)
    leftArrow = font.render("<", False, WHITE)
    rightArrow = font.render(">", False, WHITE)
    if diff == 1:
      ball = pygame.Rect(rect_X, rect_Y, 35, 35)
      paddle1 = pygame.Rect(90, ping, 10, 150)
      paddle2 = pygame.Rect(590, pong, 10, 150)
    if diff == 0:
      ball = pygame.Rect(rect_X, rect_Y, 50, 50)
      paddle1 = pygame.Rect(90, ping - 25, 10, 200)
      paddle2 = pygame.Rect(590, pong - 25, 10, 200)
    if diff == 2:
      ball = pygame.Rect(rect_X, rect_Y, 20, 20)
      paddle1 = pygame.Rect(90, ping + 10, 10, 100)
      paddle2 = pygame.Rect(590, pong + 10, 10, 100)      
    clicky = pygame.Rect([275, 185, 120, 65])
    click1 = pygame.Rect([275, 185, 120, 65])
    click2 = pygame.Rect([265, 260, 140, 65])
    click3 = pygame.Rect([275, 335, 120, 65])
    click4 = pygame.Rect([255, 410, 160, 65])
    click5 = pygame.Rect([187.5, 417.5, 50, 50])
    click6 = pygame.Rect([442.5, 417.5, 50, 50])
    
    title = font2.render("pong", False, WHITE)
    
    if not start or win:
        speed.set_alpha(0)
    
    if not win:
      if start:
        rect_X += change_X
        rect_Y += change_Y
      
      if start:  
        if paddle1.top >= 0:
          ping += s1up
          test1 += s1up
          test2 += s1up
        if paddle1.bottom <= 500:
          ping += s1down
          test2 += s1down
          test1 += s1down
        if paddle2.top >= 0:
          pong += s2up
        if paddle2.bottom <= 500:
          pong += s2down
        
      if rect_X <= -100:
        start = False
        p1 -= 1
        rect_X = 325
        rect_Y = 225
        ping = 162.5
        pong = 162.5
      if rect_X >= 800:
        start = False
        p2 -= 1
        rect_X = 325
        rect_Y = 225
        ping = 162.5
        pong = 162.5
        
      if diff == 1:
        if rect_Y > 455 or rect_Y < 0:
            change_Y = change_Y * -1
      if diff == 0:
        if rect_Y > 445 or rect_Y < 0:
            change_Y = change_Y * -1
      if diff == 2:
        if rect_Y > 480 or rect_Y < 0:
            change_Y = change_Y * -1
        
      if change_X < 0:    
        if pygame.Rect.colliderect(ball, paddle1):
          change_X = change_X * -1
          if rect_Y <= test1 or rect_Y >= test2:
            if s1up != 0 or s1down != 0:
              if (s1up < 0 and change_Y > 0) or (s1down > 0 and change_Y < 0):
                change_Y = change_Y * -1
      if change_X > 0:    
        if pygame.Rect.colliderect(ball, paddle2):
          change_X = change_X * -1
          if rect_Y <= test1 or rect_Y >= test2:
            if s2up != 0 or s2down != 0:
              if (s2up < 0 and change_Y > 0) or (s2down > 0 and change_Y < 0):
                change_Y = change_Y * -1
            
      if p1 == 0 or p2 == 0:
        win = True

    screen.fill(BLACK)
 
    # --- Drawing code should go here
    
    if screens == 0:
      screen.blit(title, [280, 100])
      if not diffSelect:
        pygame.draw.rect(screen, WHITE, clicky, 5)
        screen.blit(play, [305, 190])
      else:
        pygame.draw.rect(screen, WHITE, click1, 5)
        pygame.draw.rect(screen, WHITE, click2, 5)
        pygame.draw.rect(screen, WHITE, click3, 5)
        pygame.draw.rect(screen, WHITE, click4, 5)
        pygame.draw.rect(screen, WHITE, click5, 5)
        pygame.draw.rect(screen, WHITE, click6, 5)
        screen.blit(easy, [300, 190])
        screen.blit(normal, [275, 265])
        screen.blit(hard, [295, 340])
        screen.blit(lives, [275, 415])
        screen.blit(leftArrow, [205, 415])
        screen.blit(rightArrow, [460, 415])
    
    if screens == 1:
      pygame.draw.rect(screen, WHITE, ball)
      pygame.draw.rect(screen, WHITE, paddle1)
      pygame.draw.rect(screen, WHITE, paddle2)
      
      screen.blit(life1, [60, 50])
      screen.blit(life2, [620, 50])
      screen.blit(speed, [275, 100])
      
    if win:
      if p1 == 0:
        screen.blit(win2, [290, 100])
      if p2 == 0:
        screen.blit(win1, [290, 100])
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(144)
 
# Close the window and quit.
pygame.quit()
