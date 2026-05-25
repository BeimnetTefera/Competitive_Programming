class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if self.stack2:
            top = self.stack2.pop()
            return top
        else:
            while self.stack1:
                val = self.stack1.pop()
                self.stack2.append(val)

            return self.stack2.pop()

        return None

    def peek(self) -> int:
        if self.stack2:
            top = self.stack2[-1]
            return top
        else:
            while self.stack1:
                val = self.stack1.pop()
                self.stack2.append(val)

            return self.stack2[-1]

        return None 

    def empty(self) -> bool:
        if self.stack1 or self.stack2:
            return False

        return True

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()