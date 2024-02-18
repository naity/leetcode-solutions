class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Use two variables, prefix and suffix to track
        the products of prefix and suffix

        Can do it in one or two iterations

        Time: O(N)
        Space: O(1)
        """
        n = len(nums)
        res = [1] * n
        prefix, suffix = 1, 1

        for i, num in enumerate(nums):
            # prefix
            res[i] *= prefix
            prefix *= num

            # can take care of the suffix of n-1-i as well
            res[n - 1 - i] *= suffix
            suffix *= nums[n - 1 - i]

        return res
