class Solution:
    def numTilings(self, n: int) -> int:
        """
        f(k): the number of ways to fully cover a board of width k
        p(k): the number of ways to partially cover a board of width k with one tile missing

        f(k) = f(k-1) + f(k-2) + 2*p(k-1)
        p(k) = p(k-1) + f(k-2)

        Time: O(N)
        Space: O(1)
        """
        MOD = 1_000_000_007

        if n <= 2:
            return n

        p = 1
        k_curr, k_p = 2, 1

        for _ in range(3, n + 1):
            tmp = k_curr
            k_curr = tmp + k_p + 2 * p
            p = p + k_p
            k_p = tmp

        return k_curr % MOD
