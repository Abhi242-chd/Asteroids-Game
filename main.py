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
                    player.scatter_shot = not player.scatter_shot
  
                # pass though
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    player.is_pass_though = not player.is_pass_though
                
                # time stop
                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    player.is_time_stop = not player.is_time_stop
               

        dt = clock_object.tick(60) / 1000
        updatable.update(dt, player.is_time_stop)
        screen.fill("black")
       
        

            # check for colligion
        for asteroid in asteroids:
            if player.collides_with(asteroid) and not player.is_pass_though:
                #log_event("player_hit")
                sys.exit("Game Over!")

            for shot in shots:
                
                # destory the shoted asteroid
                if shot.collides_with(asteroid):
                 #   log_event("asteroid_shot")
                    shot.kill_pierce()
                    asteroid.split()

        for obj in drawable:
 
           # draw object on screen
            obj.draw(screen)

           # remove the off screen objects
            obj.out_of_field(SCREEN_HEIGHT, SCREEN_WIDTH, player.scatter_shot)
                       
         
                        

        pygame.display.flip()


if __name__ == "__main__":
    main()
