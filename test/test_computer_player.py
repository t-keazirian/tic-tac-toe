import unittest
from src.computer_player import ComputerPlayer


class TestComputerPlayer(unittest.TestCase):
    def test_computer_input_returns_random_str_int_bn_1_and_9(self):
        comp_player = ComputerPlayer()
        options = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        result = comp_player.computer_input()

        self.assertIn(result, options)
