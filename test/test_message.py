import unittest

from src.message import Message


class TestMessage(unittest.TestCase):
    def test_welcome_message_prints_to_console(self):
        message = Message()
        expected_message = "Welcome to Tic Tac Toe"
        actual_message = message.welcome_message()
        self.assertEqual(expected_message, actual_message)

    def test_game_over_prints_to_console(self):
        message = Message()
        expected_message = "Game over - it's a draw!"
        actual_message = message.game_over_message()
        self.assertEqual(expected_message, actual_message)

    def test_X_player_is_prompted_for_move_when_is_current_player(self):
        message = Message()
        current_player = "X"
        expected_message = (
            f"Player {current_player} - enter a number to place your mark"
        )
        actual_message = message.prompt_for_move(current_player)
        self.assertEqual(expected_message, actual_message)

    def test_formatted_board(self):
        message = Message()
        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        expected_message = f"{board[0]} | {board[1]} | {board[2]}\n--+--+--\n{board[3]} | {board[4]} | {board[5]}\n--+--+--\n{board[6]} | {board[7]} | {board[8]}"
        actual_message = message.formatted_board(board)
        self.assertEqual(expected_message, actual_message)

    def test_spot_taken_message(self):
        message = Message()
        expected_message = (
            "That spot is already occupied. Please choose another spot on the board."
        )
        actual_message = message.spot_taken_message()
        self.assertEqual(expected_message, actual_message)

    def test_declare_winner_with_correct_mark_as_winner(self):
        message = Message()
        winner = "X"
        expected_message = f"Congrats Player {winner} - you are the winner!"
        actual_message = message.declare_winner(winner)
        self.assertEqual(expected_message, actual_message)

    def test_incorrect_board_input(self):
        message = Message()
        expected_message = "That input is incorrect. Please input a number 1-9."
        actual_message = message.incorrect_board_input()
        self.assertEqual(expected_message, actual_message)

    def test_play_again_prompt(self):
        message = Message()
        expected_message = "Would you like to play again? (Y/N)"
        actual_message = message.play_again_prompt()
        self.assertEqual(expected_message, actual_message)

    def test_goodbye_message(self):
        message = Message()
        expected_message = "Thanks for playing - goodbye!"
        actual_message = message.goodbye_message()
        self.assertEqual(expected_message, actual_message)

    def test_incorrect_repeat_game_message(self):
        message = Message()
        expected_message = "That input is incorrect. Please input Y to play again or N to exit the game."
        actual_message = message.incorrect_repeat_game_input()
        self.assertEqual(expected_message, actual_message)

    def test_print_rules_prints_rules_to_console(self):
        message = Message()
        rules = """
Play this game by taking turns marking the board.
When prompted, type a number between 1 and 9 and press enter.
If that spot is taken, the computer will prompt you for a different spot.
The first player who gets three of their marks in a row wins!
If the board is full and neither player has three in a row, it is a draw and the game is over.
At the end of every game, you will have the option to play again or to exit.\n
"""
        actual_message = message.rules()
        self.assertEqual(rules, actual_message)
