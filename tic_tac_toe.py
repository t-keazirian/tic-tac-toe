from src.game import Game
from src.message import Message
from src.user_interface import UserInterface

if __name__ == "__main__":
    ui = UserInterface()
    message = Message()
    game = Game(ui, message)
    game.run()
