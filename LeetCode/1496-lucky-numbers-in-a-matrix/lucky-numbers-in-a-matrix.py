class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])

        result = []
        for row in range(rows):
            min_val = float('inf')
            for col in range(cols):
                if min_val > matrix[row][col]:
                    min_val = matrix[row][col]
                    col_idx = col

            max_col_val = float('-inf')
            for i in range(rows):
                
                if i == row:
                    continue
                else:
                    if max_col_val < matrix[i][col_idx]:
                        max_col_val = matrix[i][col_idx]

            if max_col_val < min_val:
                result.append(min_val)

        return result
