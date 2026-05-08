class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        def helper(power, num):
            # base case
            if power == 0:
                return 1

            half_res = helper(power // 2, num)

            if power % 2 == 0:
                return (half_res * half_res) % MOD
            else:
                return (half_res * half_res * num) % MOD

        # check if it is even or odd
        is_even = False
        if n % 2 == 0:
            is_even = True
        
        power = n // 2

        # do the recursion for the half of them
        res1 = helper(power, 5)
        res2 = helper(power, 4)

        if is_even:
            return (res1 * res2) % MOD
        else:
            return (res1 * res2 * 5) % MOD