class Board:
    def __init__(self):
        self.status = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def count_marks_in_board(self, player_one, player_two):
        for mark in self.status:
            play_count = self.status.count(player_one) + self.status.count(player_two)
        return play_count

    def get_current_player(self, play_count):
        if play_count == 0:
            return "X"
        elif play_count % 2 == 0:
            return "X"
        else:
            return "O"
