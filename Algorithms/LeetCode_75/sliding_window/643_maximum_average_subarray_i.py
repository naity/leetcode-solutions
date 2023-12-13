class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Use two pointers to maintain a sliding window of length k.
        Use a variable to track sum of the elements in the window and the maximum avg

        Time: O(N)
        Space: O(1)
        """

        left, right = 0, 0
        window_sum = 0
        max_avg = float("-inf")
        while right < len(nums):
            if right - left == k:
                # remove the num at the left pointer before adding right
                window_sum -= nums[left]
                left += 1

            # add right
            window_sum += nums[right]

            # move right pointer
            right += 1

            # average if window size is k
            if right - left == k:
                max_avg = max(max_avg, window_sum / k)

        return max_avg
