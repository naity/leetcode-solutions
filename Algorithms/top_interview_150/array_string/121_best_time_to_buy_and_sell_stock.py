class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Two pointers and a variable to track max return
        Use right pointer to iterate through the list,
        move left to right if prices[right] < prices[left]
        update max return if needed

        Time: O(N)
        Space: O(1)
        """

        left, right = 0, 1
        max_return = 0

        while right < len(prices):
            p1, p2 = prices[left], prices[right]
            max_return = max(max_return, p2 - p1)

            if p2 < p1:
                left = right

            right += 1

        return max_return
