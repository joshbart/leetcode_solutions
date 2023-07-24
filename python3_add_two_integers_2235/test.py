import unittest
import solution

s = solution.Solution()

class TestProblem(unittest.TestCase):

    def test_case_1(self):
        data1 = 12
        data2 = 5
        result = s.sum(data1, data2)
        self.assertEqual(result, 17)

    def test_case_2(self):
        data1 = -10
        data2 = 4
        result = s.sum(data1, data2)
        self.assertEqual(result, -6)

if __name__ == "__main__":
    unittest.main()