import pygame
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.score import Score

from dino_runner.utils.constants import BG, FONT_STYLE, ICON, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, SMALL_CACTUS, TITLE, FPS

class Game:
    
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = True
        self.executing = False

        self.game_speed = 20
        
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.game_state=0
        self.obstacle_manager = ObstacleManager()

        self.death_count = 0
        self.score = Score()

    def run(self):
        while self.playing:
            self.events()
            if(self.game_state==0):
                self.menu_state()
            elif (self.game_state==1):
                self.update()
                self.draw()
            elif (self.game_state==2):
                self.gameOver_state()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
        if pygame.key.get_pressed()[pygame.K_RIGHT] and self.game_state==0:
            self.game_state=1

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.player.check_collision(self.obstacle_manager.cactus)
        self.obstacle_manager.update(self)
        self.score.update(self)
        if(self.player.life==0):
            self.game_state=2
        

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255)) #white
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def menu_state(self):
        self.screen.fill((255,255,255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        font = pygame.font.Font(FONT_STYLE, 30)
        text_component = font.render("Press any key to play", True, (0,0,0))
        text_rect = text_component.get_rect()
        text_rect.center = (half_screen_width, half_screen_height)
        
        self.screen.blit(text_component,text_rect)
        self.screen.blit(RUNNING[0], (half_screen_width - 30, half_screen_height + 140))

        pygame.display.update()
    
    def gameOver_state(self):
        self.screen.fill((255,255,255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        font = pygame.font.Font(FONT_STYLE, 30)
        text_component = font.render("Press any key to play", True, (0,0,0))
        text_rect = text_component.get_rect()
        text_rect.center = (half_screen_width, half_screen_height)
        
        self.screen.blit(text_component,text_rect)
        self.screen.blit(RUNNING[0], (half_screen_width - 30, half_screen_height + 140))

        pygame.display.update()

        
        
