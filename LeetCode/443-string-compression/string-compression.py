class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        
        p1 = 0
        p2 = 0
        cnt = 0

        while p2 < len(chars):
            
            if chars[p1] == chars[p2]:
                p2 += 1

            else:
                cnt = (p2 - p1)
                s += chars[p1]
                if cnt > 1:
                    s += f"{cnt}"
                p1 = p2
                

        if p1 < len(chars):
            cnt = (p2 - p1)
            s += chars[p1]
            if cnt > 1:
                s += f"{cnt}"

            p1 = p2

        for i in range(len(s)):
            chars[i] = s[i]

        return len(s)