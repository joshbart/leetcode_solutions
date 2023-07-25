import unittest
import solution

s = solution.Solution()

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        data = 0
        expected_result = 0
        actual_result = s.numberOfSteps(data)
        self.assertEqual(actual_result, expected_result)

if __name__ == "__main__":
    unittest.main()