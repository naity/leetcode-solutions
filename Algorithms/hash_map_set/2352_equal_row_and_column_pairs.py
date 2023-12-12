class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        """
        Naive: compare every row and every column: O(N^3)

        Trick: build a hashmap with the rows as keys, counts as the values
        then use the columns to check
        1) if the column is in the hashmap
        2.1) if not, 0 pairs
        2) if so, retrieve the value, which is the number of the pairs
        Sum the result for each value as the final result

        Time: O(N^2) => iterate each row and each column
        Space: O(N^2) => at most n keys with length n
        """
        n = len(grid)

        # create hashmap with rows as keys
        counts = defaultdict(int)
        for i in range(n):
            # conver to tuple
            counts[tuple(grid[i])] += 1

        res = 0

        # now check each column
        for j in range(n):
            col = []
            for i in range(n):
                col.append(grid[i][j])
            res += counts.get(tuple(col), 0)

        return res
