class Board:
    def __init__(self):
        self.starter_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.player_one = "X"
        self.player_two = "O"

    def to_string(self, board):
        return f"{board[0]} | {board[1]} | {board[2]}\n--+--+--\n{board[3]} | {board[4]} | {board[5]}\n--+--+--\n{board[6]} | {board[7]} | {board[8]}"

    def count_marks(self, board):
        for mark in board:
            total_marks_on_board = board.count(self.player_one) + board.count(
                self.player_two
            )
        return total_marks_on_board

    def calculate_index(self, user_input):
        return user_input - 1

    def mark_board(self, user_input, board, mark):
        input_index = self.calculate_index(user_input)
        board[input_index] = mark
        return board

    def is_full(self, total_marks_on_board, board):
        if total_marks_on_board == len(board):
            return True
        else:
            return False
