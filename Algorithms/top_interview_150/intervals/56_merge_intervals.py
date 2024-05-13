class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Sort the intervals

        Initiate the result list with the first interval and iterate from the second
        compare to the last interval in the result list
        1) if start > last end: append a new interval
        2) otherwise, extend the last interval if needed

        Time: sort O(NlogN) + O(N) => O(NLogN)
        Space: sort O(N), result list O(N) => O(N)
        """

        intervals.sort()

        res = [intervals[0]]

        for start, end in intervals[1:]:
            last_start, last_end = res[-1]

            if start > last_end:
                res.append([start, end])

            else:
                new_end = max(last_end, end)

                # update
                res[-1][1] = new_end

        return res
