class Solution:
    def fib(self, n: int) -> int:
        # base case
        if n <= 1:
            return n

        first = self.fib(n-1)
        second = self.fib(n-2)

        return first + second