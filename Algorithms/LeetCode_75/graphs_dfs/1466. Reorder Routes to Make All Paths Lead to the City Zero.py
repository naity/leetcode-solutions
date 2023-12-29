class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        Make the connections undirected by adding bi->ai for each ai-> bi. Do a DFS from 0 to every other city. If we use an edge from the original connections, we will need to increase the count of edges that need to be changed.

        Assign a value to the edges to distinguish original and added edges.

        Time: O(N) since it's a tree, there is going to be n-1 undirected edges
        Space: O(N)
        """

        tree = defaultdict(list)

        for a, b in connections:
            # 1 for original edges
            tree[a].append((b, 1))
            # 0 marks added edges
            tree[b].append((a, 0))

        res = 0
        visited = set()

        def dfs(i):
            nonlocal res
            for j, source in tree[i]:
                if j not in visited:
                    res += source
                    visited.add(j)
                    dfs(j)

        visited.add(0)
        dfs(0)
        return res
