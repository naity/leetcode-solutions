class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        Find consecutive intervals

        Time: O(N)
        Space: O(1)
        """

        left, right = 0, 0
        res = []

        while right < len(nums):
            # current interval ends
            if right == len(nums) - 1 or nums[right + 1] > nums[right] + 1:
                # left == right
                if nums[left] == nums[right]:
                    res.append(str(nums[left]))
                else:
                    res.append(f"{nums[left]}->{nums[right]}")

                # move left pointer
                left = right + 1

            right += 1

        return res
