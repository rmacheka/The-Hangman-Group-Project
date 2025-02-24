# =============================
# Take-home Exercise: Create a hangman game (Group Assignment)
# =============================

# Directions:
    # Please work on this assignment in your groups of 2-5 students.
    # If you do not have a group, please let me know, and I will assign you to one.
    # Each group should create a hangman game in pseudo-code format and python code format.

# Tasks:
    # Create a hangman game.
    # Use Psuedo Code to write out your plan for the main script and module functions
    # Save the functions in a separate module and import them into the main program.
    # Use a list of words to choose from. This can be a fixed list or read from a file.
    # The program should display the current state of the word (with underscores for missing letters).
    # The program should allow the user to guess a single letter.
    # The program should update the state of the word with the guessed letter.
    # The program should keep track of the letters that have been guessed.
    # The program should display the number of tries remaining.
    # The program should display a message if the user wins or loses.
    # The program should allow the user to play again.

"""
Hangman Game - Group Assignment

This script implements a complete hangman game by combining work from multiple team members.
The game allows players to guess letters to reveal a hidden word, with a limited number of tries.

Contributors:
- Person 1 (Julie): Word Management & Game State
- Person 2 (Emmanuel): User Interface & Display
- Person 3 (Rujeko): Game Logic & Rules
- Person 4 (Zhang): Testing & Error Handling
- Person 5 (Ade): Main Game Coordination & Documentation

Usage:
    python hangman_game.py
"""

"""
# Hangman Game Pseudo-code

## Main Game Loop
1. Initialize all components:
   - Create WordManager with list of words
   - Create Display for user interface
   - Create GameLogic for game rules

2. WHILE player wants to play:
   - Start a new game
   - Select random word
   - Reset game state
   
   - WHILE game is not over:
     - Display current hangman state
     - Display word with blanks for unguessed letters
     - Display already guessed letters
     - Display remaining tries
     
     - Get user input (a single letter)
     - Validate the input (must be single letter, not already guessed)
     - IF valid input:
        - Process the guess
        - Check if letter is in word
        - Update game state
     - ELSE:
        - Show error message and prompt again
     
     - Check if game is over (player won or lost)
   
   - Display final game state
   - IF player won:
     - Display victory message
   - ELSE:
     - Display defeat message and reveal the word
   
   - Ask if player wants to play again
   
3. End game with goodbye message

## Component Responsibilities

### WordManager (Person 1 - Julie)
- Store list of available words
- Select random word for a game
- Track which letters have been revealed
- Check if word is complete
- Get display version of word (with blanks)

### Display (Person 2 - Emmanuel)
- Show hangman ASCII art
- Show current word state
- Show guessed letters
- Show remaining tries
- Show victory/defeat messages
- Handle user input

### GameLogic/GameState (Person 3 - Rujeko)
- Validate guesses
- Process guesses
- Update word state after guess
- Track game progress
- Check win/loss conditions
- Implement game retry

### Testing & Error Handling (Person 4 - Zhang)
- Test all game functionality
- Handle invalid inputs
- Handle file errors
- Handle edge cases

### Main Game Coordination (Person 5 - Ade)
- Create main game loop
- Coordinate between components
- Ensure smooth game flow
- Handle module integration
- Document the code
"""

import random
import unittest
import os

# =============================================================================
# Person 1 (Julie): Word Management and Game State
# =============================================================================

class WordManager:
    def __init__(self, words=None):
        self.words = words if words else ["challenge", "galaxy", "adventure", "puzzle", "mystery", "fantasy", "treasure", "enchanted"]
        self.selected_word = ""
        self.revealed_letters = []
    
    def select_word(self):
        self.selected_word = random.choice(self.words)
        self.revealed_letters = ["_" for _ in self.selected_word]
    
    def reveal_letter(self, letter):
        for idx, char in enumerate(self.selected_word):
            if char == letter:
                self.revealed_letters[idx] = letter
    
    def is_word_complete(self):
        return "_" not in self.revealed_letters
    
    def get_display_word(self):
        return " ".join(self.revealed_letters)


class GameState:
    def __init__(self, max_tries=6):
        self.max_tries = max_tries
        self.remaining_tries = max_tries
        self.guessed_letters = set()
    
    def guess_letter(self, letter, word_manager):
        if letter in self.guessed_letters:
            return False  # Letter already guessed
        
        self.guessed_letters.add(letter)
        
        if letter in word_manager.selected_word:
            word_manager.reveal_letter(letter)
            return True
        else:
            self.remaining_tries -= 1
            return False
    
    def is_game_over(self, word_manager):
        return self.remaining_tries == 0 or word_manager.is_word_complete()
    
    def is_winner(self, word_manager):
        return word_manager.is_word_complete()


# =============================================================================
# Person 2 (Emmanuel): Display
# =============================================================================

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


# =============================================================================
# Person 3 (Rujeko): Game Logic
# =============================================================================

class GameLogic:
    def __init__(self):
        """
        Initialize the game logic with default values.
        The actual values will be set when starting a new game.
        """
        self.word = ""
        self.word_state = []
        self.guessed_letters = set()
        self.remaining_tries = 6
        self.game_won = False
        self.game_over = False

    def start_new_game(self, word):
        """
        Start a new game with the given word.
        
        Args:
            word (str): The word to be guessed
        """
        self.word = word.lower()
        self.word_state = ['_' for _ in word]
        self.guessed_letters = set()
        self.remaining_tries = 6
        self.game_won = False
        self.game_over = False

    def validate_guess(self, guess):
        """
        Validate if the guess is acceptable.
        
        Args:
            guess (str): The letter guessed by the player
            
        Returns:
            tuple: (bool, str) - (is_valid, error_message)
        """
        if not guess.isalpha():
            return False, "Please enter a letter."
        if len(guess) != 1:
            return False, "Please enter a single letter."
        if guess.lower() in self.guessed_letters:
            return False, "You already guessed that letter."
        return True, ""

    def make_guess(self, guess):
        """
        Process a player's guess and update game state.
        
        Args:
            guess (str): The letter guessed by the player
            
        Returns:
            tuple: (bool, str) - (is_correct, message)
        """
        guess = guess.lower()
        self.guessed_letters.add(guess)
        
        if guess in self.word:
            # Update word state with correct guess
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_state[i] = guess
            return True, "Correct guess!"
        else:
            self.remaining_tries -= 1
            return False, "Incorrect guess!"

    def update_game_status(self):
        """
        Update the game status after each guess.
        
        Returns:
            tuple: (bool, str) - (is_game_over, status_message)
        """
        # Check for win condition
        if '_' not in self.word_state:
            self.game_won = True
            self.game_over = True
            return True, "Congratulations! You won!"
        
        # Check for loss condition
        if self.remaining_tries <= 0:
            self.game_over = True
            return True, f"Game Over! The word was: {self.word}"
        
        return False, f"Remaining tries: {self.remaining_tries}"

    def get_game_state(self):
        """
        Get the current state of the game.
        
        Returns:
            dict: Current game state information
        """
        return {
            'word_state': ' '.join(self.word_state),
            'guessed_letters': sorted(list(self.guessed_letters)),
            'remaining_tries': self.remaining_tries,
            'game_over': self.game_over,
            'game_won': self.game_won
        }

    def retry_game(self):
        """
        Check if player can retry and prepare for a new game.
        
        Returns:
            bool: True if retry is possible
        """
        if self.game_over:
            return True
        return False


# =============================================================================
# Person 4 (Zhang): Testing and Error Handling
# =============================================================================

class HangmanGame:
    """
    Adapter class to make testing work with our implementation.
    This bridges Zhang's tests with our actual implementation.
    """
    def __init__(self, word_list=None):
        self.word_manager = WordManager(word_list)
        self.word_manager.select_word()
        self.game_state = GameState()
        self.game_logic = GameLogic()
        self.game_logic.start_new_game(self.word_manager.selected_word)
    
    def guess(self, letter):
        # Validate input
        is_valid, error_message = self.game_logic.validate_guess(letter)
        if not is_valid:
            raise ValueError(error_message)
        
        # Make the guess
        return self.game_state.guess_letter(letter, self.word_manager)
    
    def get_display_word(self):
        return self.word_manager.get_display_word()
    
    def is_game_over(self):
        return self.game_state.is_game_over(self.word_manager)
    
    @staticmethod
    def load_words(filename):
        """Load words from a file."""
        try:
            with open(filename, 'r') as f:
                words = [line.strip() for line in f if line.strip().isalpha()]
            
            if not words:
                raise ValueError("File contains no valid words")
                
            return words
        except FileNotFoundError:
            raise FileNotFoundError(f"Word file '{filename}' not found")


class TestHangmanGame(unittest.TestCase):
    
    def setUp(self):
        """Initialize a Hangman game instance before each test"""
        self.game = HangmanGame(["python", "java", "kotlin"])

    # 1. Test invalid inputs
    def test_invalid_input_numbers(self):
        with self.assertRaises(ValueError):
            self.game.guess("5")  

    def test_invalid_input_special_chars(self):
        with self.assertRaises(ValueError):
            self.game.guess("@")  

    def test_invalid_input_multiple_letters(self):
        with self.assertRaises(ValueError):
            self.game.guess("ab")  

    def test_invalid_input_empty_string(self):
        with self.assertRaises(ValueError):
            self.game.guess("")  

    def test_invalid_input_whitespace(self):
        with self.assertRaises(ValueError):
            self.game.guess("  ")  

    # 2. Test valid guess
    def test_valid_guess(self):
        self.assertTrue(self.game.guess("p"))  

    # 3. Test repeated guess
    def test_repeated_guess(self):
        self.game.guess("p")  
        with self.assertRaises(ValueError):
            self.game.guess("p")  

    # 4. Test word reveal after correct guesses
    def test_reveal_word(self):
        self.game.guess("p")
        self.assertEqual(self.game.get_display_word(), "p _ _ _ _ _")

    # 5. Test losing the game (max guesses exceeded)
    def test_max_attempts_exceeded(self):
        for letter in "xyzmnbv":  
            self.game.guess(letter)
        self.assertTrue(self.game.is_game_over())

    # 6. Test file operations
    def test_missing_word_file(self):
        """Ensure error is handled when file is missing"""
        with self.assertRaises(FileNotFoundError):
            HangmanGame.load_words("non_existent_file.txt")

    def test_corrupt_file_handling(self):
        """Ensure error is handled when file has invalid data"""
        with open("test_words.txt", "w") as f:
            f.write("1234\n!@#$\n") 
        with self.assertRaises(ValueError):
            HangmanGame.load_words("test_words.txt")
        os.remove("test_words.txt")


# Create a test suite
def test_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestHangmanGame))
    return test_suite


# =============================================================================
# Person 5 (Ade): Main Game Coordination & Documentation
# =============================================================================

def run_tests():
    """Run the test suite to verify game functionality."""
    print("Running Hangman Game tests...")
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite())
    print("Tests completed.\n")
    return result.wasSuccessful()


def main():
    """
    Main game loop that coordinates all components.
    
    This function:
    1. Initializes all game components
    2. Manages the game flow
    3. Handles user interaction
    4. Controls game restart
    """
    # Welcome message
    print("\n===== HANGMAN GAME =====")
    print("Try to guess the word by suggesting letters.\n")
    
    # Initialize components
    word_list = ["challenge", "galaxy", "adventure", "puzzle", "mystery", 
                "fantasy", "treasure", "enchanted", "python", "journey",
                "victory", "champion", "knowledge", "discovery", "imagination"]
    word_manager = WordManager(word_list)
    display = Display()
    
    play_again = True
    
    # Main game loop
    while play_again:
        # Start a new game
        word_manager.select_word()
        game_state = GameState()
        game_logic = GameLogic()
        game_logic.start_new_game(word_manager.selected_word)
        
        print("\nA new game has started!")
        
        # Game round loop
        while not game_state.is_game_over(word_manager):
            # Display current game state
            display.display_hangman(game_state.remaining_tries)
            display.show_word_state(word_manager)
            display.show_guessed_letters(game_state)
            display.display_remaining_tries(game_state)
            
            # Get and validate user input
            user_guess = display.handle_user_input()
            
            is_valid, error_message = game_logic.validate_guess(user_guess)
            if not is_valid:
                print(error_message)
                continue
            
            # Process the guess
            result = game_state.guess_letter(user_guess, word_manager)
            
            # Update GameLogic state to match GameState for validation
            game_logic.guessed_letters = game_state.guessed_letters
            game_logic.remaining_tries = game_state.remaining_tries
            
            # Display result of the guess
            if result:
                print("Good guess!")
            else:
                print("Incorrect guess!")
        
        # Game over - display final result
        display.display_hangman(game_state.remaining_tries)
        display.show_word_state(word_manager)
        
        if game_state.is_winner(word_manager):
            display.display_victory_message()
        else:
            display.display_defeat_message(word_manager)
        
        # Ask to play again
        play_again_input = input("\nDo you want to play again? (y/n): ").lower()
        play_again = play_again_input.startswith('y')
    
    print("\nThanks for playing Hangman! Goodbye!\n")


if __name__ == "__main__":
    # Optionally run tests before starting the game
    # Uncomment the next line to run tests first
    # run_tests()
    
    # Start the game
    main()
