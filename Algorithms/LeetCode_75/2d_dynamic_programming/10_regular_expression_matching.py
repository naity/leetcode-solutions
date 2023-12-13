class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        DFS with memoization

        For s[i] and p[j], we need to consider if p[j] is followed by "*"

        - If yes, we can choose to either use p[j] or not using p[j]
            1. If use p[j], we need to check if p[j] matches s[i] AND
                whether dfs(i+1, j) -> (use it 1 or more times) or
                dfs(i+1, j+2) -> (use it only once) is True
            2. If we don't use it, we need to check if dfs[i, j+2] is true
        - If p[j] is not followed by "*"
            1. we just need to check if p[j] matches s[i] AND whether dfs(i+1, j+1) is true

        Time: O(m*n) since there are m*n possiblities, for each combination, constant work
        Space: O(m*n) for memoization
        """

        mem = {}

        def dfs(i, j):
            # basecase: both s and p are exhausted
            if i == len(s) and j == len(p):
                return True

            # basecase: remaining unmatched chars in s
            if j == len(p):
                return False

            # solved before
            if (i, j) in mem:
                return mem[(i, j)]

            # whether there is a match
            match = i < len(s) and p[j] in (s[i], ".")
            # if p[j] is followed by a *
            if j + 1 < len(p) and p[j + 1] == "*":
                # we can skip p[j] or use it
                res = dfs(i, j + 2) or (
                    match
                    and (  # if we use it, there mush be a match
                        dfs(i + 1, j)
                        or dfs(i + 1, j + 2)  # keep using it  # or just use it once
                    )
                )

            # if p[j] is not followed by a *
            else:
                # wether p[j] matches s[i] and wether dfs(i+1, j+1) is true
                res = match and dfs(i + 1, j + 1)

            mem[(i, j)] = res
            return res

        return dfs(0, 0)
