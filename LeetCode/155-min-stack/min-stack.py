class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            if self.stack[-1][1] > val:
                self.stack.append([val, val])
            else:
                self.stack.append([val, self.stack[-1][1]])

        else:
            self.stack.append([val, val])

    def pop(self) -> None:
        if not self.stack:
            return None

        del self.stack[-1]
            
    def top(self) -> int:
        if not self.stack:
            return None
        else:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack[-1][1] != float('inf'):
            return self.stack[-1][1]

        return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()