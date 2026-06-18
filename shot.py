from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS 
import pygame

class Shot(CircleShape):
    def __init__(self, x: float, y: float, muscle_shot: bool=False):
        self.__muscle_shot = muscle_shot
        super().__init__(x, y, SHOT_RADIUS + 2  if self.__muscle_shot else SHOT_RADIUS)

     
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt, is_time_stop=False):
        self.position += self.velocity * dt

    def kill_pierce(self):
        if self.__muscle_shot:
            pass
        else:
            self.kill()

    def out_of_field(self, screen_hight, screen_width, should_remove):
        should_remove = not should_remove
        return super().out_of_field(screen_hight, screen_width, should_remove)
