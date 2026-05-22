from circleshape import CircleShape
from constants import LINE_WIDTH 


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "while", self.postion, self.radius, LINE_WIDTH)

    def update(self, dt):
        return self.velocity * dt
