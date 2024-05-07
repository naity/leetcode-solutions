class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Put all nums in a hashset.
        The longest sequence will start from the smallest num

        Time: O(N). During the for-loop, each num is visited at most twice
        Space: O(N)
        """

        nums = set(nums)

        longest = 0
        for num in nums:
            if num - 1 not in nums:
                # smallest
                smallest = num
                count = 1
                while smallest + 1 in nums:
                    count += 1
                    smallest += 1

                longest = max(count, longest)

        return longest
