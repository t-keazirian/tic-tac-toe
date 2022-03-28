import unittest

from src.player import Player


class PlayerTest(unittest.TestCase):
    def test_zero_turns_player_x_goes_first(self):
        player = Player()
        total_marks_on_board = 0
        current_player = player.get_current_player(total_marks_on_board)
        self.assertEqual("X", current_player)

    def test_one_turn_player_o_goes_next(self):
        player = Player()
        total_marks_on_board = 1
        current_player = player.get_current_player(total_marks_on_board)
        self.assertEqual("O", current_player)

    def test_two_turn_player_x_goes_next(self):
        player = Player()
        total_marks_on_board = 2
        current_player = player.get_current_player(total_marks_on_board)
        self.assertEqual("X", current_player)
