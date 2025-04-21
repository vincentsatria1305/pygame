# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    pygame.init()
    
    dt =0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullet = pygame.sprite.Group()
    
    Asteroid.containers=(asteroids,updateable,drawable)
    AsteroidField.containers = (updateable)
    asteroid_field = AsteroidField()

    Shot.containers = (updateable,drawable, bullet)

    Player.containers=(updateable,drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        #print("inside loop")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updateable.update(dt)

        for astrd in asteroids:
            if astrd.collides_with(player):
                print("Game over!")
                sys.exit()
            for bullet_shooted in bullet:
                if astrd.collides_with(bullet_shooted):
                    astrd.split()
                    bullet_shooted.kill()

        screen.fill(color="black")
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()


        dt = clock.tick(60)/1000
        #print(dt)
        
if __name__ == "__main__":
    main()




