class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        """
        Find the shortest path to a available exit.
        Use BFS to find the closet exit

        Time: O(M*N) visit each cell at most once
        Space: O(M+N) the queue can have at most this number of cells, think of as the boarder of the maze
        """
        m, n = len(maze), len(maze[0])

        q = deque()
        start_row, start_col = entrance
        q.append((start_row, start_col))
        # mark the entrance as + so we don't visit it again
        maze[start_row][start_col] = "+"
        steps = 1

        while q:
            cells = len(q)

            for _ in range(cells):
                i, j = q.popleft()

                # four directions
                dirs = [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]

                for x, y in dirs:
                    if 0 <= x < m and 0 <= y < n and maze[x][y] == ".":
                        # check if (x, y) is an exit
                        if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                            # (x, y) is an exit
                            return steps
                        # enqueue and mark it as visited
                        q.append((x, y))
                        maze[x][y] = "+"

            steps += 1

        # exit is not found
        return -1
