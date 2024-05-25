class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        Use a hashmap to count the unique numbers in the array

        In order to find the minimum operations, we need to pick three elements
        as many times as possible
        1) Is the count divisible by 3 or count % 3 == 0?
        2) the highest it can go is count // 3, lowest is 0
        3) use a  loop to check if the remainder is divisible by 2

        If none satisfies, return -1

        The total steps is the sum of all numbers

        The solution offers a trick: math.ceil(count/3)
        which is insane to me to come up with

        Key insight:
        if count % 3 is not zero, what can it be?
        1 or 2.
        If 1: just need to take one step back and add back 3 yielding 4, which will take 2 steps
        if 2: divisible by 2

        In any case, just one extra step

        Time: O(N)
        Space: O(N)
        """

        counts = Counter(nums)

        total = 0
        for num, count in counts.items():
            if count == 1:
                return -1

            total += count // 3

            if count % 3 != 0:
                total += 1

        return total
