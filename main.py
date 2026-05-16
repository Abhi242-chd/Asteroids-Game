import sys
import asteroid
import asteroidfield
import pygame
from constants import (SCREEN_HEIGHT, SCREEN_WIDTH)
from logger import (log_state, log_event)
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock_object = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
   
# containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    print("Starting Asteroids")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
  
  # game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock_object.tick(60) / 1000
        updatable.update(dt)
        screen.fill("black")
       
        for obj in drawable:
 
           # draw object on screen
            obj.draw(screen)

            # check for colligion
            for asteroid in asteroids:
                if player.collides_with(asteroid):
                    log_event("player_hit")
                    sys.exit("Game Over!")
            




        pygame.display.flip()


if __name__ == "__main__":
    main()
