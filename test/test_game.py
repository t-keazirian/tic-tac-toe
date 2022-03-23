import unittest
from unittest.mock import patch

from src.game import Game


class TestGame(unittest.TestCase):

    # mocks print
    @patch("builtins.print")
    def test_prompt_x_for_first_turn(self, mock_print):
        game = Game()
        total_marks_on_board = 0
        game.get_prompt(total_marks_on_board)
        mock_print.assert_called_with("Player X - enter a number to place your mark")

    @patch("builtins.print")
    def test_prompt_o_for_second_turn(self, mock_print):
        game = Game()
        total_marks_on_board = 1
        game.get_prompt(total_marks_on_board)
        mock_print.assert_called_with("Player O - enter a number to place your mark")

    @patch("builtins.print")
    def test_prompt_x_for_third_turn(self, mock_print):
        game = Game()
        total_marks_on_board = 2
        game.get_prompt(total_marks_on_board)
        mock_print.assert_called_with("Player X - enter a number to place your mark")

    @patch("builtins.print")
    def test_full_board_game_over(self, mock_print):
        game = Game()
        total_marks_on_board = 9
        game.get_prompt(total_marks_on_board)
        mock_print.assert_called_with("Game Over!")

    def test_takes_in_user_input_returns_integer(self):
        game = Game()
        user_input = game.convert_input_to_integer("5")
        output = 5
        self.assertEqual(user_input, output)

    # mocks user input
    @patch("builtins.input", side_effect=["3"])
    def test_gets_user_input(self, mock_input):
        game = Game()
        output = game.get_user_input()
        self.assertEqual(output, "3")

    @patch("builtins.input", side_effect=["3"])
    def test_gets_user_input_returns_string(self, mock_input):
        game = Game()
        output = type(game.get_user_input())
        self.assertEqual(output, str)

    @patch("builtins.input", side_effect=["5"])
    def test_gets_user_input_function_not_returning_false_positive(self, mock_input):
        game = Game()
        output = game.get_user_input()
        self.assertNotEqual(output, "3")
