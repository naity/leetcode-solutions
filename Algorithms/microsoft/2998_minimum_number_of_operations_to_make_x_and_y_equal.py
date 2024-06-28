class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        """
        Use BFS, essentially convert it to the shortest path

        Time: O(abs(x-y)):
        Space: O(abs(x-y))
        """
        q = deque([])
        visited = set()

        q.append((x, 0))

        while q:
            num, ops = q.popleft()

            if num == y:
                return ops

            # add to visited
            visited.add(num)

            # four possible choices
            choices = [num + 1, num - 1]

            if num % 11 == 0:
                choices.append(num // 11)
            if num % 5 == 0:
                choices.append(num // 5)

            for choice in choices:
                if choice not in visited:
                    q.append((choice, ops + 1))
