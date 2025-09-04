import unittest
from task_3 import is_sentence_palindrome


class TestIsSentencePalindrome(unittest.TestCase):
    def test_true_cases(self):
        self.assertTrue(is_sentence_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_sentence_palindrome("No lemon, no melon"))
        self.assertTrue(is_sentence_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_sentence_palindrome("12321"))
        self.assertTrue(is_sentence_palindrome("a"))
        self.assertTrue(is_sentence_palindrome(""))

    def test_false_cases(self):
        self.assertFalse(is_sentence_palindrome("Hello, World!"))
        self.assertFalse(is_sentence_palindrome("Palindrome"))
        self.assertFalse(is_sentence_palindrome("12345"))

    def test_mixed_punctuation_and_case(self):
        self.assertTrue(is_sentence_palindrome("Able was I, ere I saw Elba!"))
        self.assertTrue(is_sentence_palindrome("Eva, can I see bees in a cave?"))
        self.assertTrue(is_sentence_palindrome("Never odd or even."))
        self.assertTrue(is_sentence_palindrome("Step on no pets"))
        self.assertTrue(is_sentence_palindrome("Top spot"))


if __name__ == "__main__":
    unittest.main()

