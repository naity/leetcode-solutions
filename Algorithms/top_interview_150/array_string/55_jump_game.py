class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        DFS with memorization

        Time: O(N^2)
        Space: O(N)

        mem = {}
        def search(i):
            if i >= len(nums)-1:
                return True

            if i in mem:
                return mem[i]

            max_steps = nums[i]

            for step in range(max_steps, 0, -1):
                if search(i+step):
                    mem[i] = True
                    return True

            mem[i] = False
            return False

        return search(0)

        Key insight: Track the left-most index that can reach the last index to
        avoid the for loop.

        Even if there are other possible indices after the left-most one,
        if they can be reached, the left-most can be reached as well

        Iterate from the last element to the first

        Time: O(N)
        Space: O(1)
        """

        last_index = len(nums) - 1

        for i in range(last_index - 1, -1, -1):
            if i + nums[i] >= last_index:
                last_index = i

        return last_index == 0
