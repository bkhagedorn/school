import pygame
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

IDK = (132, 182, 141)
P = (110, 153, 202)
RED_MAYBE = (226, 155, 64)
NOT_BROWN = (191, 183, 177)

offset = 50
 
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
 
    screen.fill(IDK)

    pygame.draw.circle(screen, WHITE, [200, 150], 100) #right eye
    pygame.draw.circle(screen, WHITE, [500, 150], 100) #left eye

    pygame.draw.ellipse(screen, P, [225, 150, 35, 75]) #right pupil
    pygame.draw.ellipse(screen, P, [445, 150, 35, 75]) #left pupil

    pygame.draw.rect(screen, RED_MAYBE, [325, 225, 50, 50]) #nose

    pygame.draw.line(screen, NOT_BROWN, [200 + offset, 350], [250 + offset, 450], 20)
    pygame.draw.line(screen, NOT_BROWN, [250 + offset, 450], [300 + offset, 350], 20)
    pygame.draw.line(screen, NOT_BROWN, [300 + offset, 350], [350 + offset, 450], 20)
    pygame.draw.line(screen, NOT_BROWN, [350 + offset, 450], [400 + offset, 350], 20)
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
