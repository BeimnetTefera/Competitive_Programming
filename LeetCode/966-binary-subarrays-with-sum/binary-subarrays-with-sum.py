class Solution:

    def atMost(self, nums, goal):
        left, right, cnt, summation  = 0, 0, 0, 0
        if goal < 0:
            return 0

        while right < len(nums):

            summation += nums[right]

            while summation > goal:
                summation -= nums[left]
                left += 1

            cnt += (right - left + 1)

            right += 1
        
        return cnt

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        result = self.atMost(nums, goal) - self.atMost(nums, goal - 1)

        return result