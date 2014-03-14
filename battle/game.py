import pygame, os, sys, time, Laser, Enemy, Battlecruiser
from pygame.locals import *
from random import randint, choice

class Background(pygame.sprite.Sprite):
    def __init__(self, screen, image_file, scroll_speed):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.scrolling = True

        self.image = self.load_image(image_file)
        self.image_w, self.image_h = self.image.get_size()
    
        self.screen_w = self.screen.get_size()[0]
        self.screen_h = self.screen.get_size()[1]
        
        # set initial position and speed
        self.x = 0
        self.y = -1 * (self.image_h - self.screen_h) + 1
        self.dy = scroll_speed
        self.dx = 0

    def load_image(self, image_file):
        """ loads image and throws exception if not found """
        try:
            image = pygame.image.load(image_file)
        except pygame.error:
            print "Unable to load image " + image_file
            sys.exit()
        return image.convert_alpha()

    def update(self):
        """ updates background position """
        if self.y >= 0 or self.y <= -1 * (self.image_h - self.screen_h):
            self.dy *= -1
            
        self.y += self.dy

    def draw(self):
        """ draws background """
        if self.scrolling == True:
            draw_pos = self.image.get_rect().move(self.x, self.y)
            self.screen.blit(self.image, draw_pos)


def main(args):
    # make sure font and sound are enabled
    if not pygame.font:
        print "Font not enabled"
    if not pygame.mixer:
        print "Font not enabled"
    
    # constants
    FPS = 50
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    BACKGROUND_IMAGE = 'assets/ram_aras.png'
    ENEMY_IMAGE = 'assets/mutalisk.gif'
    EXPLODE_IMAGE = 'assets/laser_explosion.gif'
    CRUISER_IMAGE = 'assets/battlecruiser.gif'
    LASER_IMAGE = 'assets/laser.gif'
    LASER_SOUND = 'assets/laser.wav'
    DEATH_SOUND = 'assets/death_explode.wav'
    SCORE_LOCATION = (10, 10)
    SHIP_SPEED = 1000
    LASER_SPEED = 20
    SHIP_COOLDOWN = 200  # ms between shots
    ENEMY_MAX_SPEED = 5
    SCROLL_SPEED = 4
    
    # initialize pygame
    pygame.init()
    pygame.display.set_caption('The Battle for Ram Aras')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    clock = pygame.time.Clock()
    score_font = pygame.font.Font(None, 30)
    dead_font = pygame.font.Font(None, 80)

    # initialize background
    background = Background(screen, BACKGROUND_IMAGE, SCROLL_SPEED)
    
    # initialize battle cruiser
    ship = Battlecruiser.Battlecruiser(screen, CRUISER_IMAGE, 350, 400, 
                                       SHIP_SPEED, LASER_SPEED, SHIP_COOLDOWN)
    last_fired = float("-inf") #time of last shot fired for cooldown calculation
   
    # initialize 10 enemies
    enemies = []
    for i in range (0, 5):
        dx = choice([-1, 1]) * randint(2, ENEMY_MAX_SPEED)
        dy = choice([-1, 1]) * randint(2, ENEMY_MAX_SPEED)
        x = randint(1, 600)
        y = randint(1, 200)
        enemies.append(Enemy.Enemy(screen, ENEMY_IMAGE, x, y, dx, dy, None)) 

    # initialize score
    score = 0
    
    # game status
    status = 1


    # GAME LOOP
    while True:
        time_passed = clock.tick(FPS)
        current_time = pygame.time.get_ticks() # elapsed time of program
        
        if status == 1: # YOU ARE ALIVE
           
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
                            ship.lasers.append(Laser.Laser(LASER_IMAGE, screen,
                                                           l_x, ship.y, 0, 
                                                           -1*ship.laser_speed,
                                                           LASER_SOUND))
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

            # update, draw background
            background.update()
            background.draw()

            # update, redraw enemies
            for enemy in enemies:
                enemy.update()
                enemy.draw()
        
            # update, draw ship
            ship.update()
            ship.draw()

            # update, redraw lasers
            for active_laser in ship.lasers:
                active_laser.update()
                active_laser.draw()
                if active_laser.rect.y <= -50: # kill laser if it goes offscreen
                    active_laser.kill()
                    ship.lasers.remove(active_laser)

            # draw score on screen
            score_text = score_font.render("Score: " + str(score), 1, 
                                           (34, 139, 34))
            screen.blit(score_text, SCORE_LOCATION)
      
            # collision detection for lasers and enemies
            for laser in ship.lasers:
                for enemy in enemies:
                    if pygame.sprite.collide_rect(laser, enemy):
                        enemy.explode(EXPLODE_IMAGE)
                        score += 100
                        laser.kill()
                        ship.lasers.remove(laser)
                        enemy.kill()
                        enemies.remove(enemy)

                        dx = choice([-1, 1]) * randint(2, ENEMY_MAX_SPEED)
                        dy = choice([-1, 1]) * randint(2, ENEMY_MAX_SPEED)
                        x = randint(1, 600)
                        y = randint(1, 200)
                        enemies.append(Enemy.Enemy(screen, ENEMY_IMAGE, 
                                                   x, y, dx, dy, None))
                        break

            # collision detection for enemies and ship
            for enemy in enemies:
                if pygame.sprite.collide_rect(enemy, ship):
                    try:
                        sound = pygame.mixer.Sound(DEATH_SOUND)
                    except pygame.error:
                        print "Failed to load death sound"
                        sys.exit()
                    sound.play()                    
                    status = 0
            
            # draw sprites
            pygame.display.flip()

        
        elif status == 0:   # YOU ARE DEAD
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # quit event
                    pygame.quit()
                    sys.exit()
                    
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:  # exit
                        pygame.quit()
                        sys.exit()
  
            screen.fill((0,0,0))
            dead = dead_font.render("GAME OVER", 40, (34, 139, 34))
            screen.blit(dead, (240, 250))
            screen.blit(score_text, (360, 330))
            pygame.display.flip()
        

if __name__ == "__main__":
    main(sys.argv)
 
