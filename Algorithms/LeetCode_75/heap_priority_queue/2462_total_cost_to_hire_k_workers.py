class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        """
        Divide the costs array into three parts, [0:candidates], [-candidates:], and potential items in the middle.
        Then use two min heaps for the front and end, pop the smaller one for each k iterations. If there are items in the remainder group and we pop from the front, add the first item from the remainder to the front heap, otherwise add the last remainder item to the end

        Time: O(candidates + kLogcandidates)
        Space: O(N)
        """
        if len(costs) > candidates * 2:
            front, end = costs[:candidates], costs[-candidates:]
            # use a deque for popping from both ends
            remainder = deque(costs[candidates:-candidates])
        else:
            # to avoid adding the same item to both front and end
            front, end = costs[:candidates], costs[candidates:]
            remainder = []

        # convert to min-heap
        heapq.heapify(front)
        heapq.heapify(end)

        total = 0

        for _ in range(k):
            # if front is empty, pop from the end and vice versa
            # also pop from the end if it has a smaller item
            if not front or (len(end) > 0 and front[0] > end[0]):
                cost = heapq.heappop(end)
                # check the remainder
                if remainder:
                    heapq.heappush(end, remainder.pop())
            else:
                # from front
                cost = heapq.heappop(front)
                # check the remainder
                if remainder:
                    heapq.heappush(front, remainder.popleft())

            total += cost

        return total
