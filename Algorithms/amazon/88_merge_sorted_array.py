class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        Since 0s at the end, start with the largest number and work backwards
        Need three pointers, one for each array, and one for the current insertion index in nums1

        123000
        256

        123006
        25

        123056
        2

        123356
        2

        122356

        Time: O(M+N)
        Space: O(1)
        """

        p1, p2 = m - 1, n - 1
        curr = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] <= nums2[p2]:
                nums1[curr] = nums2[p2]
                p2 -= 1
            else:
                nums1[curr] = nums1[p1]
                p1 -= 1

            curr -= 1

        while p2 >= 0:
            # nums left in nums2
            nums1[curr] = nums2[p2]
            p2 -= 1
            curr -= 1
