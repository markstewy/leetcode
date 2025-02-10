class Solution:
    def clearDigits(self, s: str) -> str:
        s = list(s)
        
        prevCharIdxs = []
        for i , c in enumerate(s):
            if not c.isdigit():
                prevCharIdxs.append(i)
            else:
                s[i] = ""
                if prevCharIdxs:
                    s[prevCharIdxs.pop()] = ""
            
        
        return "".join(s)
