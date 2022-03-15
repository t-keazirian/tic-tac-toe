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

    def test_handle_prompt_message(self):
        game = Game()
        self.assertEqual(
            "Choose a number 1-9 to input your player: ", game.handle_prompt_message()
        )

    def test_X_displays_in_index_0_when_1_is_inputted(self):
        game = Game()
        Game().handle_first_player()
        self.assertEqual(
            "X | 2 | 3\n--+--+--\n4 | 5 | 6\n--+--+--\n7 | 8 | 9",
            game.initialize_board(),
        )
