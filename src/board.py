class Board:
    def __init__(self):
        self.starter_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.player_one = "X"
        self.player_two = "O"

    def count_marks(self, board, player_one, player_two):
        for mark in board:
            total_marks_on_board = board.count(player_one) + board.count(player_two)
        return total_marks_on_board

    # this is both here and in game, and I'm calling it in two places because of circular imports if I pull it in here
    def get_current_player(self, total_marks_on_board):
        if total_marks_on_board % 2 == 0:
            return self.player_one
        else:
            return self.player_two

    def assign_board_index_to_current_player_mark(
        self, user_input, board, total_marks_on_board
    ):
        input_index = user_input - 1
        board[input_index] = self.get_current_player(total_marks_on_board)
        return board[input_index]

    def mark_board(self, user_input, board, total_marks_on_board):
        self.assign_board_index_to_current_player_mark(
            user_input, board, total_marks_on_board
        )
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
