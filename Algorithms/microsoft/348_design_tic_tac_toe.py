class TicTacToe:

    def __init__(self, n: int):
        """
        use a 2D array to represent the board
        use 0 to indicate empty, 1 for player 1, 2 for player 2

        space: O(N^2)

        self.n = n
        self.board = [[0] * n for i in range(n)]

        However, the problem states each move is valid, so if
        a row is marked N times, each time will be on a different column
        same applies to columns, diagonal, and antidiagonal
        thus, can count each row/column/diagonals, once each N, wins
        Instead of storing the counts for each player, we can use the same counts
        +1 for one player, and -1 for the other player, N or -N will indicate a win

        Space: O(2N+2) => O(N)
        """
        self.n = n
        self.row_counts = [0] * n
        self.col_counts = [0] * n
        self.diag_count = 0
        self.antidiag_count = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        mark the (row, col) block and then check for winner

        Time: O(N), check at most 4 times, each O(N)

        self.board[row][col] = player

        def check_row():
            # check row
            for c in range(self.n):
                if self.board[row][c] != player:
                    return False

            return True

        def check_col():
            # check column
            for r in range(self.n):
                if self.board[r][col] != player:
                    return False
            return True

        # check diagnoals
        # only the two main diagnoals have length n
        def check_diag():
            if row == col:
                # start from 0, 0
                i = 0
                while i < self.n:
                    if self.board[i][i] != player:
                        return False
                    i += 1

                return True

            return False

        def check_antidiag():
            # anti-diagonal
            if row+col == self.n-1:
                # start from 0, n-1
                i, j = 0, self.n-1

                while i < self.n:
                    if self.board[i][j] != player:
                        return False

                    i+=1
                    j-=1

                return True

            return False

        if check_row() or check_col() or check_diag() or check_antidiag():
            return player

        return 0

        Given by the optimized approach, update the counts and check if any of them reaches N
        O(1)
        """
        amount = 1 if player == 1 else -1
        self.row_counts[row] += amount
        self.col_counts[col] += amount

        if row == col:
            self.diag_count += amount

        if row + col == self.n - 1:
            self.antidiag_count += amount

        if (
            abs(self.row_counts[row]) == self.n
            or abs(self.col_counts[col]) == self.n
            or abs(self.diag_count) == self.n
            or abs(self.antidiag_count) == self.n
        ):
            return player

        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
