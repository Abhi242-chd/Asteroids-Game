from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS 
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
     
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def out_of_field(self, screen_hight, screen_weight, should_remove):
        should_remove = not should_remove
        return super().out_of_field(screen_hight, screen_weight, should_remove)
