import unittest

from main import check_guess


class CheckGuessTests(unittest.TestCase):
    def test_guess_below_secret_is_low(self):
        self.assertEqual(check_guess(50, 25), "low")

    def test_guess_above_secret_is_high(self):
        self.assertEqual(check_guess(50, 75), "high")

    def test_guess_equal_to_secret_is_correct(self):
        self.assertEqual(check_guess(50, 50), "correct")


if __name__ == "__main__":
    unittest.main()
