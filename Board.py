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
    
    def __init__(self):
        self.spaces = [[None for i in range(0,3)] for j in range(0,3)]

    def play(self, symbol, x, y):
        if self.check_winner():
            return False
        if x >= 3 or y >= 3:
            return False
        if self.spaces[x][y] != None:
            return False
        self.spaces[x][y] = symbol
        return True

    def check_winner(self):
        for winner in Board.winners:
            symbol = self.spaces[winner[0][0]][winner[0][1]]
            if symbol == None:
                continue
            if self.spaces[winner[0][0]][winner[0][1]] == self.spaces[winner[1][0]][winner[1][1]] and self.spaces[winner[0][0]][winner[0][1]] == self.spaces[winner[2][0]][winner[2][1]]:
                   return symbol
        return False

    def get_symbol_at_coord(self, x, y):
        return self.spaces[x][y]
