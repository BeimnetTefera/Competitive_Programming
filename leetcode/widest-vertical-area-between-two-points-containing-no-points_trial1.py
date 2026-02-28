class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        size = len(points)
        max_dist = float('-inf')

        points.sort(key = lambda x: x[0])

        for i in range(size - 1):
            width = points[i + 1][0] - points[i][0]
            if width > max_dist:
                max_dist = width

        return max_dist