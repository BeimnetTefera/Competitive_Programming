class Solution:
    def myPow(self, x: float, n: int) -> float:
        sign = 1
        
        if n < 0:
            sign = -1
            n = n * -1
    
        def helper(x, n):
            if n == 0:
                return 1

            half = helper(x, n //2)
            
            if n % 2 == 0:
                return half * half
            else:
                return x * half * half

        value = helper(x,n)

        if sign < 0:
            return 1 / value
        else:
            return value