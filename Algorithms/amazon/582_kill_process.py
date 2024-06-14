class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        """
        for a kill, we add it to the list, and then recursively
        kill each of its children. Instead of scan through ppid
        each time, can use a hashmap to store the children of a process
        such that it takes O(1) time to get its children

        each node is visited at most once, as each process can only have one parent

        Time: build hashmap O(N), DFS O(N) => O(N)
        Space: hashmap: O(N), recursion stack O(N) = > O(N)
        """

        hashmap = defaultdict(list)

        for p, pp in zip(pid, ppid):
            # 0 means no parent
            if pp != 0:
                hashmap[pp].append(p)

        ans = []

        def dfs(k):
            ans.append(k)

            for child in hashmap[k]:
                dfs(child)

        # start the dfs
        dfs(kill)
        return ans
