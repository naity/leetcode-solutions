class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Iterate through s and obtain the indices and values for vowels.
        Reverse the values and change the value at each index

        Time: O(N)
        Space: O(N)
        """

        # use set for O(1) look up
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])

        # convert s to list for mutating in place
        s = list(s)

        indices = []
        values = []
        for i, c in enumerate(s):
            if c in vowels:
                indices.append(i)
                values.append(c)

        for i, c in zip(indices, values[::-1]):
            # modify s[i] in place
            s[i] = c

        # convert back to string
        return "".join(s)
