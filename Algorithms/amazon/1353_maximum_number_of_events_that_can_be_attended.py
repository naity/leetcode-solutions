class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """
        Sort the events based on start day.

        The trick is to use a min-heap based on the end day.
        Always attend the event that ends the earliest as we would
        have more opportunies to attend the events that end later

        Iterate from day 1 to the latest end day, on each day:
        1) add events that start on the day to the min-heap
        2) get rid of events that end before this day from the min-heap
        3) attend the event that ends the earlies in the min-heap

        Time: find the last end day D, O(N),
              sort O(NlogN), for each event, enqueue and dequeue O(D+NlogN)
              => O(D+NlogN)
        Space: O(N)
        """

        events.sort()
        min_heap = []

        max_end = max(event[1] for event in events)
        i = 0
        num_events = 0
        day = 1

        while day <= max_end:
            # enqueue
            while i < len(events) and events[i][0] == day:
                # just need the end day
                heapq.heappush(min_heap, events[i][1])
                i += 1

            while min_heap:
                # check end time
                end_time = heapq.heappop(min_heap)
                if end_time >= day:
                    # one event per day
                    num_events += 1
                    break

            if not min_heap:
                if i < len(events):
                    # if min_heap is empty we can advance day to the next start date if exists
                    # as nothing can happen before then
                    day = events[i][0]
                else:
                    # no more events
                    break
            else:
                # otherwise try the next day
                day += 1

        return num_events
