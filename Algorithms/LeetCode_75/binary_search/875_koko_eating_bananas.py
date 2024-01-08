class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        The fast way is to eat max(piles) bananas per hour, which will take n hours to finish all bananas. The slowest will be to eat 1 banana per hour, which will take sum(piles) hours to finish.
        The strategy will be to do a binary search from 1 to max. Search the left half if time <= h, otherwise search the right half until left meets right. The trick is to set right equal to mid if mid works and return either left or right when finishes.

        Time: O(nlogm)
        Space: O(1)
        """

        left, right = 1, max(piles)

        def get_time(k):
            total = 0
            for p in piles:
                total += math.ceil(p / k)

            return total

        while left < right:
            mid = (left + right) // 2
            total = get_time(mid)
            if total <= h:
                # mid works
                right = mid
            else:
                # mid doesn't work
                left = mid + 1

        return left
