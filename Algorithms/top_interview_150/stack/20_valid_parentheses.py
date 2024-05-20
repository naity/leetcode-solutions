class Solution:
    def isValid(self, s: str) -> bool:
        """
        Iterate through chars in s, push open brackets into a stack
        if the current char closes the open bracket at the top of the stack
        pop it from the stack

        If valid, the stack should be empty at the end

        Time: O(N)
        Space: O(N)
        """
        stack = []

        brackets = {"(": ")", "{": "}", "[": "]"}

        for c in s:
            if c in brackets:
                stack.append(c)
            else:
                if not stack or brackets[stack[-1]] != c:
                    return False

                stack.pop()

        # check if there is unmatched open brackets left in the stack
        return len(stack) == 0
