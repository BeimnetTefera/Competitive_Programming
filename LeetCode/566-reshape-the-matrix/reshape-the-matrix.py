class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        if rows * cols != r * c:
            return mat

        res = [0 for _ in range (rows * cols)]

        for row in range (rows):
            for col in range(cols):
                idx = row * cols + col
                res[idx] = mat[row][col]

        final_result = [[0] * c for _ in range(r)]

        for cell_number in range(len(res)):

            row_number = cell_number // c
            column_number = cell_number % c
            final_result[row_number][column_number] = res[cell_number]

        return final_result