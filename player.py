import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_TURN_SPEED, PLAYER_SPEED, LINE_WIDTH, PLAYER_SHOOT_COOLDOWN_SECONDS, SUPER_CHARGE_TIME, SCATTER_SHOT_TIME
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0
        #ablities
        # super shot
        self.super_shoot = False
        self.super_shoot_charge = SUPER_CHARGE_TIME
                
        # scatter_shot
        self.scatter_shot = False
        self.scatter_shot_time = SCATTER_SHOT_TIME


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        return PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector


    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(- dt)


        if keys[pygame.K_a]:
           self.rotation -= self.rotate(dt)

        if keys[pygame.K_d]:
           self.rotation += self.rotate(dt)

        if keys[pygame.K_SPACE]:
            if self.shot_cooldown <= 0:
                self.shoot()
                if self.super_shoot and  self.super_shoot_charge > 0:
                    self.shot_cooldown = 0
                    self.super_shoot_charge -= dt
                    if self.super_shoot_charge <= 0:
                        self.super_shoot = not self.super_shoot
                else:
                    self.shot_cooldown += PLAYER_SHOOT_COOLDOWN_SECONDS
                            
        # shot cooldown reset
        if self.shot_cooldown > 0:        
            self.shot_cooldown -= dt
        if self.super_shoot_charge < SUPER_CHARGE_TIME and self.super_shoot == False:
            self.super_shoot_charge += dt
        
        # scatter shot
        if self.scatter_shot_time > 0 and self.scatter_shot:        
            self.scatter_shot_time -= dt

        if self.scatter_shot_time <= 0:
            self.scatter_shot = False
        if self.scatter_shot_time < SCATTER_SHOT_TIME and self.scatter_shot == False:
            self.scatter_shot_time += dt

        
                    

    def shoot(self):
        tip = self.triangle()[0] 
        shot = Shot(tip.x, tip.y) # locate the tip of thr tringle
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def out_of_field(self, screen_hight, screen_weight, should_remove=False):
        should_remove = False
        return super().out_of_field(screen_hight, screen_weight, should_remove)
