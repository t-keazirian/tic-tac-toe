class Message:
    def __init__(self):
        pass

    def display_welcome_message(self):
        print("Welcome to Tic Tac Toe")

    def display_game_over_message(self):
        print("Game Over!")

    def display_prompt_message_for_move(self, current_player):
        print(f"Player {current_player} - enter a number to place your mark")

    def display_error_prompt_for_occupied_spot(self):
        print("Spot is taken - choose another spot")
