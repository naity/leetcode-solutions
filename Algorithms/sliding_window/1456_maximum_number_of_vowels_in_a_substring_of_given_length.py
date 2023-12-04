class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
        Maintain a sliding window of size k and track the number of vowels

        Time: O(N)
        Space: O(1)
        """
        vowels = set(["a", "e", "i", "o", "u"])

        # number of vowels in window
        num_vowels = 0

        for i in range(k):
            if s[i] in vowels:
                num_vowels += 1

        res = num_vowels
        # move the window
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                num_vowels -= 1

            if s[i] in vowels:
                num_vowels += 1

            res = max(res, num_vowels)

        return res
