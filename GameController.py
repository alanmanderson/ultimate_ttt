import pygame as pg
from Controller import Controller
from BoardController import BoardController
from MenuController import MenuController
from MenuView import MenuView
from Board import Board
from BoardView import BoardView
from Event import Event

class GameController(Controller):

    def __init__(self):
        self.controllers = []
        self.close_game = False
        self.main_surface = None
        self.board_surface = None
        self.board_rect = None
        self.menu_surface = None
        self.menu_rect = None

    def init(self):
        pg.init()
        pg.display.set_caption("Ultimate TicTacToe")
        self.generateControllers()

    def generateControllers(self):
        self.main_surface = pg.display.set_mode([900, 1000])
        self.board_surface = pg.Surface((900,1000))
        self.board_rect = pg.Rect([0, 23], [900,900])
        self.menu_surface = pg.Surface((900, 23))
        self.menu_rect = pg.Rect([0, 0], [900, 23])
        master_board = Board(True)
        self.controllers.append(BoardController(master_board, BoardView(master_board, self.board_surface)))
        self.controllers.append(MenuController(MenuView(self.menu_surface)))

    def update_ui(self):
        for c in self.controllers:
            c.update_ui()
        self.main_surface.blit(self.board_surface, (0,23))
        self.main_surface.blit(self.menu_surface, (0, 0))
        pg.display.flip()

    def run_event_loop(self):
        for event in pg.event.get():
            self.handle_event(event)

    def handle_event(self, event):
        if event.type == pg.QUIT or event.type == Event.QUIT_GAME_EVENT:
            self.close_game = True
            return
        if event.type == pg.KEYDOWN and event.key == pg.K_q:
            self.close_game = True
            return
        if event.type == pg.MOUSEBUTTONUP and event.button == 1:
            mouse_pos = pg.mouse.get_pos()
            if self.board_rect.collidepoint(mouse_pos):
                new_event = pg.event.Event(Event.BOARD_CLICK_EVENT, {'pos': (mouse_pos[0], mouse_pos[1] - 23)})
                self.controllers[0].handle_event(new_event)
            elif self.menu_rect.collidepoint(mouse_pos):
                new_event = pg.event.Event(Event.MENU_CLICK_EVENT, event.__dict__)
                self.controllers[1].handle_event(new_event)
        for c in self.controllers:
            c.handle_event(event)
