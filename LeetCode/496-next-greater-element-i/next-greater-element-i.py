class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        res = [-1] * len(nums2)
        stack = []

        for i in range(n):
            while stack and nums2[stack[-1]] < nums2[i]:
                top_stack = stack.pop()
                res[top_stack] = nums2[i]

            stack.append(i)

        ans = []
        for num in nums1:
            idx = nums2.index(num)
            ans.append(res[idx])

        return ans