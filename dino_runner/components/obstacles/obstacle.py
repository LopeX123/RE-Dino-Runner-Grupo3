
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacle(Sprite):
    def __init__(self, images, type):
        self.images = images
        self.type = type
        self.rect = self.images[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.eliminate=False

    def update(self, game_speed):
        self.rect.x -= game_speed    

    def draw(self, screen):
        screen.blit(self.images[self.type], (self.rect.x, self.rect.y))
        
        