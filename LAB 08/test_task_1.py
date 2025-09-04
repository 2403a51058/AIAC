import unittest
from task_1 import is_valid_email


class TestIsValidEmail(unittest.TestCase):
    def test_valid_emails(self):
        self.assertTrue(is_valid_email("user@example.com"))
        self.assertTrue(is_valid_email("john.doe@domain.co.uk"))
        self.assertTrue(is_valid_email("a_b.c-d@sub.domain.com"))

    def test_missing_at(self):
        self.assertFalse(is_valid_email("userexample.com"))
        self.assertFalse(is_valid_email("user.example.com"))

    def test_multiple_at(self):
        self.assertFalse(is_valid_email("user@@example.com"))
        self.assertFalse(is_valid_email("user@ex@ample.com"))

    def test_missing_dot(self):
        self.assertFalse(is_valid_email("user@examplecom"))
        self.assertFalse(is_valid_email("user@com"))

    def test_starts_or_ends_with_special(self):
        self.assertFalse(is_valid_email(".user@example.com"))
        self.assertFalse(is_valid_email("user@example.com."))
        self.assertFalse(is_valid_email("@user@example.com"))
        self.assertFalse(is_valid_email("user@example.com@"))

    def test_adjacent_or_doubled_specials(self):
        self.assertFalse(is_valid_email("user..name@example.com"))
        self.assertFalse(is_valid_email("user.@example.com"))
        self.assertFalse(is_valid_email("user@.example.com"))

    def test_empty_and_non_string(self):
        self.assertFalse(is_valid_email(""))
        self.assertFalse(is_valid_email(None))
        self.assertFalse(is_valid_email(12345))
        self.assertFalse(is_valid_email([]))


if __name__ == "__main__":
    unittest.main()



