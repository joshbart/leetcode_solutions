import unittest
import solution

s = solution.Solution()

class TestProblem(unittest.TestCase):

    def test_case_1(self):
        data = [[1,2,3],[3,2,1]]
        result = s.maximumWealth(data)
        self.assertEqual(result, 6)

    def test_case_2(self):
        data = [[1,5],[7,3],[3,5]]
        result = s.maximumWealth(data)
        self.assertEqual(result, 10)

    def test_case_3(self):
        data = [[2,8,7],[7,1,3],[1,9,5]]
        result = s.maximumWealth(data)
        self.assertEqual(result, 17)

if __name__ == "__main__":
    unittest.main()