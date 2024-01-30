class StockSpanner:
    def __init__(self):
        """
        Use a stack to store (price, days) pairs

        Time: O(N)
        Space: O(N)
        N is the number of times next is called
        """
        self.stack = []

    def next(self, price: int) -> int:
        """
        Maintain a monotonic stack. Keep popping from the stack if the last item's price is <= price. push the price and span days to stack.
        """
        # starting from 1
        count = 1
        while self.stack and self.stack[-1][0] <= price:
            _, days = self.stack.pop()
            count += days

        self.stack.append((price, count))

        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
