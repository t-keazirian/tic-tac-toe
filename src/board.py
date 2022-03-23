class Board:
    def __init__(self):
        self.starter_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def count_marks_in_board(self, board, player_one, player_two):
        for mark in board:
            total_marks_on_board = board.count(player_one) + board.count(player_two)
        return total_marks_on_board

    def get_current_player(self, total_marks_on_board):
        if total_marks_on_board == 0:
            return "X"
        elif total_marks_on_board % 2 == 0:
            return "X"
        else:
            return "O"

    def place_mark_on_board(self, user_input, board, total_marks_on_board):
        input_index = user_input - 1
        board[input_index] = self.get_current_player(total_marks_on_board)
        return board

    def is_board_full(self, total_marks_on_board, board):
        if total_marks_on_board == len(board):
            return True
        else:
            return False

    def take_turns_marking_board(self, board):
        while self.is_board_full is False:
            return self.place_mark_on_board()
