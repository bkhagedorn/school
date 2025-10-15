import pygame
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Moving Cube")   #1
 
done = False
clock = pygame.time.Clock()

rect_x=50
rect_y=50
rect_change_x=3                     #2
rect_change_y=3                     #3

screen.fill(BLACK)                  #4 
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    rect_x += rect_change_x    
    rect_y += rect_change_y    

    #bouncing a rectangle
    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 650 or rect_x < 0:                       #6
        rect_change_x = rect_change_x * -5               #7
    screen.fill(BLACK)                  
    
    pygame.draw.rect(screen,WHITE, [rect_x,rect_y,50,50])      #5
   
    pygame.display.flip()
    clock.tick(60)            #8    #9
    
    pygame.quit()      #10
