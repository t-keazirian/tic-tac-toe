import random
import math
from src.validator import Validator as validator
from src.rules import Rules
from src.human_player import HumanPlayer
from src.board import Board


class ComputerPlayer:
    def __init__(self, mark):
        self.mark = mark

    def get_move(self, board, message):
        # move = random.randint(1, 9)
        # move = self.best_move(board)
        # if not validator.spot_is_available(self, board, move):
        #     return self.get_move(board, message)
        # return move
        return self.best_move_fn(board)

    def best_move_fn(self, board):
        best_score = -math.inf
        best_move = None
        for mark in board:
            if mark != "X" and mark != "O":
                board[int(mark) - 1] = "X"
                score = self.minimax(board, 0, False)
                board[int(mark) - 1] = mark
                if score > best_score:
                    best_score = score
                    # best_move = board[int(mark) - 1]
                    best_move = mark
        board[int(best_move) - 1] = "X"
        return int(best_move)

    def minimax(self, board, depth, is_maximizing):
        winning_mark = Rules().get_winning_mark(board)

        if Rules().is_winner(board):
            if winning_mark == "O":
                return -10
            elif winning_mark == "X":
                return 10
            elif winning_mark == None:
                return 0

        if is_maximizing:
            best_score = -math.inf
            for mark in board:
                if mark != "X" and mark != "O":
                    board[int(mark) - 1] = "X"
                    score = self.minimax(board, depth + 1, False)
                    board[int(mark) - 1] = mark
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for mark in board:
                if mark != "X" and mark != "O":
                    board[int(mark) - 1] = "O"
                    score = self.minimax(board, depth + 1, True)
                    board[int(mark) - 1] = mark
                    best_score = min(score, best_score)
            return best_score
