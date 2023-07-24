import unittest
import solution

s = solution.Solution()

class TestProblem(unittest.TestCase):

    def test_case_1(self):
        data = [1,2,3,4,5]
        expected_result = [3,4,5]
        actual_result = s.middleNode(data)
        self.assertEqual(actual_result, expected_result)

if __name__ == "__main__":
    unittest.main()