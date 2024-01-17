class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        Can do a dfs with memoization, however, I received a memory error.

        DP:
        For each day, we track two results:
        1) already have a stock or bought: we can either sell or do nothing
        2) don't have a stock or empty: we can either buy or do nothing

        For a given day i, its result will depend on day i-1. Use two variables to track the have and empty profit for each day.

        Time: O(N)
        Space: O(1)
        """

        # profits = 0
        # @cache
        # def search(i, bought, total):
        #     nonlocal profits
        #     if i == len(prices):
        #         profits = max(profits, total)
        #         return

        #     if bought:
        #         # sell
        #         new_total = total+prices[i]-fee
        #         search(i+1, not bought, new_total)

        #         # don't sell
        #         search(i+1, bought, total)

        #     else:
        #         # buy
        #         new_total = total-prices[i]
        #         search(i+1, not bought, new_total)

        #         # don't buy
        #         search(i+1, bought, total)

        # search(0, False, 0)
        # return profits

        # day 0:
        bought = -prices[0]
        empty = 0

        for i in range(1, len(prices)):
            # for empty status, we either already have a stock and sell or don't have a stock and do nothing
            new_empty = max(bought + prices[i] - fee, empty)

            # for bought status we either don't have a stock and buy or have a stock and do nothing
            new_bought = max(bought, empty - prices[i])

            empty = new_empty
            bought = new_bought

        # for the last day, we can return the max of empty and bought
        return max(empty, bought)
