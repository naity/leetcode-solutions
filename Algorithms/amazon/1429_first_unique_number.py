class FirstUnique:

    def __init__(self, nums: List[int]):
        """
        Don't need to count the numbers, just need to know if unique or not
        A dictionary to map numbers to uniqueness. Also need to know the order. Can use a queue/deque
        Enqueue each number only once. If the top number if the queue is not unique, pop it from the queue

        Time: O(N)
        Space: O(N)
        """

        self.unique = {}
        self.queue = deque()

        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        """
        best O(1), worst O(N)
        O(1) (amortized)
        Because the number of O(1) removals is proportional to the number of calls to add(),
        we say that the time complexity amortizes across all calls to add() and showFirstUnique(),
        giving an overall time complexity of O(1)(amortized).
        """

        # check the numbers in queue one by one
        while self.queue:
            num = self.queue[0]
            if self.unique[num]:
                return num

            self.queue.popleft()

        # return -1 if not found
        return -1

    def add(self, value: int) -> None:
        # O(1)
        if value in self.unique:
            self.unique[value] = False
        else:
            # value is unique
            self.unique[value] = True
            # add to queue
            self.queue.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
