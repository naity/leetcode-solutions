class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Binary search

        Check if mid is a peak, if not, only need to search the bigger half. Why? for [left, mid, right], if mid is not a peak, let's assume right > mid, if right+1 < right, right is a peak, if right +1 > right, as long as there is i after right+1 where nums[i] < nums[i-1], we will have peak. If not, we will reach the end of the array, and the last item will be a peak. In summary, it is guaranteed that there will be a peak in the bigger half.

        Time: O(logn)
        Space: O(1)
        """

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if (mid - 1 < 0 or nums[mid - 1] < nums[mid]) and (
                mid + 1 == len(nums) or nums[mid] > nums[mid + 1]
            ):
                # found a peak
                return mid

            # search the bigger half
            if mid - 1 >= 0 and nums[mid - 1] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
