class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]

        if len(nums) == 0:
            return res

        # find first occurance
        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        if left >= len(nums) or nums[left] != target:
            return res

        res[0] = left

        # find second occurance
        left_2 = 0
        right_2 = len(nums) - 1

        while left_2 <= right_2:

            mid_2 = left_2 + (right_2 - left_2) // 2

            if nums[mid_2] <= target:
                left_2 = mid_2 + 1
            else:
                right_2 = mid_2 - 1
            
        res[1] = right_2

        return res