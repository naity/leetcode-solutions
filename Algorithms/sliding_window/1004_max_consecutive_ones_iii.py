class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Maintain a sliding window of at most k 0s, return the longest window length

        Time: O(N)
        Space: O(1)
        """

        left, right = 0, 0
        num_zeros = 0
        max_len = 0

        while right < len(nums):
            num = nums[right]
            # advance right pointer
            right += 1

            if num == 0:
                while num_zeros == k:
                    # need to remove a zero from window
                    if nums[left] == 0:
                        num_zeros -= 1
                    left += 1

                # now add the 0 at right to window
                num_zeros += 1

            # update max_len if needed
            max_len = max(max_len, right - left)

        return max_len
