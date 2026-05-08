import pygame
from constants import (SCREEN_HEIGHT, SCREEN_WIDTH)
from logger import log_state
from player import Player


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock_object = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print("Starting Asteroids")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock_object.tick(60) / 1000
        player.update(dt)

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
