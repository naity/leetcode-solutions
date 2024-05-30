class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        """
        The main idea is to use two min-heaps, one for available servers with (weight, index),
        and one for unavailable servers with (time_to_free, weight, index).

        at time t, if available min-heap is empty, need to advance t to when the top unavailable server becomes free
        at time t, if any unailable server becomes available, pop and insert
        into the available min-heap
        pop the top server from the available min-heap, update the answer and time_to_free,
        and insert into the unavailable min-heap

        ** be aware of the timestamp t. if no waitime, t is equal to the task index j
        However, with waitime, t will be max(t, j)
        Time: O(NLogM)
        Space: O(M)
        """

        avai = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(avai)

        unavai = []

        ans = []
        t = 0

        for j, task in enumerate(tasks):
            t = max(t, j)
            if not avai:
                # need to advance t
                t = unavai[0][0]

            while unavai and unavai[0][0] <= t:
                _, w, i = heapq.heappop(unavai)

                # push into avai
                heapq.heappush(avai, (w, i))

            # the first server available based on priorities
            w, i = heapq.heappop(avai)
            ans.append(i)

            # update time_to_free and push to unavai
            heapq.heappush(unavai, (task + t, w, i))

        return ans
