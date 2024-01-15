class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        DP:
        Since the robot can only move right or down. For a given cell grid[i][j], the way to reach it is grid[i-1][j] + grid[i][j-1] if i-1 and j-1 are in bounds.
        The first row can only be reached by moving right, and the first column can only be reached by moving down.

        We can maintain an array to store the results from the previous row and update it as move from left to right in the current row.

        Time: O(m*n)
        Space: O(n)
        """
        dp = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                # the sum of the cell above and the cell on the left
                dp[j] = dp[j] + dp[j - 1]

        # return the result of the last cell
        return dp[-1]
