# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        BFS traversal, append the last node at each level to the result list

        Time: O(N)
        Space: O(N): the last layer can contain N/2 nodes

        Height: Log2(N), last layer 2^(height-1)
        2^(log2(N)-1) => 2^(log2(N))/2 => N/2
        """

        q = deque()

        if root is not None:
            q.append(root)

        result = []
        while q:
            num_nodes = len(q)

            for i in range(num_nodes):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

                # append the right most node value to the result
                if i == num_nodes - 1:
                    result.append(node.val)

        return result
