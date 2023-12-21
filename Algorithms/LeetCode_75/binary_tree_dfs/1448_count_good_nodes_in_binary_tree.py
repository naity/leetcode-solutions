# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        DFS and track the max value along the path and compare it with the value of the current node

        Time: O(N)
        Space: O(N)
        """

        good = 0

        def dfs(root, path_max):
            # base case
            if root is None:
                return

            nonlocal good
            # check the current node
            if path_max is None or root.val >= path_max:
                good += 1
                # update max value
                path_max = root.val

            # left and right subtrees
            dfs(root.left, path_max)
            dfs(root.right, path_max)

        dfs(root, None)

        return good
