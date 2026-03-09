class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1

        cnt = len(nums)
        while right < len(nums):
            if nums[left] != nums[right]:
                left += 1
                right += 1
                
            else:
                nums.pop(right)
                nums.append('_')
                cnt -= 1

            if right > cnt:
                break

        return cnt
