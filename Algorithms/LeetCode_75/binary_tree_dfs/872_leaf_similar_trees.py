# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        DFS on each tree, and then compare the leaf values

        Time: O(M+N)
        Space: O(M+N)
        """

        def dfs(root):
            if root is None:
                return []

            # leaf node
            if root.left is None and root.right is None:
                return [root.val]

            left = dfs(root.left)
            right = dfs(root.right)
            return left + right

        leaves1 = dfs(root1)
        leaves2 = dfs(root2)

        if len(leaves1) != len(leaves2):
            return False

        for num1, num2 in zip(leaves1, leaves2):
            if num1 != num2:
                return False
        return True
