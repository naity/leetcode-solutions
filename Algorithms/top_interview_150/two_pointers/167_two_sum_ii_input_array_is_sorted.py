class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Two pointer, one at the start, one at the end
        Move right if sum > target
        Move left if sum < target

        Time: O(N)
        Space: O(1)
        """

        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]

            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
