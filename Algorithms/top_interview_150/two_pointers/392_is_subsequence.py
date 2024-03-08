class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Use two pointers, one for each, move s pointer if there is match
        return true if s pointer is out of bound

        Time: O(N) where N is the length of t
        Space: O(1)
        """

        p1, p2 = 0, 0

        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 1

        return p1 == len(s)
