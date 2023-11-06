import unittest
from math_quiz import random_int, random_operation_selection, calculate


class TestMathGame(unittest.TestCase):

    def test_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operation_selection(self):
        # Test whether the random_operation_selection only returns 3 types of possible operations.
        for _ in range(10):  
            operation_selected = random_operation_selection()
            self.assertTrue(operation_selected == '+' or operation_selected == '-' or operation_selected == '*') 

    def test_calculate(self):
            # Test whether the problem-created and answer-calculated by the calculate function are correct. 
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (4, 3, '-', '4 - 3', 1),
                (1, 8, '*', '1 * 8', 8),
                (6, 9, '*', '6 * 9', 54),
                (8, 6, '-', '8 - 6', 2),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = calculate(num1,num2,operator)
                self.assertTrue(problem == expected_problem and answer == expected_answer)

if __name__ == "__main__":
    unittest.main()
