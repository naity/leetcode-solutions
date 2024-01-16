class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Two cases:
        1. The first letter of each string is the same:
            Remove the first letter from both strings, add 1 and solve the subproblem
        2. Remove the first letter from one of the two sequences, and solve the two subproblems and take the max

        Iterate each row in reverse order, so that the subproblems are solved first.

        Time: O(M*N)
        Space: O(N)
        """
        m, n = len(text1), len(text2)

        # use an extra row for the last row
        dp_prev = [0] * (n + 1)

        for i in range(m - 1, -1, -1):
            # new result row for the current row
            dp_curr = [0] * (n + 1)
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp_curr[j] = 1 + dp_prev[j + 1]

                else:
                    dp_curr[j] = max(dp_curr[j + 1], dp_prev[j])

            # update dp_prev
            dp_prev = dp_curr

        return dp_prev[0]
