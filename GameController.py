import pygame
from Controller import Controller
from BoardController import BoardController
from MenuController import MenuController
from MenuView import MenuView
from GameInfoController import GameInfoController
from GameInfoView import GameInfoView
from Board import Board
from MasterBoardView import MasterBoardView


class GameController(Controller):

    def __init__(self):
        self.controllers = []
        self.close_game = False

    def init(self):
        pygame.display.set_caption("Ultimate TicTacToe")
        self.generateControllers()

    def generateControllers(self):
        main_surface = pygame.display.set_mode([MasterBoardView.MASTER_WIDTH, 1000])
        boards = [[Board() for i in range(3)] for j in range(3)]
        self.controllers.append(BoardController(Board(), boards, MasterBoardView(main_surface)))
        self.controllers.append(MenuController(MenuView(main_surface)))
        self.controllers.append(GameInfoController(GameInfoView(main_surface)))

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
