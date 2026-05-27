import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE_SECONDS
import random
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)       

    def update(self, dt: float):        
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: 
            return
        log_event("asteroid_split") 
        velocity = random.uniform(20, 50)
        new_astroit = Asteroid(self.velocity.rotate(velocity)[0], self.velocity.rotate(velocity)[1], self.radius - ASTEROID_MIN_RADIUS)      
        new_astroit2 = Asteroid(self.velocity.rotate(- velocity)[0],self.velocity.rotate(- velocity)[1] , self.radius - ASTEROID_MIN_RADIUS)
        new_astroit.velocity = new_astroit.velocity * 1.2
        new_astroit2.velocity = new_astroit2.velocity * 1.2
        return new_astroit, new_astroit2

          
