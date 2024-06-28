class Solution:
    def numSteps(self, s: str) -> int:
        """
        Convert it to a deque, invovles bit manupilation
        1. even => last digit is 0 => divide by 2 => right shit by 1 (pop from the deque)
        2. add by 1 => find the first 0, and convert it 1, and convert all 1s to 0
            along the way. If no 0, add a one at the front

        Time: O(N), 2 steps to remove one digit if odd, 1 step if even.
        For addition, the worse case if O(N), however, won't happen everytime,
        as the next n-1 step will only take O(1)
        Space: O(N) for deque
        """

        bits = deque([int(c) for c in s])
        steps = 0
        while len(bits) > 1:
            if bits[-1] == 0:
                # even, divide by 2
                bits.pop()
            else:
                i = len(bits) - 1
                while i >= 0:
                    if bits[i] == 0:
                        bits[i] = 1
                        break
                    else:
                        bits[i] = 0
                    i -= 1
                if i == -1:
                    bits.appendleft(1)

            # increase steps
            steps += 1

        return steps
