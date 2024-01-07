class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        """
        Brute force approach: calcuate every product of spells and potions: O(n*m)

        Sort potions first, and for each spell, run binary search on the potions. When The find the target, keep searching on the left potion to in case there is more repetitive element. The trick is to return the left pointer: left pointer and any thing on the right will form a succesful pair with the spell.

        Time: O(n*logm+m*logm)
        Space: O(m) for sorting
        """

        potions.sort()

        def binary_search(spell):
            left, right = 0, len(potions) - 1

            while left <= right:
                mid = (left + right) // 2
                if spell * potions[mid] >= success:
                    right = mid - 1
                else:
                    left = mid + 1

            return left

        res = []
        for spell in spells:
            left = binary_search(spell)
            res.append(len(potions) - left)

        return res
