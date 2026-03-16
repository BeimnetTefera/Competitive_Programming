class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left = 0
        turbulent = 0
        ans = 1
        
        if len(arr) == 1:
            return 1

        for right in range(len(arr) - 1):
            if right % 2 == 0:

                if arr[right] < arr[right + 1]:
                    turbulent = right - left + 1
                else:
                    left = right

            else:
                if arr[right] > arr[right + 1]:
                    turbulent = right - left + 1
                    
                else:
                    left = right

            ans = max(turbulent, ans)

        return ans