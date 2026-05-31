class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for cur_day in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[cur_day]:
                prev_day = stack.pop()
                ans[prev_day] = cur_day - prev_day

            stack.append(cur_day)

        return ans