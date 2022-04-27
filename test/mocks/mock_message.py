from src.symbol import SymbolOptions


class MockMessage:
    def welcome_message(self):
        return "welcome_message"

    def menu(self):
        return "menu"

    def display_symbols(self):
        symbols = SymbolOptions().symbols
        return f"display_symbols {symbols}"

    def invalid_menu_input(self):
        return "invalid_menu_input"
    def invalid_choose_symbol_input(self):
        return "invalid_choose_symbol_input"

    def invalid_symbol_option(self):
        return "invalid_symbol_option"

    def choose_player_symbol(self):
        return "choose_player_symbol"

    def rules(self):
        return "rules"

    def game_over_message(self):
        return "game_over_message"

    def prompt_for_move(self, current_player):
        return f"prompt_for_move {current_player}"

    def declare_winner(self, winner):
        return f"declare_winner {winner}"

    def invalid_board_input(self):
        return "invalid_board_input"

    def play_again_prompt(self):
        return "play_again_prompt"

    def goodbye_message(self):
        return "goodbye_message"

    def invalid_repeat_game_input(self):
        return "invalid_repeat_game_input"

    def choose_language(self):
        return "choose_language"
