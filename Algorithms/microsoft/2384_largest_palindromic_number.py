class Solution:
    def largestPalindromic(self, num: str) -> str:
        """
        Need to count each digit
        and try to put larger digits outside and/or in the middle

        use two lists (deque) to store the left/right halves, which allows
        for pop from the left and append to the left in O(1) time

        Time: O(N)
        Space: O(N)
        """

        counts = [0] * 10

        for n in num:
            counts[int(n)] += 1

        # edge case: all zeros
        if counts[0] == len(num):
            return "0"

        first = deque([])
        second = deque([])

        # need to know if the current result is odd or even
        center = ""

        for i in range(9, -1, -1):
            count = counts[i]
            if count == 0:
                continue

            if count // 2 != 0:
                for _ in range(count // 2):
                    # first half append at the end
                    first.append(str(i))
                    # second half append at the front
                    second.appendleft(str(i))

            # is center is not set and there is one digit left, use
            # it as the center
            if count % 2 == 1 and not center:
                center = str(i)

        # edge case: leading zeros
        while first and first[0] == "0":
            first.popleft()
            second.pop()

        return "".join(first) + center + "".join(second)
