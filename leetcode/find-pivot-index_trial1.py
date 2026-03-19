class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix_sum = 0
        pivot_idx = -1

        for i in range(len(nums)):
            
            right_sum = total - prefix_sum - nums[i]

            if prefix_sum == right_sum:
                pivot_idx = i
                break

            prefix_sum += nums[i]

        return pivot_idx



# [1,7,3,6,5,6]
# 1 8 11 17 22 28
#     3

# 6 11 17 20 27 28