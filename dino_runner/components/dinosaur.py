from pygame.sprite import Sprite
import pygame
from dino_runner.components.fire import Fire
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.components.obstacles.powerUp import PowerUp
from dino_runner.utils.constants import DUCKING, HEART, JUMPING, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, SHIELD

class Dinosaur(Sprite):
    JUMP_VELOCITY = 8
    Y_POS=310
    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = 80
        self.dino_rect.y = 310
        self.life=3
        self.fires = []

        self.power_up_shild=False
        self.power_up_fire=False

        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False

        self.jump_velocity = self.JUMP_VELOCITY
        self.durationPowerUp=0
        self.durationPowerUp_Fire=0
        self.step_index = 0
        self.step_index_Fire = 0

    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()
        
        if self.step_index >= 10:
            self.step_index = 0
        
        self.inputs (user_input)

        self.temporizadorAtributo() 

        if(len(self.fires)!=0): #movimiento del fuego
            for fire in self.fires:
                fire.update(self)
    
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
        
        for number in range(self.life):
            screen.blit(HEART, ( 50+30*number, SCREEN_HEIGHT-60))
        if(self.power_up_shild):
            sild = pygame.transform.scale(SHIELD, (140, 140))
            screen.blit(sild, (self.dino_rect.x-30, self.dino_rect.y-30))
        if(len(self.fires)!=0):
            for fire in self.fires:
                fire.draw(screen)

    def inputs (self, user_input):
        if user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_jump = False
            self.dino_run = False  
            self.dino_duck = True  
        elif user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif not self.dino_jump:
            self.dino_jump = False
            self.dino_run = True
            self.dino_duck = False

        if user_input[pygame.K_a] and self.power_up_fire and self.step_index_Fire>10:
            self.shoot()
            self.step_index_Fire=0
        self.step_index_Fire+=1

    def jump(self):
        self.image = JUMPING
        self.dino_rect.y -= self.jump_velocity * 4
        self.jump_velocity -=0.8
        if  self.jump_velocity < -self.JUMP_VELOCITY:
            self.dino_rect.y = self.Y_POS
            self.jump_velocity = self.JUMP_VELOCITY
            self.dino_jump = False

    def run (self):
        self.dino_rect.y = self.Y_POS
        if self.step_index > 5:
            self.image = RUNNING[1]
        else:
            self.image = RUNNING[0]
        self.step_index +=1
    
    def duck(self):
        self.dino_rect.y = self.Y_POS+35
        if self.step_index > 5:
            self.image = DUCKING[1]
        else:
            self.image = DUCKING[0]
        self.step_index +=1

    def shoot(self):
        self.fires.append(Fire(self))
    
    def check_pos_misil(self):
        if(len(self.fires)!=0):
            for fire in self.fires:    
                if fire.rect.x > SCREEN_WIDTH:
                    self.fires.remove(fire)

    def check_collision(self, object):
        if self.dino_rect.colliderect(object.rect):
            if isinstance(object, Obstacle) and object.eliminate==False and not self.power_up_shild:
                object.eliminate=True
                self.life-=1
            elif  isinstance(object, PowerUp) :
                object.darPowerUp(self) 
        
    def check_colicion_fires(self, obstacle):
        if(len(self.fires)!=0):
            for fire in self.fires:
                if fire.rect.colliderect(obstacle.rect): 
                    self.fires.remove(fire)
                    obstacle.eliminate=True
                    
    def temporizadorAtributo(self):
        if(self.power_up_shild):
            if(self.durationPowerUp>100):
                self.power_up_shild=False
                self.durationPowerUp=0
            self.durationPowerUp+=1

        if(self.power_up_fire):
            if(self.durationPowerUp_Fire>100):
                self.power_up_fire=False
                self.durationPowerUp_Fire=0
            self.durationPowerUp_Fire+=1

        
       

    


            
                
        