import pygame as pg
from View import View
from Color import Color

class MenuView(View):

    def __init__(self, main_surface):
        self.main_surface = main_surface
        #self.menu_items = {"Game": ["Restart", "Save", "Load", "Quit"]}
        #self.menu_items = {"Restart":[], "Quit":[]}
        self.menu_items = {"Restart": [], "Save":[], "Load": [], "Quit": []}
        self.menu_rects = {"Restart": None, "Save": None, "Load": None, "Quit": None}
        self.selected_item = None

    def update(self):
        self.main_surface.fill(Color.DARK_GREEN)
        pg.draw.rect(self.main_surface, Color.DARK_GREEN, [250, 1000, 100, 100])
        font = pg.font.Font('Chalkduster/Chalkduster.ttf', 18)
        mouse_pos = pg.mouse.get_pos()
        for i, item in enumerate(self.menu_items):
            fore = Color.WHITE
            back = Color.DARK_GREEN
            text = font.render(item, True, fore, back)
            text_rect = text.get_rect()
            text_rect.move_ip(i*100, 0)
            self.menu_rects[item] = text_rect
            hover = self.menu_rects[item].collidepoint(mouse_pos)
            if i == self.selected_item:
                fore = Color.YELLOW
                back = Color.RED
            elif hover:
                fore = Color.YELLOW
            text = font.render(item, True, fore, back)
            self.main_surface.blit(text, text_rect)

