"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
 
From:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example
 
Explanation video: http://youtu.be/8IRyt7ft7zg
 
Part of a series:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example.py
http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py
http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
http://programarcadegames.com/python_examples/sprite_sheets/
"""
 
import pygame
 
# -- Global constants
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
RED = (255, 50, 50)
YELLOW = (249, 233, 153)
HIDDEN = (25, 25, 25)
 
# Screen dimensions
SCREEN_WIDTH = 725
SCREEN_HEIGHT = 425
 
 
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """
 
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(WHITE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None
 
    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y
 
    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
 
 
class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
 
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface([10, 10])
        self.image.fill(YELLOW)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
 
# Set the title of the window
pygame.display.set_caption('Test')
 
# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()
 
# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()

win_list = pygame.sprite.Group()

coin_list = pygame.sprite.Group()

hidden_list = pygame.sprite.Group()
 
wall = Wall(0, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(350, 0, 10, 125)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(290, 50, 10, 75)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(190, 50, 10, 37.5)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(50, 50, 10, 37.5)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(240, 0, 10, 50)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(140, 0, 10, 50)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(715, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)
 
wall = Wall(0, 0, 300, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(290, 125, 110, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(50, 85, 240, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(0, 125, 240, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(50, 40, 50, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(350, 0, 450, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 415, 480, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(530, 415, 300, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(240, 125, 10, 200)
wall_list.add(wall)
all_sprite_list.add(wall)
 
wall = Wall(240, 325, 50, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(290, 260, 10, 75)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(290, 260, 100, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(380, 220, 10, 50)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(290, 170, 10, 50)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(290, 220, 50, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(290, 170, 150, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(440, 80, 10, 100)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(590, 80, 10, 255)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(390, 80, 285, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(390, 42.5, 10, 37.5)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(440, 42.5, 285, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(450, 125, 50, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(625, 125, 50, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(625, 125, 10, 55)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(625, 175, 100, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(625, 225, 50, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(590, 335, 85, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(625, 225, 10, 115)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(665, 265, 10, 35)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(665, 300, 50, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(190, 375, 485, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(340, 300, 10, 75)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(530, 375, 10, 50)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(190, 225, 10, 150)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(340, 300, 100, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(440, 262.5, 10, 80)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(400, 335, 150, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(550, 265, 10, 80)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(390, 220, 200, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(495, 215, 10, 80)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(495, 165, 10, 50)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(495, 165, 50, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(545, 125, 10, 50)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(50, 225, 140, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(50, 175, 150, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(50, 175, 10, 50)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(50, 275, 100, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(50, 275, 10, 100)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(150, 275, 10, 150)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(100, 325, 10, 150)
wall_list.add(wall)
all_sprite_list.add(wall)

win_block = Wall(490, 415, 40, 10)
all_sprite_list.add(win_block)
win_list.add(win_block)
win_block.image.fill(WHITE)

coin = Coin(505, 395)
all_sprite_list.add(coin)
coin_list.add(coin)

coin = Coin(265, 300)
all_sprite_list.add(coin)
coin_list.add(coin)

coin = Coin(650, 150)
all_sprite_list.add(coin)
coin_list.add(coin)

coin = Coin(370, 325)
all_sprite_list.add(coin)
coin_list.add(coin)

coin = Coin(75, 200)
all_sprite_list.add(coin)
coin_list.add(coin)

hidden_wall = Wall(540, 385, 10, 30)
hidden_wall.image.fill(HIDDEN)
all_sprite_list.add(hidden_wall)
hidden_list.add(hidden_wall)

hidden_wall2 = Wall(190, 185, 10, 50)
wall_list.add(hidden_wall2)
all_sprite_list.add(hidden_wall2)

# Create the player paddle object
player = Player(317.5, 50)
player.walls = wall_list
 
all_sprite_list.add(player)
    
clock = pygame.time.Clock()
 
done = False

font = pygame.font.SysFont("mscomicsans", 35, False)
win = font.render("You win!", False, WHITE)
hide = font.render("", False, WHITE)
fontcolor = WHITE

end_num = 0

count = 0
score = 0
timer = True
pygame.time.set_timer(pygame.USEREVENT, 1000)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.USEREVENT:
            if timer:
                count += 1
            else:
                if fontcolor == WHITE:
                    fontcolor = RED
                else:
                    fontcolor = WHITE
        elif event.type == pygame.KEYDOWN:
            if end_num == 0:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(1, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, -1)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, 1)
 
        elif event.type == pygame.KEYUP:
            if end_num == 0:
                if event.key == pygame.K_LEFT:
                    player.changespeed(1, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(-1, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, 1)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, -1)
 
    all_sprite_list.update()

    coin_hit_list = pygame.sprite.spritecollide(player, coin_list, True)
    for i in coin_hit_list:
        score += 1

    hidden_hit_list = pygame.sprite.spritecollide(player, hidden_list, False)
    if hidden_wall in hidden_hit_list:
        hide = font.render("Wall unlocked", False, WHITE)
        all_sprite_list.remove(hidden_wall2)
        wall_list.remove(hidden_wall2)

    end_list = pygame.sprite.spritecollide(player, win_list, False)
    for i in end_list:
        end_num += 1

    if end_num > 0:
        timer = False
        player.change_x = 0
        player.change_y = 0
    
    text = font.render("Time: " + str(count), False, fontcolor)
    scoretxt = font.render("Coins: " + str(score), False, fontcolor)

    if player.rect.y < -15:
        pygame.quit()

    text = font.render("Time: " + str(count), False, fontcolor)

    screen.fill(BLACK)
 
    all_sprite_list.draw(screen)
    screen.blit(text, [0, 0])
    screen.blit(scoretxt, [0, 25])
    screen.blit(hide, [0, 50])
    if end_num > 0:
        screen.blit(win, [615, 0])
 
    pygame.display.flip()

    clock.tick(144)
        
pygame.quit()
