class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        Count the chars in s

        use a priority queue to place the most frequent char in turns
        need to check if the popped char is the same as the last one
        if it is, need to pop another char from the priority queue
        if there is no more to pop, return ""

        Time: O(N) + O(Nlogk) => O(N)
        Space: O(k) => O(1)
        """

        counts = defaultdict(int)

        for char in s:
            counts[char] += 1

        # use negative for max heap, enqueue
        q = [(-v, k) for k, v in counts.items()]
        heapq.heapify(q)

        result = []
        while q:
            # pop the most frequent char
            count1, char1 = heapq.heappop(q)

            # check the most frequent char
            if not result or char1 != result[-1]:

                result.append(char1)

                # update count
                count1 += 1

                if count1 < 0:
                    # push it back
                    heapq.heappush(q, (count1, char1))

            else:
                # need to pop the second most frequent
                if not q:
                    # no more chars to pop
                    return ""
                count2, char2 = heapq.heappop(q)

                result.append(char2)

                # update count2
                count2 += 1

                if count2 < 0:
                    # push it back
                    heapq.heappush(q, (count2, char2))

                # push char1 back as well
                heapq.heappush(q, (count1, char1))

        return "".join(result)
