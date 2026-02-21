class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        res = []
        for row in range(rows):
            for col in range(cols):
                res.append(grid[row][col])

        for _ in range(k):
            value = []
            value.append(res.pop())
            for i in range(len(res)):
                value.append(res[i])
            res = value

        matrix = [[0] * cols for _ in range(rows)]

        for j in range(len(res)):
            row_number = j // cols
            column_number = j % cols
            matrix[row_number][column_number] = res[j]

        return matrix