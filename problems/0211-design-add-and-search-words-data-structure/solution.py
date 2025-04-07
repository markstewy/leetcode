class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False

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

        def helper(curr, i):
            if word[i] == ".":
                if i == len(word) - 1:
                    for child in curr.children.values():
                        if child.isWord:
                            return True
                    return False
                else:
                    for child in curr.children.values():
                        if helper(child, i + 1) == True:
                            return True
                    return False
            else:
                if word[i] not in curr.children:
                    return False
                if i == len(word) - 1:
                    return curr.children[word[i]].isWord
                
                return helper(curr.children[word[i]], i + 1)
        
        return helper(self.root, 0)


        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
