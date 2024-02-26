class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Start from the end, and start count from first non-space character,
        end before the first space

        Time: O(N)
        Space: O(1)
        """
        length = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                continue

            # start counting
            j = i

            while j >= 0 and s[j] != " ":
                length += 1
                j -= 1

            # break from the for loop
            break

        return length
