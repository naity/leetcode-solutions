class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Two pointer plus another variable to track the repetitions
        a repetition of 1 or 2 is allowed

        Time: O(N)
        Space: O(1)
        """

        left, right, count = 0, 0, 0

        while right < len(nums):
            if nums[left] == nums[right]:
                count += 1
                right += 1
            else:
                if count > 1:
                    # at most 2
                    nums[left + 1] = nums[left]
                    left += 1
                left += 1
                nums[left] = nums[right]

                # reset count
                count = 0

        # for the last digit, if it occurs more than once
        if count > 1:
            nums[left + 1] = nums[left]
            left += 1

        return left + 1
