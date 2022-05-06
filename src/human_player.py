from src.user_interface import UserInterface
from src.validator import Validator
from src.message import Message


class HumanPlayer:
    def __init__(self, mark):
        self.mark = mark

    def get_move(self, board):
        move = UserInterface().get_user_input()
        if not Validator().is_valid_move(board, move):
            UserInterface().display_message(Message().invalid_board_input())
            return self.get_move(board)
        return int(move)
