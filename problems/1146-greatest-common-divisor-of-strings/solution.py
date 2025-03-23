class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        shorter = str1 if len(str1) < len(str2) else str2

        while shorter:
            if str1.replace(shorter, "") == "" and str2.replace(shorter, "") == "":
                return shorter
            shorter = "".join(shorter[:-1])
        
        return shorter
