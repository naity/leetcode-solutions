class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        Reverse on the diagonal and then reversee left to right

        Time: O(N^2)
        Space: O(1)
        """
        n = len(matrix)
        # transpose
        for i in range(n):
            for j in range(i + 1, n):
                # swap
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reflect
        for i in range(n):
            left, right = 0, n - 1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1
