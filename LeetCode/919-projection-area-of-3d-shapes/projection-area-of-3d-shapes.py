class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        top = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 0:
                    top += 1


        yz = []
        for row in range(rows):
            max_row = float('-inf')
            for col in range(cols):
                if grid[row][col] > max_row:
                    max_row = grid[row][col]
            yz.append(max_row)

        left = sum(yz)

        xy = []
        for col in range(cols):
            max_col = float('-inf')
            for row in range(rows):
                if grid[row][col] > max_col:
                    max_col = grid[row][col]
            xy.append(max_col)

        right = sum(xy)

        return left + right + top