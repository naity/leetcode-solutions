class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Use two pointers
        left starts at 0, and right starts at -1
        Use a variable to tract the max_water

        Always move the pointer with lower height,
        because if we move the higher one, the width becomes shorter,
        while the height can't be any higher.
        However, if we move the lower one, it possible that we obtain
        a larger height even though the width shrinks

        Time: O(N)
        Space: O(1)
        """

        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left

            # update if needed
            max_water = max(max_water, h * w)

            # move the pointer with a smaller value
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
