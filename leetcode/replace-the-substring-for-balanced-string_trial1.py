class Solution:
    def balancedString(self, s: str) -> int:
        chars = ["Q", "E", "W", "R"]
        freq = Counter(s)
        exp = len(s) // 4
        cnt = 0

        for char in chars:
            if char in freq:
                cnt += (freq[char] - exp)

        return cnt