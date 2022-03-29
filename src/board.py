class Board:
    def __init__(self):
        self.starter_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.player_one = "X"
        self.player_two = "O"

    def count_marks(self, board):
        for mark in board:
            total_marks_on_board = board.count(self.player_one) + board.count(
                self.player_two
            )
        return total_marks_on_board

    def assign_board_index_to_current_player_mark(self, user_input, board, mark):
        input_index = user_input - 1
        board[input_index] = mark
        return board[input_index]

    def mark_board(self, user_input, board, mark):
        self.assign_board_index_to_current_player_mark(user_input, board, mark)
        return board

    def is_full(self, total_marks_on_board, board):
        if total_marks_on_board == len(board):
            return True
        else:
            return False

    # tests are passing but not working as expected
    def is_spot_taken(self, board, user_input):
        if (board[user_input] == self.player_one) or (
            board[user_input] == self.player_two
        ):
            return True
        else:
            return False
