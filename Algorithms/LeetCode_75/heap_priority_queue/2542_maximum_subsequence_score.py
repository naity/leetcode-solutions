class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """
        How to choose k nums from nums1 to maximize the sum? use a min-heap to track the k largest nums in nums1.

        What about the min of the selected numbers from nums2? The key is to treat (nums1[i], nums2[i]) as pairs since they share the same index, and then sort by nums2[i]. For each i from k-1, we can use nums2[i] as the min from nums2, and pick the largest k nums from nums1 including nums1[i], iterate through and track the largest product

        Time: O(NLogN) + k + NLogk => O(NlogN)
        Space: O(N)
        """

        pairs = [pair for pair in zip(nums1, nums2)]
        pairs = sorted(pairs, key=lambda p: p[1], reverse=True)

        # min heap
        h = [pairs[i][0] for i in range(k)]
        heapq.heapify(h)

        total = sum(h)
        res = total * pairs[k - 1][1]

        # iterate all other possible solutions
        for i in range(k, len(nums1)):
            # remove the smallest and pair[i][0]
            popped = heapq.heappop(h)
            total -= popped
            total += pairs[i][0]
            heapq.heappush(h, pairs[i][0])

            res = max(res, total * pairs[i][1])

        return res
