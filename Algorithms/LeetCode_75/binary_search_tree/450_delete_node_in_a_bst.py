# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Use recursion to find and delete the key.
        if the node with value key doesn't have children, delete it,
        otherwise delete the right-most node of the left subtree or the left-most child of the right subtree. Use recursion to avoiding tracking the parent node

        Time: O(H), we keep going down the tree until reaching the leaves
        Space: O(H)
        """
        if root is None:
            return root

        if root.val > key:
            # recursion on the left substree
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            # recursion on the right subtree
            root.right = self.deleteNode(root.right, key)
        else:
            # need to remove root
            # if root is leave node
            if root.left is None and root.right is None:
                root = None
            elif root.left is not None:
                # find the right most node
                target = root.left
                while target.right:
                    target = target.right

                # swap the value
                root.val = target.val
                # use recursion to delete the target node
                root.left = self.deleteNode(root.left, target.val)
            else:
                # find the left most node
                target = root.right
                while target.left:
                    target = target.left

                # similar process
                root.val = target.val
                root.right = self.deleteNode(root.right, target.val)

        return root
