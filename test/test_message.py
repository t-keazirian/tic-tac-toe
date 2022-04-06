import unittest
from unittest.mock import patch

from src.message import Message


class TestMessage(unittest.TestCase):
    @patch("builtins.print")
    def test_welcome_message_prints_to_console(self, mock_print):
        message = Message()
        message.display_welcome_message()
        mock_print.assert_called_with("Welcome to Tic Tac Toe")

    @patch("builtins.print")
    def test_game_over_prints_to_console(self, mock_print):
        message = Message()
        message.display_game_over_message()
        mock_print.assert_called_with("Game Over!")

    @patch("builtins.print")
    def test_X_player_is_prompted_for_move_when_is_current_player(self, mock_print):
        message = Message()
        current_player = "X"
        message.display_prompt_message_for_move(current_player)
        mock_print.assert_called_with(
            f"Player {current_player} - enter a number to place your mark"
        )

    @patch("builtins.print")
    def test_display_formatted_board(self, mock_print):
        message = Message()
        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        message.display_formatted_board(board)
        mock_print.assert_called_with(
            "1 | 2 | 3\n--+--+--\n4 | 5 | 6\n--+--+--\n7 | 8 | 9",
        )

    @patch("builtins.print")
    def test_display_spot_taken_message(self, mock_print):
        message = Message()
        message.display_spot_taken_message()
        mock_print.assert_called_with(
            "That spot is already occupied. Please choose another spot on the board."
        )

    @patch("builtins.print")
    def test_display_winner_message_with_correct_mark_as_winner(self, mock_print):
        message = Message()
        winner = "X"
        message.display_winner_message(winner)
        mock_print.assert_called_with(f"Congrats Player {winner} - you are the winner!")

    @patch("builtins.print")
    def test_display_incorrect_input_message(self, mock_print):
        message = Message()
        message.display_incorrect_input_message()
        mock_print.assert_called_with(
            "That input is incorrect. Please input a number 1-9."
        )
