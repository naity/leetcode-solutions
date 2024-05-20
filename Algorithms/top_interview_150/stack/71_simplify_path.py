class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Create an empty stack
        split the path by / and iterate through the items
        1. if .., pop if stack is not empty
        2. elif . do nothing
        3. else, push to stack

        join the items in the stack with / and add a / at the start

        Time: O(N)
        Space: O(N)
        """

        stack = []

        for item in path.split("/"):
            if not item or item == ".":
                continue
            elif item == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(item)

        return "/" + "/".join(stack)
