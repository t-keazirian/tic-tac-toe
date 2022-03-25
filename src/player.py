class Player:
    def __init__(self):
        self.player_one = "X"
        self.player_two = "O"

    def mark_board_with_user_selection(self, user_input, board, total_marks_on_board):
        self.assign_board_index_to_current_player_mark(
            user_input, board, total_marks_on_board
        )
        return board
