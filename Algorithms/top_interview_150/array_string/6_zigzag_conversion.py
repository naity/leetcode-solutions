class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Do this in "blocks" of 2*numRows - 2 chars

        insert one char for each row from up to bottom
        then from bottom to top except for the first and last rows

        Time: O(N): N number of chars in s
        Space: O(N)
        """
        # special case
        if numRows == 1:
            return s

        rows = [[] for _ in range(numRows)]
        block = 0
        block_size = 2 * numRows - 2
        max_block = math.ceil(len(s) / block_size)

        while block < max_block:
            # top to bottom
            i = 0
            while i <= numRows - 1 and i + block * block_size < len(s):
                rows[i].append(s[i + block * block_size])
                i += 1

            # is there still chars for bottom to up?
            if i != numRows:
                break

            curr_row = numRows - 2
            while i < block_size and i + block * block_size < len(s):
                rows[curr_row].append(s[i + block * block_size])
                curr_row -= 1
                i += 1

            # finished current block
            block += 1

        # join each row first and then join all the rows
        rows = ["".join(row) for row in rows]
        return "".join(rows)
