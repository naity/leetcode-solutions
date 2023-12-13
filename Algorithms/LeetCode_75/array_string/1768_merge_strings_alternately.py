class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Two pointer p1 and p2, one for each string,
        build the merged string as we move p1 and p2 until both of them are out of bounds

        Time: O(m+n)
        Space: O(1)
        """

        p1, p2 = 0, 0

        res = []
        while p1 < len(word1) or p2 < len(word2):
            if p1 < len(word1):
                res.append(word1[p1])
                p1 += 1

            if p2 < len(word2):
                res.append(word2[p2])
                p2 += 1

        return "".join(res)
