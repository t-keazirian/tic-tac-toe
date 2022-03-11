from src.game import Game

if __name__ == "__main__":
    board = Game.board
    game = Game()
    game.display_welcome_message()
    game.display_board(board)
