class MyStack:

    def __init__(self):
        self.que1 = deque()
        self.length = 0
        
    def push(self, x: int) -> None:
        self.que1.append(x)
        self.length += 1

    def pop(self) -> int:

        if not self.que1:
            return None

        mov = self.length - 1

        while mov:
            top = self.que1.popleft()
            self.que1.append(top)
            mov -= 1

        self.length -= 1
        
        return self.que1.popleft()

    def top(self) -> int:
        if self.que1:
            return self.que1[-1]

        return None

    def empty(self) -> bool:
        if self.que1:
            return False

        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()