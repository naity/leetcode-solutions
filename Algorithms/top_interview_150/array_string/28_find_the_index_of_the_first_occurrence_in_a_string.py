class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        check every index i in haystack to see if
        haystack[i:i+len(needle)] == needle

        Time: O(m*n) m is the length of haystack, n is the lenght of needle
        Space: O(n) for string slicing
        """

        for i in range(len(haystack)):
            if haystack[i : i + len(needle)] == needle:
                return i

        return -1
