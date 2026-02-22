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

        min_yz = min(yz)
        left = 0
        for val in yz:
            left += (val - min_yz)

        left += (min_yz * rows)

        xy = []
        for col in range(cols):
            max_col = float('-inf')
            for row in range(rows):
                if grid[row][col] > max_col:
                    max_col = grid[row][col]

            xy.append(max_col)

        min_xy = min(xy)
        right = 0
        for val in xy:
            right += (val - min_xy)

        right += (min_xy * cols)

        return left + right + top