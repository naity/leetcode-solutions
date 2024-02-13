class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        for each day, compare today's price with tomorrow's
        If tomorrow is higher, buy today and sell tomorrow
        to take the profit. This will make sure we only hold
        at most one share at any time

        Time: O(N)
        Space: O(1)

        """
        profits = 0
        for i in range(len(prices) - 1):
            profits += max(0, prices[i + 1] - prices[i])

        return profits
