# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        """
        Use the property of BST.
        If p.val >= root.val, we know that the successor cannot be in the
        left subtree, so we can update root to root.right
        else, root could be the answer, use a variale to track this and then
        keep searching

        Time: O(N), O(LogN) is balanced
        Space: O(1)
        """

        ans = None

        while root:
            if p.val >= root.val:
                root = root.right
            else:
                ans = root
                root = root.left

        return ans
