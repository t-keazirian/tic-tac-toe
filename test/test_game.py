import unittest
from unittest.mock import patch

from src.board import Board
from src.game import Game
from src.message import Message


class TestGame(unittest.TestCase):
    def test_get_formatted_board_with_real_values(self):
        game = Game()
        self.assertEqual(
            "1 | 2 | 3\n--+--+--\n4 | 5 | 6\n--+--+--\n7 | 8 | 9",
            game.get_formatted_board(),
        )

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

    def test_X_is_placed_in_index_0_with_input_1(self):
        game = Game()
        board = Board()
        current_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        user_input = 1
        total_marks_on_board = 0
        current_player = board.get_current_player(total_marks_on_board)
        board.place_mark_on_board(user_input, current_board, total_marks_on_board)
        self.assertEqual(current_board[0], current_player)

    def test_O_is_placed_in_index_1_with_input_2(self):
        game = Game()
        board = Board()
        current_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        user_input = 2
        total_marks_on_board = 1
        current_player = board.get_current_player(total_marks_on_board)
        board.place_mark_on_board(user_input, current_board, total_marks_on_board)
        self.assertEqual(current_board[1], current_player)

    def test_X_is_placed_in_index_2_with_input_3(self):
        game = Game()
        board = Board()
        current_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        user_input = 3
        total_marks_on_board = 2
        current_player = board.get_current_player(total_marks_on_board)
        board.place_mark_on_board(user_input, current_board, total_marks_on_board)
        self.assertEqual(current_board[2], current_player)

    def test_takes_in_user_input_returns_integer(self):
        game = Game()
        user_input = game.convert_input_to_integer("5")
        output = 5
        self.assertEqual(user_input, output)

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
