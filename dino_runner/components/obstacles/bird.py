import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD, SCREEN_WIDTH


class Bird (Obstacle):
    def __init__(self, images):
        self.type = 1
        super().__init__(images, self.type)
        self.rect.y = 280
        self.step_index=0
        self.rect.x=SCREEN_WIDTH+600
    
    def update(self,game_speed):
        super().update(game_speed)
        if self.step_index > 5:
            self.type=0
        else:
            self.type=1

        self.step_index +=1

        if self.step_index >= 10:
            self.step_index = 0
        
