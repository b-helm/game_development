import pygame, os, sys, Laser
from pygame.locals import *
from random import randint, choice

class Enemy(pygame.sprite.Sprite):
    """ enemy sprite class"""

    def __init__(self, screen, image_file, init_x, init_y, init_dx, 
                 init_dy,the_player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.rotate(self.load_image(image_file), 90)
        self.image_w, self.image_h = self.image.get_size()
        self.screen = screen

        # set enemy to active
        self.active = True

        # the player's battlecruiser
        self.thePlayer = the_player

        # collision box
        self.rect = self.image.get_rect()

        # set initial position, speed
        self.x = init_x
        self.y = init_y
        self.rect.x = init_x
        self.rect.y = init_y
        self.dx = init_dx
        self.dy = init_dy

    def load_image(self, image_file):
        """ loads image and throws exception if not found """
        try:
            image = pygame.image.load(image_file)
        except pygame.error:
            print "Unable to load image " + fullname
            sys.exit()
        return image.convert_alpha()

    def explode(self, explode_image):
        """ sets image to explosion, deactivates sprite """
        self.image = self.load_image(explode_image)
        self.dx = 0
        self.dy = 0
        self.active = False
        self.update()
        self.draw()

    def update(self):
        """ updates enemy position """
        
        # make them bounce off walls
        if self.x <= 0 or self.x + self.image_w >= self.screen.get_size()[0]:
            self.dx *= -1
        if self.y <= 0 or self.y + self.image_h >= self.screen.get_size()[1]:
            self.dy *= -1
        
        # update positions
        self.x += self.dx
        self.y += self.dy
        self.rect.x += self.dx
        self.rect.y += self.dy
            
    def draw(self):
        """ draws enemy """
        draw_pos = self.image.get_rect().move(self.rect.x, self.rect.y)
        self.screen.blit(self.image, draw_pos)



if __name__ == "__main__":
    # make sure font and sound are enabled
    if not pygame.font:
        print "Font not enabled"
    if not pygame.mixer:
        print "Font not enabled"
    
    # constants
    FPS = 50
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    BACKGROUND_COLOR = (255, 255, 255)
    ENEMY_IMAGE = 'assets/mutalisk.gif'
    ENEMY_MAX_SPEED = 10

    # initialize pygame
    pygame.init()
    pygame.display.set_caption('Enemies')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    clock = pygame.time.Clock()
    
    # initialize 10 enemies
    enemies = []
    for i in range (0, 10):
        dx = choice([-1, 1]) * randint(2, ENEMY_MAX_SPEED)
        dy = choice([-1, 1]) * randint(2, ENEMY_MAX_SPEED)
        x = randint(1, 600)
        y = randint(1, 500)
        enemies.append(Enemy(screen, ENEMY_IMAGE, x, y, dx, dy, None)) 

    # game loop
    while True:
        time_passed = clock.tick(FPS)
        current_time = pygame.time.get_ticks() # elapsed time of program

        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # quit event
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # exit
                    pygame.quit()
                    sys.exit()

        # redraw background
        screen.fill(BACKGROUND_COLOR)

        # update, redraw enemies
        for enemy in enemies:
            enemy.update()
            enemy.draw()
            
        # draw sprites
        pygame.display.flip()  
