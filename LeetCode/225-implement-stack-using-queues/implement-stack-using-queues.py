class MyStack:

    def __init__(self):
        self.que1 = deque()
        self.que2 = deque()
        

    def push(self, x: int) -> None:

        while self.que1:
            top = self.que1.popleft()
            self.que2.append(top)

        self.que1.append(x)

        while self.que2:
            top = self.que2.popleft()
            self.que1.append(top)


    def pop(self) -> int:
        top = None
        if self.que1:
            top = self.que1.popleft()
        return top

    def top(self) -> int:
        if self.que1:
            return self.que1[0]
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