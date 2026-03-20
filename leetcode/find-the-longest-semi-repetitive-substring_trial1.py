class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        left, cnt, best = 0, 0, 0
        if len(s) == 1:
            return 1

        for right in range(1, len(s)):

            if s[right] == s[right - 1]:
                cnt += 1

            while cnt > 1:
                if s[left] == s[left + 1]:
                    cnt -= 1

                left += 1

            best = max(best, right - left + 1)

        return best