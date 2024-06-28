class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        """
        Each team can be represented by a list of [count1, count2...name]

        then need to sort them using the counts by descending, but name ascending

        M: len of votes, N, number of teams
        Time: O(MN + NlogN) => O(M) as N is O(26)
        Space: O(N*N) => O(1)
        """
        counts = {}

        for vote in votes:
            for i, team in enumerate(vote):
                if team not in counts:
                    counts[team] = [0] * len(votes[0]) + [team]
                counts[team][i] += 1

        # results for each time
        results = list(counts.values())

        # votes are sort descending, but team ascending
        results = sorted(
            results, key=lambda x: tuple(-val for val in x[:-1]) + tuple(x[-1])
        )

        ans = [res[-1] for res in results]

        # return a string
        return "".join(ans)
