class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        """
        we iterate through both lists, and do two things:
        1) calculate the total number of candies
        2) store the # of candies in box in a hashset

        Afterwords, calculate the difference between
        the total number of candies of Alice and Bob
        iterate the boxes of Alice,
        and check if Size[i] - diff//2 in the hashset of the other person,
        if so, return Size[i] and Size[i] - diff//2

        note it is diff//2
        as one will increase by diff//2, the other one will gain diff//2

        mathmatically:
        Alice swap x, Bob swap y:
        Sa - x + y = Sb + x - y => y = (Sb-Sa) / 2 + x

        can just use on set to save memory

        M, N = len(aliceSizes), len(bobSizes)
        Time: O(M+N)
        Space: O(N) can further optimize this to O(MIN(M, N))
        """

        bobSet = set(bobSizes)

        alice_total = sum(aliceSizes)
        bob_total = sum(bobSizes)

        for size in aliceSizes:
            size2 = (bob_total - alice_total) // 2 + size
            if size2 in bobSet:
                return [size, size2]
