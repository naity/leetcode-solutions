class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Essentially cycle detection, use a hashset to store numbers that have been checked

        It is very difficult to figure out the time and space complexicity
        LogN is the number of digits, we go over all the digits in each while loop
        the next number's largest value is logN * 81, hence log(N) + log(log(N)) + ...

        since the next number of 999 is 243, once it is below 243, it is impossible to go back up again
        either stock or 1

        Time: log(N) + log(log(N)) => Log(N)
        Space: Log(N)
        """

        # simple case
        if n == 1:
            return True

        mem = set()

        while n != 1:
            mem.add(n)
            total = 0

            # sum up the square of each digit
            for d in str(n):
                total += int(d) ** 2

            n = total

            if n in mem:
                return False

        return True
