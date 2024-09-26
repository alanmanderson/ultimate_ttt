from Controller import Controller
from Color import Color
from Event import Event
from Board import Board
import pygame as pg
import math
import random
import time
import json

class BoardController(Controller):
    master_board_width = 900
    
    def __init__(self, master_board, view):
        self.master_board = master_board
        self.view = view
        self.game_over = False
        self.current_board = None
        e = pg.event.Event(Event.NEXT_PLAYER_EVENT, {"player": self.master_board.get_current_player()})
        pg.event.post(e)


    def update_ui(self):
        self.update_view()


    def handle_event(self, event):
        if event.type == Event.BOARD_CLICK_EVENT:
            self.handle_left_click_event(event)
        elif event.type == Event.RESTART_GAME_EVENT:
            self.master_board.restart()
        elif event.type == Event.SAVE_GAME_EVENT:
            self.save_game_v2()
        elif event.type == Event.LOAD_GAME_EVENT:
            self.load_game_v2(event.fn)
        elif event.type == Event.PLAY_EVENT:
            if event.player == self.master_board.get_current_player():
                self.make_play(event.player, event.play)
        elif event.type == Event.NEXT_PLAYER_EVENT:
            play = event.player.play(self.master_board)
            print(play)
            if play != None:
                e = pg.event.Event(Event.PLAY_EVENT, {"player": event.player, "play": play})
                pg.event.post(e)


    def get_board_coordinate_from_x_y(self, x, y):
        game_width = BoardController.master_board_width / 3
        square_width = game_width / 3
        board_x = math.floor(x/game_width)
        board_y = math.floor(y/game_width)
        square_x = math.floor((x - board_x * game_width)/square_width)
        square_y = math.floor((y - board_y * game_width)/square_width)
        return [board_x, board_y], [square_x, square_y]


    def is_click_on_board (self, pos):
        return pos[0] >= 0 and pos[0] < 900 and pos[1] >= 0 and pos[1] < 900


    def handle_left_click_event(self, event):
        if not self.is_click_on_board(event.pos):
            return
        board_coord, square_coord = self.get_board_coordinate_from_x_y(event.pos[0], event.pos[1])
        e = pg.event.Event(Event.PLAY_EVENT, {'player': self.master_board.get_current_player(), 'play': [board_coord,
                                                                                                         square_coord]})
        pg.event.post(e)
        if self.master_board.check_winner():
            self.save_game_v2()


    def make_play(self, player, play):
        success = self.master_board.play(play)
        if not success:
            print("play: ", play)
            e = pg.event.Event(Event.NEXT_PLAYER_EVENT, {"player": player})
            pg.event.post(e)
        else:
            e = pg.event.Event(Event.NEXT_PLAYER_EVENT, {"player": self.master_board.get_current_player()})
            pg.event.post(e)


    def update_view(self):
        self.view.update()

    def _get_filename(self, version):
        winner = self.master_board.check_winner()
        if winner == False:
            winner = "IP"
        fn = "games_v"+str(version)+"/" + self.master_board.players[0].id + '_' + self.master_board.players[1].id + "_"
        fn += winner + "_" + str(int(time.time())) + '.ttt'
        return fn


    def save_game_v1(self):
        with open(self._get_filename(1), 'w') as fd:
            fd.write(json.dumps(self.master_board.moves))

    def save_game_v2(self):
        if len(self.master_board.moves) == 0:
            return
        state = []
        for x1 in range(3):
            for y1 in range(3):
                for x2 in range(3):
                    for y2 in range(3):
                        symbol = self.master_board.get_symbol_at_coord(x1, y1).get_symbol_at_coord(x2,y2)
                        if symbol == Board.X:
                            state.append(1)
                        elif symbol == Board.O:
                            state.append(255)
                        elif symbol == None:
                            state.append(0)
        with open(self._get_filename(2), 'wb') as fd:
            fd.write(bytes(bytearray(state)))
            #fd.write(b'\n')
            last_board, last_square = self.master_board.moves[-1]
            fd.write(bytes(bytearray(last_board)))
            #fd.write(b'\n')
            fd.write(bytes(bytearray(last_square)))


    def load_game_v1(self, fn):
        with open(fn, 'r') as fd:
            moves = json.loads(fd.read())
            self.master_board.initialize_by_moves(moves)

    def load_game_v2(self, fn):
        fn = 'games_v2/X_O_IP_1711645244.ttt'
        with open(fn, 'rb') as fd:
            data = list(fd.readline())
            state = data[0:-5]
            last_board = [data[-4], data[-3]]
            last_square = [data[-2], data[-1]]
            self.master_board.initialize_by_state(state, last_board, last_square)
