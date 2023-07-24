class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for x in range(n)]
        column_index = 0
        row_index = 0
        for i in range(n**2):
            matrix[row_index][column_index] = (i + 1)
            if i < (n-1):
                column_index += 1
                print(column_index)
        return matrix