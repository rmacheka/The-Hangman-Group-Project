import unittest
from hangman import HangmanGame
import os

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
        self.assertEqual(self.game.get_display_word(), "p______")

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
def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestHangmanGame))
    return test_suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
