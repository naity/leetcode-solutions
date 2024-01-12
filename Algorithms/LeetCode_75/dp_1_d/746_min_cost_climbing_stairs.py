class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        DP:
        For a step i, the cost is going to be the min of cost[i-1] and cost[i-2]. Therefore, we just need two variables to track the cost of the two steps before.

        Time O(N)
        Space O(1)
        """

        # cost length >= 2
        n = len(cost)
        a, b = 0, 0

        for i in range(2, n + 1):
            a, b = b, min(a + cost[i - 2], b + cost[i - 1])

        return b
