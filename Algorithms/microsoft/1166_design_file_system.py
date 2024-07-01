class FileSystem:

    def __init__(self):
        """
        Use a dictionary to store the pathes and their values
        for retreiving path in O(1) time
        N is the number of unique paths in the system
        space: O(N)
        """
        self.paths = {}

    def createPath(self, path: str, value: int) -> bool:
        """
        Need to check if the parent path exists before adding
        O(M) where M is the length of path string
        """

        # non-valid paths or already exists
        if not path or path == "/" or path in self.paths:
            return False

        # O(M)
        parent = path.rsplit("/", 1)[0]

        if parent and parent not in self.paths:
            return False

        self.paths[path] = value
        return True

    def get(self, path: str) -> int:
        # O(1) time
        return self.paths.get(path, -1)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
