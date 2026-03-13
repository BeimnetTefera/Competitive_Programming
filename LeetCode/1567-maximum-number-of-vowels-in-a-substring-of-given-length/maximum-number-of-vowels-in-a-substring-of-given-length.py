class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        size = len(s)
        vowels = set(["a", "e", "i", "o", "u"])
        vowel_count, max_vowels, left = 0, 0, 0
        word = []

        for right in range(size):

            word.append(s[right])

            if s[right] in vowels:
                vowel_count += 1

            while len(word) > k:
                char = word.pop(left)
                if char in vowels:
                    vowel_count -= 1

            max_vowels = max(max_vowels, vowel_count)

        return max_vowels