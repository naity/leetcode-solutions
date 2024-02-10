class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Could count each unique element in nums using a hashtable.
        But would require O(N) space

        count = defaultdict(int)

        for num in nums:
            count[num] += 1

            if count[num] > len(nums) // 2:
                return num

        Boyer-Moore Voting Algorithm:
        Count majority element as 1 others as -1. Set the first element as
        the candidate majority element whenever the sum is 0

        Time: O(N)
        Space: O(1)
        """
        count = 0
        majority = None

        for num in nums:
            if count == 0:
                majority = num

            if num == majority:
                count += 1
            else:
                count -= 1

        return majority
