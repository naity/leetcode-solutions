class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        How to rotate by one step?

        create a new array and for each nums[i], append nums[i-1] to it

        repeat this process k times
        Time: O(k * N)
        Space: O(N)

        for _ in range(k):
            temp = []

            for i, num in enumerate(nums):
                temp.append(nums[i-1])

            for i in range(len(nums)):
                nums[i] = temp[i]

        convert nums to a deque, each rotation just pop the last element and
        append it to the left

        Time: O(K + N)
        Space O(N)

        # take the modulo
        n = len(nums)
        k = k % n

        nums2 = deque(nums)

        for _ in range(k):
            num = nums2.pop()
            nums2.appendleft(num)

        nums[:] = nums2


        *Reverse*:

        rotate k times, the last k elements will become the first k elements
        1. reverse the whole list
        2. reverse the first k elements
        3. reverse the rest n-k elements

        Time: O(N)
        Space: O(1)
        """

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        n = len(nums)
        k = k % n

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
