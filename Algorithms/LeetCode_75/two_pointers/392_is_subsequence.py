class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        One pointer p1 for s and one pointer p2 for t,
        iterate p2 through t and move p1 if s[p1] == t[p2],
        return true if p2 is out of bound

        Time: O(N)
        Space: O(1)
        """

        p1, p2 = 0, 0

        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1

            p2 += 1

        return p1 == len(s)
