import pygame
from View import View

class BoardView(View):

    def __init__(self, board, surface, top_left, width):
        self.board = board
        self.surface = surface
        self.top_left = top_left
        self.width = width

    def update(self):
        self.draw_board()

    def draw_board(self):
        x = top_left[0]
        y = top_left[1]
        pygame.draw.line(
            self.surface, 
            (color), 
            (x + 1 / 3 * self.width, y),(x + 1 / 3 * self.width, y + self.width),
            10
        )
        pygame.draw.line(self.surface, (color), (x+2/3*width,y),(x+2/3*width,y+width),10)
        pygame.draw.line(self.surface, (color), (x,y+1/3*width),(x+width,y+1/3*width),10)
        pygame.draw.line(self.surface, (color), (x,y+2/3*width),(x+width,y+2/3*width),10)
