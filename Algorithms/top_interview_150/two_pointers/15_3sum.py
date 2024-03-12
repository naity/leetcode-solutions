class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Convert this to a 2Sum problem, for each i, find two numbers
        in nums[i+1:] that sum up to -nums[i]

        avoid duplicates by sorting first.

        Early break:
        the first num should be negative, bacause the number after it
        are all larger than it, and the sum of two larger positive numbers
        cannot be negative.

        Time: O(N^2)
        Space: O(N) for sorting
        """
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == -nums[i]:
                    res.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # need to skip repeating numbers
                    # note we only need to do this for left
                    # as the right value won't work any more if it is duplicated
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # while right > i and nums[right] == nums[right+1]:
                    #     right -= 1

                elif nums[left] + nums[right] < -nums[i]:
                    left += 1

                else:
                    right -= 1

        return res
