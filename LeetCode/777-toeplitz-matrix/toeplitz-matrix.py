class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                if row + 1 < rows and col + 1 < cols:
                    if matrix[row][col] != matrix[row + 1][col + 1]:
                        return False
        
        return True