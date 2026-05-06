class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        def helper( n):
            # base case
            if n == 1:
                return True
            #  if it is odd return no need to check
            if n % 2 != 0:
                return False

            return helper(n // 2)

        return helper(n)