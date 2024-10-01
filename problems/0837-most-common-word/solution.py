class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        count = {}
        mx = ""
        t = ""
        paragraph += "."
        for c in paragraph:
            if c.isalpha():
                t += c.lower()
            else:
                if t and t not in banned:
                    count[t] = count.get(t, 0) + 1
                    if mx == "" or count[t] > count[mx]:
                        mx = t
                t = ""


        return mx
            
