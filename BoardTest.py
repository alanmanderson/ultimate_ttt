import unittest
from Board import Board

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_check_win_cat(self):
        b = Board()
        b.play("x", 0, 0)
        b.play("o", 0, 1)
        b.play("x", 0, 2)
        b.play("x", 1, 2)
        b.play("o", 1, 1)
        b.play("x", 1, 0)
        b.play("o", 2, 2)
        b.play("x", 2, 1)
        b.play("o", 2, 0)
        self.assertEqual(b.check_winner(), "CAT")

        b = Board()
        b.play("x", 0, 0)
        b.play("o", 0, 1)
        b.play("x", 0, 2)
        b.play("o", 1, 2)
        b.play("x", 1, 1)
        b.play("o", 1, 0)
        b.play("o", 2, 2)
        b.play("x", 2, 1)
        b.play("o", 2, 0)
        self.assertEqual(b.check_winner(), "CAT")

        b = Board()
        b.play("x", 0, 0)
        b.play("o", 0, 1)
        b.play("o", 0, 2)
        b.play("o", 1, 0)
        b.play("x", 1, 1)
        b.play("x", 1, 2)
        b.play("o", 2, 0)
        b.play("x", 2, 1)
        b.play("o", 2, 2)
        self.assertEqual(b.check_winner(), "CAT")

    def test_win_check_win_false(self):
        b = Board()
        b.play("x", 1, 1)
        b.play("x", 2, 2)
        self.assertEqual(b.check_winner(), False)

        b = Board()
        b.play("x", 1, 1)
        b.play("x", 2, 2)
        self.assertEqual(b.check_winner(), False)

    def test_check_win_win(self):
        b = Board()
        b.play("x", 0, 0)
        b.play("x", 0, 1)
        b.play("x", 0, 2)
        self.assertEqual(b.check_winner(), "x")

        b = Board()
        b.play("o", 0, 0)
        b.play("o", 1, 1)
        b.play("o", 2, 2)
        self.assertEqual(b.check_winner(), "o")

        b = Board()
        b.play("x", 0, 2)
        b.play("x", 1, 1)
        b.play("x", 2, 0)
        self.assertEqual(b.check_winner(), "x")

        b = Board()
        b.play("x", 0, 2)
        b.play("x", 1, 2)
        b.play("x", 2, 2)
        self.assertEqual(b.check_winner(), "x")

    def test_get_symbol_at_coord(self):
        b = Board()
        b.play("x", 0, 0)
        b.play("o", 1, 1)
        b.play("+", 2, 2)
        self.assertEqual(b.get_symbol_at_coord(0, 0), "x")
        self.assertEqual(b.get_symbol_at_coord(1, 1), "o")
        self.assertEqual(b.get_symbol_at_coord(2, 2), "+")
        self.assertEqual(b.get_symbol_at_coord(0, 2), None)
    
if __name__ == '__main__':
    unittest.main()
