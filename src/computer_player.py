import random


class ComputerPlayer:
    def __init__(self):
        self.player_one_mark = "X"
        self.player_two_mark = "O"

    def computer_input(self):
        return random.randint(1, 9)
