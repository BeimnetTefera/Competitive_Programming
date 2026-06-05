class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for num in asteroids:
            # remove value from stack if the currnet number is negative and if there is a positive value in the stack
            if num < 0 and stack and stack[-1] > 0:
                # case 1: current num > top of the stack
                if stack[-1] < abs(num):
                    while stack and stack[-1] > 0 and stack[-1] < abs(num):
                        stack.pop()
                        
                    if not stack :
                        stack.append(num)
                    elif stack and stack[-1] == abs(num):
                        stack.pop()
                    elif stack and stack[-1] > abs(num):
                        continue 
                    elif stack or stack[-1] < 0:
                        stack.append(num)

                # case 2: if top of stack is greater than current num
                elif stack[-1] > abs(num):
                    continue
                # case 3: top of stack equals with current number
                elif stack[-1] == abs(num):
                    stack.pop()
            # if we don't have value in the stack or the num is positive or stacks top is negative 
            else:
                stack.append(num)

        return stack