import math
from src.rules import Rules


class AIUnbeatable:
    def get_computer_move(self, board, mark, opponent_mark):
        return self.best_move_fn(board, mark, opponent_mark)

    def best_move_fn(self, board, maximizing_player, minimizing_player):
        best_score = -math.inf
        best_move = None
        for spot in board:
            if spot != maximizing_player and spot != minimizing_player:
                board[int(spot) - 1] = maximizing_player
                score = self.minimax(
                    board, 0, False, maximizing_player, minimizing_player
                )
                board[int(spot) - 1] = spot
                if score > best_score:
                    best_score = score
                    best_move = spot
        return int(best_move)

    def minimax(
        self, board, depth, is_maximizing, maximizing_player, minimizing_player
    ):
        winning_mark = Rules().get_winning_mark(board)

        if Rules().is_winner(board):
            if winning_mark == minimizing_player:
                return -10
            elif winning_mark == maximizing_player:
                return 10
            elif winning_mark == None:
                return 0

        if is_maximizing:
            best_score = -math.inf
            for spot in board:
                if spot != maximizing_player and spot != minimizing_player:
                    board[int(spot) - 1] = maximizing_player
                    score = self.minimax(
                        board, depth + 1, False, maximizing_player, minimizing_player
                    )
                    board[int(spot) - 1] = spot
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for spot in board:
                if spot != maximizing_player and spot != minimizing_player:
                    board[int(spot) - 1] = minimizing_player
                    score = self.minimax(
                        board, depth + 1, True, maximizing_player, minimizing_player
                    )
                    board[int(spot) - 1] = spot
                    best_score = min(score, best_score)
            return best_score
