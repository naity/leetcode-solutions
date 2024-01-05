# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        """
        Binary search

        Time: O(LogN)
        Space: O(1)
        """

        left, right = 1, n

        while True:
            mid = (left + right) // 2
            if guess(mid) == 0:
                return mid

            if guess(mid) == 1:
                left = mid + 1
            else:
                right = mid - 1
