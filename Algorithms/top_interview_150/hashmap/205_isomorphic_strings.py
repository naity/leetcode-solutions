class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        check letters in s and t one by one. Use a hashmap to store mapping
        return False if
        1) two chars mapped to the same value in t
        2) the same char in s mapp to two different chars in t

        Need two dictionaries

        Time: O(n)
        Space: O(1) only ascii chars
        """

        # easy case
        if len(s) != len(t):
            return False

        # chars in s that map to a char in t
        mapping = {}

        # store chars in t that have already been mapped
        mapped = {}

        for i in range(len(s)):
            if s[i] in mapping and mapping[s[i]] != t[i]:
                # mapping to different chars
                return False

            if t[i] in mapped and mapped[t[i]] != s[i]:
                # two chars mapp to the same value
                return False

            # create new mapping, doesn't matter if already exists
            mapping[s[i]] = t[i]
            mapped[t[i]] = s[i]

        return True
