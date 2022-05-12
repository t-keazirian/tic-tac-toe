import unittest
from unittest.mock import patch

from src.user_interface import UserInterface


class TestUserInterface(unittest.TestCase):
    def setUp(self):
        self.ui = UserInterface()

    @patch("builtins.print")
    def test_display_message_prints_welcome_message_passed_in(self, mock_print):
        message = "Welcome to Tic Tac Toe"

        self.ui.display_message(message)

        mock_print.assert_called_with("Welcome to Tic Tac Toe")

    @patch("builtins.print")
    def test_display_board_prints_board(self, mock_print):
        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        self.ui.display_board(board)

        mock_print.assert_called_with(["1", "2", "3", "4", "5", "6", "7", "8", "9"])

    @patch("builtins.input", side_effect=["3"])
    def test_get_user_input_returns_input(self, mock_input):
        result = self.ui.get_user_input()

        self.assertEqual("3", result)

    @patch("builtins.input", side_effect=["5"])
    def test_gets_user_input_function_not_returning_false_positive(self, mock_input):
        output = self.ui.get_user_input()

        self.assertNotEqual("3", output)
