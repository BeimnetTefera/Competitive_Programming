class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        acc = 0
        min_num = float("inf")
        for i in range(len(nums)):
            acc += nums[i]

            if acc < min_num:
                min_num = acc

        if min_num > 0:
            return 1
        else:
            return abs(min_num) + 1

"""
2 5 10 5 4
"""