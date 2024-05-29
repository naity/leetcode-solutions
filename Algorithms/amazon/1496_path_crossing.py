class Solution:
    def isPathCrossing(self, path: str) -> bool:
        """
        Use a set to store visited locations as tuples of (x, y)

        return true once a location is visited twice

        Time: O(N)
        Space: O(N)
        """

        visited = set()

        directions = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}

        x, y = 0, 0
        visited.add((x, y))

        for d in path:
            x1, y1 = directions[d]

            x += x1
            y += y1

            if (x, y) in visited:
                return True

            visited.add((x, y))

        return False
