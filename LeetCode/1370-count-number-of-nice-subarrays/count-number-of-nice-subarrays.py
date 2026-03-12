class Solution:
    def atMost(self, nums, goal):
        left, right, cnt, summation  = 0, 0, 0, 0
        if goal < 0:
            return 0

        while right < len(nums):

            summation += (nums[right] % 2)

            while summation > goal:
                summation -= (nums[left] % 2)
                left += 1

            cnt += (right - left + 1)

            right += 1
        
        return cnt

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        result = self.atMost(nums, k) - self.atMost(nums, k - 1)
        
        return result
        