# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

# class NodeCopy:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random


class Solution:
    def copyRandomBinaryTree(self, root: "Optional[Node]") -> "Optional[NodeCopy]":
        """
        post-order traversal to copy the tree first
        use a hashmap to store mapping between original and copied nodes

        then do a second traversal for the random pointer

        Time: O(N)
        Space: O(N) hashmap and recursive stack
        """

        hashmap = {}

        def traversal(root):
            if root is None:
                return root

            left = traversal(root.left)
            right = traversal(root.right)

            # make copy
            copy = NodeCopy(root.val)

            copy.left = left
            copy.right = right

            # mapping
            hashmap[root] = copy

            return copy

        # first traversal
        copy = traversal(root)

        # now deal with random pointer in a preorder fashion
        def traversal2(root):
            if root is None:
                return

            copy = hashmap[root]

            # the mapping of the node that root's random pointer points to
            if root.random is not None:
                copy.random = hashmap[root.random]

            # left and right children
            traversal2(root.left)
            traversal2(root.right)

        traversal2(root)

        return copy
