class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        If two nums a, b are the same, a ^ b = 0.
        XOR everything, the result is the single number

        Time:O(N)
        Space: O(1)
        """

        res = nums[0]

        for i in range(1, len(nums)):
            res = res ^ nums[i]

        return res
