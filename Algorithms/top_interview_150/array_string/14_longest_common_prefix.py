class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        check letter one by one for each str in strs

        Time: O(M*N), where M is the number of strings in strs,
        N is the length of the shortest string
        Space: O(1)
        """

        # if there is only one string
        if len(strs) == 1:
            return strs[0]

        res = []
        m = len(strs)
        n = min([len(s) for s in strs])

        for i in range(n):
            l = strs[0][i]
            match = True
            for j in range(1, m):
                # doesn't match
                if strs[j][i] != l:
                    match = False
                    break

            if match:
                res.append(l)
            else:
                break

        return "".join(res)
