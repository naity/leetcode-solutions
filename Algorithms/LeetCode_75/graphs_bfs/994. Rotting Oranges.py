class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Start from rotten oranges and run BFS, compute how many levels are needed to reach all fresh oranges. If there is fresh oranges that cannot be reached, return -1.

        Time: O(M*N)
        Space: O(M*N) if all the oranges are rotten, we will need to initialize the queue with all cells
        """

        q = deque()
        m, n = len(grid), len(grid[0])
        # add all rotten oranges to queue
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))

        # initialize with -1 as we will still run BFS for the last layer
        minutes = -1

        while q:
            num_oranges = len(q)
            minutes += 1

            for _ in range(num_oranges):
                i, j = q.popleft()
                # four directions
                dirs = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

                for x, y in dirs:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        # mark (x, y) as rotten
                        grid[x][y] = 2
                        q.append((x, y))

        # check if there is still fresh oranges left
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        # need to take care of the edge case where is no rotten orange or fresh orange to begin with and the while loop will never run
        return max(0, minutes)
