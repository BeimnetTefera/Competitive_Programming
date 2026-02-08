class Solution:    
    def findUnion(self, a, b):
        
        combined = a + b
        combined.sort() 
        
        left = 0
        right = 1
        result = []
        
        while right < len(combined):
            if combined[left] != combined[right]:
                result.append(combined[left])
                left = right
        
            right += 1
            
        if combined:
            result.append(combined[-1])
            
        return result
