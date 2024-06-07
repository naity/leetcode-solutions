from itertools import combinations


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        """
        Use this formula:
        Area = 1/2*abs(x1(y2-y3)+x2(y3-y1)+x3(y1-y2))

        Time: N chose 3 => O(N3)
        Space: O(1)
        """

        max_area = 0
        for (x1, y1), (x2, y2), (x3, y3) in combinations(points, 3):
            area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
            max_area = max(area, max_area)

        return max_area
