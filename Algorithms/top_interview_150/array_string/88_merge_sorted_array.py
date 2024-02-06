class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        The problem would be easy if it is allowed to create a new array.

        Since the 0s are at the end, we could start from the largest numbers
        1 2 3 0 0 0
        2 5 6

        1 2 3 0 0 6
        2 5

        1 2 3 0 5 6
        2

        1 2 3 3 5 6
        1 2 2 3 5 6

        Three pointers: one for nums1, one for nums2, one for the curr index in nums1 for insertion

        Time: O(m+n)
        Space: O(1)
        """

        # start from the end
        p1 = m - 1
        p2 = n - 1
        curr = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] <= nums2[p2]:
                # insert nums2[p2] to the end
                nums1[curr] = nums2[p2]
                p2 -= 1
            else:
                nums1[curr] = nums1[p1]
                p1 -= 1

            # move curr
            curr -= 1

        # must insert all numbers in nums2
        while p2 >= 0:
            nums1[curr] = nums2[p2]
            p2 -= 1
            curr -= 1
