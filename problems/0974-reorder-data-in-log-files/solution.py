class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        alpha = []
        digit = []

        for l in logs:
            if l[-1].isalpha():
                alpha.append(l)
            else:
                digit.append(l)
        
        alpha.sort(key=lambda x : (x.split(" ")[1:], x.split(" ")[:1]))

        return alpha + digit
