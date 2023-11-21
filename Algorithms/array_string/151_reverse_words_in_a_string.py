class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Convert to a list and then just reverse the list.
        The key is to take care of extra spaces

        Time: O(N)
        Space: O(N)
        """

        s = s.split(" ")
        s = [item for item in s if item]
        return " ".join(s[::-1])
