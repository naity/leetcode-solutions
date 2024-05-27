from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        """
        The revealed ordered should be sorted, e.g.
        [2, 3, 5, 7, 11, 13, 17]

        The trick is to consider the order of the indices that will be revealed
        in the reordered list:

        [0, 1, 2, 3, 4, 5, 6]

        We can simulate with process using a queue, and assign the correct cards to
        the corresponding indices

        Time: O(NlogN) + O(N) => O(NlogN)
        Space: O(N)
        """

        # sort cards
        deck.sort()

        # the indices of the reordered list
        q = deque([i for i in range(len(deck))])

        ans = [0] * len(deck)

        for card in deck:
            # put car in the index that will be revealed
            idx = q.popleft()
            ans[idx] = card

            if q:
                # skip the next index and put it at the end of the queue
                nxt = q.popleft()
                q.append(nxt)

        return ans
