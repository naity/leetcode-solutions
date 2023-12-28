class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Use DFS and store visited cities in a set. Only run search on unvisited cities.

        Time: O(N^2) # Two for loops
        Space: O(N) # visted set and recursion call stack
        """
        n = len(isConnected)
        visited = set()

        provinces = 0

        def dfs(i):
            # connected cities
            for city, connected in enumerate(isConnected[i]):
                if connected == 1 and city not in visited:
                    visited.add(city)
                    dfs(city)

        for i in range(n):
            if i not in visited:
                # new component
                provinces += 1
                visited.add(i)
                dfs(i)

        return provinces
