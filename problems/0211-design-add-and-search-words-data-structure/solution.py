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

        def isWord(i, word, curr):
            c = word[i]
            isLast = i == len(word) - 1

            if c == ".":
                if isLast:
                    for k in curr.children:
                        if curr.children[k].isWord == True:
                            return True
                    return False
                for k in curr.children:
                    if isWord(i + 1, word, curr.children[k]) == True:
                        return True
                return False
            
            if isLast:
                return c in curr.children and curr.children[c].isWord
            if c in curr.children:
                return isWord(i + 1, word, curr.children[c])
            else: 
                return False

        return isWord(0, word, self.root)
        
            


            

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
