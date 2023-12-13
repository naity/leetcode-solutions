class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        Two iterations
        first: determine the max value of the array
        second: check if candies[i] + extraCandies >= max

        Time: O(n)
        Space: O(1)
        """

        max_candies = max(candies)

        return [candy + extraCandies >= max_candies for candy in candies]
