class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        
        need = Counter(p)
        got = Counter(s[:k])

        left = 0
        result = []
        
        if need == got:
            result.append(left)

        for right in range(k, len(s)):
            
            got[s[left]] -= 1
            if got[s[left]] == 0:
                del got[s[left]]

            left += 1

            got[s[right]] = got.get(s[right], 0) + 1

            if got == need:
                result.append(left)

        return result