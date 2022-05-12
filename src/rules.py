class Rules:
    def top_row(self, board):
        return board[0:3]

    def middle_row(self, board):
        return board[3:6]

    def bottom_row(self, board):
        return board[6:9]

    def left_column(self, board):
        return [board[0], board[3], board[6]]

    def middle_column(self, board):
        return [board[1], board[4], board[7]]

    def right_column(self, board):
        return [board[2], board[5], board[8]]

    def top_left_btm_right_diag(self, board):
        return [board[0], board[4], board[8]]

    def top_right_btm_left_diag(self, board):
        return [board[2], board[4], board[6]]

    def is_winner_horizontal(self, board):
        top_row_win = self.is_row_array_same(self.top_row(board))
        middle_row_win = self.is_row_array_same(self.middle_row(board))
        bottom_row_win = self.is_row_array_same(self.bottom_row(board))

        if top_row_win or middle_row_win or bottom_row_win:
            return True
        else:
            return False

    def is_winner_vertical(self, board):
        left_column_win = self.is_row_array_same(self.left_column(board))
        middle_column_win = self.is_row_array_same(self.middle_column(board))
        bottom_column_win = self.is_row_array_same(self.right_column(board))

        if left_column_win or middle_column_win or bottom_column_win:
            return True
        else:
            return False

    def is_winner_diagonal(self, board):
        left_to_btm_right_win = self.is_row_array_same(
            self.top_left_btm_right_diag(board)
        )
        right_to_btm_left_win = self.is_row_array_same(
            self.top_right_btm_left_diag(board)
        )
        if left_to_btm_right_win or right_to_btm_left_win:
            return True
        else:
            return False

    def is_winner(self, board):
        if (
            self.is_winner_horizontal(board)
            or self.is_winner_vertical(board)
            or self.is_winner_diagonal(board)
        ):
            return True
        else:
            return False

    def is_row_array_same(self, row_array):
        if len(set(row_array)) <= 1:
            return True
        else:
            return False

    def get_winning_mark(self, board):
        board_rows = [
            self.top_row(board),
            self.middle_row(board),
            self.bottom_row(board),
            self.left_column(board),
            self.middle_column(board),
            self.right_column(board),
            self.top_left_btm_right_diag(board),
            self.top_right_btm_left_diag(board),
        ]
        for row in board_rows:
            if self.is_row_array_same(row):
                return row[0]
