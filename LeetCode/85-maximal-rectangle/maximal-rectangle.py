class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        def largest_histogram(heights):
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


        row = len(matrix)
        col = len(matrix[0])
        max_area_1 = 0
        heights = [0] * col

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == "1":
                    heights[c] += int(matrix[r][c])
                else:
                    heights[c] = 0

            cur_area = largest_histogram(heights)
            max_area_1 = max(cur_area, max_area_1)

        return max_area_1