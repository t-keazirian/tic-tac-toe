import random
from src.validator import Validator as validator


class AIRandom:
    def get_computer_move(self, board, mark, opponent_mark):
        move = random.randint(1, 9)
        if not validator.spot_is_available(self, board, move):
            return self.get_computer_move(board, mark)
        return move
