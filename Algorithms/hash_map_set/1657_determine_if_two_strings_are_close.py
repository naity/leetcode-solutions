class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        Operation 1: characters and their occurances are identifcal between the two strings
        Operation 2: The occurances of the characters can be swapped. As long as the character set are identical and have the same counts (order doesn't matter), the strings are close.

        The two strings must have the same length
        Counting characters in word1 and word2: O(N)
        -> check keys: O(1) => max length is 26 since word1 and word2 contain only lowercase letters
        -> check counts: sort and then compare O(26log26) => O(1)

        Time: O(N)
        Space: O(1) => max size is 26 for all lowercase letters
        """
        # check length
        if len(word1) != len(word2):
            return False

        counts1, counts2 = defaultdict(int), defaultdict(int)

        for char in word1:
            counts1[char] += 1

        for char in word2:
            counts2[char] += 1

        # check if keys are identical
        if len(counts1) != len(counts2):
            return False

        for char in counts1:
            if char not in counts2:
                return False

        # now check counts
        freqs1, freqs2 = list(counts1.values()), list(counts2.values())
        freqs1.sort()
        freqs2.sort()
        for i in range(len(freqs1)):
            if freqs1[i] != freqs2[i]:
                return False

        return True
