class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Can use three for loops to check every possible combination
        O(N^3)

        To help remove duplicates, we can first sort the numbers so that
        we can skip duplicated numbers. Convert it to a 2Sum problem,
        for each num at i, we check if there are two numbers that sum up to -num
        since they are sorted, num must be negative or 0, otherwise the sum will always to positive.


        Time: O(NLogN) for storting, check sum for each location i O(N*N) = > O(N^2)
        Space: O(N) for sorting
        """

        nums.sort()

        ans = []

        for i, num in enumerate(nums):
            # doesn't really need to second condition as left < right is False
            if num > 0 or i >= len(nums) - 2:
                break

            # avoid duplicates
            if i > 0 and nums[i - 1] == num:
                continue

            # find two numbers that sum up to -num
            left = i + 1
            right = len(nums) - 1

            while left < right:
                # they are sorted
                if nums[left] + nums[right] == -num:
                    ans.append([num, nums[left], nums[right]])

                    # need to keep searching
                    left += 1
                    right -= 1
                    # again avoid duplicates
                    # only need to do left, as left changes, right will change too
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif nums[left] + nums[right] < -num:
                    # need a bigger number
                    left += 1
                else:
                    right -= 1

        return ans
