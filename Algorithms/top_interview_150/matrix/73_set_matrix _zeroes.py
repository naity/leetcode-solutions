class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        Find rows and cols that needs to be set to 0
        Then do it. Two iterations

        Time: O(MN)
        Space: O(M+N)

        m, n = len(matrix), len(matrix[0])

        rows = set()
        cols = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0

        Instead of using two sets, use the first cell in each row/column
        as flag. Use an additional variable since the first row and column
        share the same cell

        Time: O(MN)
        Space: O(1)
        """

        m, n = len(matrix), len(matrix[0])
        first_col = False

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j == 0:
                        first_col = True
                    else:
                        matrix[0][j] = 0

        # second loop for modifying matrix in-place
        # note that we need to start from (1, 1) without modifying the first row/column
        # otherwise it will change the flags
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # first row
        if matrix[0][0] == 0:
            for j in range(1, n):
                matrix[0][j] = 0

        # first col:
        if first_col:
            for i in range(m):
                matrix[i][0] = 0
