from Player import Player
import random
import time

class AiPlayer(Player):

    def play(self, board):
        if board.check_winner():
            return None
        time.sleep(1)
        available_moves = []
        if board.active_board != None:
            x1, y1 = board.active_board
            for i in range(3):
                for j in range(3):
                    if board.spaces[x1][y1].get_symbol_at_coord(i, j) == None:
                        available_moves.append([board.active_board, [i,j]])
        else:
            for x1 in range(3):
                for y1 in range(3):
                    for x2 in range(3):
                        for y2 in range(3):
                            if board.spaces[x1][y1].get_symbol_at_coord(x2,y2) == None:
                                available_moves.append([[x1,y1], [x2, y2]])
        if len(available_moves) == 0:
            raise Exception("No available moves")
        idx = random.randint(0, len(available_moves) - 1)
        return available_moves[idx]

