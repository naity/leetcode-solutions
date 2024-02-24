class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Iterate the string and check if the symbol at i is less than i+1
        if yes, times -1

        Time: O(N), since s.length <= 15, one can also argue O(1)
        Space: O(1)
        """
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        res = 0

        for i in range(len(s) - 1):
            if mapping[s[i]] < mapping[s[i + 1]]:
                res -= mapping[s[i]]
            else:
                res += mapping[s[i]]

        # last symbol
        res += mapping[s[-1]]

        return res
