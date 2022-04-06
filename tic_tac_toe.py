from src.game import Game
from src.user_interface import UserInterface

if __name__ == "__main__":
    ui = UserInterface()
    game = Game(ui)
    game.run()
