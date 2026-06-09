import sys
import asteroid
import asteroidfield
import pygame
from constants import (SCREEN_HEIGHT, SCREEN_WIDTH)
from logger import (log_state, log_event)
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import copy


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock_object = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
   
# containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    
    print("Starting Asteroids")
    print("...")  
  # game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            #activate the ablities
            if event.type == pygame.KEYDOWN:
                # super shot
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    player.super_shoot = not player.super_shoot
                #scatter
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    shot.is_scatter = not shot.is_scatter


        dt = clock_object.tick(60) / 1000
        updatable.update(dt)
        screen.fill("black")
       
        for obj in drawable:
 
           # draw object on screen
            obj.draw(screen)

            # check for colligion
            for asteroid in asteroids:
                asteroid.kill() #debugging code rm
                for shot in shots:
                    
                    # destory the shoted asteroid
                    if shot.collides_with(asteroid):
                        log_event("asteroid_shot")
                        shot.kill()
                        asteroid.split()
                    # remove the off screen objects
                    shot.out_of_field(SCREEN_HEIGHT, SCREEN_WIDTH, not shot.is_scatter)
                asteroid.out_of_field(SCREEN_HEIGHT, SCREEN_WIDTH)
                player.out_of_field(SCREEN_HEIGHT, SCREEN_WIDTH)

                if player.collides_with(asteroid):
                    log_event("player_hit")
                    sys.exit("Game Over!")



        pygame.display.flip()


if __name__ == "__main__":
    main()
