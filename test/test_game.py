import unittest
from unittest.mock import patch

from src.board import Board
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

    @patch("builtins.input", side_effect=["1"])
    def test_process_user_input_returns_updated_board_when_1_is_inputted(
        self, mock_input
    ):
        game = Game()
        output = game.process_user_input()
        self.assertEqual(output, ["X", "2", "3", "4", "5", "6", "7", "8", "9"])

    @patch("builtins.input", side_effect=["2"])
    def test_process_user_input_returns_updated_board_when_2_is_inputted(
        self, mock_input
    ):
        game = Game()
        output = game.process_user_input()
        self.assertEqual(output, ["1", "X", "3", "4", "5", "6", "7", "8", "9"])

    def test_is_winner_returns_true_when_third_column_winner(self):
        game = Game()
        board = ["1", "2", "X", "4", "5", "X", "7", "8", "X"]
        winner = game.is_winner(board)
        self.assertEqual(True, winner)

    def test_is_winner_returns_true_when_first_column_winner(self):
        game = Game()
        board = ["X", "2", "3", "X", "5", "6", "X", "8", "9"]
        winner = game.is_winner(board)
        self.assertEqual(True, winner)

    def test_is_winner_returns_true_when_first_row_winner(self):
        game = Game()
        board = ["X", "X", "X", "4", "5", "6", "7", "8", "9"]
        winner = game.is_winner(board)
        self.assertEqual(True, winner)

    def test_is_winner_returns_false_when_not_three_in_row(self):
        game = Game()
        board = ["1", "X", "O", "X", "5", "6", "O", "8", "9"]
        winner = game.is_winner(board)
        self.assertEqual(False, winner)

    def test_board_is_marked_with_user_selection_when_no_marks_and_X_is_going_first(
        self,
    ):
        board = Board()
        current_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        new_board_with_marks = ["X", "2", "3", "4", "5", "6", "7", "8", "9"]
        user_input = 1
        self.assertEqual(
            new_board_with_marks,
            board.mark_board(user_input, current_board, "X"),
        )

    def test_board_is_marked_with_user_selection_when_one_mark_and_O_is_next_player(
        self,
    ):
        board = Board()
        current_board = ["X", "2", "3", "4", "5", "6", "7", "8", "9"]
        new_board_with_marks = ["X", "O", "3", "4", "5", "6", "7", "8", "9"]
        user_input = 2
        self.assertEqual(
            new_board_with_marks,
            board.mark_board(user_input, current_board, "O"),
        )

    def test_board_is_marked_with_user_selection_when_two_marks_and_X_is_next_player(
        self,
    ):
        board = Board()
        current_board = ["X", "O", "3", "4", "5", "6", "7", "8", "9"]
        new_board_with_marks = ["X", "O", "X", "4", "5", "6", "7", "8", "9"]
        user_input = 3
        self.assertEqual(
            new_board_with_marks,
            board.mark_board(user_input, current_board, "X"),
        )

    def test_zero_turns_player_x_goes_first(self):
        game = Game()
        total_marks_on_board = 0
        current_player = game.get_current_player(total_marks_on_board)
        self.assertEqual("X", current_player)

    def test_one_turn_player_o_goes_next(self):
        game = Game()
        total_marks_on_board = 1
        current_player = game.get_current_player(total_marks_on_board)
        self.assertEqual("O", current_player)

    def test_two_turn_player_x_goes_next(self):
        game = Game()
        total_marks_on_board = 2
        current_player = game.get_current_player(total_marks_on_board)
        self.assertEqual("X", current_player)

    def test_if_current_player_is_O_then_X_wins(self):
        game = Game()
        total_marks_on_board = 5
        winner = game.determine_winner(total_marks_on_board)
        self.assertEqual("X", winner)

    def test_if_current_player_is_X_then_O_wins(self):
        game = Game()
        total_marks_on_board = 6
        winner = game.determine_winner(total_marks_on_board)
        self.assertEqual("O", winner)
