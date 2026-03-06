class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        p1 = 0
        p2 = 0

        while p2 < (m + n) and p2 < n:
            # if the number is not 0
            if nums1[p1] != 0:

                if nums1[p1] < nums2[p2]:
                    p1 += 1

                else:
                    nums1.insert(p1, nums2[p2])
                    nums1.pop()
                    p2 += 1

            # if the number is 0       
            else:
                    nums1.insert(p1, nums2[p2])
                    nums1.pop()
                    p2 += 1
                    p1 += 1

        return nums1