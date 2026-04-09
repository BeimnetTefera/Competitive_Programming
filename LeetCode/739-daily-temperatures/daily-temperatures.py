class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # create empty array and populate it with "0"
        result = [0] * len(temperatures)
        stack = []
        # loop through the array
        for i in range(len(temperatures)):

        # insd the loop there is while loop to check if the cur num is greater to update the result array and remove the values lesserr
            while stack and temperatures[stack[-1]] < temperatures[i]:
                top_stack = stack.pop()

                result[top_stack] = i - top_stack

        # add the curr element index
            stack.append(i)

        return result