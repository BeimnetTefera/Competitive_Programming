class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+", "-", "/", "*"}

        for op in tokens:

            if op in operations :
                
                last = stack.pop()
                second_last = stack.pop()

                if op == '+':
                    res = second_last + last
                elif op == '-':
                    res = second_last - last
                elif op == '*':
                    res = second_last * last
                else: 
                    res = int(second_last / last)

                stack.append(res)

            else:
                stack.append(int(op))

        return stack[0]