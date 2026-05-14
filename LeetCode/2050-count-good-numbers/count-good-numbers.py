class Solution:
    def countGoodNumbers(self, n: int) -> int:

        Mod = 10**9 + 7

        def power (num, exp):

            if exp == 0:
                return 1

            half = power(num, exp // 2)

            if exp % 2 == 0:
                return  (half * half) % Mod

            else:
                return (half * half * num) % Mod

        odd_cnt = n // 2
        even_cnt = n - odd_cnt

        total = (power(5, even_cnt) * power(4, odd_cnt)) % Mod 

        return total