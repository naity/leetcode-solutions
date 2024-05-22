from itertools import combinations


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        """
        Get a list of visited websites for each user
        and then count the unique patterns

        Time: O(N**3)
        Space: O(N**3)
        """

        patterns = defaultdict(list)

        for user, t, web in zip(username, timestamp, website):
            patterns[user].append((t, web))


        counts = defaultdict(int)

        for k, v in patterns.items():
            # sort by timestamp
            v.sort()

            webs = [item[1] for item in v]

            # combinations of 3
            for combo in set(combinations(webs, 3)):
                counts[combo] += 1

        # sort combo by counts DESC then name ASC
        sorted_counts = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

        return sorted_counts[0][0]