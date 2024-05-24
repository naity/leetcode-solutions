from collections import defaultdict


class Solution:
    def minimumKeypresses(self, s: str) -> int:
        """
        Count the unique chars in s

        put the top 9 as the first in each button
        the next 9 as the second etc.

        Time: O(NlogN)
        Space: O(26) => O(1)
        """

        counts = defaultdict(int)

        for c in s:
            counts[c] += 1

        # sort
        counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)

        total_keypresses = 0

        for i, (c, count) in enumerate(counts):
            total_keypresses += count * (i // 9 + 1)

        return total_keypresses
