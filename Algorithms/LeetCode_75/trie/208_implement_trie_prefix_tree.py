class Node:
    def __init__(self, is_key, num_chars=26):
        self.is_key = is_key
        self.children = [None] * num_chars


class Trie:
    """
    Trie:
    Each node has a is_key property to indicate a key end
    Lowercase letters only: use a list for the next letter. Initialize with all Nones

    Traverse the nodes for insertion and search
    """

    def __init__(self):
        self.root = Node(False)

    def insert(self, word: str) -> None:
        """
        Time: O(m): word length
        Space: O(m): create at most m new nodes
        """
        curr = self.root
        for l in word:
            idx = ord(l) - ord("a")
            if curr.children[idx] is None:
                # only create node if not existing
                curr.children[idx] = Node(False)
            curr = curr.children[idx]

        curr.is_key = True

    def find(self, word):
        """
        Time: O(m): word length
        Space: O(1)
        """
        curr = self.root
        for l in word:
            idx = ord(l) - ord("a")

            if curr.children[idx] is None:
                return None

            curr = curr.children[idx]
        return curr

    def search(self, word: str) -> bool:
        res = self.find(word)
        return res is not None and res.is_key

    def startsWith(self, prefix: str) -> bool:
        res = self.find(prefix)
        # don't need to be an end
        return res is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
