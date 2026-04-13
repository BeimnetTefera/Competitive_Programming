class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        arr.sort()
        left, right = 0, 1 
        if arr[0] != 0:
            arr[0] = 1

        while right < len(arr):
            dif = abs(arr[right] - arr[left])
            if dif > 1:
                arr[right] = arr[left] + 1
                
            right += 1
            left += 1

        return arr[n - 1]
