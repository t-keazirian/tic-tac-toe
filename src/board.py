class Board:
    def __init__(self):
        self.starter_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def count_marks_in_board(self, player_one, player_two):
        for mark in self.starter_board:
            total_marks_on_board = self.starter_board.count(
                player_one
            ) + self.starter_board.count(player_two)
        return total_marks_on_board

    def get_current_player(self, total_marks_on_board):
        if total_marks_on_board == 0:
            return "X"
        elif total_marks_on_board % 2 == 0:
            return "X"
        else:
            return "O"
