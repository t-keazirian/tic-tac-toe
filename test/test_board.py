import unittest

from src.board import Board


class TestBoard(unittest.TestCase):
    def test_is_board_full_returns_true_if_board_is_full(self):
        board = Board()
        full_board = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]
        total_marks_on_board = board.count_marks_in_board(full_board, "X", "O")
        self.assertEqual(True, board.is_board_full(total_marks_on_board, full_board))

    def test_is_board_full_returns_false_if_board_isnt_full(self):
        board = Board()
        full_board = ["X", "2", "3", "4", "X", "O", "X", "O", "X"]
        total_marks_on_board = board.count_marks_in_board(full_board, "X", "O")
        self.assertEqual(False, board.is_board_full(total_marks_on_board, full_board))

    def test_no_turns_taken_yet(self):
        board = Board()
        current_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        total_marks_on_board = board.count_marks_in_board(current_board, "X", "O")
        self.assertEqual(0, total_marks_on_board)

    def test_zero_turns_player_x_goes_first(self):
        board = Board()
        total_marks_on_board = 0
        current_player = board.get_current_player(total_marks_on_board)
        self.assertEqual("X", current_player)

    def test_one_turn_player_o_goes_next(self):
        board = Board()
        total_marks_on_board = 1
        current_player = board.get_current_player(total_marks_on_board)
        self.assertEqual("O", current_player)

    def test_two_turn_player_x_goes_next(self):
        board = Board()
        total_marks_on_board = 2
        current_player = board.get_current_player(total_marks_on_board)
        self.assertEqual("X", current_player)
