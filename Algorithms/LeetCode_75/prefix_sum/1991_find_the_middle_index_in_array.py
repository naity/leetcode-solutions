class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        """
        Find the smallest index whose prefix and suffix sums are the same.
        Trick: right prefix = Sum(nums) - left prefix - nums[i]

        Time: O(N)
        Space: O(1)
        """

        prefix = 0
        total = sum(nums)

        for i, num in enumerate(nums):
            if prefix == total - prefix - num:
                return i
            prefix += num

        return -1
