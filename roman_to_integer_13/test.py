import unittest
import solution as s

class TestProblem13(unittest.TestCase):

    def test_case_1(self):
        data = "III"
        result = s.romanToInt(data)
        self.assertEqual(result, 3)

    def test_case_2(self):
        data = "LVIII"
        result = s.romanToInt(data)
        self.assertEqual(result, 58)

    def test_case_3(self, parameter_list):
        data = "MCMXCIV"
        result = s.romanToInt(data)
        self.assertEqual(result, 1994)