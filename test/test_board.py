import unittest

from src.board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.starter_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.full_board = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]
        self.player_one_mark = "X"
        self.player_two_mark = "O"

    def test_board_to_string(self):
        expected_message = f" {self.starter_board[0]} | {self.starter_board[1]} | {self.starter_board[2]} \n---+---+---\n {self.starter_board[3]} | {self.starter_board[4]} | {self.starter_board[5]} \n---+---+---\n {self.starter_board[6]} | {self.starter_board[7]} | {self.starter_board[8]}"
        actual_message = self.board.to_string(self.starter_board)
        self.assertEqual(expected_message, actual_message)

    def test_is_full_returns_true_if_board_is_full(self):
        total_marks_on_board = self.board.count_marks(
            self.full_board, self.player_one_mark, self.player_two_mark
        )
        self.assertTrue(self.board.is_full(total_marks_on_board, self.full_board))

    def test_is_full_returns_false_if_board_isnt_full(self):
        not_full_board = ["X", "2", "3", "4", "X", "O", "X", "O", "X"]
        total_marks_on_board = self.board.count_marks(
            not_full_board, self.player_one_mark, self.player_two_mark
        )
        self.assertFalse(self.board.is_full(total_marks_on_board, not_full_board))

    def test_is_full_returns_true_if_board_is_full_with_emojis(self):
        full_board = ["🤡", "👻", "🤡", "👻", "🤡", "👻", "🤡", "👻", "🤡"]
        player_one_mark = "🤡"
        player_two_mark = "👻"
        total_marks_on_board = self.board.count_marks(
            full_board, player_one_mark, player_two_mark
        )
        self.assertTrue(self.board.is_full(total_marks_on_board, full_board))

    def test_no_turns_taken_yet(self):
        total_marks_on_board = self.board.count_marks(
            self.starter_board, self.player_two_mark, self.player_two_mark
        )
        self.assertEqual(0, total_marks_on_board)

    def test_one_turn_taken_returns_one_mark_on_board(self):
        current_board = ["X", "2", "3", "4", "5", "6", "7", "8", "9"]
        total_marks_on_board = self.board.count_marks(
            current_board, self.player_one_mark, self.player_two_mark
        )
        self.assertEqual(1, total_marks_on_board)

    def test_two_turns_taken_returns_two_marks_on_board(self):
        current_board = ["X", "O", "3", "4", "5", "6", "7", "8", "9"]
        total_marks_on_board = self.board.count_marks(
            current_board, self.player_one_mark, self.player_two_mark
        )
        self.assertEqual(2, total_marks_on_board)

    def test_one_turn_taken_returns_one_mark_on_board_with_emoji(self):
        current_board = ["1", "🤡", "3", "4", "5", "6", "7", "8", "9"]
        player_one_mark = "🤡"
        player_two_mark = "👻"
        total_marks_on_board = self.board.count_marks(
            current_board, player_one_mark, player_two_mark
        )
        self.assertEqual(1, total_marks_on_board)

    def test_mark_board_marks_board_with_user_selection(self):
        board_with_one_x = ["X", "2", "3", "4", "5", "6", "7", "8", "9"]
        board_with_one_x_and_o = ["X", "O", "3", "4", "5", "6", "7", "8", "9"]
        board_with_multiple_marks = ["X", "O", "X", "4", "5", "6", "7", "8", "9"]
        board_with_emoji = ["🤡", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.assertEqual(
            board_with_one_x,
            self.board.mark_board(1, self.starter_board, "X"),
        )
        self.assertEqual(
            board_with_one_x_and_o,
            self.board.mark_board(2, board_with_one_x, "O"),
        )
        self.assertEqual(
            board_with_multiple_marks,
            self.board.mark_board(3, board_with_multiple_marks, "X"),
        )
        self.assertEqual(
            board_with_emoji,
            self.board.mark_board(1, self.starter_board, "🤡"),
        )

    def test_is_spot_taken_returns_true_when_spot_is_taken(self):
        test_board_one = ["X", "2", "3", "4", "5", "6", "7", "8", "9"]
        test_board_two = ["1", "X", "3", "4", "5", "6", "7", "8", "9"]
        test_board_emoji = ["🤡", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.assertTrue(self.board.is_spot_taken(test_board_one, 1))
        self.assertTrue(self.board.is_spot_taken(test_board_two, 2))
        self.assertTrue(self.board.is_spot_taken(test_board_emoji, 1))

    def test_is_spot_taken_returns_false_if_spot_is_not_taken(self):
        test_board = ["1", "X", "3", "O", "X", "6", "O", "8", "9"]
        self.assertFalse(self.board.is_spot_taken(self.starter_board, 1))
        self.assertFalse(self.board.is_spot_taken(test_board, 3))
        self.assertFalse(self.board.is_spot_taken(test_board, 9))
