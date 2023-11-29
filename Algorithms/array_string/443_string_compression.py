class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        the length of each compressed group is always <= the orginal length:
        a -> a
        aa -> a2
        aaa -> a3
        Therefore, we can modify chars in place without changing the characters after the current group

        Use two pointers for count the number of consecutive chars, left and right, keep moving right until chars[left] != chars[right], the number of chars[left] is right - left.

        Time: O(N) visit each char in chars once and change its value at most once
        Space: O(1)
        """
        left, right = 0, 0

        # length of the current compressed string
        res = 0

        while left < len(chars):
            # a group finishes if right is out of bound or right points to a different char
            if right == len(chars) or chars[right] != chars[left]:
                count = right - left

                # modify the char at res
                chars[res] = chars[left]
                res += 1

                # add count if count > 1
                if count > 1:
                    for x in str(count):
                        chars[res] = x
                        res += 1

                # move left pointer
                left = right

            # advance the right pointer
            right += 1

        return res
