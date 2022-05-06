import unittest
from src.computer_player import ComputerPlayer


class TestComputerPlayer(unittest.TestCase):
    def test_computer_input_returns_random_str_int_bn_1_and_9(self):
        comp_player = ComputerPlayer()
        options = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        result = comp_player.computer_input()

        self.assertIn(result, options)

    def test_valid_computer_input_returns_true_when_spot_is_not_taken(self):
        comp_player = ComputerPlayer()

        game_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        move = 1

        result = comp_player.valid_computer_move(move, game_board)

        self.assertEqual(True, result)

    def test_valid_computer_input_returns_false_when_spot_is_taken(self):
        comp_player = ComputerPlayer()

        game_board = ["X", "2", "3", "4", "5", "6", "7", "8", "9"]
        move = 1

        result = comp_player.valid_computer_move(move, game_board)

        self.assertEqual(False, result)

    def test_get_computer_move_does_not_mark_board_if_spot_is_taken(self):
        comp_player = ComputerPlayer()

        game_board = ["X", "2", "3", "4", "5", "6", "7", "8", "9"]
        move = 1

        result = comp_player.get_computer_move(move, game_board)

        self.assertNotEqual(1, result)

    def test_get_computer_move_returns_valid_move(self):
        comp_player = ComputerPlayer()

        game_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        move = 1

        result = comp_player.get_computer_move(move, game_board)

        self.assertEqual(1, result)
