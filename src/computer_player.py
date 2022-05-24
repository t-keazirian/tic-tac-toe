class ComputerPlayer:
    def __init__(self, mark, ai):
        self.mark = mark
        self.ai = ai

    def get_move(self, board, mark, opponent_mark):
        return self.ai.get_computer_move(board, mark, opponent_mark)
