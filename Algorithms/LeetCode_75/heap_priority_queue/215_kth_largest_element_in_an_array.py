class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Push the items into a min-heap and maintain the heap of size k. The smallest item in the heap is the answer

        Time: O(Nlogk)
        Space: O(k)
        """

        h = []

        for num in nums:
            heapq.heappush(h, num)
            if len(h) > k:
                heapq.heappop(h)

        return h[0]
