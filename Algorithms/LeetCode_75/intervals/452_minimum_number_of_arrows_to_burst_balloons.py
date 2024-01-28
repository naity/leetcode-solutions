class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        Overlapping intervals.

        Sort intervals, set last_end to points[0][1]
            for i from 1 to len(points)-1
            check intervals[i]:
                if intervals[i][0] > last end:
                    increase count and update last_end
                if intervals[i][0] <= last end:
                    update last_end as the min of last_end and intervals[i][1]

        Time: O(NLogN)
        Space: O(N) for sorting
        """
        points.sort()

        res = 1
        last_end = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] <= last_end:
                # take the min end
                last_end = min(last_end, points[i][1])

            else:
                res += 1
                last_end = points[i][1]

        return res
