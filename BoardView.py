import pygame as pg
from View import View
from Color import Color
from Board import Board

class BoardView(View):

    def __init__(self, board, surface):
        self.board = board
        self.surface = surface
        self.children = []
        self.cell_width = self.surface.get_rect().width // 3
        for x in range(3):
            self.children.append([])
            for y in range(3):
                self.children[x].append(pg.Rect([x*self.cell_width, y * self.cell_width],[self.cell_width, self.cell_width]))

    def get_symbol(self, symbol, color, width):
        font = pg.font.Font("Chalkduster/Chalkduster.ttf", 230)
        text = font.render(symbol, True, color, Color.DARK_GREEN)
        text = pg.transform.scale(text, (width, width))
        text_rect = text.get_rect()
        text_rect.center = (width // 2, width // 2)
        return text, text_rect
                
    def update(self):
        self.surface.fill(Color.DARK_GREEN)
        winner = self.board.check_winner()
        if winner == "CAT":
            self._draw_cat()
            return self.surface
        if winner == "X" or winner == "O":
            width = self.surface.get_rect().width
            if winner == "X":
                color = Color.YELLOW 
            else:
                color = Color.WHITE
            text, text_rect = self.get_symbol(winner, color, width)
            self.surface.blit(text, text_rect)
            return self.surface
        for x in range(3):
            for y in range(3):
                rect = self.children[x][y]
                s = pg.Surface((rect.width, rect.height))
                s.fill(Color.DARK_GREEN)
                symbol = self.board.get_symbol_at_coord(x,y)
                if isinstance(symbol, Board):
                    bv = BoardView(symbol, s)
                    s = bv.update()
                    if self.board.active_board == [x, y]:
                        self._highlight_board(s)
                elif symbol != None:
                    if [x, y] == self.board.last_play:
                        color = Color.RED
                    elif symbol == "X":
                        color = Color.YELLOW
                    else :
                        color = Color.WHITE
                    text, text_rect = self.get_symbol(symbol, color, self.cell_width)
                    s.blit(text, text_rect)
                self.surface.blit(s, rect)
        self._draw_grid(1,1)
        self._draw_current_player()
        return self.surface


    def _draw_current_player(self):
        font = pg.font.Font('Chalkduster/Chalkduster.ttf', 32)
        if self.board.current_player == "X":
            color = Color.YELLOW
        else:
            color = Color.WHITE
        text = font.render('Current Player: ' + self.board.current_player, True, color, Color.DARK_GREEN)
        textRect = pg.Rect((0,900),(400, 60))
        textRect.center = (self.surface.get_rect().width // 2, 930)
        self.surface.blit(text, textRect)


    def _draw_cat(self):
        width = self.surface.get_rect().width
        surface = pg.Surface((width, width))
        surface.fill(Color.DARK_GREEN)
        cat_image = pg.image.load('cat.png').convert_alpha()
        cat_image = pg.transform.scale(cat_image, (width, width))
        surface.blit(cat_image, cat_image.get_rect(center = (width // 2, width // 2)))
        self.surface.blit(surface, surface.get_rect())


    def _draw_grid(self, x, y):
        margin = 15
        pg.draw.line(
            self.surface, 
            (Color.L_GREY), 
            [self.cell_width, margin], 
            [self.cell_width, self.cell_width * 3 - margin], 
            self.cell_width // 30)
        pg.draw.line(
            self.surface, 
            (Color.L_GREY), 
            [self.cell_width * 2, margin], 
            [self.cell_width * 2, self.cell_width * 3-margin], 
            self.cell_width // 30)
        pg.draw.line(
            self.surface, 
            (Color.L_GREY), 
            [margin, self.cell_width], 
            [self.cell_width * 3 - margin, self.cell_width], 
            self.cell_width // 30)
        pg.draw.line(
            self.surface, 
            (Color.L_GREY), [margin, self.cell_width * 2], 
            [self.cell_width * 3 - margin, self.cell_width * 2], 
            self.cell_width // 30)

    def _highlight_board(self, s):
        r = s.get_rect()
        pg.draw.rect(s, Color.GREEN, r, 15)
