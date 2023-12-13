class Solution:
    def removeStars(self, s: str) -> str:
        """
        Use a stack, pop when see a *

        Time: O(N)
        Space: O(N)
        """
        res = []
        for char in s:
            if char == "*":
                res.pop()
            else:
                res.append(char)

        return "".join(res)
