class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        val = n
        count = 0

        while val > 0:
            val -= i

            if val >= 0:
                count += 1

            i += 1

        return count