class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        arr = sorted(set(nums), reverse = True)

        if len(arr) < 3:
            return arr[0]
        else:
            return arr[2]