class Node:
    def __init__(self):
        self.isWord = False
        self.next = {}

class WordDictionary:

    def __init__(self):
        self.tree = Node()

    def addWord(self, word: str) -> None:
        curr = self.tree
        for c in word:
            if c not in curr.next:
                curr.next[c] = Node()
            curr = curr.next[c]
        curr.isWord = True

    def search(self, word: str) -> bool:
        return self.helper(word, 0, self.tree)
    

    def helper(self, word: str, i, curr) -> bool:
        c = word[i]
        isLastChar = i == len(word) - 1

        if c == ".":
            if isLastChar:
                for k in curr.next.keys():
                    if curr.next[k].isWord:
                        return True
                return False
            
            for k in curr.next.keys():
                if self.helper(word, i + 1, curr.next[k]) == True:
                    return True
            return False

        else:
            if isLastChar:
                return c in curr.next and curr.next[c].isWord

            if c in curr.next:
                return self.helper(word, i + 1, curr.next[c])
            else:
                return False
            



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
