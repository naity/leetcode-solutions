class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        The naive algorithm will be calcuate the product for each i,
        which takes O(N^2) time

        Next, we can calculate the product of the prefix and suffix for each i,
        and then calculate the product of prefix and suffix.
        This will take O(N) but O(N) space as well, since we will use two arrays
        to store prefix and suffix.

        We don't really need two arrays to store the prefix and suffix, instead,
        we can directly store the result in the output array

        Time: O(N): two iterations
        Space: O(1)
        """

        result = []

        # first loop for prefix
        prefix = 1
        for i in range(len(nums)):
            result.append(prefix)
            prefix *= nums[i]

        # second loop for suffix
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result
