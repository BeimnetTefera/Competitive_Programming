class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # This problem has 4 patterns:
            # left ---> right
            # top -----> bottom
            # right ----> left
            # bottom ---> top

        # this process has to go until all elments were appended into result so the loop will be 
        # len(result) < col * row

        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        top = 0
        right = cols - 1
        bottom = rows - 1

        result = []

        while left <= right and top <= bottom:

            # left ----> right:
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # top -----> bottom:
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # right ----> left 
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result