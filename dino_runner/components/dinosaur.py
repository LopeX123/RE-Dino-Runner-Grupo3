from pygame.sprite import Sprite
import pygame
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacle import Obstacle

from dino_runner.utils.constants import DUCKING, HEART, JUMPING, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    JUMP_VELOCITY = 8

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.life=5

        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_velocity = self.JUMP_VELOCITY

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

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
        
        for number in range(self.life):
            screen.blit(HEART, ( 50+30*number, SCREEN_HEIGHT-60))
    
    def check_collision(self, object):
        if self.dino_rect.colliderect(object.rect):
            if isinstance(object, Obstacle) and object.dead==False :
                self.life-=1
                object.dead=True
                if isinstance(object, Cactus):
                    object.type=3  
                    object.rect.y = 380
                print(self.life) 
            #elif  isinstance(object, Bird) and object.dead==False : 

        
       

    


            
                
        