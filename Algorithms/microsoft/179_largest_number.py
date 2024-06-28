class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        Sort the number so that "larger" values will be placed
        first

        How to define larger?
        10, 2 => 2 is larger
        3, 30 = > 3 is larger

        essentially, we can compare the two number formed by different order
        and see which one is larger in value

        Note that we will want to place the "larger" first, we can either
        1) treat it "smaller" when sorting
        2) treat it as "larger" but reverse sort

        the key is to use cmp_to_key to define a custom sorting mechanism

        Time: O(NlogN)
        Space: O(N)
        """
        # be aware of the edge case when all numbers are 0
        # alternative, just need to check if the first item is "0" after sorting
        if sum(nums) == 0:
            return "0"

        def compare(a, b):
            if int(a + b) > int(b + a):
                return -1
            return 1

        nums = [str(num) for num in nums]

        nums = sorted(nums, key=cmp_to_key(compare))

        return "".join(nums)
