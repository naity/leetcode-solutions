class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        Find unique overlaps, try to find the overlaps for as many intervals as possible

        Sort first and workin the intervals one by one

        Time: O(NlogN)
        Space: O(N) for sorting
        """
        # sort
        points.sort()

        res = 1
        last_end = points[0][1]

        for point in points[1:]:
            # overlap?
            if point[0] > last_end:
                # no overlap
                res += 1
                last_end = point[1]
            else:
                # take the min of the ends
                last_end = min(point[1], last_end)

        # the number of arrows is just the number of unique overlaps
        return res
