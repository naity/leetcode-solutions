class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Iterate through the list and change 0s that are between 0s to 1
        Then check if number of changes >= n

        Time: O(N)
        Space: O(1)
        """

        changes = 0

        for i, num in enumerate(flowerbed):
            if num == 1:
                continue

            # check left and right
            if (i - 1 < 0 or flowerbed[i - 1] == 0) and (
                i + 1 == len(flowerbed) or flowerbed[i + 1] == 0
            ):
                changes += 1
                flowerbed[i] = 1

                # can return early
                if changes >= n:
                    return True

        # still need to check changes and n as we may not be able to plant any followers
        # while n == 0
        return changes >= n
