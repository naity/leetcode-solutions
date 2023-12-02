class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Two pointers and variable to track the current max area while moving the right pointer.
        Set the two pointers at the left and right ends of the list and move towards each other. Since the area is determined by (right - left) * min(height[left], height[right]), we move the pointer with lower height to see if we can get a larger area. Stop when they meet.

        Time: O(N)
        Space: O(1)
        """

        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1

        return max_area
