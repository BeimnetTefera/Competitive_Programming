class Solution:
    def isValid(self, s: str) -> bool:
        rule = {
            ")" : "(",
            "]" : "[" ,
            "}" : "{" 
        }

        stack = []

        for char in s:
            # if it is opening keep adding into staackk
            if char in rule.values():
                stack.append(char)
            else:
                # if there is opening and no closing in stack return false
                if not stack:
                    return False

                # check the last closing from stack and current opening
                matches = stack.pop()
                if matches != rule[char]:
                    return False

        return stack == []
