class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        The highest hIndex is the length of the citations n
        We sort the values and start from n
        if hIndex is n, then citations[0] should >= n
        check from n to 0

        Time: O(NlongN + N) => O(NLogN)
        Space: O(1), O(N) if includes sorting
        """

        n = len(citations)
        h_index = n

        citations.sort()

        # h_index cannot be negative
        while h_index > 0 and citations[n - h_index] < h_index:
            h_index -= 1

        return h_index
