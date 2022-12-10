import pygame
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.score import Score
from dino_runner.utils.constants import BG, CLOUD, FONT_STYLE, ICON, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, SMALL_CACTUS, STATE_GAMEOVER, STATE_MAIN, TITLE, FPS

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.playing = True
        self.game_speed = 20
        self.game_state=0
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.score = Score()

    def run(self):
        while self.playing:
            self.events()
            if(self.game_state==0): #menu
                self.menu_state()
            elif (self.game_state==1): #juego
                self.playing_state()
                self.update_Game_Object()
                if(self.player.life==0):
                    self.game_state=2
            elif (self.game_state==2): # menu Game over
                self.gameOver_state()

    def menu_state(self):
        self.screen.blit(STATE_MAIN, (0, 0))
        pygame.display.update()
    
    def playing_state(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 204))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def gameOver_state(self):
        self.screen.blit(STATE_GAMEOVER, (0, 0))
        self.score.comparation()
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        font = pygame.font.Font(FONT_STYLE, 60)
        text_component1 = font.render(str(self.score.score), True, (0,0,0))
        text_rect = text_component1.get_rect()
        text_rect.center = (half_screen_width+300, half_screen_height+120)

        text_component2 = font.render(str(self.score.best_score), True, (0,0,0))
        text_rect2 = text_component2.get_rect()
        text_rect2.center = (half_screen_width-300, half_screen_height+120)

        self.screen.blit(text_component1,text_rect)
        self.screen.blit(text_component2,text_rect2)
        pygame.display.update()
            
    def update_Game_Object(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.player.check_collision(self.obstacle_manager.cactus)
        self.player.check_collision(self.obstacle_manager.birds)
        self.player.check_collision(self.obstacle_manager.powerUp)

        self.player.check_colicion_fires(self.obstacle_manager.cactus)
        self.player.check_colicion_fires(self.obstacle_manager.birds)

        self.obstacle_manager.update(self)
        self.score.update(self)

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
        if pygame.key.get_pressed()[pygame.K_RIGHT] and self.game_state==0: # de menu a juego
            self.game_state=1
        elif pygame.key.get_pressed()[pygame.K_a] and self.game_state==2: # de gameOver a juego
            self.game_state=1
            self.player = Dinosaur()
            self.obstacle_manager = ObstacleManager()
            self.score.comparation()
            self.score.reset()
            self.game_speed = 20

    
    
    

        
        
