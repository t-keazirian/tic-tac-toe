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
        self.assertEqual("Player X - enter the number of an empty spot", prompt)

    def test_prompt_o_for_second_turn(self):
        game = Game()
        play_count = 1
        prompt = game.get_prompt(play_count)
        self.assertEqual("Player O - enter the number of an empty spot", prompt)

    def test_prompt_x_for_third_turn(self):
        game = Game()
        play_count = 2
        prompt = game.get_prompt(play_count)
        self.assertEqual("Player X - enter the number of an empty spot", prompt)

    def test_full_board_game_over(self):
        game = Game()
        play_count = 9
        prompt = game.get_prompt(play_count)
        self.assertEqual("Game Over!", prompt)

    def test_no_turns_taken_yet(self):
        game = Game()
        play_count = game.count_plays()
        self.assertEqual(0, play_count)

    def test_zero_turns_player_x_goes_first(self):
        game = Game()
        play_count = 0
        next_player = game.get_next_player(play_count)
        self.assertEqual("X", next_player)

    def test_one_turn_player_o_goes_next(self):
        game = Game()
        play_count = 1
        next_player = game.get_next_player(play_count)
        self.assertEqual("O", next_player)

    def test_two_turn_player_x_goes_next(self):
        game = Game()
        play_count = 2
        next_player = game.get_next_player(play_count)
        self.assertEqual("X", next_player)
