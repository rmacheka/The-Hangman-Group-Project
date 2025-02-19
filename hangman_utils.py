import random

HANGMAN_STAGES = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """
]

def select_word(word_list):
    """Randomly select a word from the list"""
    return random.choice(word_list)

def validate_letter(guess, guessed_letters):
    """Validate letter input"""
    return len(guess) == 1 and guess.isalpha() and guess not in guessed_letters

def validate_word(guess, guessed_words, target_length):
    """Validate word input"""
    return (len(guess) == target_length 
            and guess.isalpha() 
            and guess not in guessed_words)

def get_display(word, guessed_letters):
    """Create display string with guessed letters revealed"""
    return ' '.join([char if char in guessed_letters else '_' for char in word])

