class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_capacity = 0

        left = 0
        right = len(height) - 1

        while left <  right:
            # dimentions
            width = right - left
            length = min(height[left], height[right])

            # calculation
            area = length * width

            if area > max_capacity:
                max_capacity = area

            # always smaller one moves
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_capacity