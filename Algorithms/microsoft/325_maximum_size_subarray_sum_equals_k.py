class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        """
        The trick is to use prefix sum, and the hashmap trick for 2 sum
        note that prefix[i] - prefix[j] = k, not sum
        Essentially, prefix sum + hashmap

        At each location i:
        1) the sum until index i (inclusive) is k, if so, update answer
        2) check if preSum[i] - k is already in hashmap (save presum -> index j)
            update answer if i-j > answer
        3) add i:presum to hashmap if not already exists

        Time: O(N)
        Space: O(N) hashmap
        """
        # can just store the previous value instead of all presums
        presum = 0
        hashmap = {}
        ans = 0

        for i, num in enumerate(nums):
            presum += num

            if presum == k:
                ans = i + 1

            if presum - k in hashmap:
                j = hashmap[presum - k]
                ans = max(ans, i - j)

            # update only if presum is not in hashmap to maximize length
            if presum not in hashmap:
                hashmap[presum] = i

        return ans
