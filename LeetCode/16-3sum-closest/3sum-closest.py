class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float("inf")

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:

                dist = nums[i] + nums[left] + nums[right]

                if abs(target - dist) < abs(target - closest):
                    closest = dist

                if dist < target:
                    left += 1
                elif dist > target:
                    right -= 1
                else:
                    return dist

        return closest