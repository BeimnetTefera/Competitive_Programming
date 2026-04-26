class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        size = 0
        max_sub = 0

        for char in s:
            if char not in seen:
                seen.append(char)
                size += 1
            else:
                while char in seen:
                    seen.pop(0)
                    size -= 1

                seen.append(char)
                size += 1

            max_sub = max(max_sub, size)

        return max_sub