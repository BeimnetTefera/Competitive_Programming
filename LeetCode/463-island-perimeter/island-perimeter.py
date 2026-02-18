class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == 1:
                    perimeter += 4

                    for vertical in (row - 1, row + 1):
                        if vertical >= 0 and vertical < rows:
                            if grid[vertical][col] == 1:
                                perimeter -= 1

                    for horizontal in (col - 1, col + 1):
                        if horizontal >= 0 and horizontal < cols: 
                            if grid[row][horizontal] == 1:
                                perimeter -= 1

        return perimeter