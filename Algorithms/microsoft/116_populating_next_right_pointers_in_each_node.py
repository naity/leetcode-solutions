"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        """
        Use BFS to traverse the tree level by level

        Time: O(N)
        Space: O(N)
        """

        if root is None:
            return root

        q = deque([root])

        while q:
            num_nodes = len(q)

            # level by level
            for i in range(num_nodes):
                # dequeue
                node = q.popleft()

                # update next pointer except for the last node at the current level
                if i < num_nodes - 1:
                    node.next = q[0]
                # enqueue children
                if node.left is not None:
                    q.append(node.left)
                    q.append(node.right)

        return root
