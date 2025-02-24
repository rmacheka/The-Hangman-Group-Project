# display.py
class Display:
    def __init__(self):
        self.hangman_stages = [
            """
               -----
               |   |
                   |
                   |
                   |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
                   |
                   |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
               |   |
                   |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
              /|   |
                   |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
                   |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
              /    |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
              / \\  |
                   |
            =========
            """
        ]

    def display_hangman(self, tries_remaining):
        print(self.hangman_stages[6 - tries_remaining])

    def show_word_state(self, word_manager):
        print("Current word: " + word_manager.get_display_word())

    def show_guessed_letters(self, game_state):
        print("Guessed letters: " + ", ".join(sorted(game_state.guessed_letters)))

    def display_remaining_tries(self, game_state):
        print(f"Remaining tries: {game_state.remaining_tries}")

    def display_victory_message(self):
        print("Congratulations! You've won!")

    def display_defeat_message(self, word_manager):
        print(f"Game Over! The word was: {word_manager.selected_word}")

    def handle_user_input(self):
        return input("Enter your guess: ").lower().strip()
