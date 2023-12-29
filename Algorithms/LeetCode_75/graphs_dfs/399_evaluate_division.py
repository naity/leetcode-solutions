class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        """
        Build a graph with equations, a -> b = value, b -> a = 1/value, for each query, use DFS to find a path from c to d whose value is the products of the edges. If the path does not exist, return -1.0.

        Time: O(M*N)
        Space: O(N): graph O(N), recursion stack O(N), visited set O(N)
        where M is the number of queries, N is the number of equations or edges
        """

        graph = defaultdict(list)

        for (a, b), v in zip(equations, values):
            graph[a].append((b, v))
            graph[b].append((a, 1 / v))

        def dfs(start, end, product):
            if start == end:
                # found it
                return product

            # add to visited
            visited.add(start)

            for nxt, value in graph[start]:
                if nxt not in visited:
                    ans = dfs(nxt, end, product * value)
                    if ans != -1.0:
                        # exit
                        visited.remove(start)
                        return ans
            # exit
            visited.remove(start)
            return -1.0

        res = []
        visited = set()
        for start, end in queries:
            # must both in graph
            if start not in graph or end not in graph:
                res.append(-1.0)
            else:
                res.append(dfs(start, end, 1))

        return res
