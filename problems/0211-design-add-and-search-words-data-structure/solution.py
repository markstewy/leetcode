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
        
        def hasWord(word: str, i: int, node: Node):
            c: str = word[i]
            isLastChar: bool =  i == len(word) - 1

            if c == ".":
                if isLastChar:
                    for k in node.next:
                        if node.next[k].isWord:
                            return True
                    return False
                for k in node.next:
                    if hasWord(word, i + 1, node.next[k]) == True:
                        return True
                return False

            if isLastChar:
                return c in node.next and node.next[c].isWord
            
            if c not in node.next:
                return False
            
            return hasWord(word, i + 1, node.next[c])
        
        return hasWord(word, 0, self.root)




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
