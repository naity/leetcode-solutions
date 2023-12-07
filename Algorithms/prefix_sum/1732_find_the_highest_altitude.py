class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        """
        Use a variabe to track the prefix sum
        Use another variable to track the highest altitude

        Time: O(N)
        Space: O(1)
        """

        prefix = 0
        highest = 0

        for x in gain:
            prefix += x
            highest = max(highest, prefix)

        return highest
