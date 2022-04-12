import re
from src.board import Board


class Validator:
    def is_integer(self, move):
        if re.match(r"^[0-9]*$", move) is None:
            return False
        else:
            return True

    def is_in_range(self, spot):
        if spot in range(1, 10):
            return True
        else:
            return False

    def spot_is_available(self, game_board, spot):
        return not Board().is_spot_taken(game_board, spot)

    def is_valid_move(self, game_board, move):
        if self.is_integer(move):
            spot = int(move)
            if self.is_in_range(spot) and self.spot_is_available(game_board, spot):
                return True
        return False

    def is_valid_play_again_input(self, user_input):
        if user_input.upper() == "Y" or user_input.upper() == "N":
            return True
        else:
            return False
