class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Count the chars in s and t, they should be identical

        Can use two hashmaps ann check for matching
        OR a single hashmap, +1 for s, and -1 for t. All values should be 0.

        Time: O(N)
        Space: O(1) since all lower case letters
        """

        # easy case
        if len(s) != len(t):
            return False

        counts = defaultdict(int)

        for l_s, l_t in zip(s, t):
            counts[l_s] += 1
            counts[l_t] -= 1

        for c in counts.values():
            if c != 0:
                return False

        return True
