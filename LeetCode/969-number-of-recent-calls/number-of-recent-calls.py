class RecentCounter:

    def __init__(self):
        self.store = deque()

    def ping(self, t: int) -> int:
        self.store.append(t)

        while self.store[0] < (t - 3000):
            self.store.popleft()

        return len(self.store)

        

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)