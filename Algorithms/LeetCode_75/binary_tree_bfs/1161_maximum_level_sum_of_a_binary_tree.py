# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
        BFS traversal, calculate the sum of each level using a queue and track the max sum

        Time: O(N)
        Space: O(N) 1+2+...+2^h = n => 2^(h+1)-1=n =>2^h = (n+1)/2
        """

        max_sum = float("-inf")
        max_level = -1

        q = deque()
        q.append(root)
        level = 0

        while q:
            num_nodes = len(q)
            level += 1
            total = 0
            for i in range(num_nodes):
                node = q.popleft()
                total += node.val

                # add children to queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # update max if needed
            if total > max_sum:
                max_sum = total
                max_level = level

        return max_level
