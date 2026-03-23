class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        if len(nums) < 2 * k:
            return [-1] * len(nums)

        left = 0
        right = (2 * k)
        divisor = (2 * k) + 1

        total = sum(nums[:right])
        res = [-1] * k

        while right < len(nums):

            total += nums[right]
            res.append(total // divisor)

            total -= nums[left]

            left += 1
            right += 1

        res.extend([-1] * k)

        return res
