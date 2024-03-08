import pygame
from Controller import Controller
from BoardController import BoardController
from MenuController import MenuController
from GameInfoController import GameInfoController
from Board import Board
from MasterBoardView import MasterBoardView

class GameController(Controller):

    def __init__(self):
        self.controllers = []
        self.close_game = False

    def generateControllers(self):
        boards = [[Board() for i in range(3)] for j in range(3)]
        self.controllers.append(BoardController(Board(), boards, MasterBoardView()))
        self.controllers.append(MenuController())
        self.controllers.append(GameInfoController())

    def update_ui(self):
        for c in self.controllers:
            c.update_ui()

    def run_event_loop(self):
        for event in pygame.event.get():
            self.handle_event(event)

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.close_game = True
            pygame.quit()
            return
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            self.close_game = True
            return
        for c in self.controllers:
            c.handle_event(event)
