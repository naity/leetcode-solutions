# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Use DFS, the current depth will be the max depth of the left and right and then plus 1

        Time: visit each node once O(N)
        Space: stack is O(N)
        """

        if root is None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
