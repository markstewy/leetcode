class Node:
    def __init__(self):
        self.next = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        self.dummyHead = Node()

    def insert(self, word: str) -> None:
        curr = self.dummyHead
        for i, c in enumerate(word):
            if c in curr.next:
                curr = curr.next[c]
            else:
                curr.next[c] = Node()
                curr = curr.next[c]
            if i == len(word) - 1:
                curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.dummyHead
        for i, c in enumerate(word):
            if c in curr.next:
                curr = curr.next[c]
            else:
                return False
            
            if i == len(word) - 1:
                return curr.isEnd == True
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.dummyHead
        for i, c in enumerate(prefix):
            if c in curr.next:
                curr = curr.next[c]
            else:
                return False
        return True
  

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
