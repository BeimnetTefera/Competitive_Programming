class Solution:
    # Function to check if b is a subset of a.
    def isSubset(self, a, b):
        a.sort()
        b.sort()
        
        a_ptr = 0
        b_ptr = 0
        
        while a_ptr < len(a) and b_ptr < len(b):
            if a[a_ptr] == b[b_ptr]:
                a_ptr += 1
                b_ptr += 1
            elif a[a_ptr] < b[b_ptr]:
                a_ptr += 1
            else:
                return False
                
        return b_ptr == len(b)
