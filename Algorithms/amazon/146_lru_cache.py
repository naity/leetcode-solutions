from collections import OrderedDict


class LRUCache:
    """
    A hashmap can suports get and put in O(1) time
    The important thing is to maintain the hashmap size by
    ordering the key by when they are used

    Python has OrderedDict for this, which utilizs a hashmap and double-linked list
    so as to delete and insert in O(1) time

    Time: O(1)
    Space: O(capacity)
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # move it to the end
            self.cache.move_to_end(key)

        # update or insert
        self.cache[key] = value

        # pop the least used key if needed
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
