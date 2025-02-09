class Node:
    def __init__(self):
        self.isWord = False
        self.next = {}

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.next:
                curr.next[c] = Node()
            curr = curr.next[c]
        curr.isWord = True


    def search(self, word: str) -> bool:
        
        def containsWord(curr, word, i):
            c = word[i]
            isLast = i == len(word) - 1

            if c == ".":
                if isLast:
                    for k in curr.next.keys():
                        if curr.next[k].isWord:
                            return True
                    return False
                for k in curr.next.keys():
                    if containsWord(curr.next[k], word, i + 1) == True:
                        return True
                return False
            
            else:
                if isLast:
                    return c in curr.next and curr.next[c].isWord
                if c in curr.next:
                    return containsWord(curr.next[c], word, i + 1)
                return False
        
        return containsWord(self.root, word, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
