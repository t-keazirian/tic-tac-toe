import unittest

from src.game import Game


class TestGame(unittest.TestCase):
    def test_welcome_message(self):
        game = Game()
        self.assertEqual("Welcome to Tic Tac Toe", game.get_welcome_message())

    def test_initialize_board_with_real_values(self):
        game = Game()
        self.assertEqual(
            "1 | 2 | 3\n--+--+--\n4 | 5 | 6\n--+--+--\n7 | 8 | 9",
            game.initialize_board(),
        )
