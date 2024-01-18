class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
            r o s
        h   3 3 4 5
        o   3 2 3 4
        r   2 2 2 3
        s   3 2 1 2
        e   3 2 1 1
            3 2 1 0
        If both word1 and word2 are empty, 0 edit needed
        if word1[i] == word2[j], the result should be word1[i+1:] and word[j+1]
        if word1[i] != word2[j]:
            1) replace word1[i] with word2[j]: 1+ # of operations for word1[i+1] and word2[j+1]
            2) delete word1[i]: 1 + # of operations for word1[i+1] and word2[j]
            3) insert word2[j] at this location: 1 + # operations for word1[i] and word2[j+1]

        Choose the minimum of the three options

        Time: O(M*N)
        Space: O(N)
        """
        m, n = len(word1), len(word2)

        # in case at least of word is empty
        if m == 0:
            return n

        if n == 0:
            return m

        # the dp row should be set based on the length of the substring of word2
        dp = [len(word2) - i for i in range(n + 1)]

        for i in range(m - 1, -1, -1):
            new_dp = [0] * n
            # the last column should be set based on the length of word1 substring
            new_dp.append(m - i)
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    # match
                    new_dp[j] = dp[j + 1]

                else:
                    # pick the minimum of three options
                    new_dp[j] = 1 + min(
                        # replace
                        dp[j + 1],
                        # delete
                        dp[j],
                        # insert
                        new_dp[j + 1],
                    )

            # update dp
            dp = new_dp

        return dp[0]
