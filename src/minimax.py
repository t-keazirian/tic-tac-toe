import math
from src.board import Board
from src.human_player import HumanPlayer
from src.computer_player import ComputerPlayer
from src.rules import Rules


class Minimax:
    def __init__(self):
        self.computer_player = ComputerPlayer("X")
        self.human_player = HumanPlayer("O")
        # self.game_board = Board().starter_board

    def best_move(self, board):
        best_score = -math.inf
        # best_move = None
        message = None
        move = self.computer_player.get_move(board, message)
        for mark in self.game_board:
            if not board.is_spot_taken(board, move):
                board[mark] = self.computer_player.mark
                score = self.minimax(board, 0, False)
                # reset the mark to the index #
                board[mark] = mark
                if score > best_score:
                    best_score = score
                    move = board[mark]
        board[move] = self.computer_player.mark

    def minimax(self, board, depth, is_maximizing):
        scores = {"X": 10, "O": -10, "tie": 0}

        is_winner = Rules().is_winner(board)
        if is_winner:
            # return scores[get_winning_mark]
            return scores["X"]

        if is_maximizing:
            best_score = -math.inf
            move = self.computer_player.get_move(board, message=None)
            for mark in board:
                if not board.is_spot_taken(board, move):
                    board[mark] = self.computer_player.mark
                    score = self.minimax(board, depth + 1, False)
                    # reset the mark to the index #
                    board[mark] = mark
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for mark in board:
                if not board.is_spot_taken(board, move):
                    board[mark] = self.human_player.mark
                    score = self.minimax(board, depth + 1, True)
                    # reset the mark to the index #
                    board[mark] = mark
                    best_score = min(score, best_score)
            return best_score
