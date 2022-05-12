import unittest

from src.board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.starter_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.full_board = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]

    def test_board_to_string(self):
        expected_message = f" {self.starter_board[0]} | {self.starter_board[1]} | {self.starter_board[2]} \n---+---+---\n {self.starter_board[3]} | {self.starter_board[4]} | {self.starter_board[5]} \n---+---+---\n {self.starter_board[6]} | {self.starter_board[7]} | {self.starter_board[8]}"
        actual_message = self.board.to_string(self.starter_board)
        self.assertEqual(expected_message, actual_message)

    def test_is_full_returns_true_if_board_is_full(self):
        total_marks_on_board = self.board.count_marks(self.full_board, "X", "O")
        self.assertTrue(self.board.is_full(total_marks_on_board, self.full_board))

    def test_is_full_returns_false_if_board_isnt_full(self):
        not_full_board = ["X", "2", "3", "4", "X", "O", "X", "O", "X"]
        total_marks_on_board = self.board.count_marks(not_full_board, "X", "O")
        self.assertFalse(self.board.is_full(total_marks_on_board, not_full_board))

    def test_is_full_returns_true_if_board_is_full_with_emojis(self):
        full_board = ["🤡", "👻", "🤡", "👻", "🤡", "👻", "🤡", "👻", "🤡"]
        total_marks_on_board = self.board.count_marks(full_board, "🤡", "👻")
        self.assertTrue(self.board.is_full(total_marks_on_board, full_board))

    def test_no_turns_taken_yet(self):
        total_marks_on_board = self.board.count_marks(self.starter_board, "X", "O")
        self.assertEqual(0, total_marks_on_board)

    def test_one_turn_taken_returns_one_mark_on_board(self):
        current_board = ["X", "2", "3", "4", "5", "6", "7", "8", "9"]
        total_marks_on_board = self.board.count_marks(current_board, "X", "O")
        self.assertEqual(1, total_marks_on_board)

    def test_two_turns_taken_returns_two_marks_on_board(self):
        current_board = ["X", "O", "3", "4", "5", "6", "7", "8", "9"]
        total_marks_on_board = self.board.count_marks(current_board, "X", "O")
        self.assertEqual(2, total_marks_on_board)

    def test_one_turn_taken_returns_one_mark_on_board_with_emoji(self):
        current_board = ["1", "🤡", "3", "4", "5", "6", "7", "8", "9"]
        total_marks_on_board = self.board.count_marks(current_board, "🤡", "👻")
        self.assertEqual(1, total_marks_on_board)

    def test_mark_board_marks_board_with_user_selection(self):
        self.assertEqual(
            ["X", "2", "3", "4", "5", "6", "7", "8", "9"],
            self.board.mark_board(1, self.starter_board, "X"),
        )
        self.assertEqual(
            ["X", "O", "3", "4", "5", "6", "7", "8", "9"],
            self.board.mark_board(
                2, ["X", "2", "3", "4", "5", "6", "7", "8", "9"], "O"
            ),
        )
        self.assertEqual(
            ["X", "O", "X", "4", "5", "6", "7", "8", "9"],
            self.board.mark_board(
                3, ["X", "O", "3", "4", "5", "6", "7", "8", "9"], "X"
            ),
        )
        self.assertEqual(
            ["🤡", "2", "3", "4", "5", "6", "7", "8", "9"],
            self.board.mark_board(1, self.starter_board, "🤡"),
        )

    def test_is_spot_taken_returns_true_when_spot_is_taken(self):
        self.assertTrue(
            self.board.is_spot_taken(["X", "2", "3", "4", "5", "6", "7", "8", "9"], 1)
        )
        self.assertTrue(
            self.board.is_spot_taken(["1", "X", "3", "4", "5", "6", "7", "8", "9"], 2)
        )
        self.assertTrue(
            self.board.is_spot_taken(["🤡", "2", "3", "4", "5", "6", "7", "8", "9"], 1)
        )

    def test_is_spot_taken_returns_false_if_spot_is_not_taken(self):
        test_board = ["1", "X", "3", "O", "X", "6", "O", "8", "9"]
        test_emoji_board = ["1", "🤡", "3", "4", "5", "6", "7", "8", "9"]
        self.assertFalse(self.board.is_spot_taken(self.starter_board, 1))
        self.assertFalse(self.board.is_spot_taken(test_board, 3))
        self.assertFalse(self.board.is_spot_taken(test_emoji_board, 9))
