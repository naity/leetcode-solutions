class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Use a stack, push numbers in stack
        pop two numbers when seeing an operator
        do the calcuatation and push the result to the stack

        Two tricks:
        1) the second number is popped first
        2) how to handel /:
            if using //: need to specially handel num1 and num2 are different signs
            and num1/num2 is not an iteger
            or just use int()

        Time: O(N)
        Space: O(N)
        """

        stack = []
        ops = set(["+", "-", "*", "/"])

        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                # note that the second number is popped first
                num2 = stack.pop()
                num1 = stack.pop()

                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num1 - num2)
                elif token == "*":
                    stack.append(num1 * num2)
                else:
                    # need to check if the two numbers are one
                    # positive and one negative, and num1 % num2 is not 0
                    # e.g. -5 // 2 = -3
                    stack.append(int(num1 / num2))

        return stack[0]
