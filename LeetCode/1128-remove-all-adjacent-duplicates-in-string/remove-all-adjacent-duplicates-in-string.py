class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            flag = True
            while stack and stack[-1] == char:
                stack.pop()
                flag = False

            if flag:
                stack.append(char)

        return "".join(stack)