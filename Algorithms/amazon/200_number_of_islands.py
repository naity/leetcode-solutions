from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Use BFS to search each cell, skip if land has already been visited
        else increase islands by 1 and start BFS

        Time: O(MN)
        Space: O(min(m,n)) or O(m+n)
        This reflects the fact that at most, the frontier queue might
        need to store nodes around the perimeter
        """
        m, n = len(grid), len(grid[0])
        visited = set()

        def bfs(start):
            frontiers = deque([start])

            while frontiers:
                x, y = frontiers.popleft()

                if (x, y) not in visited:
                    visited.add((x, y))

                    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

                    for d in directions:
                        x_new, y_new = x + d[0], y + d[1]

                        if (
                            0 <= x_new < m
                            and 0 <= y_new < n
                            and (x_new, y_new) not in visited
                            and grid[x_new][y_new] == "1"
                        ):
                            frontiers.append((x_new, y_new))

        num_islands = 0
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == "1":
                    num_islands += 1
                    bfs((i, j))

        return num_islands
