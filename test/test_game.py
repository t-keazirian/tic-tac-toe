import unittest
from unittest.mock import patch

from src.game import Game


class TestGame(unittest.TestCase):
    def test_dummy_test(self):
        subject = Game().hello_world
        self.assertEqual(subject(), "Hello, world!")

    @patch("builtins.print")
    def test_welcome_message(self, mock_print):
        Game().display_welcome_message()
        mock_print.assert_called_with("Welcome to Tic Tac Toe")

    @patch("builtins.print")
    def test_print_board(self, mock_print):
        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        Game().display_board()
        mock_print.assert_called_with(
            f"{board[0]} | {board[1]} | {board[2]}\n--+--+--\n{board[3]} | {board[4]} | {board[5]}\n--+--+--\n{board[6]} | {board[7]} | {board[8]}",
        )
