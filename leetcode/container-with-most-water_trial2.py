class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_capacity = 0

        while left < right:

            width = right - left

            if height[left] <= height[right]:
                cur_capacity = height[left] * width
                left += 1

            else:
                cur_capacity = height[right] * width
                right -= 1

            max_capacity = max(max_capacity, cur_capacity)

        return max_capacity