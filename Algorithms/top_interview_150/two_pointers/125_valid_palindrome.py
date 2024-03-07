class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Need to first remove non-alphanumeric chars from s

        Then use two pointer, one starting from start, and the other
        starting forom the end.
        Check if the two chars are the same while moving the two pointers towards each other

        Time: O(N)
        Space: O(N): store the string with non-alphanumeric chars removed.
        Can also skip non-alphanumeric chars during the while loop remove the first step
        and save a copy of s. This way, space is O(1)
        """

        left, right = 0, len(s) - 1

        while left < right:
            if not s[left].isalnum():
                # skip
                left += 1
            elif not s[right].isalnum():
                # skip
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False

                left += 1
                right -= 1

        return True
