# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Check the value of the root, if > the val, search the left tree, equal to the value, return the root, otherwise search the right subtree

        Time: O(H) Average: LogN, worst: N
        Space: O(H)
        """

        if root is None or root.val == val:
            return root

        if root.val < val:
            return self.searchBST(root.right, val)

        return self.searchBST(root.left, val)
