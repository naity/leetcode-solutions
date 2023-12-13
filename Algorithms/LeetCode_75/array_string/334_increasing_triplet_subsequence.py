class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        Keep track of the first two numbers where num2 > num1 and find num3 that is
        greater than num1 and num2. Update num1 and num2 while scanning nums

        Time: O(N)
        Space: O(1)
        """

        num1, num2 = float("inf"), float("inf")

        for num in nums:
            if num <= num1:
                num1 = num
            elif num <= num2:
                num2 = num
            else:
                return True

        return False
