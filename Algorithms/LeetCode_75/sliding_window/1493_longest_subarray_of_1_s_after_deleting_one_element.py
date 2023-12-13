class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        Maintain a sliding window that has most one 0. The result will be the longest window size -1

        Time: O(N)
        Space: O(1)
        """

        left, right = 0, 0
        longest = 0
        num_zero = 0

        while right < len(nums):
            num = nums[right]
            right += 1

            num_zero += 1 - num

            # need to move left pointer to remove 0 if there is already one
            while num_zero > 1:
                num_zero -= 1 - nums[left]
                left += 1

            # update longest if possible
            longest = max(longest, right - left - 1)

        return longest
