class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.append(float("-inf"))
        # if first element greater than elment next to it print its index
        if nums[0] > nums[1]:
            return 0

        cur, right = 1, 2
        while right < len(nums):

            # check if it is greater than its neighbours
            if nums[cur] > nums[cur - 1] and nums[cur] > nums[right]:
                return cur
            # move pointer
            cur += 1
            right += 1