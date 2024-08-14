"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        """
        Use a hashmap to map old nodes to new nodes
        two passes first pass to copy nodes
        second pass to copy random pointers

        Time: O(N)
        Space: O(N)
        """

        sentinel = Node(0)
        p_old = head
        p_new = sentinel

        hashmap = {}

        # first pass
        while p_old:
            new_node = Node(p_old.val)
            hashmap[p_old] = new_node
            p_new.next = new_node
            p_new = p_new.next
            p_old = p_old.next

        # second pass
        p_old = head
        while p_old:
            # in case random points to None
            hashmap[p_old].random = hashmap.get(p_old.random, None)
            p_old = p_old.next

        return sentinel.next
