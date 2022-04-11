import unittest
from unittest.mock import patch

from src.user_interface import UserInterface


class MockMessage:
    def incorrect_board_input(self):
        return "Incorrect board input"


class TestUserInterface(unittest.TestCase):
    @patch("builtins.print")
    def test_display_message_prints_welcome_message_passed_in(self, mock_print):
        user_interface = UserInterface()
        message = "Welcome to Tic Tac Toe"
        user_interface.display_message(message)
        mock_print.assert_called_with("Welcome to Tic Tac Toe")

    @patch("builtins.input", side_effect=["3"])
    def test_get_user_input_returns_input(self, mock_input):
        user_interface = UserInterface()
        result = user_interface.get_user_input()
        self.assertEqual("3", result)

    @patch("builtins.input", side_effect=["5"])
    def test_gets_user_input_function_not_returning_false_positive(self, mock_input):
        user_interface = UserInterface()
        output = user_interface.get_user_input()
        self.assertNotEqual(output, "3")

    @patch("builtins.input", side_effect=["Y"])
    def test_get_play_again_user_input_returns_input(self, mock_input):
        user_interface = UserInterface()
        output = user_interface.get_play_again_user_input()
        self.assertEqual("Y", output)
