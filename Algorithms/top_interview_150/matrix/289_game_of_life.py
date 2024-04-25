class Solution:

    def get_val(self, i, j):
        if i < 0 or i >= self.m or j < 0 or j >= self.n:
            return 0

        return self.board[i][j]

    def neighbor_sum(self, i, j):
        # 8 possible neighbors
        dirs = [
            (i - 1, j),
            (i + 1, j),
            (i, j - 1),
            (i, j + 1),
            (i + 1, j + 1),
            (i - 1, j - 1),
            (i - 1, j + 1),
            (i + 1, j - 1),
        ]

        total = 0

        for x, y in dirs:
            total += self.get_val(x, y)

        return total

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        Visit each cell and save cells that needs to be updated

        make a copy of the board to reference the original values

        Time: O(MN)
        Space: O(MN)
        """

        self.m, self.n = len(board), len(board[0])
        self.board = [[board[i][j] for j in range(self.n)] for i in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                total = self.neighbor_sum(i, j)
                if board[i][j] == 0:
                    # sum of neighbors
                    if total == 3:
                        board[i][j] = 1
                else:
                    if total < 2 or total > 3:
                        board[i][j] = 0
