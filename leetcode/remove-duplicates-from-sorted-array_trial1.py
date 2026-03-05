class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1
        cnt = len(nums)

        while right < cnt:

            if nums[left] != nums[right]:
                right += 1
                left += 1

            else:
                nums.pop(right)
                nums.append('_')
                cnt -= 1

        return cnt