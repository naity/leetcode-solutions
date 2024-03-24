class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Sliding window:
        Use a set to track letters in the window
        Move right to expand the window, in case repeating chars,
        move left to shrink the window and remove the repeating char before expanding

        Time: O(N)
        Space: O(N) for hashset
        """

        chars = set()
        left, right = 0, 0
        max_len = 0
        while right < len(s):
            c = s[right]
            right += 1

            while c in chars:
                # shrink left
                chars.remove(s[left])
                left += 1

            # add to window
            chars.add(c)

            # update max_len
            max_len = max(max_len, len(chars))

        return max_len
