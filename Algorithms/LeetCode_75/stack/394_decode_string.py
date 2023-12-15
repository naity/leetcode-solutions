class Solution:
    def decodeString(self, s: str) -> str:
        """
        Maintain a stack to store the result
        Iterate char over s:
        1. push to stack
        2. start decoding if char is ]
            2.1. pop until [
            2.2. pop if digit
            2.3. repeat k times
            2.4. push back to stack in reverse order

        Time: ?
        Space: ?
        """

        res = []

        for char in s:
            if char != "]":
                res.append(char)
            else:
                string = []
                while res[-1] != "[":
                    string.append(res.pop())
                # pop [
                res.pop()

                # get k
                k = []
                while res and res[-1].isdigit():
                    k.append(res.pop())

                # k is in reverse order
                k = int("".join(k)[::-1])

                # now decode
                decoded = "".join(string) * k

                # push back
                for i in range(len(decoded) - 1, -1, -1):
                    res.append(decoded[i])

        return "".join(res)
