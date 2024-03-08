import pygame
from View import View
from ButtonView import ButtonView
from Color import Color


class MasterBoardView(View):
    MASTER_WIDTH = 900

    def __init__(self):
        pygame.init()
        self.game = pygame.display.set_mode([MasterBoardView.MASTER_WIDTH, 1000])
        self.game.fill(Color.DARK_GREEN)
        self.save_game_button = ButtonView(0, 900, 200, 100, Color.WHITE, Color.DARK_GREEN, "Save Game", 32)
#        self.print_debug_lines()

    def print_debug_lines(self):
        pygame.draw.line(self.game, (200, 200, 200), (0, 100), (900, 100), 1)
        pygame.draw.line(self.game, (200, 200, 200), (0, 200), (900, 200), 1)
        pygame.draw.line(self.game, (200, 200, 200), (0, 300), (900, 300), 1)
        pygame.draw.line(self.game, (200, 200, 200), (0, 400), (900, 400), 1)
        pygame.draw.line(self.game, (200, 200, 200), (0, 500), (900, 500), 1)
        pygame.draw.line(self.game, (200, 200, 200), (0, 600), (900, 600), 1)
        pygame.draw.line(self.game, (200, 200, 200), (0, 700), (900, 700), 1)
        pygame.draw.line(self.game, (200, 200, 200), (0, 800), (900, 800), 1)
        pygame.draw.line(self.game, (200, 200, 200), (0, 900), (900, 900), 1)
        pygame.draw.line(self.game, (200, 200, 200), (100, 0), (100, 900), 1)
        pygame.draw.line(self.game, (200, 200, 200), (200, 0), (200, 900), 1)
        pygame.draw.line(self.game, (200, 200, 200), (300, 0), (300, 900), 1)
        pygame.draw.line(self.game, (200, 200, 200), (400, 0), (400, 900), 1)
        pygame.draw.line(self.game, (200, 200, 200), (500, 0), (500, 900), 1)
        pygame.draw.line(self.game, (200, 200, 200), (600, 0), (600, 900), 1)
        pygame.draw.line(self.game, (200, 200, 200), (700, 0), (700, 900), 1)
        pygame.draw.line(self.game, (200, 200, 200), (800, 0), (800, 900), 1)
        pygame.draw.line(self.game, (200, 200, 200), (900, 0), (900, 900), 1)
        

    def print_game_info(self, current_player):
        x, y = (0, 900)
        font = pygame.font.SysFont('chalkduster', 32)
        text = font.render('Current Player: ' + current_player, True, Color.WHITE, Color.DARK_GREEN)
        text_button = font.render('New Game ', True, Color.WHITE, Color.DARK_GREEN)
        textRect = text.get_rect()
        text_buttonRect = text_button.get_rect()
        textRect.center = (MasterBoardView.MASTER_WIDTH / 2 + x, y + 20)
        self.game.blit(text, textRect)
        text_buttonRect.center = (MasterBoardView.MASTER_WIDTH / 2 + x, y + 50)
        self.game.blit(text_button, text_buttonRect)
        save_game, save_game_rect = self.save_game_button.print()
        self.game.blit(save_game, save_game_rect)
        
        
    def print_board( self, x, y, width, color):
        margin = width // 20
        pygame.draw.line(self.game,(color),(x+ width // 3,y + margin),(x+width // 3,y+width - margin),10)
        pygame.draw.line(self.game,(color),(x+ width // 3 * 2,y + margin),(x+2*width // 3,y + width - margin),10)
        pygame.draw.line(self.game,(color),(x + margin,y+1/3*width),(x+width - margin,y+1/3*width),10)
        pygame.draw.line(self.game,(color),(x + margin,y+2/3*width),(x+width - margin,y+2/3*width),10)
        

    def draw_x(self, x, y, width, thickness,color):
        if width <= 100:
            font_size = 68
        else:
            font_size = 230
        font = pygame.font.SysFont('chalkduster', font_size)
        font_surface = font.render('X', True, color, Color.DARK_GREEN)
        font_rect = font_surface.get_rect()
        font_rect.center = (x + width // 2, y + width // 2)
        self.game.blit(font_surface, font_rect)
        
        
    def draw_o(self,x, y, width, thickness,color):
        if width <= 100:
            font_size = 68
        else:
            font_size = 230
        font = pygame.font.SysFont('chalkduster', font_size)
        text = font.render('O', True, color, Color.DARK_GREEN)
        textRect = text.get_rect()
        textRect.center = (x + width // 2, y + width // 2)
        self.game.blit(text, textRect)

    def draw_cat(self, x, y, width):
        surface = pygame.Surface((width, width))
        surface.fill(Color.DARK_GREEN)
        cat_image = pygame.image.load('cat.png').convert_alpha()
        cat_image = pygame.transform.scale(cat_image, (width, width))
        surface.blit(cat_image, cat_image.get_rect(center = (width // 2, width // 2)))
        self.game.blit(surface, pygame.Rect(x, y, width, width))
        
        
    def draw_square(self, x,y,width,color):
        pygame.draw.line(self.game,(color),(x,y),(x+width,y),10)
        pygame.draw.line(self.game,(color),(x,y),(x,y+width),10)
        pygame.draw.line(self.game,(color),(x+width,y),(x+width,y+width),10)
        pygame.draw.line(self.game,(color),(x,y+width),(x+width,y+width),10)

    def handle_mouse_pos(self):
        mouse_pos = pygame.mouse.get_pos()
        self.save_game_button.handle_mouse_pos(mouse_pos[0], mouse_pos[1])

    def update(self):
        pygame.display.flip()

