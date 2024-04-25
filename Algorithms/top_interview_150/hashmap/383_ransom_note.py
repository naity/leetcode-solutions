class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Count the letters in ransomNote and magazine using hashmap,
        then check each letter in randomNote in magazine

        Time: O(M+N+M) or O(N) since N>=M (M: r, N: m)
        Space: O(26+26) = O(1)
        """

        # simple case
        if len(ransomNote) > len(magazine):
            return False

        hash_r = defaultdict(int)
        hash_m = defaultdict(int)

        for l in ransomNote:
            hash_r[l] += 1

        for l in magazine:
            hash_m[l] += 1

        for k, v in hash_r.items():
            if v > hash_m[k]:
                return False

        return True
