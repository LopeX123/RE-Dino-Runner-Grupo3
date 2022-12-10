import pygame
from dino_runner.utils.constants import FONT_STYLE

class Score:
    def __init__(self):
        self.score = 0
        self.best_score=0

    def update (self, game):
        self.score +=1
        if self.score % 100 == 0:
            game.game_speed += 1
    
    def comparation(self):
        if self.score>self.best_score:
            self.best_score=self.score

    def draw(self, screen):
        font = pygame.font.Font(FONT_STYLE, 22)
        text_score = font.render(f"Score: {self.score}", True, (0,0,0))
        text_score_best = font.render(f"HI: {self.best_score}", True, (0,0,0))

        text_rect2 = text_score_best.get_rect()
        text_rect2.center = (880, 50)

        text_rect = text_score.get_rect()
        text_rect.center = (1000, 50)
        screen.blit(text_score,text_rect)
        screen.blit(text_score_best,text_rect2)

    def reset(self):
        self.score=0