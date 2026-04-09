class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for j in range(len(s)):
            if freq[s[j]] == 1:
                return j

        return -1