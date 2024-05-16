class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        """
        find overlapping invervals and the merge

        use while loops for searching and merging along the way,
        avoiding using extra space

        Time: O(N)
        Space: O(1)
        """
        res = []

        i = 0

        # intervals ends before newInterval
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # overlapping ones
        start, end = newInterval
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            # new start and end
            start = min(intervals[i][0], start)
            end = max(intervals[i][1], end)

            i += 1

        # add this merged interval
        res.append([start, end])

        # intervals that starts after the merged interval
        while i < len(intervals):
            res.append(intervals[i])
            i += 1

        return res
