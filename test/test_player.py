import unittest

from src.player import Player


class PlayerTest(unittest.TestCase):
    def test_board_is_marked_with_user_selection_when_no_marks_and_X_is_going_first(
        self,
    ):
        player = Player()
        current_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        new_board_with_marks = ["X", "2", "3", "4", "5", "6", "7", "8", "9"]
        user_input = 1
        total_marks_on_board = 0
        self.assertEqual(
            new_board_with_marks,
            player.mark_board_with_user_selection(
                user_input, current_board, total_marks_on_board
            ),
        )

    def test_board_is_marked_with_user_selection_when_one_mark_and_O_is_next_player(
        self,
    ):
        player = Player()
        current_board = ["X", "2", "3", "4", "5", "6", "7", "8", "9"]
        new_board_with_marks = ["X", "O", "3", "4", "5", "6", "7", "8", "9"]
        user_input = 2
        total_marks_on_board = 1
        self.assertEqual(
            new_board_with_marks,
            player.mark_board_with_user_selection(
                user_input, current_board, total_marks_on_board
            ),
        )

    def test_board_is_marked_with_user_selection_when_two_marks_and_X_is_next_player(
        self,
    ):
        player = Player()
        current_board = ["X", "O", "3", "4", "5", "6", "7", "8", "9"]
        new_board_with_marks = ["X", "O", "X", "4", "5", "6", "7", "8", "9"]
        user_input = 3
        total_marks_on_board = 2
        self.assertEqual(
            new_board_with_marks,
            player.mark_board_with_user_selection(
                user_input, current_board, total_marks_on_board
            ),
        )
