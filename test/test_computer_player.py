import unittest
from src.computer_player import ComputerPlayer


class TestComputerPlayer(unittest.TestCase):
    def test_get_move_returns_valid_move(self):
        comp_player = ComputerPlayer("X")

        game_board = ["X", "X", "X", "X", "5", "X", "X", "X", "X"]

        result = comp_player.get_move(game_board)

        self.assertEqual(5, result)


