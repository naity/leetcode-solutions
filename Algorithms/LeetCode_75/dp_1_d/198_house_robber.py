class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        DP
        For every house i take the maximum of
        1) rob the i-1 house and skip the current house
        2) rob the i-2 house, skip i-1, and rob the current house

        Use two variables to track the results of the previous two houses

        Time: O(N)
        Space: O(1)
        """

        a, b = 0, 0

        for i in range(len(nums)):
            a, b = b, max(a + nums[i], b)

        return b
