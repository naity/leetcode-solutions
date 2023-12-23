# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        """
        DFS, check parent direction, if different, increase length
        if the same reset length to 1. Note reset to 1 not zero, as the current node will count as 1
        Another case is for the root, both left and right will work, use parent is None to catch this case

        Time: O(N)
        Space: O(N)
        """
        max_length = 0

        def dfs(node, parent, length):
            if node is None:
                return

            nonlocal max_length
            max_length = max(length, max_length)

            if parent is None:
                dfs(node.left, "left", length + 1)
                dfs(node.right, "right", length + 1)
            elif parent == "left":
                dfs(node.left, "left", 1)
                dfs(node.right, "right", length + 1)
            else:
                dfs(node.left, "left", length + 1)
                dfs(node.right, "right", 1)

        dfs(root, None, 0)
        return max_length
