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

    def test_top_row_returns_top_row_of_board(self):
        rules = Rules()
        current_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        top_row_board = rules.top_row(current_board)
        self.assertEqual(["1", "2", "3"], top_row_board)

    def test_middle_row_returns_middle_row_of_board(self):
        rules = Rules()
        current_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        middle_row_board = rules.middle_row(current_board)
        self.assertEqual(["4", "5", "6"], middle_row_board)

    def test_bottom_row_returns_bottom_row_of_board(self):
        rules = Rules()
        current_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        bottom_row_board = rules.bottom_row(current_board)
        self.assertEqual(["7", "8", "9"], bottom_row_board)

    def test_first_column_returns_left_column_of_board(self):
        rules = Rules()
        current_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        left_column_board = rules.left_column(current_board)
        self.assertEqual(["1", "4", "7"], left_column_board)

    def test_middle_column_returns_middle_column_of_board(self):
        rules = Rules()
        current_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        middle_column_board = rules.middle_column(current_board)
        self.assertEqual(["2", "5", "8"], middle_column_board)

    def test_right_column_returns_right_column_of_board(self):
        rules = Rules()
        current_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        right_column_board = rules.right_column(current_board)
        self.assertEqual(["3", "6", "9"], right_column_board)

    def test_left_to_right_diag_returns_diagonal_board(self):
        rules = Rules()
        current_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        left_to_right_diag_board = rules.top_left_btm_right_diag(current_board)
        self.assertEqual(["1", "5", "9"], left_to_right_diag_board)

    def test_top_right_to_bottom_left_returns_opposite_diagonal(self):
        rules = Rules()
        current_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        right_to_left_diag_board = rules.top_right_btm_left_diag(current_board)
        self.assertEqual(["3", "5", "7"], right_to_left_diag_board)

    def test_is_row_array_same_returns_true_if_array_elements_are_equal_with_X(self):
        rules = Rules()
        row_array = ["X", "X", "X"]
        result = rules.is_row_array_same(row_array)
        self.assertEqual(True, result)

    def test_is_row_array_same_returns_true_if_array_elements_are_equal_with_O(self):
        rules = Rules()
        row_array = ["O", "O", "O"]
        result = rules.is_row_array_same(row_array)
        self.assertEqual(True, result)

    def test_is_row_array_same_returns_false_if_array_elements_are_not_equal(self):
        rules = Rules()
        row_array = ["X", "X", "O"]
        result = rules.is_row_array_same(row_array)
        self.assertEqual(False, result)

    def test_is_row_array_same_returns_false_with_numbers(self):
        rules = Rules()
        row_array = ["1", "X", "3"]
        result = rules.is_row_array_same(row_array)
        self.assertEqual(False, result)

    def test_get_winning_mark_returns_X_winning_mark(self):
        rules = Rules()
        current_board = ["X", "X", "X", "4", "5", "6", "7", "8", "9"]
        result = rules.get_winning_mark(current_board)
        self.assertEqual("X", result)

    def test_get_winning_mark_returns_O_winning_mark(self):
        rules = Rules()
        current_board = ["1", "2", "3", "O", "O", "O", "7", "8", "9"]
        result = rules.get_winning_mark(current_board)
        self.assertEqual("O", result)

    def test_get_winning_returns_None_if_no_winner(self):
        rules = Rules()
        current_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        result = rules.get_winning_mark(current_board)
        self.assertEqual(None, result)
