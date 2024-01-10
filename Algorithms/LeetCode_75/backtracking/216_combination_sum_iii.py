class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        9 choose k, check if sum of the k number if is euqal to n

        backtracking

        Time: O(k*9!/(k!*(9-k)!) k for copying the path 
        Space: O(k) for path and recursion stack
        """

        path = []
        res = []
        def search(i):
            if len(path) == k:
                if sum(path) == n:
                    # make a copy of path
                    res.append(path[:])

                return

            # only use 1 to 9
            if i > 9:
                return 

            # use i
            path.append(i)
            search(i+1)
            # exit
            path.pop()

            # do not use i
            search(i+1)
        

        search(1)
        return res