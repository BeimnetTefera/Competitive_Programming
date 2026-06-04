class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        stack = []
        max_area = 0

        for i in range(n):

            while stack and heights[stack[-1]] > heights[i]:
                cur = stack.pop()
                nse = i

                if stack:
                    pse = stack[-1]
                else:
                    pse = -1

                width = (nse - (pse) - 1)
                cur_area = heights[cur] * width
                max_area = max(max_area, cur_area)


            stack.append(i)

        while stack:
            cur = stack.pop()
            nse = n

            if stack:
                pse = stack[-1]
            else:
                pse = -1

            width = (nse - (pse) - 1)
            cur_area = heights[cur] * width
            max_area = max(max_area, cur_area)

        return max_area