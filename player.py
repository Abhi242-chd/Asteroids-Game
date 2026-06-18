import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_TURN_SPEED, PLAYER_SPEED, LINE_WIDTH, PLAYER_SHOOT_COOLDOWN_SECONDS, SUPER_CHARGE_TIME, WARP_SHOT_TIME, TIME_STOP_DURATION, PASS_THOUGH_DURATION, MUSCLE_SHOTS
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
                
        # warp shot
        self.warp_shot = False
        self.warp_shot_time = WARP_SHOT_TIME

        # pass though
        self.is_pass_though = False
        self.pass_though_duration = PASS_THOUGH_DURATION

        # mucsle shot
        self.__muscle_shots = MUSCLE_SHOTS 

        # time stop
        self.is_time_stop = False
        self.time_stop_duration = TIME_STOP_DURATION


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


    def update(self, dt, is_time_stop=False):
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
        if keys[pygame.K_LCTRL]:
            if self.shot_cooldown <= 0:
                if self.__muscle_shots > 0:
                    self.shoot(is_muscle_shot=True)
                    self.__muscle_shots -= 1
                    self.shot_cooldown += PLAYER_SHOOT_COOLDOWN_SECONDS



        # shot cooldown reset
        if self.shot_cooldown > 0:        
            self.shot_cooldown -= dt
        if self.super_shoot_charge < SUPER_CHARGE_TIME and self.super_shoot == False:
            self.super_shoot_charge += dt
        
        # warp shot
        if self.warp_shot_time > 0 and self.warp_shot:        
            self.warp_shot_time -= dt

        elif self.warp_shot_time <= 0:
            self.warp_shot = False
        if self.warp_shot_time < WARP_SHOT_TIME and self.warp_shot == False:
            self.warp_shot_time += dt

            # time stop
        if self.is_time_stop and self.time_stop_duration > 0:
            self.time_stop_duration -= dt
        elif self.time_stop_duration <= 0:
            self.is_time_stop = False
        if self.is_time_stop == False and self.time_stop_duration < TIME_STOP_DURATION:
            self.time_stop_duration += dt

           # pass though
        if self.is_pass_though and self.pass_though_duration> 0:
            self.pass_though_duration -= dt
        elif self.pass_though_duration <= 0:
            self.is_pass_though = False
        if self.pass_though_duration < PASS_THOUGH_DURATION and self.is_pass_though == False:
            self.pass_though_duration += dt


        
                    

    def shoot(self, is_muscle_shot=False):
        tip = self.triangle()[0] 
        shot = Shot(tip.x, tip.y, is_muscle_shot) # locate the tip of thr tringle
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def out_of_field(self, screen_hight, screen_width, should_remove=False):
        should_remove = False
        return super().out_of_field(screen_hight, screen_width, should_remove)
