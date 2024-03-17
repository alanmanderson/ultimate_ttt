class Board:
    winners = [
            ((0,0),(0,1),(0,2)),
            ((1,0),(1,1),(1,2)),
            ((2,0),(2,1),(2,2)),
            ((0,0),(1,0),(2,0)),
            ((0,1),(1,1),(2,1)),
            ((0,2),(1,2),(2,2)),
            ((0,0),(1,1),(2,2)),
            ((2,0),(1,1),(0,2))
        ]
    X = "X"
    O = "O"
    CAT = "CAT"
    
    def __init__(self, is_recursive = False):
        if is_recursive:
            self.spaces = [[Board() for i in range(0,3)] for j in range(0,3)]
        else:
            self.spaces = [[None for i in range(0,3)] for j in range(0,3)]
        self.winner = None
        self.has_children = is_recursive
        self.last_play = None
        self.active_board = None
        self.current_player = Board.X

    def play(self, coordinates, symbol = None):
        if symbol is None:
            symbol = self.current_player
        if self.check_winner():
            return False
        x, y = coordinates[0]
        if x >= 3 or y >= 3:
            return False
        if len(coordinates) > 1:
            rest = coordinates[1:]
        if isinstance(self.spaces[x][y], Board):
            if self.active_board != None and self.active_board != [x,y]:
                return False
            success = self.spaces[x][y].play(rest, self.current_player)
            if success:
                if self.last_play != None:
                    last_board = self.last_play[0]
                    self.spaces[last_board[0]][last_board[1]].last_play = None
                self.spaces[x][y].last_play = rest[0]
                self.last_play = coordinates
                if self.spaces[rest[0][0]][rest[0][1]].check_winner():
                    self.active_board = None
                else:
                    self.active_board = rest[0]
                self.switch_current_player()
            return success
        if self.spaces[x][y] != None:
            return False
        self.spaces[x][y] = symbol
        return True

    def check_winner(self):
        if self.winner != None:
            return self.winner
        spaces = [[],[],[]]
        for i in range(3):
            for j in range(3):
                spaces[i].append(self.spaces[i][j])
                if isinstance(spaces[i][j], Board):
                    spaces[i][j] = self.spaces[i][j].check_winner()
        for winner in Board.winners:
            symbols = []
            symbols.append(spaces[winner[0][0]][winner[0][1]])
            symbols.append(spaces[winner[1][0]][winner[1][1]])
            symbols.append(spaces[winner[2][0]][winner[2][1]])
            if symbols[0] == None:
                empty_square_found = True
                continue
            if symbols[0] == symbols[1] and symbols[0] == symbols[2]:
                if symbols[0] == "CAT" or symbols[0] == False:
                    continue
                self.winner = symbols[0]
                return symbols[0]
        
        for i in self.spaces:
            for j in i:
                if j == None or isinstance(j, Board):
                    return False
        self.winner = Board.CAT
        return self.winner 

    def switch_current_player(self):
        if self.current_player == Board.X:
            self.current_player = Board.O
        else:
            self.current_player = Board.X


    def get_symbol_at_coord(self, x, y):
        return self.spaces[x][y]


    def restart(self):
        if self.has_children:
            self.spaces = [[Board() for i in range(0,3)] for j in range(0,3)]
        else:
            self.spaces = [[None for i in range(0,3)] for j in range(0,3)]
        self.winner = None
        self.last_play = None
        self.active_board = None

