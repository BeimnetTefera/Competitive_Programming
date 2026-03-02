class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        unique_nums = sorted(set(nums))

        freq = Counter(nums)

        result = 0
        for i in range(len(unique_nums)):
            
            result += freq[unique_nums[i]] * i

        return result
