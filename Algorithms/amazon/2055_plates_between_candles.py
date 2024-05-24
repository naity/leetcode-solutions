from bisect import bisect_left, bisect_right


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        """
        Key idea:
        Find the indices of candles, and use binary search to find the leftmost
        and rightmost candels for a given query

        use bisect_left and bisect_right to locate the indices with binary search

        Time: O(N + qLogN)
        Space: O(N)
        """

        # O(N)
        candle_indicies = [i for i, char in enumerate(s) if char == "|"]

        results = [0] * len(queries)

        # edge case
        if len(candle_indicies) < 2:
            return results

        for i, (left, right) in enumerate(queries):
            # candle_indicies[leftmost] >= left
            leftmost = bisect_left(candle_indicies, left)
            # candle_indices[rightmost] <= right
            rightmost = bisect_right(candle_indicies, right) - 1

            if leftmost < rightmost:
                # found two candles
                leftmost_idx, rightmost_idx = (
                    candle_indicies[leftmost],
                    candle_indicies[rightmost],
                )

                # total chars in s between leftmost_idx and rightmost_idx in s
                total = rightmost_idx - leftmost_idx - 1

                # then number of candles in between
                num_candles = rightmost - leftmost - 1

                results[i] = total - num_candles

        return results
