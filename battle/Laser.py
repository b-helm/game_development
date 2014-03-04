import pygame, os, sys
from pygame.locals import *
from random import randint

class Laser(pygame.sprite.Sprite):
    """ Laser sprite """

    def __init__(self, image_file, screen, init_x, init_y, init_dx, init_dy,
                 sound_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.load_image(image_file)
        self.image_w, self.image_h = self.image.get_size()
        self.screen = screen
        
        self.sound = self.load_sound(sound_file)
        self.sound.play()
        
        self.rect = self.image.get_rect()
        
        # set initial position and speed
        self.rect.x = init_x
        self.rect.y = init_y
        self.x = init_x
        self.y = init_y
        self.dx = init_dx
        self.dy = init_dy
    
    def load_sound(self, sound_file):
        try:
            sound = pygame.mixer.Sound(sound_file)
        except pygame.error:
            print "Failed to load laser sound"
            sys.exit()
        return sound

    def load_image(self, image_file):
        """ loads image and throws exception if not found """
        try:
            image = pygame.image.load(image_file)
        except pygame.error:
            print "Unable to load image " + image_file
            sys.exit()
        return image.convert_alpha()

    def update(self):
        """ updates laser position and speed """
        self.x += self.dx
        self.y += self.dy
        self.rect.x += self.dx
        self.rect.y += self.dy

    def draw(self):
        """ draws laser """
        draw_pos = self.image.get_rect().move(self.rect.x, self.rect.y)
        self.screen.blit(self.image, draw_pos)



if __name__ == "__main__":
    # make sure font and sound are enabled
    if not pygame.font:
        print "Font not enabled"
    if not pygame.mixer:
        print "Sound not enabled"
    
    # constants
    FPS = 50
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    BACKGROUND_COLOR = (0,0,0)
    LASER_IMAGE = 'assets/laser.gif'
    
    # initialize pygame
    pygame.init()
    pygame.display.set_caption('Lasers for Lab 3')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    clock = pygame.time.Clock()

    # keep track of a list of active lasers
    laser_list = []
    
    # game loop
    while True:
        time_passed = clock.tick(FPS)

        # add a new laser every iteration of the loop
        laser_list.append(Laser(LASER_IMAGE, screen, randint(1, SCREEN_WIDTH),
                                550, 0, randint(1, 10) * -1))
     
        # handle quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    
        # redraw background
        screen.fill(BACKGROUND_COLOR)

        # update, redraw sprites
        for laser in laser_list:
            laser.update()
            laser.draw()
            if laser.rect.y <= 0:  # remove sprite when it goes offscreen
                laser.kill()
                laser_list.remove(laser)

        # draw sprites
        pygame.display.flip()
        
    
