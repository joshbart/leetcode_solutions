import unittest
import solution

s = solution.Solution()

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        data = 14
        expected_result = 6
        actual_result = s.numberOfSteps(data)
        self.assertEqual(actual_result, expected_result)

    def test_case_2(self):
        data = 8
        expected_result = 4
        actual_result = s.numberOfSteps(data)
        self.assertEqual(actual_result, expected_result)

    def test_case_3(self):
        data = 123
        expected_result = 12
        actual_result = s.numberOfSteps(data)
        self.assertEqual(actual_result, expected_result)

if __name__ == "__main__":
    unittest.main()