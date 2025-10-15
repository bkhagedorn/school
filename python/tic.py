import pygame

#default colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#color used for when mouse is hovering over box
NOT_WHITE = (225, 225, 225)

pygame.init()

#function definitions to draw the x's and o's
def createX(box):
  pygame.draw.line(screen, RED, [box.x+20, box.y+20], [box.x+180, box.y+180], 5)
  pygame.draw.line(screen, RED, [box.x+20, box.y+180], [box.x+180, box.y+20], 5)
  
def createO(box):
  pygame.draw.circle(screen, BLUE, [box.x+100, box.y+100], 90, 5)
    

turn = "p1" #whose turn it is
win = True #has anyone won
noLock = True #variable to make sure it doesn't print stuff forever
tieTest = 0 #increases every time a box is used
pygame.mouse.set_visible(False) #makes mouse invisible

size = (600, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

done = False

clock = pygame.time.Clock()

box1 = pygame.Rect([0, 0, 200, 200])
box2 = pygame.Rect([200, 0, 200, 200])
box3 = pygame.Rect([400, 0, 200, 200])
box4 = pygame.Rect([0, 200, 200, 200])
box5 = pygame.Rect([200, 200, 200, 200])
box6 = pygame.Rect([400, 200, 200, 200])
box7 = pygame.Rect([0, 400, 200, 200])
box8 = pygame.Rect([200, 400, 200, 200])
box9 = pygame.Rect([400, 400, 200, 200])

active = [True, True, True, True, True, True, True, True, True]
control = ["none1", "none2", "none3", "none4", "none5", "none6", "none7", "none8", "none9"]
boxList = []
boxList2 = []
actualBoxList = [box1, box2, box3, box4, box5, box6, box7, box8, box9]

CLICK = pygame.USEREVENT + 1

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    if event.type == pygame.MOUSEBUTTONUP and win:
      if event.button == 1:
        for i in range(9):
          if actualBoxList[i].collidepoint(pos[0], pos[1]) and active[i]:
            active[i] = False
            pygame.event.post(pygame.event.Event(CLICK))
            if turn == "p1":
              control[i] = "p1"
              boxList.append(actualBoxList[i])
            else:
              control[i] = "p2"
              boxList2.append(actualBoxList[i])
    if event.type == CLICK:
      if turn == "p1":
        turn = "p2"
      else:
        turn = "p1"
      tieTest += 1
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_r:
        turn = "p1"
        win = True
        noLock = True
        tieTest = 0;
        active = [True, True, True, True, True, True, True, True, True]
        control = ["none1", "none2", "none3", "none4", "none5", "none6", "none7", "none8", "none9"]
        boxList = []
        boxList2 = []
        
        
  pos = pygame.mouse.get_pos()
  
  row1 = [control[0], control[1], control[2]]
  row2 = [control[3], control[4], control[5]]
  row3 = [control[6], control[7], control[8]]
  test = [row1, row2, row3]

  if row1[0] == row2[1] == row3[2] and noLock:
      print(turn, "win")
      win = False
      noLock = False
  elif row1[2] == row2[1] == row3[0] and noLock:
      print(turn, "win")
      win = False
      noLock = False
  for i in range(3):
    if row1[i] == row2[i] == row3[i] and noLock:
      print(turn, "win")
      win = False
      noLock = False
    elif test[i][0] == test[i][1] == test[i][2] and noLock:
      print(turn, "win")
      win = False
      noLock = False
      
  if tieTest == 9 and noLock:
    print("tie")
    win = False
    noLock = False

  screen.fill(WHITE)

  for i in range(9):
    if actualBoxList[i].collidepoint(pos[0], pos[1]) and active[i] and win:
      pygame.draw.rect(screen, NOT_WHITE, actualBoxList[i])
    else:
      pygame.draw.rect(screen, WHITE, actualBoxList[i])

  pygame.draw.line(screen, BLACK, [200, 0], [200, 600], 3)
  pygame.draw.line(screen, BLACK, [400, 0], [400, 600], 3)
  pygame.draw.line(screen, BLACK, [0, 200], [600, 200], 3)
  pygame.draw.line(screen, BLACK, [0, 400], [600, 400], 3)
  
  for i in boxList:
    createX(i)
    
  for i in boxList2:
    createO(i)
  
  if win:
    if turn == "p1":
      pygame.draw.line(screen, RED, [pos[0]-10, pos[1]-10], [pos[0]+10, pos[1]+10], 5)
      pygame.draw.line(screen, RED, [pos[0]+10, pos[1]-10], [pos[0]-10, pos[1]+10], 5)
    else:
      pygame.draw.circle(screen, BLUE, [pos[0], pos[1]], 15, 5)
  
  pygame.display.flip()

  clock.tick(60)

pygame.quit()
