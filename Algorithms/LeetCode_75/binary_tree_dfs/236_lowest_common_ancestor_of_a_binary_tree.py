# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """
        DFS, the base case is either node is None or node's value is p or q, we don't need to keep searching as the node will be LCA if the other value is within this subtree.
        We search the left and right subtrees until reaching these base cases. If p and q are in the left and right tree separately, we will return the current node. Otherwise, return the result from either left or right tree

        Time: O(N)
        Space: O(N)
        """

        if root is None:
            return

        if root.val in (p.val, q.val):
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        elif left:
            return left
        else:
            return right
