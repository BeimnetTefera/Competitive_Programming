class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        ans = [-1] * len(nums)

        for i in range(len(nums)):
            found = False
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    ans[i] = nums[j]
                    found = True
                    break

            if not found:
                for k in range (0, i):
                    if nums[k] > nums[i]:
                        ans[i] = nums[k]
                        break

        return ans