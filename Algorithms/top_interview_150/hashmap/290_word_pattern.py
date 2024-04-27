class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Similar to 205, need two dictionaries for the mappings
        return False if
        1) a pattern matches to two different words
        2) a word matches to two different patterns

        Time: O(N)
        Space: O(1) All lower case letters
        """
        s = s.split()

        # simple case
        if len(pattern) != len(s):
            return False

        p_to_w = {}
        w_to_p = {}

        for i in range(len(s)):
            p, w = pattern[i], s[i]

            if (p in p_to_w and p_to_w[p] != w) or (w in w_to_p and w_to_p[w] != p):
                return False

            # adde to mapping, doesn't matter if already exists
            p_to_w[p] = w
            w_to_p[w] = p

        return True
