class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        left = 0
        right = k
        max_sum = sum(nums[:k])
        cur_sum = max_sum

        while right < len(nums):

            cur_sum = cur_sum - nums[left] + nums[right]

            max_sum = max(cur_sum, max_sum )

            left += 1
            right += 1

        return max_sum / k