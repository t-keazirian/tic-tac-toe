import unittest
from unittest.mock import patch

from src.game import Game


class TestGame(unittest.TestCase):
    def test_welcome_message(self):
        game = Game()
        self.assertEqual("Welcome to Tic Tac Toe", game.get_welcome_message())

    def test_initialize_board_with_real_values(self):
        game = Game()
        self.assertEqual(
            "1 | 2 | 3\n--+--+--\n4 | 5 | 6\n--+--+--\n7 | 8 | 9",
            game.initialize_board(),
        )

    def test_prompt_x_for_first_turn(self):
        game = Game()
        play_count = 0
        prompt = game.get_prompt(play_count)
        self.assertEqual("Player X - enter a number to place your mark", prompt)

    def test_prompt_o_for_second_turn(self):
        game = Game()
        play_count = 1
        prompt = game.get_prompt(play_count)
        self.assertEqual("Player O - enter a number to place your mark", prompt)

    def test_prompt_x_for_third_turn(self):
        game = Game()
        play_count = 2
        prompt = game.get_prompt(play_count)
        self.assertEqual("Player X - enter a number to place your mark", prompt)

    def test_full_board_game_over(self):
        game = Game()
        play_count = 9
        prompt = game.get_prompt(play_count)
        self.assertEqual("Game Over!", prompt)

    def test_no_turns_taken_yet(self):
        game = Game()
        play_count = game.count_marks_in_board()
        self.assertEqual(0, play_count)

    def test_zero_turns_player_x_goes_first(self):
        game = Game()
        play_count = 0
        current_player = game.get_current_player(play_count)
        self.assertEqual("X", current_player)

    def test_one_turn_player_o_goes_next(self):
        game = Game()
        play_count = 1
        current_player = game.get_current_player(play_count)
        self.assertEqual("O", current_player)

    def test_two_turn_player_x_goes_next(self):
        game = Game()
        play_count = 2
        current_player = game.get_current_player(play_count)
        self.assertEqual("X", current_player)

    def test_X_is_placed_in_index_0_with_input_1(self):
        game = Game()
        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        user_input = 1
        play_count = 0
        current_player = game.get_current_player(play_count)
        game.place_mark_on_board(user_input, board, play_count)
        self.assertEqual(board[0], current_player)

    def test_O_is_placed_in_index_1_with_input_2(self):
        game = Game()
        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        user_input = 2
        play_count = 1
        current_player = game.get_current_player(play_count)
        game.place_mark_on_board(user_input, board, play_count)
        self.assertEqual(board[1], current_player)

    def test_X_is_placed_in_index_2_with_input_3(self):
        game = Game()
        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        user_input = 3
        play_count = 2
        current_player = game.get_current_player(play_count)
        game.place_mark_on_board(user_input, board, play_count)
        self.assertEqual(board[2], current_player)

    def test_return_true_if_spot_is_taken(self):
        game = Game()
        board = ["1", "2", "X", "4", "5", "6", "7", "8", "9"]
        user_input = 3
        self.assertEqual(True, game.is_spot_taken(board, user_input))

    def test_return_false_if_spot_is_not_taken(self):
        game = Game()
        board = ["1", "2", "X", "4", "5", "6", "7", "8", "9"]
        user_input = 4
        self.assertEqual(False, game.is_spot_taken(board, user_input))

    def test_return_true_if_spot_is_taken_in_two_places(self):
        game = Game()
        board = ["1", "2", "X", "4", "5", "6", "7", "8", "O"]
        user_input = 9
        self.assertEqual(True, game.is_spot_taken(board, user_input))

    def test_return_true_if_spot_is_taken_in_three_places(self):
        game = Game()
        board = ["1", "2", "X", "4", "5", "6", "X", "8", "O"]
        user_input = 7
        self.assertEqual(True, game.is_spot_taken(board, user_input))

    def test_return_false_if_spot_is_not_taken_two(self):
        game = Game()
        board = ["X", "O", "X", "O", "X", "6", "7", "8", "9"]
        user_input = 9
        self.assertEqual(False, game.is_spot_taken(board, user_input))

    def test_take_turns_alternates_play(self):
        game = Game()
        board = ["1", "2", "X", "4", "5", "6", "7", "8", "9"]
        user_input = 2
        play_count = 1
        new_board = game.place_mark_on_board(user_input, board, play_count)
        self.assertEqual(new_board, game.take_turns())
