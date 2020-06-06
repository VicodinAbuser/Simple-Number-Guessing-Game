import unittest
import random_number_guess

class run_test(unittest.TestCase):
    def test01(self):
        guess = 5
        answer = 5
        result = random_number_guess.guess_number(guess,answer)
        self.assertTrue(result)

    def test02(self):
        guess = 2
        answer = 5
        result = random_number_guess.guess_number(guess,answer)
        self.assertFalse(result)

    def test03(self):
        result = random_number_guess.guess_number(80, 6)
        self.assertEqual(result, None )

if __name__ == '__main__':
   unittest.main()