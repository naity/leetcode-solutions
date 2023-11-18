import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        Start with the shorter of (str1 and str2) check if it divides both strings
        if not, keeps remove the last character

        How to check if x divides s?
        1. len(s) % len(x) == 0 AND
        2. x * (len(s) // len(x)) = s

        Note that the length of the largest string x that divides both strings will be the
        GCD of the lenghts of the two strings

        Time: O(min(m, n) * (m+n)) -> for each x we check if str1 and str2 are divided by x
        Space: O(min(m, n))

        m, n = len(str1), len(str2)
        x = str1 if m < n else str2

        def check_divide(x):
            k = len(x)
            return (m % k == 0 and
                n % k == 0 and
                x * (m // k) == str1 and
                x * (n // k) == str2
            )

        while x:
            if check_divide(x):
                return x
            x = x[:-1]
        return x

        A more clever approach is to first check if the gcd string exsits for str1 and str2,
        str1 + str2 must be the same as str2 + str1

        If gcd string exists, its length must be the gcd of len(str1) and len(str2)
        Therefore, we just need to check once

        Time: O(m+n)
        Space: O(1)
        """

        # check if common divisor exisits
        if str1 + str2 != str2 + str1:
            return ""
        k = math.gcd(len(str1), len(str2))
        return str1[:k]
