import random
from src.validator import Validator as validator


class ComputerPlayer:
    def __init__(self, mark):
        self.mark = mark

    def get_move(self, board):
        move = random.randint(1, 9)
        if not validator.spot_is_available(self, board, move):
            return self.get_move(board)
        return move
