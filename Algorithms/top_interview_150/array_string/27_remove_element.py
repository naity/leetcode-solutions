class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Use two pointers, one to iterate through nums,
        the other one for the curr index in nums to save elements not equal to val

        Time: O(N)
        Space: O(1)
        """

        p, k = 0, 0

        while p < len(nums):
            if nums[p] != val:
                nums[k] = nums[p]
                k += 1

            # move p anyways
            p += 1

        # return k
        return k
