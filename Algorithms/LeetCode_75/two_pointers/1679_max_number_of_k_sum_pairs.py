class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        Sort the array first, then use two pointer at each end
        While p1 < p2
        1. if nums[p1] + nums[p2] == k: move both p1 and p2, increase operations by 1
        2 if < k: move p1
        3 if > k: move p2

        Time: O(NlogN)
        Space: O(1)
        """

        nums.sort()

        left, right = 0, len(nums) - 1

        res = 0
        while left < right:
            if nums[left] + nums[right] == k:
                res += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1

        return res
