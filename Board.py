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
        self.winner = None

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
        if self.winner != None:
            return self.winner
        for winner in Board.winners:
            symbol = self.spaces[winner[0][0]][winner[0][1]]
            if symbol == None:
                empty_square_found = True
                continue
            if self.spaces[winner[0][0]][winner[0][1]] == self.spaces[winner[1][0]][winner[1][1]] and self.spaces[winner[0][0]][winner[0][1]] == self.spaces[winner[2][0]][winner[2][1]]:
                if symbol == "CAT":
                    continue
                self.winner = symbol
                return symbol
        
        for i in self.spaces:
            for j in i:
                if j == None:
                    return False
        self.winner = "CAT"
        return self.winner 


    def get_symbol_at_coord(self, x, y):
        return self.spaces[x][y]

   
