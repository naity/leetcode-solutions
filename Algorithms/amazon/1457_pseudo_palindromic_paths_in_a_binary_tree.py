# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        """
        traverse the tree and then check if each path is a palindrome

        Time: O(N), counting O(10) => O(1)
        Space: O(logN) recursion stack, count hashmap is O(10) => O(1)
        """

        def check_palindrome(path):

            # path is palindrome if
            # at most one digit has an odd count
            num_odd = 0
            for count in path.values():
                if count % 2 != 0:
                    num_odd += 1

            if num_odd <= 1:
                return True

            return False

        palindrome_paths = 0

        def traversal(root, path):
            # preorder traversal
            if root is None:
                return

            val = root.val

            path[val] += 1

            # leaf node
            if root.left is None and root.right is None:
                if check_palindrome(path):
                    nonlocal palindrome_paths
                    palindrome_paths += 1

            if root.left is not None:
                traversal(root.left, path)

            if root.right is not None:
                traversal(root.right, path)

            # exit from current node
            path[val] -= 1

        path = defaultdict(int)
        traversal(root, path)

        return palindrome_paths
