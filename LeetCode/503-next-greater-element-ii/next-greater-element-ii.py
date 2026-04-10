class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = [] # decreasing stack
        ans = [-1] * len(nums)

        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                top_idx = stack.pop()

                ans[top_idx] = nums[i]

            stack.append(i)

        while stack:
            idx = stack.pop()
            for j in range(len(nums)):
                if nums[j] > nums[idx]:
                    ans[idx] = nums[j]
                    break

        return ans