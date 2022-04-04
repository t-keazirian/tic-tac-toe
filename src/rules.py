class Rules:
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

    def is_winner_diagonal(self, board):
        if board[0] == board[4] and board[4] == board[8] and board[0] == board[8]:
            return True
        if board[2] == board[4] and board[4] == board[6] and board[2] == board[6]:
            return True
        else:
            return False

    def determine_is_winner(self, board):
        if (
            self.is_winner_horizontal(board)
            or self.is_winner_vertical(board)
            or self.is_winner_diagonal(board)
        ):
            return True
        else:
            return False
