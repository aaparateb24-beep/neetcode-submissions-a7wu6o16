class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        # Every new day contributes
        # at least one day (today itself)
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            # Previous price becomes useless
            # because current price is bigger.
            self.stack.pop()

        # Save today's price
        # together with its span
        self.stack.append((price, span))

        # Return today's span
        return span

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)