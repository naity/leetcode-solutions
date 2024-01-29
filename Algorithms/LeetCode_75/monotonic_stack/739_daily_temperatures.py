class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Use stack:
        for each number in temperatures, compare it with the items int the stack, pop all number that are smaller than the curr number and then push it into stack

        Time: O(N)
        Space: O(N)
        """

        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            # save as tuple (temp, i) in stack
            while stack and stack[-1][0] < temp:
                _, j = stack.pop()
                res[j] = i - j
            # push
            stack.append((temp, i))

        return res
