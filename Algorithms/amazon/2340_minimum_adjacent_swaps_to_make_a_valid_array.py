class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        """
        Find the index of the max and min values
        For ties, want the largest index for max and
        smallest index for min

        the total steps is
        move the min index to 0 plus
        max index to n-1

        if they cross subtract one from the total steps as 
        min will be swapped once during the max process

        Time: O(N)
        Space: O(1)
        """

        min_val = float("inf")
        min_idx = None

        max_val = float("-inf")
        max_idx = None

        for i, val in enumerate(nums):
            if val < min_val:
                min_val = val
                min_idx = i

            if val >= max_val:
                max_val = val
                max_idx = i

        # now calculate the steps
        total_steps = min_idx + len(nums)-1-max_idx
        
        # cross
        if min_idx > max_idx:
            total_steps -= 1

        return total_steps 