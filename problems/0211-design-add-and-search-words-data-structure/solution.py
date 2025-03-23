class Node:
    def __init__(self):
        self.isWord = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.isWord = True

    def search(self, word: str) -> bool:
        
        def hasWord(i, curr):
            c = word[i]
            if c == ".":
                if i == len(word) - 1:
                    for child in curr.children.values():
                        if child.isWord:
                            return True
                    return False
                else:
                    for child in curr.children.values():
                        if hasWord(i + 1, child):
                            return True
                    return False
            else:
                if c not in curr.children:
                    return False
                if i == len(word) - 1:
                    return curr.children[c].isWord
                else:
                    return hasWord(i + 1, curr.children[c])
        
        return hasWord(0, self.root)


        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
