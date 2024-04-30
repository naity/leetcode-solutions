class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Use a hashmap to store num and its index
        For each num check if target-num is in hashmap, if not add it

        Time: O(N)
        Space: O(N)
        """

        mem = {}

        for i, num in enumerate(nums):
            if target - num in mem:
                return [mem[target - num], i]

            mem[num] = i
