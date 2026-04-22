class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = len(matrix[0])
        row = len(matrix)

        top_idx = 0
        bottom_idx = row - 1

        left = 0
        right = col - 1

        while top_idx <= bottom_idx:

            arr_idx = top_idx + (bottom_idx - top_idx) // 2
            lower_bound = matrix[arr_idx][0]
            upper_bound = matrix[arr_idx][col - 1]

            if target >= lower_bound and upper_bound >= target:

                while left <= right:

                    mid = left + (right - left) // 2

                    if matrix[arr_idx][mid] == target:
                        return True

                    elif matrix[arr_idx][mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1

                return False

            elif target < lower_bound:
                bottom_idx = arr_idx - 1

            else:
                top_idx = arr_idx + 1

        return False
