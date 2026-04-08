class DataStream:

    def __init__(self, value: int, k: int):
        self.store = deque()
        self.value = value
        self.k = k
        self.count = 0
        
    def consec(self, num: int) -> bool:

        self.store.append(num)
        if self.value == num:
            self.count += 1

        if len(self.store) > self.k:
            out = self.store.popleft()
            if out == self.value:
                self.count -= 1

        return self.count == self.k
# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)