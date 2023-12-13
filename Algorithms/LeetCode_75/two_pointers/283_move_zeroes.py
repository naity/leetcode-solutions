class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Move zeros to the end => move non-zeros to the front.

        Use two pointers, whenever right points to a non-zero number,
        swap with left

        Time: O(N)
        Space: O(1)
        """

        left, right = 0, 0

        while right < len(nums):
            if nums[right] != 0:
                tmp = nums[left]
                nums[left] = nums[right]
                nums[right] = tmp

                # move left to point to the next available slot
                left += 1

            right += 1
