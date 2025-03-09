class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for i in range(len(str1) - 1, -1, -1):
            sub = str1[:i+1]
            if str1.replace(sub, "") == "" and str2.replace(sub, "") == "":
                return sub
        return ""

