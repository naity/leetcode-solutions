class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Use a hashmap to store numbers in nums and their indices
        if for a num, target-num is already in the hashmap, return
        their indices

        Time: O(N)
        Space: O(N)
        """

        mappings = {}

        for i, num in enumerate(nums):
            if target - num in mappings:
                return [mappings[target - num], i]

            mappings[num] = i
