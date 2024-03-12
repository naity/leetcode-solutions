class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Use a sliding window and a variable to track minimal length
        Use an additional variable to track window sum
        Move right to expand the window
        Move left to shrink window until the sum is less than the target

        Time:O(N)
        Space:O(1)
        """

        left, right = 0, 0
        min_length = float("inf")
        total = 0

        while right < len(nums):
            # add right to window
            total += nums[right]
            right += 1

            # if >= target, update min_length if needed
            # and shrink left
            while left < right and total >= target:
                min_length = min(min_length, right - left)

                # shrink left
                total -= nums[left]
                left += 1

        # take care of the case when no such subarray
        if min_length == float("inf"):
            return 0
        return min_length
