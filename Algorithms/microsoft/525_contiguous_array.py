class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        Can treated as a presum problem. add 1 for 1, minus 1 for 0
        find the longest subarray with the sum of 0

        use a hashmap to store the prefix sum at each index i

        iterate over nums and check at each i
        1) the accumulative sum up to i is 0, if so update answer
        2) whether there is a previous index j such that presum[i] - presum[j] = 0
        3) add presum:i to hashmap if presum does not already exists to maximize length

        Time: O(N)
        Space: O(N) when all values are 1 or 0
        """

        presum = 0
        ans = 0
        hashmap = {}

        for i, num in enumerate(nums):
            if num == 1:
                presum += 1
            else:
                presum -= 1

            if presum == 0:
                ans = i + 1

            if presum in hashmap:
                ans = max(ans, i - hashmap[presum])
            else:
                hashmap[presum] = i

        return ans
