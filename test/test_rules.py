import unittest

from src.rules import Rules


class TestRules(unittest.TestCase):
    def test_if_three_in_horizontal_first_row_return_true(self):
        rules = Rules()
        current_board = ["X", "X", "X", "O", "5", "6", "7", "8", "9"]
        winner = rules.is_winner_horizontal(current_board)
        self.assertEqual(True, winner)

    def test_if_three_in_horizontal_second_row_return_true(self):
        rules = Rules()
        current_board = ["1", "2", "3", "X", "X", "X", "7", "8", "9"]
        winner = rules.is_winner_horizontal(current_board)
        self.assertEqual(True, winner)

    def test_if_three_in_horizontal_third_row_return_true(self):
        rules = Rules()
        current_board = ["1", "2", "3", "4", "5", "6", "X", "X", "X"]
        winner = rules.is_winner_horizontal(current_board)
        self.assertEqual(True, winner)

    def test_if_not_three_in_a_horizontal_row_return_false(self):
        rules = Rules()
        current_board = ["X", "2", "X", "4", "X", "6", "7", "8", "9"]
        winner = rules.is_winner_horizontal(current_board)
        self.assertEqual(False, winner)

    def test_if_three_in_vertical_first_column_return_true(self):
        rules = Rules()
        current_board = ["X", "2", "3", "X", "5", "6", "X", "8", "9"]
        winner = rules.is_winner_vertical(current_board)
        self.assertEqual(True, winner)

    def test_if_three_in_vertical_second_column_return_true(self):
        rules = Rules()
        current_board = ["1", "X", "3", "4", "X", "6", "7", "X", "9"]
        winner = rules.is_winner_vertical(current_board)
        self.assertEqual(True, winner)

    def test_if_three_in_vertical_third_column_return_true(self):
        rules = Rules()
        current_board = ["1", "2", "X", "4", "5", "X", "7", "8", "X"]
        winner = rules.is_winner_vertical(current_board)
        self.assertEqual(True, winner)

    def test_if_not_three_in_vertical_column_return_false(self):
        rules = Rules()
        current_board = ["1", "2", "X", "4", "X", "6", "7", "X", "9"]
        winner = rules.is_winner_vertical(current_board)
        self.assertEqual(False, winner)

    def test_if_three_in_diagonal_top_left_to_bottom_right_return_true(self):
        rules = Rules()
        current_board = ["X", "2", "3", "4", "X", "6", "7", "8", "X"]
        winner = rules.is_winner_diagonal(current_board)
        self.assertEqual(True, winner)

    def test_if_three_in_diagonal_top_right_to_bottom_left_return_true(self):
        rules = Rules()
        current_board = ["1", "2", "X", "4", "X", "6", "X", "8", "9"]
        winner = rules.is_winner_diagonal(current_board)
        self.assertEqual(True, winner)

    def test_if_not_three_in_diagonal_row_return_false(self):
        rules = Rules()
        current_board = ["1", "X", "X", "4", "X", "6", "7", "8", "9"]
        winner = rules.is_winner_diagonal(current_board)
        self.assertEqual(False, winner)

    def test_if_winner_diagonal_is_winner_return_true(self):
        rules = Rules()
        current_board = ["1", "2", "X", "4", "X", "6", "X", "8", "9"]
        is_winner_true = rules.is_winner(current_board)
        self.assertEqual(True, is_winner_true)

    def test_if_winner_horizontal_is_winner_return_true(self):
        rules = Rules()
        current_board = ["1", "2", "3", "4", "5", "6", "X", "X", "X"]
        is_winner_true = rules.is_winner(current_board)
        self.assertEqual(True, is_winner_true)

    def test_if_winner_vertical_is_winner_returns_true(self):
        rules = Rules()
        current_board = ["1", "X", "3", "4", "X", "6", "7", "X", "9"]
        is_winner_true = rules.is_winner(current_board)
        self.assertEqual(True, is_winner_true)

    def test_if_not_winner_is_winner_returns_false(self):
        rules = Rules()
        current_board = ["1", "X", "3", "4", "X", "X", "7", "8", "9"]
        is_winner_true = rules.is_winner(current_board)
        self.assertEqual(False, is_winner_true)
