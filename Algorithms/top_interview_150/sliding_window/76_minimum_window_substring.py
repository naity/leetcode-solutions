class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Find a window in s that contains all the chars in t

        1. count all chars in t. initiate a variable to track the answer
        2. Set two pointers left, right starting at 0; a dictionary to track counts in window
           A variable to check how many chars have the same counts in t and window
        3. Expand the right pointer, check if char at right in t. Keep moving if not.
           Otherwise:
           - Add char to window, increase valid_chars by 1 if its count becomes the same as in t
           - if all chars share the same counts, keep shrink left while keeping this condition true.
             update the answer if needed

        Time: O(M+N): N for initial counting, M for visiting each char in s at most twice
        Space: O(N): two dictionaries for counts
        """
        ans = ""

        # edge case
        if len(s) < len(t):
            return ans

        counts = defaultdict(int)
        for char in t:
            counts[char] += 1

        left, right = 0, 0
        window = defaultdict(int)
        valid_chars = 0

        while right < len(s):
            char_r = s[right]
            right += 1

            # char_r in t
            if char_r in counts:
                # add char_r to window
                window[char_r] += 1

                if window[char_r] == counts[char_r]:
                    valid_chars += 1

                while valid_chars == len(counts):
                    if ans == "" or right - left < len(ans):
                        ans = s[left:right]

                    # shrink left
                    char_l = s[left]
                    left += 1

                    if char_l in counts:
                        if window[char_l] == counts[char_l]:
                            valid_chars -= 1
                        window[char_l] -= 1
        return ans
