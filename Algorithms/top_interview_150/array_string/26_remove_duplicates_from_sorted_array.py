class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Since the list is sorted, duplicates will be next to each other
        Use two pointers:
        1. Initiate both with 0
        Repeat:
        3. keep advancing right until num_left != num_right
        4. advance left and set num_left = num_right

        Time: O(N)
        Space: O(1)
        """

        left, right = 0, 0

        while right < len(nums):
            if nums[right] == nums[left]:
                right += 1
            else:
                left += 1
                nums[left] = nums[right]
        return left + 1
