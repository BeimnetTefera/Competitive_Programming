class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        rows = len(nums)
        cols = len(nums[0])

        step = 0
        max_values = []

        while step < cols:
            max_num = float('-inf')
            # loop for all columns to find the max of each row
            for row in range(rows):
                list_max = float('-inf')

                # find max number form each column in one row
                for col in range(cols):
                    if nums[row][col] > list_max:
                        list_max = nums[row][col]
                        idx = col

                # replace theat index with zero
                nums[row][idx] = 0

                # compare the max for all elt
                max_num = max(max_num, list_max)

            max_values.append(max_num)

            step += 1

        return sum(max_values)