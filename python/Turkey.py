import pygame
 
BLACK = (27, 42, 53)
WHITE = (236, 236, 236)
GREEN = (0, 255, 0)
RED = (255, 89, 89)
BLUE = (0, 0, 255)
BROWN = (203, 132, 66)
ORANGE = (255, 133, 65)
YELLOW = (239, 184, 56)
PRETTY_ORANGE = (235, 184, 127)
BG = (255, 255, 255)

offsetX = 27
offsetY = 20
 
pygame.init()
 
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
done = False
 
clock = pygame.time.Clock()
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    screen.fill(BG)
    
    pygame.draw.circle(screen, ORANGE, [325 + offsetX,400 + offsetY], 300) #feather
    pygame.draw.circle(screen, YELLOW, [325 + offsetX,400 + offsetY], 250) #feathers
    pygame.draw.circle(screen, PRETTY_ORANGE, [325 + offsetX,400 + offsetY], 200) #feathers	
    pygame.draw.rect(screen, BG, [0 + offsetX,400 + offsetY,700,110]) #feather cover
    pygame.draw.line(screen, BLACK, [325 + offsetX,375 + offsetY], [325 + offsetX,100 + offsetY], 1) #middle line
    pygame.draw.line(screen, BLACK, [325 + offsetX,375 + offsetY], [100 + offsetX,200 + offsetY], 1) #line
    pygame.draw.line(screen, BLACK, [325 + offsetX,375 + offsetY], [550 + offsetX,200 + offsetY], 1) #line
    pygame.draw.line(screen, BLACK, [325 + offsetX,375 + offsetY], [45 + offsetX,300 + offsetY], 1) #line
    pygame.draw.line(screen, BLACK, [325 + offsetX,375 + offsetY], [605 + offsetX,300 + offsetY], 1) #line
    pygame.draw.line(screen, BLACK, [325 + offsetX,375 + offsetY], [190 + offsetX,135 + offsetY], 1) #line
    pygame.draw.line(screen, BLACK, [325 + offsetX,375 + offsetY], [460 + offsetX,135 + offsetY], 1) #line
    pygame.draw.line(screen, YELLOW, [375 + offsetX,450 + offsetY], [400 + offsetX,480 + offsetY], 30) #foot
    pygame.draw.line(screen, YELLOW, [275 + offsetX,450 + offsetY], [250 + offsetX,480 + offsetY], 30) #foot
    pygame.draw.circle(screen, BROWN, [325 + offsetX,375 + offsetY], 100) #body
    pygame.draw.circle(screen, BROWN, [325 + offsetX,250 + offsetY], 70) #head
    pygame.draw.circle(screen, WHITE, [300 + offsetX,225 + offsetY], 25) #eye
    pygame.draw.circle(screen, WHITE, [350 + offsetX,225 + offsetY], 25) #eye
    pygame.draw.circle(screen, BLACK, [340 + offsetX,230 + offsetY], 5) #eye
    pygame.draw.circle(screen, BLACK, [310 + offsetX,230 + offsetY], 5) #eye
    pygame.draw.ellipse(screen, RED, [340 + offsetX,260 + offsetY,15,45]) #wattle
    pygame.draw.circle(screen, RED, [340 + offsetX,260 + offsetY], 10) #wattle
    pygame.draw.polygon(screen, ORANGE, [[310 + offsetX,260 + offsetY], [340 + offsetX,260 + offsetY], [325 + offsetX,300 + offsetY]]) #beak

    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
