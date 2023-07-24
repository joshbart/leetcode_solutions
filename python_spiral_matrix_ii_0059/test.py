import unittest
import solution

s = solution.Solution()

class TestProblem13(unittest.TestCase):

    def test_case_1(self):
        data = 3
        result = s.generateMatrix(data)
        self.assertEqual(result, [[1,2,3],[8,9,4],[7,6,5]])

    def test_case_2(self):
        data = 1
        result = s.generateMatrix(data)
        self.assertEqual(result, [[1]])

    def test_case_3(self):
        data = 4
        result = s.generateMatrix(data)
        self.assertEqual(result, [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]])

if __name__ == "__main__":
    unittest.main()