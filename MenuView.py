import pygame as pg
from View import View
from Color import Color

class MenuView(View):

    def __init__(self, main_surface):
        self.main_surface = main_surface
        #self.menu_items = {"Game": ["Restart", "Save", "Load", "Quit"]}
        self.menu_items = {"Restart":[], "Quit":[]}
        self.selected_item = None

    def update(self):
        self.main_surface.fill(Color.DARK_GREEN)
        pg.draw.rect(self.main_surface, Color.DARK_GREEN, [250, 1000, 100, 100])
        font = pg.font.Font('Chalkduster/Chalkduster.ttf', 18)
        for i, item in enumerate(self.menu_items):
            color = Color.YELLOW if i == self.selected_item else Color.WHITE
            text = font.render(item, True, color, Color.DARK_GREEN)
            text_rect = text.get_rect()
            text_rect.move_ip(i*100, 0)
            self.main_surface.blit(text, text_rect)

