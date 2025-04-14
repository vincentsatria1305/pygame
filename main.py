# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *



def main():
    pygame.init()
    print("Starting Asteroids!")
    clock = pygame.time.Clock()
    dt =0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT)).fill(color="black")
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()




