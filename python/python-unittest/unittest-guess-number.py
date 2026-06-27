import unittest
import to_be_test_guess_number


class testmain(unittest.TestCase):

    # def setUp(self):
    #     print("Run the function!!")

    def test_right_answer(self):
        answer = 5
        guess = 5
        result = to_be_test_guess_number.run_guess(guess, answer)
        self.assertTrue(result)

    def test_wrong_answer(self):
        answer = 5
        guess = 6
        result = to_be_test_guess_number.run_guess(guess, answer)
        self.assertEqual(result, None)

    def test_wrong_type(self):
        answer = 5
        guess = "fe"
        result = to_be_test_guess_number.run_guess(guess, answer)
        self.assertEqual(result, TypeError)


if __name__ == '__main__':
    unittest.main()
