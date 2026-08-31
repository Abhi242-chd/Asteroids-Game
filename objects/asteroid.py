import pygame
from objects.circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE_SECONDS
import random
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)       

    def update(self, dt: float, is_time_stop: bool):
        time_factor = 0 if is_time_stop else 1
        self.position += self.velocity * dt * time_factor

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: 
            return
        log_event("asteroid_split") 
        angle = random.uniform(20, 50)
        new_asteroid = Asteroid(self.position.x ,self.position.y , self.radius - ASTEROID_MIN_RADIUS)      
        new_asteroid2 = Asteroid(self.position.x ,self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        new_asteroid.velocity = self.velocity.rotate(angle) * 1.2
        new_asteroid2.velocity = self.velocity.rotate(-angle) * 1.2
        
    def out_of_field(self, screen_hight, screen_width, should_remove=False):
        should_remove = False
        return super().out_of_field(screen_hight, screen_width, should_remove)          
