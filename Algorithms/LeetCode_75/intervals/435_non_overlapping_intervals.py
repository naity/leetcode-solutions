class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Sort the intervals by start time
        Initiate an array of nonoverlapping intervals with the first interval 0

        for each interval i starting from 1:
            1) if starti >= end of nonoverlapping[-1]:
                no overlapping; add to nonoverlapping

            2) if starti < end of nonoverlapping[-1]:
                overlapping. which one to keep? Because we want to find the minumum number of intervals to remove, we should keep the one that ends earlier

        Space optimization:
             we don't really need an array, just a variable to keep the last end time

        Time: O(NLogN) for sorting, then O(N) overall O(NlogN)
        Space: O(N) sorting
        """

        intervals.sort()
        count = 0
        last_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < last_end:
                # we will remove one
                count += 1

                # update last_end
                last_end = min(intervals[i][1], last_end)
            else:
                # update last_end
                last_end = intervals[i][1]

        return count
