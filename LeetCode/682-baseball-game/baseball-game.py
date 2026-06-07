class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == '+':
                last = stack[-1]
                second_last = stack[-2]

                stack.append(last + second_last)

            elif op == 'C':
                stack.pop()

            elif op == 'D':
                last_score = stack[-1]
                stack.append(2 * last_score)
            else:
                stack.append(int(op))

        total_sum = sum(stack)

        return total_sum