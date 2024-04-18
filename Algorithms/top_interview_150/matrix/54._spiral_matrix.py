class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Iterate through the matrix following the rules.
        Use four variables to track the boundaries

        Time: O(MN)
        Space: O(1)
        """

        m, n = len(matrix), len(matrix[0])

        top, bottom, left, right = 0, m - 1, 0, n - 1

        res = []

        while len(res) < m * n:
            # top row left -> right
            for i in range(left, right + 1):
                res.append(matrix[top][i])

            # done
            top += 1

            # right column top -> bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])

            # done
            right -= 1

            # bottom row right -> left
            # CAUTION: need to check if bottom has been scanned above
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])

            # done
            bottom -= 1

            # left column bottom -> top
            # CAUTION: need to check if left has already been scanned above
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])

            # done
            left += 1

        return res
