from src.board import Board as board_class


class Player:
    def __init__(self):
        self.player_one = "X"
        self.player_two = "O"

    def mark_board_with_user_selection(self, user_input, board, total_marks_on_board):
        board_class.assign_board_index_to_current_player_mark(
            self, user_input, board, total_marks_on_board
        )
        return board

    def get_current_player(self, total_marks_on_board):
        if total_marks_on_board % 2 == 0:
            return self.player_one
        else:
            return self.player_two
