class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_freq = 0
        max_count = 0
        store = {}

        for right in range(len(s)):

            store[s[right]] = store.get(s[right], 0) + 1

            max_freq = max(max_freq, store[s[right]])
            window_size = right - left + 1

            # shrink if the next character freq is greater than k
            while window_size - max_freq > k:
                store[s[left]] -= 1
                if store[s[left]] == 0:
                    del store[s[left]]

                left += 1
                window_size = right - left + 1

            max_count = max(max_count, right - left + 1)

        return max_count