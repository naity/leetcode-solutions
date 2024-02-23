class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Figure out the water that can be trapped at each index, and then sum them up

        For each index i, consider
        1. the max height on the left side
        2. the max height on the right side
        3. the height at i itself
        Then, the water trapped at i can be calcuated as min(max_left, max_right) - height_i

        For a brute-force approach, we scan the entire array to obtain max_left, max_right,
        which takes O(N^2) time.

        A better approach is to iterate through the array first and store max_left, max_right
        for each index first, and then do another iteration to calculate the results

        Time: O(N) # 3 iterations
        Space: O(N) # 2 arrays of length n
        """

        n = len(height)
        max_left = [0] * n
        max_right = [0] * n

        # max on the left side
        max_h = 0
        for i in range(n):
            max_h = max(height[i], max_h)
            max_left[i] = max_h

        # max on the right side
        max_h = 0
        for i in range(n - 1, -1, -1):
            max_h = max(height[i], max_h)
            max_right[i] = max_h

        # calculate the results
        water = 0
        for i, h in enumerate(height):
            water += min(max_left[i], max_right[i]) - h

        return water
