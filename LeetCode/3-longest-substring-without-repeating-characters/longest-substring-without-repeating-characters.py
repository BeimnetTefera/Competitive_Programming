class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_sub = 0
        left = 0

        for right in range(len(s)):

            if s[right] not in seen:
                seen.add(s[right])
            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1

                seen.add(s[right])

            max_sub = max(max_sub, len(seen))

        return max_sub
