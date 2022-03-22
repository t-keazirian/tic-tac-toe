import unittest

from src.board import Board
from src.game import Game


class TestGame(unittest.TestCase):
    def test_welcome_message(self):
        game = Game()
        self.assertEqual("Welcome to Tic Tac Toe", game.get_welcome_message())

    def test_get_formatted_board_with_real_values(self):
        game = Game()
        self.assertEqual(
            "1 | 2 | 3\n--+--+--\n4 | 5 | 6\n--+--+--\n7 | 8 | 9",
            game.get_formatted_board(),
        )

    def test_prompt_x_for_first_turn(self):
        game = Game()
        total_marks_on_board = 0
        prompt = game.get_prompt(total_marks_on_board)
        self.assertEqual("Player X - enter a number to place your mark", prompt)

    def test_prompt_o_for_second_turn(self):
        game = Game()
        total_marks_on_board = 1
        prompt = game.get_prompt(total_marks_on_board)
        self.assertEqual("Player O - enter a number to place your mark", prompt)

    def test_prompt_x_for_third_turn(self):
        game = Game()
        total_marks_on_board = 2
        prompt = game.get_prompt(total_marks_on_board)
        self.assertEqual("Player X - enter a number to place your mark", prompt)

    def test_full_board_game_over(self):
        game = Game()
        total_marks_on_board = 9
        prompt = game.get_prompt(total_marks_on_board)
        self.assertEqual("Game Over!", prompt)

    def test_no_turns_taken_yet(self):
        game = Game()
        board = Board()
        total_marks_on_board = board.count_marks_in_board("X", "O")
        self.assertEqual(0, total_marks_on_board)

    def test_zero_turns_player_x_goes_first(self):
        game = Game()
        board = Board()
        total_marks_on_board = 0
        current_player = board.get_current_player(total_marks_on_board)
        self.assertEqual("X", current_player)

    def test_one_turn_player_o_goes_next(self):
        game = Game()
        board = Board()
        total_marks_on_board = 1
        current_player = board.get_current_player(total_marks_on_board)
        self.assertEqual("O", current_player)

    def test_two_turn_player_x_goes_next(self):
        game = Game()
        board = Board()
        total_marks_on_board = 2
        current_player = board.get_current_player(total_marks_on_board)
        self.assertEqual("X", current_player)

    def test_X_is_placed_in_index_0_with_input_1(self):
        game = Game()
        board = Board()
        current_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        user_input = 1
        total_marks_on_board = 0
        current_player = board.get_current_player(total_marks_on_board)
        board.place_mark_on_board(user_input, current_board, total_marks_on_board)
        self.assertEqual(current_board[0], current_player)

    def test_O_is_placed_in_index_1_with_input_2(self):
        game = Game()
        board = Board()
        current_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        user_input = 2
        total_marks_on_board = 1
        current_player = board.get_current_player(total_marks_on_board)
        board.place_mark_on_board(user_input, current_board, total_marks_on_board)
        self.assertEqual(current_board[1], current_player)

    def test_X_is_placed_in_index_2_with_input_3(self):
        game = Game()
        board = Board()
        current_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        user_input = 3
        total_marks_on_board = 2
        current_player = board.get_current_player(total_marks_on_board)
        board.place_mark_on_board(user_input, current_board, total_marks_on_board)
        self.assertEqual(current_board[2], current_player)
