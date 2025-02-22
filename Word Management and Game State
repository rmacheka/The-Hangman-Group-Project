import random

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
