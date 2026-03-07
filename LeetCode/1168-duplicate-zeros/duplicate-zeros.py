class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        p = 0
        while p < len(arr):
            if arr[p] != 0:
                p += 1
            else:
                p += 2
                arr.insert(p - 1, 0)
                arr.pop()

        return arr