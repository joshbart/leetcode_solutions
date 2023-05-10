class Solution:
    def romanToInt(self, s: str) -> int:
        arabic = 0
        for index, char in enumerate(s):
            if char == "I":
                try:
                    if s[index + 1] == "V":
                        arabic -= 1
                    elif s[index + 1] == "X":
                        arabic -= 1
                    else:
                        arabic += 1
                except IndexError:
                    arabic += 1
            if char == "V":
                arabic += 5
            if char == "X":
                try:
                    if s[index + 1] == "L":
                        arabic -= 10
                    elif s[index + 1] == "C":
                        arabic -= 10
                    else:
                        arabic += 10
                except IndexError:
                    arabic += 10
            if char == "L":
                arabic += 50
            if char == "C":
                try:
                    if s[index + 1] == "D":
                        arabic -= 1
                    elif s[index + 1] == "M":
                        arabic -= 100
                    else:
                        arabic += 100
                except IndexError:
                    arabic += 100
            if char == "D":
                arabic += 500
            if char == "M":
                arabic += 1000
        return arabic