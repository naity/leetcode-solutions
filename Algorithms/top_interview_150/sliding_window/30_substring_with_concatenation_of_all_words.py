class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        let n = len(s), m = len(words), l = len(words[0]), k = m * l
        First count each word in words and store in a dictionary

        check each possible index i
        for each window of length k start at i:
            for each word of length l in the window:
                check:
                1) in words? => i doesn't word if not
                2) the counts of word in window > in the given list? => i doesn't work if so

            if 1) and 2) are not true, i works

        Time: O(n * m * l + m), m for the initial counting
        Space: O(m+l) for dictionaries, since l is at most 30 chars, it can be considered as O(m)
        """
        n = len(s)
        m, l = len(words), len(words[0])
        k = m * l

        # count each words
        counts = defaultdict(int)

        for word in words:
            counts[word] += 1

        # s must at least be k long
        if n < k:
            return []

        res = []
        for i in range(n - k + 1):
            window = defaultdict(int)
            # special cases
            # contains a word not in words
            not_in_words = False
            # extra word
            excess_word = False

            for j in range(i, i + k, l):
                word = s[j : j + l]
                if word not in counts:
                    not_in_words = True
                    break

                window[word] += 1

                # check for counts in words
                if window[word] > counts[word]:
                    excess_word = True
                    break
            # check counts
            if not_in_words or excess_word:
                # check next window
                continue

            res.append(i)
        return res
