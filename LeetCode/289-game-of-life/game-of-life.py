class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        cols = len(board[0])

        copy_board = [row[:] for row in board]

        for row in range(rows):
            for col in range(cols):
                
                count_1 = 0
                count_0 = 0

                for i in (row - 1, row, row + 1):
                    for j in (col - 1, col, col + 1):

                        if 0 <= i < rows and 0 <= j < cols:
                            if copy_board[i][j] == 0:
                                count_0 += 1
                            else:
                                count_1 += 1
                

                if board[row][col] == 1:
                    count_1 -= 1
                    if count_1 < 2 or count_1 > 3:
                        board[row][col] = 0
                    elif count_1 in [2, 3]:
                        board[row][col] = 1

                else:
                    count_0 -= 1
                    if count_1 == 3:
                        board[row][col] = 1

        return board