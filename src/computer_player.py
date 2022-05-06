import random
from src.validator import Validator as validator


class ComputerPlayer:
    def __init__(self):
        self.player_one_mark = "X"
        self.player_two_mark = "O"

    def computer_input(self):
        return random.randint(1, 9)

    # def valid_computer_move(self, move, board):
    #     if not validator.spot_is_available(self, board, move):
    #         return self.valid_computer_move(self.computer_input(), board)
    #     return move

    def valid_computer_move(self, move, board):
        if validator.spot_is_available(self, board, move):
            return True
        else:
            return False

    # change to get_move
    def get_computer_move(self, move, board):
        if not self.valid_computer_move(move, board):
            move = self.computer_input()
            return self.get_computer_move(move, board)
        return move
