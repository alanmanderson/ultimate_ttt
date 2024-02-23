import pygame
from Color import Color


class View:
    MASTER_WIDTH = 900

    def __init__(self):
        pygame.init()
        self.game = pygame.display.set_mode([View.MASTER_WIDTH, 1000])
        self.game.fill(Color.PURPLE)

    def print_game_info(self, current_player):
        x, y = (0, 900)
        font = pygame.font.SysFont('chalkduster', 32)
        text = font.render('Current Player: ' + current_player, True, Color.WHITE, Color.PURPLE)
        text_button = font.render('New Game ', True, Color.WHITE, Color.PURPLE)
        textRect = text.get_rect()
        text_buttonRect = text_button.get_rect()
        textRect.center = (View.MASTER_WIDTH / 2 + x, y + 20)
        self.game.blit(text, textRect)
        text_buttonRect.center = (View.MASTER_WIDTH / 2 + x, y + 50)
        self.game.blit(text_button, text_buttonRect)
        
    def print_board( self, x, y, width, color):
        pygame.draw.line(self.game,(color),(x+1/3*width,y),(x+1/3*width,y+width),10)
        pygame.draw.line(self.game,(color),(x+2/3*width,y),(x+2/3*width,y+width),10)
        pygame.draw.line(self.game,(color),(x,y+1/3*width),(x+width,y+1/3*width),10)
        pygame.draw.line(self.game,(color),(x,y+2/3*width),(x+width,y+2/3*width),10)
        pygame.draw.rect(self.game, (70,70,70), pygame.Rect(0,0,100,100))
        #pygame.draw.rect(self.game, (90,90,90), pygame.Rect(100,0,100,100))
        pygame.draw.rect(self.game, (110,110,110), pygame.Rect(200,0,100,100))
        #pygame.draw.rect(self.game, (130,130,130), pygame.Rect(300,0,100,100))
        pygame.draw.rect(self.game, (150,150,150), pygame.Rect(400,0,100,100))
        #pygame.draw.rect(self.game, (170,170,170), pygame.Rect(500,0,100,100))
        pygame.draw.rect(self.game, (190,190,190), pygame.Rect(600,0,100,100))
        #pygame.draw.rect(self.game, (210,210,210), pygame.Rect(700,0,100,100))
        pygame.draw.rect(self.game, (230,230,230), pygame.Rect(800,0,100,100))
        pygame.draw.rect(self.game, (230,230,230), pygame.Rect(0,200,100,100))
        pygame.draw.rect(self.game, (230,230,230), pygame.Rect(0,400,100,100))
        pygame.draw.rect(self.game, (230,230,230), pygame.Rect(0,600,100,100))
        pygame.draw.rect(self.game, (230,230,230), pygame.Rect(0,800,100,100))

    def draw_x(self, x, y, width, thickness,color):
        pygame.draw.line(self.game,(color),(x,y),(x+width,y+width),thickness)
        pygame.draw.line(self.game,(color),(x+width,y),(x,y+width),thickness)
        
    def draw_o(self,x, y, width, thickness,color):
        width = 1/2*width
        pygame.draw.circle(self.game,color,(x+width,y+width),width,8)
        
    def draw_square(self, x,y,width,color):
        pygame.draw.line(self.game,(color),(x,y),(x+width,y),10)
        pygame.draw.line(self.game,(color),(x,y),(x,y+width),10)
        pygame.draw.line(self.game,(color),(x+width,y),(x+width,y+width),10)
        pygame.draw.line(self.game,(color),(x,y+width),(x+width,y+width),10)

    def update(self):
        pygame.display.flip()

