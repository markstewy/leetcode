class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            a = str1
            b = str2
        else:
            a = str2
            b = str1

        for i in range(len(a) - 1, -1, -1):
            sub = a[:i+1]
            if a.replace(sub, "") == "" and b.replace(sub, "") == "":
                return sub
        
        return ""
