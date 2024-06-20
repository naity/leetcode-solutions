class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        """
        First check if the previous position has food, if no,
        the key idea is to try to put the food at the next position first
        as it could be shared with the next hamster.
        If not possible, then try the previous position.
        If still not possible, return -1

        Time: O(N)
        Space: O(N)

        """
        min_food = 0
        hamsters = list(hamsters)
        for i, item in enumerate(hamsters):
            if item == "H":
                if i - 1 >= 0 and hamsters[i - 1] == "F":
                    continue
                if i + 1 < len(hamsters) and hamsters[i + 1] == ".":
                    hamsters[i + 1] = "F"
                    min_food += 1
                elif i - 1 >= 0 and hamsters[i - 1] == ".":
                    min_food += 1
                else:
                    return -1

        return min_food
