import unittest
from unittest.mock import patch
from src.human_player import HumanPlayer


class TestHumanPlayer(unittest.TestCase):
    @patch("builtins.input", side_effect=["1"])
    def test_get_move_returns_valid_user_move(self, mock_input):
        human_player = HumanPlayer("X")
        game_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        result = human_player.get_move(game_board)

        self.assertEqual(1, result)
