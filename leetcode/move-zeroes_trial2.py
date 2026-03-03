class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        placeholder = 0
        seeker = 1

        while seeker < len(nums):

            # s and h = num
            if nums[seeker] != 0 and nums[placeholder] != 0:
                placeholder += 1

            # h is num and s = zero
            elif nums[seeker] != 0 and nums[placeholder] == 0:
                nums[seeker], nums[placeholder] = nums[placeholder], nums[seeker]
                placeholder += 1
            # s = 0 and h = num
            elif nums[seeker] == 0 and nums[placeholder] != 0:
                placeholder += 1

            seeker += 1

        return nums