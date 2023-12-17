class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        """
        The best strategy is to ban the next closes member from the other party.

        Two queues, one for each party, while both of them are not empty, for each round
        1) compare the heads, the one with a smaller index will ban the other one
        2) dequeue the smaller head and push it back to queue, the key is to ADD N TO INDEX to because the head needs to wait until the next round to use its right
        3) dequee the banned member

        return the party whose queue is not empty

        Time: Dequeue and enqueue for each item takes O(1) time, each round the number of members decrease by half, N+N/2+N/4+....+ = O(N)
        Space: O(N)
        """
        r, d = deque(), deque()

        for i in range(len(senate)):
            if senate[i] == "R":
                r.append(i)
            else:
                d.append(i)

        # keep going if until one of them is empty
        while r and d:
            r_head, d_head = r.popleft(), d.popleft()

            if r_head < d_head:
                # R bans D, increase r_head by N to indicate the second round
                r.append(r_head + len(senate))
            else:
                # D bans R, similarly add N
                d.append(d_head + len(senate))

        # return the one who is not empty
        return "Radiant" if r else "Dire"
