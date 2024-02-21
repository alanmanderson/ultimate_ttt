import pygame

class View:
    MASTER_WIDTH = 900
    PURPLE = (245,175,255)
    BLUE = (0,43,255)
    BLACK = (0,0,0)
    WHITE = (0,0,0)
    GREEN = (0, 201, 47)
    RED = (255,0,0)
    def __init__(self):
        pygame.init()
        self.game = pygame.display.set_mode([View.MASTER_WIDTH, 1000])
        self.game.fill(View.PURPLE)

    def print_game_info(self):
        x, y = (0, 900)
        font = pygame.font.SysFont('chalkduster', 32)
        text = font.render('Current Player: ' + current_player, True, white, blue)
        text_button = font.render('New Game ', True, white, blue)
        textRect = text.get_rect()
        text_buttonRect = text_button.get_rect()
        textRect.center = (master_board_width / 2 + x, y + 20)
        game.blit(text, textRect)
        text_buttonRect.center = (master_board_width / 2 + x, y + 50)
        game.blit(text_button, text_buttonRect)
