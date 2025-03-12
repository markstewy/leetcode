class Node:
    def __init__(self):
        self.isWord = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        # print("add")
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.isWord = True

    def search(self, word: str) -> bool:

        def containsWord(i, curr):
            c = word[i]
            if c == ".":
                if i == len(word) - 1:
                    for child in curr.children.values():
                        if child.isWord:
                            return True
                    return False
                else:
                    for child in curr.children.values():
                        if containsWord(i + 1, child) == True:
                            return True
                    return False
            else:
                if i == len(word) - 1:
                    return c in curr.children and curr.children[c].isWord
                if c not in curr.children:
                    return False
                return containsWord(i + 1, curr.children[c])
        
        return containsWord(0, self.root)



        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
