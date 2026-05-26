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

    def update(self, dt):
       return self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: 
            return
        
        velocity = random.uniform(20, 50)
        new_astroit = self.velocity.rotate(velocity), self.radius - ASTEROID_MIN_RADIUS       
        new_astroit2 = self.velocity.rotate(- velocity), self.radius - ASTEROID_MIN_RADIUS
        return new_astroit, new_astroit2

          
