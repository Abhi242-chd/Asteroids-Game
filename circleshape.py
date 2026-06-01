from enum import pickle_by_enum_name
import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    
    def collides_with(self, other):

# calculate distance between two circles center
        distance = pygame.math.Vector2.distance_to(self.position, other.position)

# calculate at what distance shape should collide
        colliding_distance = self.radius + other.radius
 

        return distance < colliding_distance

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def out_of_field(self, screen_hight, screen_weight, should_remove=False):
        left_or_top_coner = 0
        right_coner = screen_weight        
        bottem_coner = screen_hight
        
        if should_remove:
            if (self.position.x < left_or_top_coner or self.position.y < left_or_top_coner or self.position.x > right_coner or self.position.y > bottem_coner):
                self.kill()
        else:
            if self.position.x < left_or_top_coner:
                self.position.x += right_coner
            
            if self.position.x > right_coner:
                self.position.x -=  right_coner
            if self.position.y < left_or_top_coner:
                self.position.y +=  bottem_coner
            if self.position.y > bottem_coner:
                self.position.y -= bottem_coner

