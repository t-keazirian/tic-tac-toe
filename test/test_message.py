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
    def test_player_is_prompted_for_move(self, mock_print):
        message = Message()
        message.display_prompt_message_for_move()
        mock_print.assert_called_with("Player X - enter a number to place your mark")
