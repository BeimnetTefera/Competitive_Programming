class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        common = {}
        unique = []
        arr = set(arr2)
        for num in arr1:
            if num in arr:
                common[num] = common.get(num, 0) + 1
            else:
                unique.append(num)

        res = []
        for num in arr2:
            freq = common[num] 
            while freq > 0:
                res.append(num)
                freq -= 1

        unique.sort()

        return res + unique