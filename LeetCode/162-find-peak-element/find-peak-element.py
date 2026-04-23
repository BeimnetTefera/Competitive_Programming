class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.append(float("-inf"))
        if nums[0] > nums[1]:
            return 0
        idx = 0
        cur, right = 1, 2
        while right < len(nums):
            if nums[cur] > nums[cur - 1] and nums[cur] > nums[right]:
                idx = cur
                return idx
            cur += 1
            right += 1