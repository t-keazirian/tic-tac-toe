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

    def is_spot_taken(self, board, user_input):
        position_choice = board[user_input - 1]
        if position_choice == self.player_one or position_choice == self.player_two:
            return True
        else:
            return False

    def is_winner_horizontal(self, board):
        if board[0] == board[1] and board[1] == board[2] and board[0] == board[2]:
            return True
        if board[3] == board[4] and board[4] == board[5] and board[3] == board[5]:
            return True
        if board[6] == board[7] and board[7] == board[8] and board[6] == board[8]:
            return True
        else:
            return False

    def is_winner_vertical(self, board):
        if board[0] == board[3] and board[3] == board[6] and board[0] == board[6]:
            return True
        if board[1] == board[4] and board[4] == board[7] and board[1] == board[7]:
            return True
        if board[2] == board[5] and board[5] == board[8] and board[2] == board[8]:
            return True
        else:
            return False
