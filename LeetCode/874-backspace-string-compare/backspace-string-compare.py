class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []

        for char1 in s:
            if char1 == '#':
                if stack1:
                    stack1.pop()
            else:
                stack1.append(char1)


        for char2 in t:
            if char2 == '#':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(char2)
                
        return stack1 == stack2