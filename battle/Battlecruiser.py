import pygame, os, sys, Laser
from pygame.locals import *
from random import randint

class Battlecruiser(pygame.sprite.Sprite):
    """ battlecruiser sprite class"""

    def __init__(self,screen, image_file, init_x, init_y, ship_speed, 
                 laser_speed, cooldown):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.load_image(image_file)
        self.image_w, self.image_h = self.image.get_size()
        self.screen = screen
        
        self.active = True
        
        # initializes collision box
        self.rect = self.image.get_rect()

        # set initial position, speed
        self.x = init_x
        self.y = init_y
        self.rect.x = init_x
        self.rect.y = init_y
        self.dx = 0
        self.dy = 0

        # set ship attributes
        self.lasers = []
        self.speed = ship_speed
        self.laser_speed = laser_speed
        self.cooldown = cooldown

    def load_image(self, image_file):
        """ loads image and throws exception if not found """
        try:
            image = pygame.image.load(image_file)
        except pygame.error:
            print "Unable to load image " 
            sys.exit()
        return image.convert_alpha()


    def update(self):
        """ updates cruiser position """
        if self.dx < 0 and self.x > 0:
            self.x += self.dx
            self.rect.x += self.dx
         
        if self.dx > 0 and self.x + self.image_w < self.screen.get_size()[0]:
            self.x += self.dx
            self.rect.x += self.dx
         
        if self.dy < 0 and self.y > 0:
            self.y += self.dy
            self.rect.y += self.dy

        if self.dy > 0 and self.y + self.image_h < self.screen.get_size()[1]:
            self.y += self.dy
            self.rect.y += self.dy

            
    def draw(self):
        """ draws cruiser """
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
    BACKGROUND_COLOR = (0, 0, 0)
    CRUISER_IMAGE = 'assets/battlecruiser.gif'
    LASER_IMAGE = 'assets/laser.gif'
    SHIP_SPEED = 10
    LASER_SPEED = 20
    SHIP_COOLDOWN = 300  # ms between shots
    
    # initialize pygame
    pygame.init()
    pygame.display.set_caption('Battlecruiser for Lab 3')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    clock = pygame.time.Clock()
    
    # initialize battle cruiser
    ship = Battlecruiser(screen, CRUISER_IMAGE, 350, 400, 
                         SHIP_SPEED, LASER_SPEED, SHIP_COOLDOWN)
    
    #time of last shot fired for cooldown calculation
    last_fired = float("-inf")
    
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

                elif event.key == K_LEFT:  # move left
                    ship.dx += -1 * ship.speed
                elif event.key == K_RIGHT:  # move right
                    ship.dx += ship.speed
                elif event.key == K_UP:  # move up
                    ship.dy += -1 * ship.speed
                elif event.key == K_DOWN:  # move down
                    ship.dy += ship.speed

                elif event.key == K_SPACE:  # fire laser
                    if current_time - last_fired > ship.cooldown:
                        l_x = ship.x + ship.rect.w / 2
                        ship.lasers.append(Laser.Laser(LASER_IMAGE, screen, l_x,
                                                       ship.y, 0, 
                                                       -1*ship.laser_speed))
                        last_fired = current_time # last shot fired was now

            elif event.type == KEYUP:
                if event.key == K_LEFT:
                    ship.dx -= -1 * ship.speed
                if event.key == K_RIGHT:
                    ship.dx -= ship.speed
                if event.key == K_UP: 
                    ship.dy -= -1 * ship.speed
                if event.key == K_DOWN:
                    ship.dy -= ship.speed

        # redraw background
        screen.fill(BACKGROUND_COLOR)

        # update, redraw cruiser
        ship.update()
        ship.draw()
            
        # update, redraw lasers
        for active_laser in ship.lasers:
            active_laser.update()
            active_laser.draw()
            if active_laser.rect.y <= 0:  # kill laser when it goes offscreen
                active_laser.kill()
                ship.lasers.remove(active_laser)

        # draw sprites
        pygame.display.flip()  
