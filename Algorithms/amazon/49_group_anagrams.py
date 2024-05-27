from collections import defaultdict


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        count the letters in each str, since all lowercase letters,
        use an array for counting and then convert it to a tuple
        to be used as key for a hashmap, use a list to store all strs
        sharing the same key

        N: length of strs, M max length of each str
        Time: O(MN)
        Space: O(MN)
        """

        hashmap = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for char in s:
                count[ord(char) - ord("a")] += 1

            # convert it to tuple and store in hashmap
            hashmap[tuple(count)].append(s)

        return list(hashmap.values())
