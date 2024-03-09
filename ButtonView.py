import pygame
from View import View

class ButtonView(View):
    def __init__(self, x, y, width, height, foreground, background, text, font_size):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.foreground = foreground
        self.background = background
        self.text = text
        self.font_size = font_size
        self.hover = False

    def update(self):
        self.print()

    def print(self):
        font = pygame.font.Font('Chalkduster/Chalkduster.ttf', self.font_size)
        if self.hover:
            text = font.render(self.text, True, self.background, self.foreground)
        else:
            text = font.render(self.text, True, self.foreground, self.background)
        text_buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        text_buttonRect.center = (self.x + self.width / 2, self.y + self.height / 2)
        return text, text_buttonRect

    def handle_mouse_pos(self, x, y):
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            self.hover = True
        else:
            self.hover = False

    def click(self):
        pass
