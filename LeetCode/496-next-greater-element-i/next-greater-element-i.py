class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num in nums1:
            idx = nums2.index(num)
            val = None
            for i in range(idx, len(nums2)):
                if nums2[i] > num:
                    val = nums2[i]
                    ans.append(val)
                    break
            if not val:
                ans.append(-1)
        return ans