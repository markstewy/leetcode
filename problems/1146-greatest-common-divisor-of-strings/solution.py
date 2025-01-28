class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        divisor = ""
        for i in range(1, len(str2) + 1):
            print(str2[:i])
            if str1.replace(str2[:i], "") == "" and str2.replace(str2[:i], "") == "":
                divisor = str2[:i]
        return divisor

