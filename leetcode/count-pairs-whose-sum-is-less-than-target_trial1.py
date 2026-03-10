class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        possible = 0

        nums.sort()

        while left < right:
            diff = nums[left] + nums[right]

            if diff < target:
                possible += (right - left)
                left += 1
            else:
                right -= 1

        return possible
