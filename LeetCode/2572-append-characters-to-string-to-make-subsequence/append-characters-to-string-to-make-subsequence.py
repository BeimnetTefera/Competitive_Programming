class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        p1 = 0
        p2 = 0

        cnt = 0
        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1
                p2 += 1
            else:
                p1 += 1

        return len(t) - p2