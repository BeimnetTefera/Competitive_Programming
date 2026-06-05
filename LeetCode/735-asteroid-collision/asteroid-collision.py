class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for num in asteroids:
            # if num is less than 0 and magnitude of num > is greater than top of stack(+ve number)
            while num < 0 and stack and stack[-1] > 0 and stack[-1] < abs(num):
                stack.pop()
                    
            if not stack:
                stack.append(num)
            elif num < 0 and stack[-1] > 0 and stack[-1] == abs(num):
                stack.pop()
            elif num < 0 and stack[-1] > 0 and stack[-1] > abs(num):
                continue 
                
            else:
                stack.append(num)

        return stack