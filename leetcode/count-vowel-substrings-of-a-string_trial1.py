class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        n = len(word)

        for left in range(n):
            
            seen =  set()

            for right in range(left, n):

                if word[right] not in vowels:
                    break

                seen.add(word[right])

                if len(seen) == 5:
                    count += 1

        return count