class SmallestInfiniteSet:
    def __init__(self):
        """
        Use a min-heap and a set.
        Min-heap for added back integers
        set for tracking integers in the heap

        Time: n: add, m: pop mlogn+nlogn
        Space: O(n)
        """
        self.min_heap = []
        self.in_heap = set()

        # use a variable to track the current integer
        self.curr = 1

    def popSmallest(self) -> int:
        # first check min_heap
        if self.min_heap:
            res = heapq.heappop(self.min_heap)
            self.in_heap.remove(res)
        else:
            res = self.curr
            self.curr += 1

        return res

    def addBack(self, num: int) -> None:
        # check if num is popped
        if num < self.curr and num not in self.in_heap:
            self.in_heap.add(num)

            # add it to min heap
            heapq.heappush(self.min_heap, num)
