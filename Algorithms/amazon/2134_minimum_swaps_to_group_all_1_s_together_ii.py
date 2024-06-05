class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        """
        Maintain a sliding window of length k, where
        k is the number of 1s in nums, we just need to find the
        window with the most 1s, and the difference between
        k and the largest number of 1s found is the swaps needed

        Time: O(N) iterate through the list three times
        Space: O(1)
        """
        n = len(nums)
        k = sum(nums)

        if k == n:
            return 0

        count = 0
        for i in range(k):
            count += nums[i]

        max_count = count
        # since the array is circular, the last index we need to
        # check is len(nums)-1
        for i in range(1, n):
            # since it's circular, use mode to get the right index
            count = count - nums[i - 1] + nums[(i + k - 1) % n]
            max_count = max(count, max_count)
        return k - max_count
