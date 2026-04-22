class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        left = 1
        right = x

        while left <= right:

            mid = left + (right - left) // 2
            mul = mid * mid

            if mul == x:
                return mid
            elif mul > x:
                right = mid - 1
            else:
                ans = mid
                left = mid + 1

        return ans