class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        """
        Check bit by bit
        1) if bit c is 1: either bit a or bit b should be 1
        2) if bit c is zero, both bit a and bit b should be zero

        Time: O(32 or 64)
        Space: O(1)
        """
        flips = 0
        while a != 0 or b != 0 or c != 0:
            bit_c = c & 1
            bit_a = a & 1
            bit_b = b & 1

            if bit_c == 0:
                flips += bit_a + bit_b

            else:
                if bit_a == 0 and bit_b == 0:
                    flips += 1

            # shift to the right
            a >>= 1
            b >>= 1
            c >>= 1
        return flips
