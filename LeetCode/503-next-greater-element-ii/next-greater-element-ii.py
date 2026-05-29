class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        ans = [None] * len(nums)

        for i in range(len(nums)):

            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    ans[i] = nums[j]
                    break

            if ans[i] == None:
                for k in range (0, i):
                    if nums[k] > nums[i]:
                        ans[i] = nums[k]
                        break

        for i in range(len(nums)):
            if ans[i] == None:
                ans[i] = -1

        return ans