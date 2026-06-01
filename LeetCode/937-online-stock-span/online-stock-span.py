class StockSpanner:

    def __init__(self):
        self.StockSpanner = []

    def next(self, price: int) -> int:

        cnt = 1

        while self.StockSpanner and self.StockSpanner[-1][1] <= price:
            top_stack = self.StockSpanner.pop()
            cnt += top_stack[0]

        self.StockSpanner.append([cnt, price])

        return  cnt

 

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)