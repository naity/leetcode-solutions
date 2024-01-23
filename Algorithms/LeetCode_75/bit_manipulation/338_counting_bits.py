class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        For each num [0, n], count the number of 1s using a mask or using the n&n-1 technique

        Time: O(32N) => O(N)
        Space: O(1)
        """

        def convert(i):
            count = 0

            while i != 0:
                count += 1
                i = i & i - 1

            return count

        res = []
        for i in range(n + 1):
            res.append(convert(i))
        return res
