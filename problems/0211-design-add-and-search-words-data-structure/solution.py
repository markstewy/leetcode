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
        print(f"{word}---- {self.hasWord(self.root, word, 0)}")
        return self.hasWord(self.root, word, 0)

    def hasWord(self, curr, word, i):
        c = word[i]
        isLastChar = i == len(word) - 1
        
        if c == ".":
            if isLastChar:
                for child in curr.children.values():
                    if child.isWord:
                        return True
                return False
            else:
                for child in curr.children.values():
                    if self.hasWord(child, word, i + 1):
                        return True
                return False

        else:
            if isLastChar:
                return c in curr.children and curr.children[c].isWord
            else:
                if c in curr.children:
                    return self.hasWord(curr.children[c], word, i + 1)
                else:
                    return False
    
    

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
