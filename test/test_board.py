import unittest

from src.board import Board


class TestBoard(unittest.TestCase):
    def test_is_full_returns_true_if_board_is_full(self):
        board = Board()
        full_board = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]
        total_marks_on_board = board.count_marks(full_board)
        self.assertEqual(True, board.is_full(total_marks_on_board, full_board))

    def test_is_full_returns_false_if_board_isnt_full(self):
        board = Board()
        full_board = ["X", "2", "3", "4", "X", "O", "X", "O", "X"]
        total_marks_on_board = board.count_marks(full_board)
        self.assertEqual(False, board.is_full(total_marks_on_board, full_board))

    def test_no_turns_taken_yet(self):
        board = Board()
        current_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        total_marks_on_board = board.count_marks(current_board)
        self.assertEqual(0, total_marks_on_board)

    def test_one_turn_taken_returns_one_mark_on_board(self):
        board = Board()
        current_board = ["X", "2", "3", "4", "5", "6", "7", "8", "9"]
        total_marks_on_board = board.count_marks(current_board)
        self.assertEqual(1, total_marks_on_board)

    def test_two_turns_taken_returns_two_marks_on_board(self):
        board = Board()
        current_board = ["X", "O", "3", "4", "5", "6", "7", "8", "9"]
        total_marks_on_board = board.count_marks(current_board)
        self.assertEqual(2, total_marks_on_board)

    def test_is_spot_taken_returns_true_when_spot_is_marked(self):
        board = Board()
        current_board = ["X", "2", "3", "4", "5", "6", "7", "8", "9"]
        user_input = 1
        spot_is_taken = board.is_spot_taken(current_board, user_input)
        self.assertEqual(True, spot_is_taken)

    def test_is_spot_taken_returns_true_when_spot_is_marked_2(self):
        board = Board()
        current_board = ["1", "X", "3", "4", "5", "6", "7", "8", "9"]
        user_input = 2
        spot_is_taken = board.is_spot_taken(current_board, user_input)
        self.assertEqual(True, spot_is_taken)

    def test_is_spot_taken_returns_false_with_multiple_spots_taken(self):
        board = Board()
        current_board = ["1", "X", "3", "O", "X", "6", "O", "8", "9"]
        user_input = 1
        spot_is_taken = board.is_spot_taken(current_board, user_input)
        self.assertEqual(False, spot_is_taken)

    def test_is_spot_taken_returns_false_if_spot_is_avail(self):
        board = Board()
        current_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        user_input = 2
        spot_is_taken = board.is_spot_taken(current_board, user_input)
        self.assertEqual(False, spot_is_taken)

    def test_if_different_spot_is_taken_return_false(self):
        board = Board()
        current_board = ["1", "2", "3", "4", "5", "X", "7", "8", "9"]
        user_input = 4
        spot_is_taken = board.is_spot_taken(current_board, user_input)
        self.assertEqual(False, spot_is_taken)

    def test_is_spot_taken_returns_false_with_multiple_spots_taken_2(self):
        board = Board()
        current_board = ["O", "X", "X", "O", "5", "6", "7", "8", "9"]
        user_input = 6
        spot_is_taken = board.is_spot_taken(current_board, user_input)
        self.assertEqual(False, spot_is_taken)

    def test_if_three_in_horizontal_first_row_returns_true(self):
        board = Board()
        current_board = ["X", "X", "X", "O", "5", "6", "7", "8", "9"]
        winner = board.is_winner_horizontal(current_board)
        self.assertEqual(True, winner)

    def test_if_three_in_horizontal_second_row_returns_true(self):
        board = Board()
        current_board = ["1", "2", "3", "X", "X", "X", "7", "8", "9"]
        winner = board.is_winner_horizontal(current_board)
        self.assertEqual(True, winner)

    def test_if_three_in_horizontal_third_row_returns_true(self):
        board = Board()
        current_board = ["1", "2", "3", "4", "5", "6", "X", "X", "X"]
        winner = board.is_winner_horizontal(current_board)
        self.assertEqual(True, winner)

    def test_if_not_three_in_a_horizontal_row_return_false(self):
        board = Board()
        current_board = ["X", "2", "X", "4", "X", "6", "7", "8", "9"]
        winner = board.is_winner_horizontal(current_board)
        self.assertEqual(False, winner)

    def test_if_three_in_vertical_first_column_returns_true(self):
        board = Board()
        current_board = ["X", "2", "3", "X", "5", "6", "X", "8", "9"]
        winner = board.is_winner_vertical(current_board)
        self.assertEqual(True, winner)

    def test_if_three_in_vertical_second_column_returns_true(self):
        board = Board()
        current_board = ["1", "X", "3", "4", "X", "6", "7", "X", "9"]
        winner = board.is_winner_vertical(current_board)
        self.assertEqual(True, winner)

    def test_if_three_in_vertical_third_column_returns_true(self):
        board = Board()
        current_board = ["1", "2", "X", "4", "5", "X", "7", "8", "X"]
        winner = board.is_winner_vertical(current_board)
        self.assertEqual(True, winner)

    def test_if_not_three_in_vertical_column_return_false(self):
        board = Board()
        current_board = ["1", "2", "X", "4", "X", "6", "7", "X", "9"]
        winner = board.is_winner_vertical(current_board)
        self.assertEqual(False, winner)
