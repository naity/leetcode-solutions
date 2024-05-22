class MinStack:

    def __init__(self):
        """
        A stack supports push, pop, top in O(1) time
        to support getMin in O(1) time, add another stack
        which stores the min from index 0 to i
        when push a new item to stack, check if it is < the top
        of the min stack, update if true

        Space: O(N)
        """
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        """
        Time: O(1)
        """
        self.stack.append(val)

        # check min
        if not self.min or self.min[-1] > val:
            self.min.append(val)
        else:
            # min is not changed
            self.min.append(self.min[-1])

    def pop(self) -> None:
        """
        pop from both stack and min stack

        Time: O(1)
        """

        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        # Time: O(1)
        return self.stack[-1]

    def getMin(self) -> int:
        # Time: O(1)
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
