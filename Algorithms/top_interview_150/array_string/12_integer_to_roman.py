class Solution:
    def intToRoman(self, num: int) -> str:
        """
        deal the digits one by one with recursion
        check the value for special cases and convert it to string

        Time: O (N) Since N is most 4, can also say O(1)
        Space: O (N)
        """

        res = ""

        def helper(number, factor):
            nonlocal res

            digit = number % 10

            if factor == 1:
                # ones digit
                if digit == 5:
                    roman = "V"
                elif digit == 4:
                    roman = "IV"
                elif digit == 9:
                    roman = "IX"
                elif digit < 4:
                    roman = "I" * digit
                else:
                    roman = "V" + "I" * (digit - 5)

            elif factor == 10:
                # tens digit
                if digit == 5:
                    roman = "L"
                elif digit == 4:
                    roman = "XL"
                elif digit == 9:
                    roman = "XC"
                elif digit < 4:
                    roman = "X" * digit
                else:
                    roman = "L" + "X" * (digit - 5)

            elif factor == 100:
                # hundreds digit
                if digit == 5:
                    roman = "D"
                elif digit == 4:
                    roman = "CD"
                elif digit == 9:
                    roman = "CM"
                elif digit < 4:
                    roman = "C" * digit
                else:
                    roman = "D" + "C" * (digit - 5)

            else:
                # thousands digit
                roman = "M" * digit

            # update result
            res = roman + res

            if number // 10 > 0:
                # recursion
                helper(number // 10, factor * 10)

        helper(num, 1)
        return res
