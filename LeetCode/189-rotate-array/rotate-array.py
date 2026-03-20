class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()
        k = k % len(nums)
        mov = k // 2
        last = k - 1
        for i in range(k):
            if mov > 0:
                nums[i], nums[last] = nums[last], nums[i]
                last -= 1
                mov -= 1
            
        cnt = (len(nums) - k) // 2
        right = len(nums) - 1
        for j in range(k, len(nums)):
            if cnt > 0:
                nums[j], nums[right] = nums[right], nums[j]
                cnt -= 1
                right -= 1
        
        return nums