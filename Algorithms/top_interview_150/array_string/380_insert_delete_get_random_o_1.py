class RandomizedSet:

    def __init__(self):
        """
        Use a dictionary to check if val exists
        Use a list for random access
        The value of a key in the dictionary is the index of the key in the list
        Space: O(N)
        """

        self.nums_dict = {}
        self.nums_list = []

    def insert(self, val: int) -> bool:
        # Time: O(1)

        if val not in self.nums_dict:
            self.nums_dict[val] = len(self.nums_list)
            self.nums_list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        # This is the tricky part
        # in order to delete O(1) from the list
        # it has to be at the end so that it can be popped
        # And this why use a dictionary not set
        # O(1)
        if val not in self.nums_dict:
            return False

        # remove val from dict
        i = self.nums_dict.pop(val)

        # if i is not the last index
        if i < len(self.nums_list) - 1:
            # store the last value in the list at index i
            last_val = self.nums_list[-1]
            self.nums_list[i] = last_val
            # update dict as well
            self.nums_dict[last_val] = i

        # now pop the last item from list
        self.nums_list.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
