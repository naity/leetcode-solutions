# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:


class Solution:
    def findCelebrity(self, n: int) -> int:
        """
        build a graph based on the each pair
        celebrity has indegree of n-1 and outdegree of 0

        Time: O(N^2)
        Space: O(N)

        ins = [0] * n
        outs = [0] * n

        for i in range(n):
            for j in range(i+1, n):
                if knows(i, j):
                    ins[j] += 1
                    outs[i] += 1

                if knows(j, i):
                    ins[i] += 1
                    outs[j] += 1

        for i in range(n):
            if ins[i] == n-1 and outs[i] == 0:
                return i

        return -1

        The key insight is that each call to knows can rule out one person
        suppose 0->1, 0 is ruled out, if 0 does not know 1, 1 is ruled out.
        first iteration to rule out n-1 person and leaves one candidiate
        then do another iteration to check the candidate.

        Time: O(N)
        Space: O(1)
        """

        candidate = 0

        # select one candidate
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i

        # check candidate
        for i in range(n):
            if i != candidate:
                if knows(candidate, i) or not knows(i, candidate):
                    return -1

        return candidate
