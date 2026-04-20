class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        prime_count = n // 2
        even_count = n - prime_count

        total = (pow(5, even_count, MOD) * pow(4, prime_count, MOD)) % MOD
        return total