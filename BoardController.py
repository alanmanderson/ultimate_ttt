from Controller import Controller
from Color import Color
from Event import Event
import math
import random

class BoardController(Controller):
    master_board_width = 900
    
    def __init__(self, master_board, view):
        self.master_board = master_board
        self.view = view
        self.game_over = False
        self.current_board = None


    def update_ui(self):
        self.update_view()


    def handle_event(self, event):
        if event.type == Event.BOARD_CLICK_EVENT:
            self.handle_left_click_event(event)
        elif event.type == Event.RESTART_GAME_EVENT:
            self.master_board.restart()


    def get_board_coordinate_from_x_y(self, x, y):
        game_width = BoardController.master_board_width / 3
        square_width = game_width / 3
        board_x = math.floor(x/game_width)
        board_y = math.floor(y/game_width)
        square_x = math.floor((x - board_x * game_width)/square_width)
        square_y = math.floor((y - board_y * game_width)/square_width)
        return [board_x, board_y], [square_x, square_y]


    def get_top_left_from_board_square_coords(self, board_coords, square_coords, x, y):
        game_width = BoardController.master_board_width / 3
        board_x = math.floor(x/game_width)
        board_y = math.floor(y/game_width)
        game_width = BoardController.master_board_width / 3
        square_width = game_width / 3
        square_x = board_coords[0] * game_width + square_coords[0] * square_width + 10 
        square_y = board_coords[1] * game_width + square_coords[1] * square_width + 10 
        return (square_x, square_y)


    def is_game_over(self):
        return self.game_over


    def is_click_on_board (self, pos):
        return pos[0] >= 0 and pos[0] < 900 and pos[1] >= 0 and pos[1] < 900


    def handle_left_click_event(self, event):
        if not self.is_click_on_board(event.pos):
            return
        board_coord, square_coord = self.get_board_coordinate_from_x_y(event.pos[0], event.pos[1])
        success = self.master_board.play([board_coord, square_coord])
        if not success:
            return


    def update_view(self):
        self.view.update()

    def save_game(self):
        pass
