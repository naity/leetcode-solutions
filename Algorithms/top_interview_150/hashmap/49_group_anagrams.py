class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Count the letters (all lower case) in each string.
        Use an array of length 26, and then convert the result to a tuple
        as keys in a hashmap

        Don't concat the counts naively as 1010 can be
        1) 10 a, 1 b
        2) 1 a, 10 c

        Time: O(MN), M for the length of strs, N for average length of each str
        Space: O(M * 26) + O(M*N) => O(MN)
        """

        mapping = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for l in s:
                count[ord(l) - ord("a")] += 1

            # convert to tuple
            mapping[tuple(count)].append(s)

        # return the values in mapping
        return list(mapping.values())
