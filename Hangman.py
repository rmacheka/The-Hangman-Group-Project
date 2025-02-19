import random
from hangman_utils import select_word, validate_letter, validate_word, get_display, HANGMAN_STAGES

def main():
    word_list = load_word_list("words.txt")
    play_again = True

    while play_again:
        word = select_word(word_list).lower()
        target_length = len(word)
        guessed_letters = set()
        guessed_words = set()
        tries_left = 6
        game_over = False
        win = False

        print(f"\n=== New Game ===\nGuess the {target_length}-letter word!")
        print(HANGMAN_STAGES[0])  # Initial empty gallows

        while not game_over:
            # Display game state
            current_display = get_display(word, guessed_letters)
            print(f"\nWord: {current_display}")
            print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
            print(f"Guessed words: {', '.join(sorted(guessed_words))}")
            print(f"Tries remaining: {tries_left}")

            # Get and validate input
            guess = input("Enter a letter or word guess: ").lower().strip()

            # Process guess
            if len(guess) == 1:
                if not validate_letter(guess, guessed_letters):
                    print("Invalid letter! Either repeat or non-alphabetic.")
                    continue
                guessed_letters.add(guess)
                
                if guess in word:
                    print("Correct letter!")
                    # Check if all letters guessed
                    if all(c in guessed_letters for c in word):
                        win = True
                        game_over = True
                else:
                    print("Wrong letter!")
                    tries_left -= 1
                    print(HANGMAN_STAGES[6 - tries_left])
            elif len(guess) == target_length:
                if not validate_word(guess, guessed_words, target_length):
                    print(f"Invalid word! Must be {target_length} letters and new guess.")
                    continue
                guessed_words.add(guess)
                
                if guess == word:
                    win = True
                    game_over = True
                else:
                    print("Incorrect word!")
                    tries_left -= 1
                    print(HANGMAN_STAGES[6 - tries_left])
            else:
                print(f"Invalid input! Enter 1 letter or {target_length}-letter word.")
                continue

            # Check game over conditions
            if tries_left <= 0:
                game_over = True
            elif all(c in guessed_letters for c in word):
                win = True
                game_over = True

        # Display final result with final hangman state
        if tries_left <= 0:
            print(HANGMAN_STAGES[6])
        if win:
            print(f"\n🎉 Congratulations! You won! The word was: {word}")
        else:
            print(f"\n💀 Game Over! The word was: {word}")

        # Play again prompt
        play_again = input("\nPlay again? (y/n): ").lower().strip() == 'y'

    print("\nThanks for playing!")

def load_word_list(filename):
    try:
        with open(filename, 'r') as file:
            return [line.strip().lower() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"⚠️ Warning: {filename} not found, using default words")
        return ["python", "programming", "challenge", "developer", "openai"]
    except Exception as e:
        print(f"⚠️ Error reading {filename}: {e}, using default words")
        return ["python", "programming", "challenge", "developer", "openai"]

if __name__ == "__main__":
    main()



"""import random
from hangman_utils import select_word, validate_letter, validate_word, get_display

def main():
    word_list = load_word_list("words.txt")
    play_again = True

    while play_again:
        word = select_word(word_list).lower()
        target_length = len(word)
        guessed_letters = set()
        guessed_words = set()
        tries_left = 6
        game_over = False
        win = False

        print(f"\n=== New Game ===\nGuess the {target_length}-letter word!")

        while not game_over:
            # Display game state
            current_display = get_display(word, guessed_letters)
            print(f"\nWord: {current_display}")
            print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
            print(f"Guessed words: {', '.join(sorted(guessed_words))}")
            print(f"Tries remaining: {tries_left}")

            # Get and validate input
            guess = input("Enter a letter or word guess: ").lower().strip()

            # Process guess
            if len(guess) == 1:
                if not validate_letter(guess, guessed_letters):
                    print("Invalid letter! Either repeat or non-alphabetic.")
                    continue
                guessed_letters.add(guess)
                
                if guess in word:
                    print("Correct letter!")
                    # Check if all letters guessed
                    if all(c in guessed_letters for c in word):
                        win = True
                        game_over = True
                else:
                    print("Wrong letter!")
                    tries_left -= 1
            elif len(guess) == target_length:
                if not validate_word(guess, guessed_words, target_length):
                    print(f"Invalid word! Must be {target_length} letters and new guess.")
                    continue
                guessed_words.add(guess)
                
                if guess == word:
                    win = True
                    game_over = True
                else:
                    print("Incorrect word!")
                    tries_left -= 1
            else:
                print(f"Invalid input! Enter 1 letter or {target_length}-letter word.")
                continue

            # Check game over conditions
            if tries_left <= 0:
                game_over = True
            elif all(c in guessed_letters for c in word):
                win = True
                game_over = True

        # Display final result
        if win:
            print(f"\n🎉 Congratulations! You won! The word was: {word}")
        else:
            print(f"\n💀 Game Over! The word was: {word}")

        # Play again prompt
        play_again = input("\nPlay again? (y/n): ").lower().strip() == 'y'

    print("\nThanks for playing!")

def load_word_list(filename):
    try:
        with open(filename, 'r') as file:
            return [line.strip().lower() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"⚠️ Warning: {filename} not found, using default words")
        return ["python", "programming", "challenge", "developer", "openai"]
    except Exception as e:
        print(f"⚠️ Error reading {filename}: {e}, using default words")
        return ["python", "programming", "challenge", "developer", "openai"]

if __name__ == "__main__":
    main()  """