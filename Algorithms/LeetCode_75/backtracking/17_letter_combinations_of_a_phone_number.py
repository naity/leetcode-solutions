class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Backtracking:
        for each digit, consider all letters it maps to and recursively call on the next digit

        Time: O(4^N*N) Note N is the cost to concatenate the combo string
        Space: O(N) for recursion
        """

        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        combo = []
        curr = []

        def dfs(i):
            if i == len(digits):
                if curr:
                    combo.append("".join(curr))
                return
            digit = digits[i]
            for l in mapping[digit]:
                curr.append(l)
                dfs(i + 1)
                # exit
                curr.pop()

        dfs(0)
        return combo
