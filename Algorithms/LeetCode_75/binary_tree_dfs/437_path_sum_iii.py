# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        DFS on the tree and use a hashmap to store prefix sums and occurances. if current prefix sum - targetSum is in the hashmap, we increase the number of paths by its occurance

        Time: O(N)
        Space: O(N)
        """

        count = 0

        # prefix sums
        prefix = defaultdict(int)

        def dfs(node, pre):
            if node is None:
                return
            nonlocal count
            pre += node.val

            # root to current node
            if pre == targetSum:
                count += 1

            # the occurance of pre - targetSum
            count += prefix[pre - targetSum]

            # update hashmap
            prefix[pre] += 1

            # dfs
            dfs(node.left, pre)
            dfs(node.right, pre)

            # remove the current node from stack
            prefix[pre] -= 1

        dfs(root, 0)
        return count
