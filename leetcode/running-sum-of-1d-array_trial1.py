class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cur_sum = nums[0]
        result = []
        result.append(cur_sum)

        for i in range(1, len(nums)):
            cur_sum += nums[i]
            result.append(cur_sum)

        return result