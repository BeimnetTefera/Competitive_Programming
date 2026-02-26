class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # find the maximum element
        # put it up front
        # then put it to the back
        # in every iteration we should go one step to the left
        
        output = []
        for size in range(len(arr), 1, -1):
            idx = arr.index(max(arr[:size]))
            
            if idx == size -1:
                continue
                
            if idx != 0:
                output.append(idx+1)
                arr[:idx+1] = reversed(arr[:idx+1])

            output.append(size)
            arr[:size] =  reversed(arr[:size])
            
        return output
