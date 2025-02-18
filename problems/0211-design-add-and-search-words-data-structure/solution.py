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

        def helper(curr, i, word):
            c = word[i]
            isLast = i == len(word) - 1

            if c == ".":
                if isLast:
                    for child in curr.children:
                        if curr.children[child].isWord:
                            return True
                    return False
                for child in curr.children:
                    if helper(curr.children[child], i + 1, word) == True:
                        return True
                return False

            else:
                if c in curr.children:
                    if isLast:
                         return curr.children[c].isWord
                    else:
                        return helper(curr.children[c], i + 1, word)
                else:
                    return False
        


        return helper(self.root, 0, word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
