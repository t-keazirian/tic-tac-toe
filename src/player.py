from src.board import Board


class Player:
    def __init__(self):
        self.board_class = Board()
        self.player_one = self.board_class.player_one
        self.player_two = self.board_class.player_two

    def mark_board_with_user_selection(self, user_input, board, total_marks_on_board):
        self.board_class.assign_board_index_to_current_player_mark(
            user_input, board, total_marks_on_board
        )
        return board

    def get_current_player(self, total_marks_on_board):
        if total_marks_on_board % 2 == 0:
            return self.player_one
        else:
            return self.player_two
