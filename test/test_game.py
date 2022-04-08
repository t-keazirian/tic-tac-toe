import unittest
from unittest.mock import patch

from src.game import Game


class MockMessage:
    def prompt_for_move(self, current_player):
        return f"Player {current_player} - prompt for turn"

    def game_over_message(self):
        return "Game over message"


class TestGame(unittest.TestCase):
    @patch("builtins.print")
    def test_prompt_x_for_first_turn(self, mock_print):
        mockMessage = MockMessage()
        game = Game(message=mockMessage)
        total_marks_on_board = 0
        game.get_prompt(total_marks_on_board)
        mock_print.assert_called_with("Player X - prompt for turn")

    @patch("builtins.print")
    def test_prompt_o_for_second_turn(self, mock_print):
        mockMessage = MockMessage()
        game = Game(message=mockMessage)
        total_marks_on_board = 1
        game.get_prompt(total_marks_on_board)
        mock_print.assert_called_with("Player O - prompt for turn")

    @patch("builtins.print")
    def test_prompt_x_for_third_turn(self, mock_print):
        mockMessage = MockMessage()
        game = Game(message=mockMessage)
        total_marks_on_board = 2
        game.get_prompt(total_marks_on_board)
        mock_print.assert_called_with("Player X - prompt for turn")

    @patch("builtins.print")
    def test_full_board_game_over(self, mock_print):
        mockMessage = MockMessage()
        game = Game(message=mockMessage)
        total_marks_on_board = 9
        game.get_prompt(total_marks_on_board)
        mock_print.assert_called_with("Game over message")

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
        winner = game.get_winning_mark(total_marks_on_board)
        self.assertEqual("X", winner)

    def test_if_current_player_is_X_then_O_wins(self):
        game = Game()
        total_marks_on_board = 6
        winner = game.get_winning_mark(total_marks_on_board)
        self.assertEqual("O", winner)
