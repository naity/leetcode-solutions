import bisect
from collections import defaultdict


class Solution:
    def countRectangles(
        self, rectangles: List[List[int]], points: List[List[int]]
    ) -> List[int]:
        """
        Just check for each point for each rectangle

        Time: O(MN)
        Space: O(1)

        res = [0] * len(points)

        for i, (x, y) in enumerate(points):
            for l, h in rectangles:
                if 0 <= x <= l and 0 <= y <= h:
                    res[i] += 1

        return res

        However, this will generate Time Limit Exceeded.

        Intuition tells me binary search, but need to consider both x, y axis

        create a hashmap mapping h to a list of l as h is limited to 100

        then sort each list in hashmap

        the for each point, for h >= y, do a binary search on the list

        M: number of rectangles, N: number of points
        Time: O(M + MLogM+ N*100*logM) => O(M+N)LogM
        Space: O(M)
        """

        hashmap = defaultdict(list)

        # sort based on l first
        rectangles = sorted(rectangles, key=lambda item: item[0])

        for l, h in rectangles:
            hashmap[h].append(l)

        res = [0] * len(points)

        for i, (x, y) in enumerate(points):
            for k, v in hashmap.items():
                if k >= y:
                    left = bisect.bisect_left(v, x)
                    res[i] += len(v) - left

        return res
