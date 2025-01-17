import random
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.powerUp import PowerUp
from dino_runner.utils.constants import BIRD, SCREEN_WIDTH, SMALL_CACTUS

class ObstacleManager:
    def __init__(self):
        self.cactus = Cactus(SMALL_CACTUS)
        self.birds=Bird (BIRD)
        self.powerUp=PowerUp()
        self.step_index_Birds=random.randint(0,250)
        self.step_index_powerUps=random.randint(0,250)

    def update (self, game):
        self.cactus.update(game.game_speed)
        self.birds.update(game.game_speed)
        self.powerUp.update(game.game_speed)
        self.crearCactus()
        self.crearBirds()
        self.crearPowerUp()

    def draw (self, screen):
        self.cactus.draw(screen)
        self.birds.draw(screen)
        self.powerUp.draw(screen)
        
    def crearCactus(self):
        if self.cactus.rect.x < -self.cactus.rect.width:
            self.cactus = Cactus(SMALL_CACTUS)
           
    def crearBirds(self):
        if self.step_index_Birds > 250 and (self.birds.rect.x < -self.birds.rect.width) and (self.cactus.rect.x <SCREEN_WIDTH//2 and self.cactus.rect.x > 80) :
            self.birds=Bird (BIRD)
            posiY=[280,150]
            self.birds.rect.y = posiY[random.randint(0,1)]
            self.step_index_Birds=random.randint(0,250)
            self.birds.rect.x =SCREEN_WIDTH   
        self.step_index_Birds+=1
    
    def crearPowerUp(self):
        if self.step_index_powerUps > 250 and self.powerUp.rect.x < -self.powerUp.rect.width:
            self.powerUp = PowerUp()
            self.step_index_powerUps=random.randint(0,250)
        self.step_index_powerUps+=1

    

    

    


    
