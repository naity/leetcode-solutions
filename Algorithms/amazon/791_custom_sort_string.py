from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        Count the chars in s

        iterate the char in order, if in s, append the count number of times
        to a list

        append the remaining chars

        Time: O(M+N), M: length of order, N length of s
        Space: O(N)
        """

        counts = Counter(s)

        res = []

        for char in order:
            if char in counts:
                for _ in range(counts[char]):
                    res.append(char)

                # remove char from counts
                counts.pop(char)

        # deal with the remaining chars in s
        for char in counts:
            for _ in range(counts[char]):
                res.append(char)

        return "".join(res)
