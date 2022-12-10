import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SCREEN_WIDTH

class Cactus (Obstacle):
    def __init__(self, images):
        self.type = random.randint(0,2)
        super().__init__(images, self.type)
        self.rect.y = 325
    
    def draw(self, screen):
        super().draw(screen)
        if self.eliminate:
            self.type=3 #imagen cactus muerto
            self.rect.y = 380

    
        
