class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Use a hashmap to store values and their corresponding indices
        If exists, check if i-j <= k, if not, update j->i

        Time: O(N) length of nums
        Space: O(N)
        """

        mem = {}

        for i, num in enumerate(nums):
            if num in mem and i - mem[num] <= k:
                return True

            # add or update
            mem[num] = i

        return False
