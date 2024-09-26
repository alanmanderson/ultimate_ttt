import unittest
from AiPlayer import AiPlayer
from Board import Board

class TestAiPlayer(unittest.TestCase):

    def test_play(self):
        ai = AiPlayer("X", "Test")
        ai.set_symbol("X")
        p = AiPlayer("O", "O")
        p.set_symbol("O")
        b = Board(True, [ai, p])
        b.play(((0, 0), (0, 0)))
        b.play(((0, 0), (0, 1)))
        b.play(((0, 0), (1, 1)))
        b.play(((0, 0), (1, 0)))
        b.play(((0, 0), (2, 2)))
        for i in range(20000):
            play = ai.play(board)
            if play[0] == (0, 0):
                print(play)
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
