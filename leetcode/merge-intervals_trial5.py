class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        values = sorted(intervals)
        
        size = len(values) 
        i = 0 

        while i < size - 1:
                     
            if values[i][1] >= values[i + 1][0]:
          
                lower_val = min(values[i][0], values[i + 1][0])
                upper_val = max(values[i][1], values[i + 1][1])
                
                values[i + 1][0] = lower_val
                values[i + 1][1] = upper_val

                values.pop(i)
                
                size -= 1
                
                continue
                
            i += 1
                 
        return values