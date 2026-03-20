class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        step 1: if len(t) is greater return ""

        step 2: start with window size of len(t)
        
        step 3: check for every window if t chars are in it 
                - if we don't increase the size of the window until we get

        step 4: if we get we use the current length 

        step 5: dcrease the size of an array until we don't find every char then when we reach there start expanding the window
        '''
        min_len = float("inf")
        start = 0
        m = len(s)
        n = len(t)
        elt = []
        if n > m:
            return ""

        left = 0
        seen = {}
        need = Counter(t)

        for right in range(m):
            elt.append(s[right])
            seen[s[right]] = seen.get(s[right], 0) + 1
            
            while True:
                valid = True
                for char in need:
                    if char not in seen or need[char] > seen[char]:
                        valid = False
                        break
                
                if not valid:
                    break
                    
                    
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left
                    
                seen[s[left]] -= 1
                if seen[s[left]] == 0:
                    del seen[s[left]]
                        
                elt.pop(0)

                left += 1
                            
                
        return "" if min_len == float("inf") else s[start:start + min_len]
                                

"""
s = "OA ABEC ODEBANC", 
A : 1
B : 1
E : 1
C : 1 

t = "AAC"
"""
