class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        arr = nums + nums

        stack = [] 
        ans = [-1] * len(nums)

        for i in range(len(arr)):
            while stack and arr[stack[-1]] < arr[i]:
                idx = stack.pop()

                ans[idx % len(nums)] = arr[i]

            stack.append(i)

        return ans 
