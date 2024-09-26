import pygame as pg
import os

class FileSelector:
    def __init__(self, path, width, height, extension = None):
        self.path = path
        self.extension = extension
        self.width = width
        self.height = height
        files = os.listdir(self.path)
        self.files = [f for f in files if os.path.isfile(self.path + '/' + f) and self.extension == None or f.endswith(self.extension)]
        self.surface = pg.Surface([width, height])
        self.selected_pos = None
        self.scroll_pos = 0
        
    def select_at(pos):
        self.selected_pos = pos

    def increment_scroll_pos(self, dy):
        self.scroll_pos = max(min(self.scroll_pos + dy, self.height - 20 * (len(self.files) - 1)), -20*(len(self.files) - 1))

    def update(self):
        #font = pg.font.Font("Chalkduster/Chalkduster.ttf", 14)
        font = pg.font.SysFont('menlo', 14)
        dy = self.scroll_pos
        mouse_pos = pg.mouse.get_pos()
        for f in self.files:
            container = pg.Surface([self.surface.get_rect().width, 20])
            cont_rect = container.get_rect()
            cont_rect.move_ip(0, dy)
            bg = [0,0,0]
            if self.selected_pos and cont_rect.collidepoint(self.selected_pos):
                bg = [20,20,20]
            txt_surface = font.render(f, True, [255,255,255], bg)
            container.blit(txt_surface, txt_surface.get_rect())
            if cont_rect.collidepoint(mouse_pos):
                pg.draw.rect(container, [0, 200, 200], pg.Rect(0,0,cont_rect.width, cont_rect.height), 2)
            self.surface.blit(container, cont_rect)
            dy += 20
        return self.surface
