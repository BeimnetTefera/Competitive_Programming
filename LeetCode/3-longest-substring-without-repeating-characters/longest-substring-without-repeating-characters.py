class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        store = {}

        for right in range(0, len(s)):

            store[s[right]] = store.get(s[right], 0) + 1

            while store[s[right]] > 1:
                store[s[left]] -= 1

                if store[s[left]] == 0:
                    del store[s[left]]

                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len