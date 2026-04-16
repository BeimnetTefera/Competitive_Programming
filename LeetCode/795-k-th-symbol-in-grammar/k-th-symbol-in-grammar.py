class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def helper(cur_n, cur_k):
            if cur_n == 1:
                return 0

            half = cur_n // 2
            if cur_k > half:
                return 1 - helper(cur_n // 2, cur_k - half)

            elif cur_k <= half:
                return helper(cur_n // 2, cur_k)

        return helper(2**(n - 1), k)