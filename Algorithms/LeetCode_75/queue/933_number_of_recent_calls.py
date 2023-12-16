class RecentCounter:
    """
    Use a queue, push the current request and pop requests out of range

    Time: O(1) at most 3000
    Space: O(1) at most 3000
    """

    def __init__(self):
        self.counter = deque()

    def ping(self, t: int) -> int:
        while len(self.counter) > 0 and self.counter[0] < t - 3000:
            self.counter.popleft()
        self.counter.append(t)
        return len(self.counter)
