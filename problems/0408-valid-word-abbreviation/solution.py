class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        expanded = []
        
        i = 0
        while i < len(abbr):
            if abbr[i].isalpha():
                expanded.append(abbr[i])
                i += 1
            else:
                if abbr[i] == "0":
                    return False
                k = ""
                while i < len(abbr) and abbr[i].isdigit():
                    k += abbr[i]
                    i += 1
                
                if int(k) > len(word):
                    return False

                for _ in range(int(k)):
                    expanded.append("*")

        if len(word) != len(expanded):
            return False
        for i in range(len(word)):
            if expanded[i] != word[i] and expanded[i] != "*":
                return False
        
        return True

