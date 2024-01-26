class Node:
    def __init__(self, is_key=False):
        self.is_key = False
        # all lower case letters
        self.nxt = [None] * 26


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        curr = self.root

        for l in word:
            idx = ord(l) - ord("a")
            if curr.nxt[idx] is None:
                curr.nxt[idx] = Node()

            curr = curr.nxt[idx]

        curr.is_key = True

    def search(self, prefix):
        curr = self.root

        # find prefix
        for l in prefix:
            idx = ord(l) - ord("a")

            # prefix doesn't exist
            if curr.nxt[idx] is None:
                return []
            curr = curr.nxt[idx]

        results = []

        def dfs(curr, str_so_far):
            if len(results) == 3:
                return

            if curr.is_key:
                results.append(str_so_far)

            for i, nxt in enumerate(curr.nxt):
                if nxt is not None:
                    dfs(nxt, str_so_far + chr(ord("a") + i))

        dfs(curr, prefix)

        return results


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        """
        Use Tri

        Time:
        - insert: O(MN): M is the length of the longest product, N is the number of products. To be more exact, O(Total number of chars in products)
        - search: O(M*N), M is the length of the longest product or the number of nodes in trie, N is the length of the search word

        Space: O(28*M) => O(M)
        """

        tri = Trie()
        for p in products:
            tri.insert(p)

        res = []

        for i in range(1, len(searchWord) + 1):
            res.append(tri.search(searchWord[0:i]))

        return res
