import random
import math
from src.validator import Validator as validator
from src.rules import Rules
from src.human_player import HumanPlayer
from src.board import Board

# from src.game import Game

# from src.minimax import Minimax


class ComputerPlayer:
    def __init__(self, mark):
        self.mark = mark
        # self.minimax = Minimax()

    def get_move(self, board, message):
        move = random.randint(1, 9)
        # move = self.best_move(board)
        if not validator.spot_is_available(self, board, move):
            return self.get_move(board, message)
        return move

    def best_move(self, board):
        best_score = -math.inf
        # best_move = None
        for mark in board:
            print(mark, "mark")
            if not Board().is_spot_taken(board, mark):
                board[int(mark)] = self.mark
                score = self.minimax(board, 0, False)
                # reset the mark to the index #
                board[mark] = mark
                if score > best_score:
                    best_score = score
                    move = board[mark]
        board[move] = self.mark

    def minimax(self, board, depth, is_maximizing):
        scores = {"X": 10, "O": -10, "tie": 0}
        winning_mark = Game().get_winning_mark(Game().total_marks_on_board)

        if winning_mark == "X":
            return scores["X"]
        elif winning_mark == "O":
            return scores["O"]
        elif Rules().is_winner is False:
            return 0

        # if Rules().is_winner(board):
        #     return scores["X"]

        if is_maximizing:
            best_score = -math.inf
            for mark in board:
                if not Board().is_spot_taken(board, mark):
                    board[int(mark)] = self.mark
                    score = self.minimax(board, depth + 1, False)
                    # reset the mark to the index #
                    board[mark] = mark
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for mark in board:
                if not Board().is_spot_taken(board, mark):
                    board[int(mark)] = self.mark
                    score = self.minimax(board, depth + 1, True)
                    # reset the mark to the index #
                    board[mark] = mark
                    best_score = min(score, best_score)
            return best_score
