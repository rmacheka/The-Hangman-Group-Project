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
