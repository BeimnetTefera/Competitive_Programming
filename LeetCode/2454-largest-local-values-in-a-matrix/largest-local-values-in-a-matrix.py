class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        size = len(grid)
        res = [[0] * (size - 2) for _ in range(size - 2)]


        rows_res = len(res)
        cols_res = len(res[0])

        for row in range(rows_res):
            for col in range(cols_res):

                max_num = 0
                for r in range(row, row + 3):
                    for c in range(col, col + 3):
                        
                        max_num = max(max_num, grid[r][c])

                res[row][col] = max_num

        return res