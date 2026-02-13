class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()

        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(row + 1, cols):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        return matrix