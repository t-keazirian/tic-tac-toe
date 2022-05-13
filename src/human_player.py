from src.user_interface import UserInterface
from src.validator import Validator


class HumanPlayer:
    def __init__(self, mark, message):
        self.mark = mark
        self.message = message

    def get_move(self, board, mark, opponent_mark):
        move = UserInterface().get_user_input()
        if not Validator().is_valid_move(board, move):
            UserInterface().display_message(self.message.invalid_board_input())
            return self.get_move(board, mark, opponent_mark)
        return int(move)
