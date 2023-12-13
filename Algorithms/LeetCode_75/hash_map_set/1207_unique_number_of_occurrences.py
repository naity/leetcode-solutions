class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
        First count the occurrences of unique numbers in arr with a dictionary.
        Then use a set to check if all counts are unique

        Time: O(N)
        Space: O(N)
        """

        counts = defaultdict(int)

        for num in arr:
            counts[num] += 1

        unique = set()

        for count in counts.values():
            if count in unique:
                return False

            unique.add(count)

        return True
