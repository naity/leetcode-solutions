class Solution:
    def tribonacci(self, n: int) -> int:
        """
        DP: Use three variables to track the 3 numbers before

        Time: O(N)
        Space: O(1)
        """

        if n == 0 or n == 1:
            return n
        if n == 2:
            return 1

        a, b, c = 0, 1, 1

        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c

        return c
