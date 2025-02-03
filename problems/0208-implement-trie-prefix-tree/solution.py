class Node:
    def __init__(self):
        self.isWord = False
        self.next = {}

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        root = self.root
        for c in word:
            root.next[c] = root.next.get(c, Node())
            root = root.next[c]
        root.isWord = True

    def search(self, word: str) -> bool:
        root = self.root
        for c in word:
            if c not in root.next:
                return False
            root = root.next[c]
        return root.isWord

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for c in prefix:
            if c not in root.next:
                return False
            root = root.next[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
