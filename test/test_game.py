import unittest
from unittest.mock import patch

from src.game import Game


class TestGame(unittest.TestCase):
    @patch("builtins.print")
    def test_welcome_message(self, mock_print):
        Game().display_welcome_message()
        mock_print.assert_called_with("Welcome to Tic Tac Toe")
