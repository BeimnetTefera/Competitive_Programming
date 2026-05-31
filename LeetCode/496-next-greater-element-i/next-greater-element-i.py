class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        next_greater = {}
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                top_stack = stack.pop()
                next_greater[top_stack] = num

            stack.append(num)

        ans = []
        for num in nums1:
            if num in next_greater:
                ans.append(next_greater[num])
            else:
                ans.append(-1)

        return ans