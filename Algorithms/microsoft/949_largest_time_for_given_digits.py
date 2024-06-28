class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        """
        24 possible permutations

        remove the one that are not valid
        get the largest one

        Time: O(1)
        Space: O(1)
        """

        perms = set(itertools.permutations(arr, len(arr)))

        max_time = -1
        res = ""

        for perm in perms:
            if perm[0] > 2:
                continue
            if perm[0] == 2 and perm[1] >= 4:
                continue

            if perm[2] > 5:
                continue

            hour = perm[0] * 10 + perm[1]
            mins = perm[2] * 10 + perm[3]

            if hour * 60 + mins > max_time:
                max_time = hour * 60 + mins
                res = f"{perm[0]}{perm[1]}:{perm[2]}{perm[3]}"

        return res
