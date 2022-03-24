import unittest

from src.board import Board


class TestBoard(unittest.TestCase):
    def test_is_full_returns_true_if_board_is_full(self):
        board = Board()
        full_board = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]
        total_marks_on_board = board.count_marks_in_board(full_board, "X", "O")
        self.assertEqual(True, board.is_full(total_marks_on_board, full_board))

    def test_is_full_returns_false_if_board_isnt_full(self):
        board = Board()
        full_board = ["X", "2", "3", "4", "X", "O", "X", "O", "X"]
        total_marks_on_board = board.count_marks_in_board(full_board, "X", "O")
        self.assertEqual(False, board.is_full(total_marks_on_board, full_board))

    def test_no_turns_taken_yet(self):
        board = Board()
        current_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        total_marks_on_board = board.count_marks_in_board(current_board, "X", "O")
        self.assertEqual(0, total_marks_on_board)

    def test_one_turn_taken_returns_one_mark_on_board(self):
        board = Board()
        current_board = ["X", "2", "3", "4", "5", "6", "7", "8", "9"]
        total_marks_on_board = board.count_marks_in_board(current_board, "X", "O")
        self.assertEqual(1, total_marks_on_board)

    def test_two_turns_taken_returns_two_marks_on_board(self):
        board = Board()
        current_board = ["X", "O", "3", "4", "5", "6", "7", "8", "9"]
        total_marks_on_board = board.count_marks_in_board(current_board, "X", "O")
        self.assertEqual(2, total_marks_on_board)

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

    def test_X_is_placed_in_index_0_with_input_1(self):
        board = Board()
        current_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        user_input = 1
        total_marks_on_board = 0
        board_index = board.assign_board_index_to_current_player_mark(
            user_input, current_board, total_marks_on_board
        )
        self.assertEqual("X", board_index)

    def test_O_is_placed_in_index_1_with_input_2(self):
        board = Board()
        current_board = ["X", "2", "3", "4", "5", "6", "7", "8", "9"]
        user_input = 2
        total_marks_on_board = 1
        board_index = board.assign_board_index_to_current_player_mark(
            user_input, current_board, total_marks_on_board
        )
        self.assertEqual("O", board_index)

    def test_X_is_placed_in_index_2_with_input_3(self):
        board = Board()
        current_board = ["X", "O", "3", "4", "5", "6", "7", "8", "9"]
        user_input = 3
        total_marks_on_board = 2
        board_index = board.assign_board_index_to_current_player_mark(
            user_input, current_board, total_marks_on_board
        )
        self.assertEqual("X", board_index)

    def test_board_is_marked_with_user_selection_when_no_marks_and_X_is_going_first(
        self,
    ):
        board = Board()
        current_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        new_board_with_marks = ["X", "2", "3", "4", "5", "6", "7", "8", "9"]
        user_input = 1
        total_marks_on_board = 0
        self.assertEqual(
            new_board_with_marks,
            board.mark_board_with_user_selection(
                user_input, current_board, total_marks_on_board
            ),
        )

    def test_board_is_marked_with_user_selection_when_one_mark_and_O_is_next_player(
        self,
    ):
        board = Board()
        current_board = ["X", "2", "3", "4", "5", "6", "7", "8", "9"]
        new_board_with_marks = ["X", "O", "3", "4", "5", "6", "7", "8", "9"]
        user_input = 2
        total_marks_on_board = 1
        self.assertEqual(
            new_board_with_marks,
            board.mark_board_with_user_selection(
                user_input, current_board, total_marks_on_board
            ),
        )

    def test_board_is_marked_with_user_selection_when_two_marks_and_X_is_next_player(
        self,
    ):
        board = Board()
        current_board = ["X", "O", "3", "4", "5", "6", "7", "8", "9"]
        new_board_with_marks = ["X", "O", "X", "4", "5", "6", "7", "8", "9"]
        user_input = 3
        total_marks_on_board = 2
        self.assertEqual(
            new_board_with_marks,
            board.mark_board_with_user_selection(
                user_input, current_board, total_marks_on_board
            ),
        )
