class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        Use DFS to visit all the rooms using available keys and a stack. Use a set to track the rooms that have been visited

        Time: O(N + E) number of rooms and "edges" (total number of keys)
        Space: O(N) for the set and stack
        """

        visited = set()

        visited.add(0)
        stack = [0]

        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    stack.append(key)
        return len(visited) == len(rooms)
