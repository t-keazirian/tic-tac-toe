import unittest
from src.computer_player import ComputerPlayer
from src.ai_random import AIRandom


class TestComputerPlayer(unittest.TestCase):
    def setUp(self):
        self.ai_random = AIRandom()
        self.test_comp_player = ComputerPlayer("O", self.ai_random)

    def test_get_move_returns_valid_move(self):

        game_board = ["X", "X", "X", "O", "5", "X", "X", "X", "X"]

        result = self.test_comp_player.get_move(game_board, "X", "O")

        self.assertEqual(5, result)
