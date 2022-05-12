import unittest

from src.rules import Rules


class TestRules(unittest.TestCase):
    def setUp(self):
        self.rules = Rules()
        self.starter_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def test_horizontal_rows_return_true_when_three_in_a_row(self):
        test_top_row = ["X", "X", "X", "O", "5", "6", "7", "8", "9"]
        test_middle_row = ["1", "2", "3", "X", "X", "X", "7", "8", "9"]
        test_bottom_row = ["1", "2", "3", "4", "5", "6", "X", "X", "X"]

        self.assertEqual(True, self.rules.is_winner_horizontal(test_top_row))
        self.assertEqual(True, self.rules.is_winner_horizontal(test_middle_row))
        self.assertEqual(True, self.rules.is_winner_horizontal(test_bottom_row))

    def test_if_not_three_in_a_horizontal_row_return_false(self):
        current_board = ["X", "2", "X", "4", "X", "6", "7", "8", "9"]
        winner = self.rules.is_winner_horizontal(current_board)
        self.assertEqual(False, winner)

    def test_vertical_columns_return_true_when_three_in_a_row(self):
        test_left_column = ["X", "2", "3", "X", "5", "6", "X", "8", "9"]
        test_middle_column = ["1", "X", "3", "4", "X", "6", "7", "X", "9"]
        test_right_column = ["1", "2", "X", "4", "5", "X", "7", "8", "X"]

        self.assertEqual(True, self.rules.is_winner_vertical(test_left_column))
        self.assertEqual(True, self.rules.is_winner_vertical(test_middle_column))
        self.assertEqual(True, self.rules.is_winner_vertical(test_right_column))

    def test_if_not_three_in_vertical_column_return_false(self):
        current_board = ["1", "2", "X", "4", "X", "6", "7", "X", "9"]
        winner = self.rules.is_winner_vertical(current_board)
        self.assertEqual(False, winner)

    def test_diagonal_returns_true_when_three_in_a_row(self):
        top_left_btm_right = ["X", "2", "3", "4", "X", "6", "7", "8", "X"]
        top_right_btm_left = ["1", "2", "X", "4", "X", "6", "X", "8", "9"]

        self.assertEqual(True, self.rules.is_winner_diagonal(top_left_btm_right))
        self.assertEqual(True, self.rules.is_winner_diagonal(top_right_btm_left))

    def test_if_not_three_in_diagonal_row_return_false(self):
        current_board = ["1", "X", "X", "4", "X", "6", "7", "8", "9"]
        winner = self.rules.is_winner_diagonal(current_board)
        self.assertEqual(False, winner)

    def test_is_winner_returns_true_if_winner_in_any_direction(self):
        horizontal_winner_board = ["1", "2", "3", "4", "5", "6", "X", "X", "X"]
        vertical_winner_board = ["1", "X", "3", "4", "X", "6", "7", "X", "9"]
        diagonal_winner_board = ["1", "2", "X", "4", "X", "6", "X", "8", "9"]
        self.assertEqual(True, self.rules.is_winner(horizontal_winner_board))
        self.assertEqual(True, self.rules.is_winner(vertical_winner_board))
        self.assertEqual(True, self.rules.is_winner(diagonal_winner_board))

    def test_if_not_winner_is_winner_returns_false(self):
        current_board = ["1", "X", "3", "4", "X", "X", "7", "8", "9"]
        is_winner_true = self.rules.is_winner(current_board)
        self.assertEqual(False, is_winner_true)

    def test_can_identify_rows_of_the_board(self):
        top_row_board = self.rules.top_row(self.starter_board)
        middle_row_board = self.rules.middle_row(self.starter_board)
        bottom_row_board = self.rules.bottom_row(self.starter_board)

        self.assertEqual(["1", "2", "3"], top_row_board)
        self.assertEqual(["4", "5", "6"], middle_row_board)
        self.assertEqual(["7", "8", "9"], bottom_row_board)

    def test_can_identify_columns_of_the_board(self):
        left_column_board = self.rules.left_column(self.starter_board)
        middle_column_board = self.rules.middle_column(self.starter_board)
        right_column_board = self.rules.right_column(self.starter_board)
        self.assertEqual(["1", "4", "7"], left_column_board)
        self.assertEqual(["2", "5", "8"], middle_column_board)
        self.assertEqual(["3", "6", "9"], right_column_board)

    def test_can_identify_diagonals_of_the_board(self):
        left_to_right_diag_board = self.rules.top_left_btm_right_diag(
            self.starter_board
        )
        right_to_left_diag_board = self.rules.top_right_btm_left_diag(
            self.starter_board
        )
        self.assertEqual(["1", "5", "9"], left_to_right_diag_board)
        self.assertEqual(["3", "5", "7"], right_to_left_diag_board)

    def test_contains_winning_mark_returns_true_if_row_elements_are_equal(self):
        x_array = ["X", "X", "X"]
        o_array = ["O", "O", "O"]
        self.assertEqual(True, self.rules.contains_winning_mark(x_array))
        self.assertEqual(True, self.rules.contains_winning_mark(o_array))

    def test_contains_winning_mark_returns_false_if_row_elements_are_not_equal(self):
        not_winner_one = ["X", "X", "O"]
        not_winner_two = ["1", "X", "3"]
        self.assertEqual(False, self.rules.contains_winning_mark(not_winner_one))
        self.assertEqual(False, self.rules.contains_winning_mark(not_winner_two))

    def test_get_winning_mark_returns_winning_mark(self):
        x_winning_board = ["X", "X", "X", "4", "5", "6", "7", "8", "9"]
        o_winning_board = ["1", "2", "3", "O", "O", "O", "7", "8", "9"]
        not_winning_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.assertEqual("X", self.rules.get_winning_mark(x_winning_board))
        self.assertEqual("O", self.rules.get_winning_mark(o_winning_board))
        self.assertEqual(None, self.rules.get_winning_mark(not_winning_board))
