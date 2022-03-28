from src.board import Board


class Player:
    def __init__(self):
        self.board_class = Board()
        self.player_one = self.board_class.player_one
        self.player_two = self.board_class.player_two

    def get_current_player(self, total_marks_on_board):
        if total_marks_on_board % 2 == 0:
            return self.player_one
        else:
            return self.player_two
