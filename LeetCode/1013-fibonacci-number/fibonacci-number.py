class Solution:
    def fib(self, n: int) -> int:

        if n <= 1:
            return n

        return self.fib(n-2) + self.fib(n-1)



"""
n = 5
fib(5) = fib(3) + fib(4)
fib(4) = 1 + fib(3)
fib(2) = fib(1) + fib(0)

fib(3) = [2]

"""