class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        have a set for each row, column, and sub-box, for filled cells check:
        1. row okay?
        2. column okay?
        3. sub-box okay?

        Time: O(N^2) => O(1)
        Space: O(3*N^2) => O(1)
        """
        m, n = 9, 9
        rows = defaultdict(set)
        cols = defaultdict(set)
        sub_boxes = defaultdict(set)

        for i in range(m):
            for j in range(n):
                val = board[i][j]
                if val == ".":
                    # pass empty cells
                    continue

                # row
                if val in rows[i]:
                    return False

                # add
                rows[i].add(val)

                # column
                if val in cols[j]:
                    return False

                # add
                cols[j].add(val)

                # sub-box row
                sub_box_row = i // 3
                sub_box_col = j // 3

                if val in sub_boxes[(sub_box_row, sub_box_col)]:
                    return False

                sub_boxes[(sub_box_row, sub_box_col)].add(val)

        return True
