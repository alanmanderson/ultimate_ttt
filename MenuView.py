import pygame
from View import View
from Color import Color

class MenuView(View):

    def __init__(self, main_surface):
        self.main_surface = main_surface
        self.menu_items = {"Game": ["Restart", "Save", "Load", "Quit"]}
        self.selected_item = 0

    def update(self):
        pygame.draw.rect(self.main_surface, Color.DARK_GREEN, [250, 1000, 100, 100])
        font = font = pygame.font.Font('Chalkduster/Chalkduster.ttf', 18)
        for i, item in enumerate(self.menu_items):
            color = Color.WHITE if i == self.selected_item else Color.YELLOW
            text = font.render(item, True, color, Color.DARK_GREEN)
            text_rect = text.get_rect()
            self.main_surface.blit(text, text_rect)

