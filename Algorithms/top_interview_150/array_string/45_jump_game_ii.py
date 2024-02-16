class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Can start from the end, and then iterate through all position
        the current position can reach to, take the minimum

        Time: O(N^2)
        Space: O(N)

        n = len(nums)
        min_steps = [0] * n

        for i in range(n-2, -1, -1):
            max_idx = min(i+nums[i], n-1)
            min_step = float("inf")
            for j in range(i+1, max_idx+1):
                min_step = min(min_step, min_steps[j] + 1)

            min_steps[i] = min_step

        return min_steps[0]

        The hard thing is to come up with a strategy to get rid of the inner loop

        Start from the beginning and greedly extend the reach

        p1 indicates the furthest starting index of the current jump
        p2 indicates the furthest reachable index of the current jump

        This solution looks simple, but it is hard to wrap my head around the two pointers

        Time: O(n)
        Space: O(1)
        """

        p1, p2 = 0, 0
        jumps = 0

        # the last index will be reachable once we are done with n-2
        # otherwise the last index is not reachable
        # cannot loop until n-1 as this will trigger a new jump
        for i in range(len(nums) - 1):
            p2 = max(p2, i + nums[i])

            if i == p1:
                # need to take jump to get to i+1
                jumps += 1

                # new furthest starting point
                p1 = p2

        return jumps
