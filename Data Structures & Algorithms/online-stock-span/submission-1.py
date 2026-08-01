class StockSpanner:

    def __init__(self):
        self.stack = [] #2d array, with idx, val
        self.idx = 0

    def next(self, price: int) -> int:
        while self.stack and self.stack[-1][1] <= price:
            self.stack.pop()
        
        if not self.stack:
            span = self.idx + 1
        else:
            span = abs(self.idx - self.stack[-1][0])
        
        self.stack.append([self.idx, price])
        self.idx += 1
        return span

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)